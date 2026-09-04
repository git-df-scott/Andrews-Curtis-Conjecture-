"""Fourth-strike finite controls. No global seam/height bound is asserted."""
from functools import lru_cache
from collections import deque
import gzip
import hashlib
import json
from pathlib import Path

from .words import parse, reduce, inverse, cyclic_reduce
from .hsc_shortening import letters
from .hsc_mixed import pair_key, signed_rotations, generator_orbit


def word_pair_bound(R):
    """All ordered freely reduced word pairs with total length <=R."""
    if not isinstance(R, int) or R < 0:
        raise ValueError('nonnegative integer required')
    return 1 if R == 0 else 1 + 8*R*3**(R-1)


def switched_two_m_bounds(L):
    """Local two-M result ONLY; the target coordinate must switch.

    The height replacement additionally requires non-diagonal, distinct
    successive signed-conjugacy fibers, hence linked one-M triples.
    """
    if not isinstance(L,int) or L < 0:
        raise ValueError('nonnegative integer required')
    return {'scope':'TWO MULTIPLICATIONS WITH SWITCHED TARGET ONLY',
            'signed_seam_width':2*L,'linked_replacement_height':3000*(2*L+1),
            'global_height_bound':None}


@lru_cache(maxsize=4096)
def tail_representatives(core, bound):
    """Exact inside-out enumeration, with free conjugators retained."""
    if bound < len(core):
        return ()
    if not core or cyclic_reduce(core) != core:
        raise ValueError('nonempty cyclically reduced core required')
    layer = [(a, (), a) for a in signed_rotations(core)]
    out = list(layer)
    for _ in range((bound-len(core))//2):
        layer = [((c,)+w+(-c,), (c,)+g, a)
                 for w, g, a in layer for c in (-2,-1,1,2)
                 if c != -w[0] and c != w[-1]]
        out.extend(layer)
    return tuple(sorted(out))


def multiplication_events(state, height):
    """Complete normalized edge domain; callers must enforce reachability.

    Scope is precisely the inherited F2-liftable endpoint domain, H<=23.
    Rejected output peaks are yielded too, for auditable work accounting.
    """
    if not 2 <= height <= 23 or state != pair_key(state) or not all(state):
        raise ValueError('requires canonical nonempty pair and 2<=H<=23')
    if sum(map(len,state)) > height:
        raise ValueError('source outside height cap')
    for i in (0,1):
        a0,b0 = state[i],state[1-i]
        for u,g,a in tail_representatives(a0,height-len(b0)):
            for b in signed_rotations(b0):
                w = reduce(u+b)
                before,after = len(u)+len(b),len(w)+len(b)
                assert before <= height
                witness = dict(target_index=i, a=letters(a), b=letters(b),
                               g=letters(g), u=letters(u), product=letters(w),
                               before_height=before, after_height=after)
                if after <= height:
                    if not w:
                        raise ValueError('identity output: outside normally generating F2 domain')
                    yield pair_key((w,b)),witness
                else:
                    yield None,witness


def _free_conjugator(u,v):
    """Return g with v=g u g^-1, or None; orientation is preserved."""
    def split(w):
        k=0
        while 2*k+1 < len(w) and w[k] == -w[-1-k]:
            k+=1
        return w[:k],w[k:len(w)-k] if k else w
    t,c=split(u);s,d=split(v)
    if not c or not d:
        return () if c == d else None
    for k in range(len(c)):
        if c[k:]+c[:k] == d:
            return reduce(s+inverse(c[:k])+inverse(t))
    return None


def fiber_bridge(source,target):
    """Literal free macro I/P/C bridge; total height <= max endpoint height.

    This constructs a bridge, not a geodesically optimal move sequence.
    """
    if pair_key(source) != pair_key(target):
        raise ValueError('different signed cyclic fibers')
    state=list(source);steps=[]
    def emit(move):
        steps.append({'move':move,'after':[letters(w) for w in state]})
    from .hsc_mixed import cyclic_key
    if cyclic_key(state[0]) != cyclic_key(target[0]):
        state.reverse();emit(['P',0,1])
    # Coordinate decreases first prevents a mixed length-transfer peak.
    for i in sorted((0,1),key=lambda j:len(target[j])-len(state[j])):
        g=_free_conjugator(state[i],target[i])
        if g is None:
            state[i]=inverse(state[i]);emit(['I',i,0])
            g=_free_conjugator(state[i],target[i])
        assert g is not None
        if state[i] != target[i]:
            state[i]=reduce(g+state[i]+inverse(g))
            emit(['C',i,letters(g)])
    assert tuple(state) == tuple(target)
    assert all(sum(map(len,s['after'])) <= max(sum(map(len,source)),sum(map(len,target)))
               for s in steps)
    return steps


def bounded_attack(folder,height=23,event_cap=2000000,state_cap=20000):
    """Deterministically capped positive search; retains discovery witnesses.

    CAP is an incomplete traversal, never a negative orbit certificate.
    A frozen standard-component contact triggers immediate return.
    """
    if not 2 <= height <= 23 or event_cap < 1 or state_cap < 1:
        raise ValueError('invalid certified domain or resource limit')
    folder=Path(folder)
    old_bytes=folder.joinpath('hsc_standard_height15.json.gz').read_bytes()
    standard=json.loads(gzip.decompress(old_bytes))
    targets={tuple(parse(w) for w in n[0]) for n in standard['nodes']}
    root=pair_key((parse('xxxYYYY'),parse('xyxYXY')))
    if sum(map(len,root)) > height:
        raise ValueError('height excludes AK3')
    records=[{'pair':[letters(w) for w in root], 'parent':None}]
    index={root:0};todo=deque([root]);events=accepted=processed=0
    status='COMPLETE_SUBLEVEL';contact=None;partial=None
    while todo:
        state=todo.popleft();sid=index[state]
        exhausted=True
        for target,witness in multiplication_events(state,height):
            if events >= event_cap:
                status='EVENT_CAP';partial=sid;exhausted=False;break
            events+=1
            if target is None:
                continue
            accepted+=1
            if target in index:
                continue
            if len(records) >= state_cap:
                status='STATE_CAP';partial=sid;exhausted=False;break
            tid=len(records);index[target]=tid;todo.append(target)
            records.append({'pair':[letters(w) for w in target],
                            'parent':sid,'witness':witness})
            if sum(map(len,target)) <= 15 and min(generator_orbit(target)) in targets:
                status='TARGET_FOUND';contact=tid;partial=sid;exhausted=False;break
        if not exhausted:
            break
        processed+=1
    return {'schema':'hsc-fourth-shell-v1','height':height,'status':status,
            'purpose':'POSITIVE_PATH_ATTEMPT_ONLY','global_height_bound':None,
            'event_cap':event_cap,'state_cap':state_cap,'candidate_events':events,
            'accepted_events':accepted,'processed_vertices':processed,
            'partial_vertex':partial,'discovered_vertices':len(records),
            'queued_vertices':len(todo),'contact':contact,
            'standard_graph_sha256':hashlib.sha256(old_bytes).hexdigest(),
            'records':records}


if __name__ == '__main__':
    import time
    root=Path(__file__).resolve().parents[1]
    start=time.perf_counter()
    result=bounded_attack(root/'certificates')
    data=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode()
    root.joinpath('certificates/hsc_height23_attempt.json.gz').write_bytes(gzip.compress(data,mtime=0))
    print(json.dumps({k:v for k,v in result.items() if k!='records'},sort_keys=True))
    print('runtime_seconds',round(time.perf_counter()-start,6))
