"""Exact height-15 sublevel graph, not unrestricted H_SC orbit enumeration.

The finite cutoff is proved in HSC_MIXED_BLOCK_NORMAL_FORM.md. All states
reachable here lift to F2; an H_SC-only connecting path must leave this shell.
"""
from collections import deque
from functools import lru_cache
from .words import parse, reduce, inverse, cyclic_reduce, cyclic_canonical, rotations
from .hsc_shortening import letters


@lru_cache(maxsize=65536)
def cyclic_key(w):
    return cyclic_canonical(w)


def pair_key(pair):
    return tuple(sorted(cyclic_key(w) for w in pair))


@lru_cache(None)
def signed_rotations(w):
    return tuple(sorted(set(rotations(w)) | set(rotations(inverse(w)))))


@lru_cache(None)
def reduced_words(bound):
    layer=[()]
    out=layer.copy()
    for _ in range(bound):
        layer=[w+(a,) for w in layer for a in (-2,-1,1,2)
               if not w or w[-1]!=-a]
        out.extend(layer)
    return tuple(out)


@lru_cache(maxsize=8192)
def representatives(core, bound):
    """All freely reduced conjugates/inverse conjugates within a word bound."""
    if bound<len(core):return ()
    tail_bound=(bound-len(core))//2
    found={}
    for g in reduced_words(tail_bound):
        for a in signed_rotations(core):
            u=reduce(g+a+inverse(g))
            if u not in found:
                found[u]=(g,a)
    return tuple((u,)+found[u] for u in sorted(found))


def normalized_edges(state, bound=15):
    """All finite normalized M-edges from a signed cyclic pair fiber.

    Return one exact witness per target fiber, and the count of distinct
    normalized (target index,u,b) multiplication transitions, including loops.
    Both BEFORE and AFTER sums are tested. No heuristic conjugator cutoff.
    """
    if not 2<=bound<=15 or len(state)!=2 or not all(state):
        raise ValueError('certified shell requires two nonempty entries and 2<=bound<=15')
    if state!=pair_key(state) or sum(map(len,state))>bound:
        raise ValueError('noncanonical or out-of-bound source')
    targets={}
    count=0
    for i in range(2):
        a0,b0=state[i],state[1-i]
        for u,g,a in representatives(a0,bound-len(b0)):
            for b in signed_rotations(b0):
                product=reduce(u+b)
                if len(product)+len(b)>bound:
                    continue
                count+=1
                if not product:
                    # Normal generation in F2 rules this out in the endpoint
                    # components. Refuse to silently drop an unexpected case.
                    raise ValueError('identity output outside the certified endpoint domain')
                target=pair_key((product,b))
                if target not in targets:
                    targets[target]={'target_index':i,'a':letters(a),'b':letters(b),
                                     'g':letters(g),'u':letters(u),'product':letters(product),
                                     'before_height':len(u)+len(b),
                                     'after_height':len(product)+len(b)}
    return targets,count


def component(root,bound=15,max_states=50000,stop_at=None,progress=None):
    root=pair_key(root)
    stop_at=pair_key(stop_at) if stop_at is not None else None
    queue=deque([root]);parents={root:None};edges={};counts={}
    while queue:
        state=queue.popleft()
        targets,count=normalized_edges(state,bound)
        edges[state]=tuple(sorted(targets));counts[state]=count
        for target in sorted(targets):
            if target not in parents:
                parents[target]=(state,targets[target])
                queue.append(target)
                if target==stop_at:
                    return {'status':'TARGET_FOUND','parents':parents,'edges':edges,'counts':counts}
                if len(parents)>max_states:
                    return {'status':'STATE_CAP','parents':parents,'edges':edges,'counts':counts}
        if progress is not None and len(edges)%1000==0:
            progress(len(edges),len(parents))
    return {'status':'COMPLETE_SUBLEVEL','parents':parents,'edges':edges,'counts':counts}


GENERATOR_MAPS=tuple((s*a,t*b) for a,b in ((1,2),(2,1))
                    for s in (1,-1) for t in (1,-1))


def map_word(w,images):
    return tuple(images[abs(a)-1] if a>0 else -images[abs(a)-1] for a in w)


@lru_cache(maxsize=131072)
def generator_orbit(state):
    return tuple(sorted({pair_key(tuple(map_word(w,im) for w in state))
                         for im in GENERATOR_MAPS}))


def standard_component_symmetric(bound=15,max_states=50000,stop_at=None,progress=None):
    """Complete standard sublevel modulo generator maps fixing its root.

    This finite action is justified ONLY through the free-graph lifting
    theorem at bound<=15. It is not an H_SC automorphism assumption.
    """
    root=pair_key((parse('x'),parse('y')))
    stop_at=min(generator_orbit(pair_key(stop_at))) if stop_at is not None else None
    queue=deque([root]);parents={root:None};edges={};counts={}
    while queue:
        state=queue.popleft()
        targets,count=normalized_edges(state,bound)
        compressed={}
        for target,witness in targets.items():
            key=min(generator_orbit(target))
            if key not in compressed:
                compressed[key]={'raw_target':target,'witness':witness}
        edges[state]=tuple(sorted(compressed));counts[state]=count
        for target in sorted(compressed):
            if target not in parents:
                parents[target]=(state,compressed[target]);queue.append(target)
                if target==stop_at:
                    return {'status':'TARGET_FOUND','parents':parents,'edges':edges,'counts':counts}
                if len(parents)>max_states:
                    return {'status':'STATE_CAP','parents':parents,'edges':edges,'counts':counts}
        if progress is not None and len(edges)%1000==0:
            progress(len(edges),len(parents))
    return {'status':'COMPLETE_SUBLEVEL','parents':parents,'edges':edges,'counts':counts}


def fiber_height_counts(state,bound=15):
    """Counts every ordered freely reduced representative, without listing it."""
    a,b=state
    if a==b or not a or not b:
        raise ValueError('endpoint fibers have two distinct nonempty signed classes')
    c=len(signed_rotations(a))*len(signed_rotations(b))*2
    def factor(t):return 1 if t==0 else 2*3**(t-1)
    return {h:c*sum(factor(t)*factor((h-len(a)-len(b))//2-t)
                    for t in range((h-len(a)-len(b))//2+1))
            for h in range(len(a)+len(b),bound+1,2)}


def graph_record(c,symmetric=False):
    from collections import Counter
    if c['status']!='COMPLETE_SUBLEVEL':raise ValueError('partial graph is not a certificate')
    states=sorted(c['parents']);index={s:i for i,s in enumerate(states)}
    root=next(s for s,p in c['parents'].items() if p is None)
    cyclic_heights=Counter();ordered_heights=Counter()
    for s in states:
        mult=len(generator_orbit(s)) if symmetric else 1
        cyclic_heights[sum(map(len,s))]+=mult
        for h,n in fiber_height_counts(s).items():ordered_heights[h]+=mult*n
    return {'scope':'COMPLETE_HEIGHT_15_SUBLEVEL_ONLY','generator_symmetry':symmetric,
            'root':index[root],
            'nodes':[[[letters(w) for w in s],[index[t] for t in c['edges'][s]],c['counts'][s]]
                     for s in states],
            'counts':{'vertices':len(states),'directed_edges':sum(map(len,c['edges'].values())),
                      'normalized_multiplications':sum(c['counts'].values()),
                      'signed_cyclic_vertices':sum(cyclic_heights.values()),
                      'cyclic_heights':dict(sorted(cyclic_heights.items())),
                      'ordered_vertices':sum(ordered_heights.values()),
                      'ordered_heights':dict(sorted(ordered_heights.items()))}}


def hidden_peak_example():
    # Input sum4, product sum5, but cyclic canonical output sum3.
    return {'height_cap':4,'input':['Xyx','x'],'raw_output':['Xyxx','x'],
            'cyclic_output':['yx','x'],'heights':[4,5,3],
            'failure':'testing only cyclic output length hides the multiplication peak'}


def pants_bounds(L):
    if not isinstance(L,int) or L<0:raise ValueError('nonnegative integer required')
    P=2*L
    F=3*P+3
    E=(61*F+P)//2
    Q=4*E+4*P
    return {'boundary_perimeter':P,'area':F,'edges':E,'cut_path':Q,
            'derived_height':4*Q+2*L,'single_m_height':3000*(L+1),
            'scope':'linked single-multiplication block ONLY; not a global peak bound'}


def escape_record(c):
    from collections import Counter
    heights=Counter();total=0;first=[]
    for state in sorted(c['parents']):
        for i in (0,1):
            a,b=state[i],state[1-i]
            for u,g,r in representatives(a,15-len(b)):
                for v in signed_rotations(b):
                    w=reduce(u+v);h=len(w)+len(v);total+=1
                    if h>15:heights[h]+=1
                    if h==16:
                        first.append({'source_fiber':[letters(z) for z in state],
                                      'before':[letters(u),letters(v)],
                                      'after':[letters(w),letters(v)]})
    return {'normalized_candidates':total,'escape_heights':dict(sorted(heights.items())),
            'first_exit_height':16,'normalized_height16_exits':first,
            'scope':'normalized M-edges; arbitrary C-escape predicate is specified in the proof'}


def write_certificates(folder,ak,standard,pants):
    import gzip,hashlib,json
    from pathlib import Path
    folder=Path(folder)
    payload=json.dumps(graph_record(standard,True),sort_keys=True,separators=(',',':')).encode()+b'\n'
    zipped=gzip.compress(payload,mtime=0)
    folder.joinpath('hsc_standard_height15.json.gz').write_bytes(zipped)
    second=folder.joinpath('astra_second_strike.json').read_bytes()
    c={'schema':'acc-third-strike-v1','height_shell':15,'global_height_bound':None,
       'conjugator_bound':'4*L**2+4*L+8','first_strike_commit':'82fe261',
       'second_strike_commit':'ecaa80a263ce4ec739a953d1be0a69bdeafffb6c',
       'second_certificate_sha256':hashlib.sha256(second).hexdigest(),
       'AK3':graph_record(ak),'AK3_boundary':escape_record(ak),
       'standard':{'file':'hsc_standard_height15.json.gz',
                   'sha256':hashlib.sha256(zipped).hexdigest(),
                   'uncompressed_sha256':hashlib.sha256(payload).hexdigest(),
                   'counts':graph_record(standard,True)['counts']},
       'AK3_unconditional_height_lower_bound':16,
       'free_lifting_height':23,'one_cell_pants':pants,
       'single_m_bounds_at_L15':pants_bounds(15),
       'hidden_peak_counterexample':hidden_peak_example(),
       'full_orbit_result':'UNKNOWN','complete_unrestricted_orbit_enumeration':False}
    folder.joinpath('astra_third_strike.json').write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
    return c


if __name__=='__main__':
    import json,time
    from pathlib import Path
    start=time.perf_counter()
    folder=Path(__file__).resolve().parents[1]/'certificates'
    a=(parse('xxxYYYY'),parse('xyxYXY'));s=(parse('x'),parse('y'))
    ak=component(a,stop_at=s)
    if ak['status']=='TARGET_FOUND':raise SystemExit('TARGET FOUND: freeze and independently verify path before continuing')
    standard=standard_component_symmetric(stop_at=a)
    if standard['status']=='TARGET_FOUND':raise SystemExit('TARGET FOUND: freeze and independently verify path before continuing')
    # Frozen literal one-cell control; no rediscovery search in the producer.
    pants=json.loads(folder.joinpath('third_strike_pants_control.json').read_text())
    c=write_certificates(folder,ak,standard,pants)
    print(json.dumps({'AK3':c['AK3']['counts'],'standard':c['standard']['counts'],
                      'runtime_seconds':time.perf_counter()-start},sort_keys=True))
