#!/usr/bin/env python3
"""Independent string/ordered-state checker; imports no acsearch code.

Completeness is for the induced height-15 graph. No global orbit verdict.
"""
from collections import deque,Counter
from functools import lru_cache
import gzip,hashlib,json
from pathlib import Path
import sys,time


def inv(w):return w.swapcase()[::-1]


def free(w):
    assert set(w)<=set('xXyY')
    while True:
        z=w
        for p in ('xX','Xx','yY','Yy'):z=z.replace(p,'')
        if z==w:return z
        w=z


def cyclic(w):
    w=free(w)
    while len(w)>1 and w[0]==inv(w[-1]):w=w[1:-1]
    return w


@lru_cache(maxsize=131072)
def rotations(w):return frozenset(w[i:]+w[:i] for i in range(len(w)))


@lru_cache(maxsize=131072)
def core(w):
    w=cyclic(w)
    return min(rotations(w)|rotations(inv(w))) if w else ''


def key(state):return tuple(sorted(core(w) for w in state))


MAPS=[str.maketrans('xXyY',a+inv(a)+b+inv(b))
      for a in 'xXyY' for b in 'xXyY' if a.lower()!=b.lower()]


@lru_cache(maxsize=131072)
def orbit(state):
    return frozenset(key(tuple(w.translate(m) for w in state)) for m in MAPS)


def gkey(state):return min(orbit(key(state)))


@lru_cache(maxsize=8192)
def all_conjugates(a,bound):
    # Independent inside-out construction. No enumeration of conjugator words.
    layer=set(rotations(a)|rotations(inv(a)));out=set(layer)
    for _ in range((bound-len(a))//2):
        layer={c+w+inv(c) for w in layer for c in 'xXyY'
               if c!=inv(w[0]) and c!=w[-1]}
        out.update(layer)
    return tuple(sorted(out))


def neighbors(state,symmetric):
    targets=set();count=0
    for i in (0,1):
        a,b=state[i],state[1-i]
        for u in all_conjugates(a,15-len(b)):
            for v in rotations(b)|rotations(inv(b)):
                w=free(u+v)
                if len(w)+len(v)>15:continue
                assert w
                count+=1
                targets.add(gkey((w,v)) if symmetric else key((w,v)))
    return targets,count


def ordered_neighbors(s):
    for i in (0,1):
        z=list(s);z[i]=inv(z[i]);yield tuple(z)
        for sign in (1,-1):
            z=list(s);v=s[1-i];z[i]=free(z[i]+(v if sign==1 else inv(v)));yield tuple(z)
        for c in 'xXyY':
            z=list(s);z[i]=free(c+z[i]+inv(c));yield tuple(z)
    yield (s[1],s[0])


def check_ak3_raw(record):
    assert record['scope']=='COMPLETE_HEIGHT_15_SUBLEVEL_ONLY'
    assert record['generator_symmetry'] is False
    start=('xxxYYYY','xyxYXY');seen={start};todo=deque([start]);tested=accepted=0
    while todo:
        s=todo.popleft()
        for t in ordered_neighbors(s):
            tested+=1
            if sum(map(len,t))>15:continue
            accepted+=1
            if t not in seen:seen.add(t);todo.append(t)
    assert ('x','y') not in seen
    classes={key(s) for s in seen}
    recorded={key(tuple(row[0])) for row in record['nodes']}
    assert len(recorded)==len(record['nodes']) and classes==recorded
    assert len(seen)==record['counts']['ordered_vertices']==13728
    assert len(classes)==record['counts']['vertices']==26
    heights=Counter(sum(map(len,s)) for s in seen)
    assert {str(h):n for h,n in heights.items()}==record['counts']['ordered_heights']
    digest=hashlib.sha256(json.dumps(sorted(seen),separators=(',',':')).encode()).hexdigest()
    return {'ordered_states':len(seen),'elementary_moves_tested':tested,
            'accepted_directed_elementary_moves':accepted,'states_sha256':digest}


def check_graph(record,symmetric):
    assert record['scope']=='COMPLETE_HEIGHT_15_SUBLEVEL_ONLY'
    assert record['generator_symmetry'] is symmetric
    canonical=gkey if symmetric else key
    rows=record['nodes'];keys=[canonical(tuple(row[0])) for row in rows]
    index={s:i for i,s in enumerate(keys)}
    assert len(index)==len(rows)
    directed=multiplications=0;cyclic_heights=Counter();ordered_heights=Counter()
    for i,((words,adj,n),state) in enumerate(zip(rows,keys)):
        assert len(words)==2 and all(cyclic(w)==w and 0<len(w)<15 for w in words)
        assert sum(map(len,words))<=15
        targets,count=neighbors(state,symmetric)
        assert len(set(adj))==len(adj) and all(type(j) is int and 0<=j<len(rows) for j in adj)
        assert {keys[j] for j in adj}==targets
        assert count==n
        directed+=len(adj);multiplications+=n
        mult=len(orbit(state)) if symmetric else 1
        cyclic_heights[sum(map(len,state))]+=mult
        a,b=state;assert a!=b
        c=2*len(rotations(a)|rotations(inv(a)))*len(rotations(b)|rotations(inv(b)))
        def factor(k):return 1 if k==0 else 2*3**(k-1)
        for height in range(len(a)+len(b),16,2):
            t=(height-len(a)-len(b))//2
            ordered_heights[height]+=mult*c*sum(factor(j)*factor(t-j) for j in range(t+1))
    # Connectivity and reverse-edge completeness of the submitted finite graph.
    root=record['root'];assert type(root) is int and 0<=root<len(rows)
    assert keys[root]==canonical(('x','y') if symmetric else ('xxxYYYY','xyxYXY'))
    seen={root};todo=[root]
    while todo:
        i=todo.pop()
        for j in rows[i][1]:
            assert i in rows[j][1]
            if j not in seen:seen.add(j);todo.append(j)
    assert len(seen)==len(rows)
    expected={'vertices':len(rows),'directed_edges':directed,
              'normalized_multiplications':multiplications,
              'signed_cyclic_vertices':sum(cyclic_heights.values()),
              'cyclic_heights':{str(h):n for h,n in cyclic_heights.items()},
              'ordered_vertices':sum(ordered_heights.values()),
              'ordered_heights':{str(h):n for h,n in ordered_heights.items()}}
    assert record['counts']==expected
    return set(keys)


def check_boundary(c):
    b=c['AK3_boundary'];counts=Counter();total=0;first=set()
    for words,_,_ in c['AK3']['nodes']:
        state=key(tuple(words))
        for i in (0,1):
            a,v=state[i],state[1-i]
            for u in all_conjugates(a,15-len(v)):
                for w in rotations(v)|rotations(inv(v)):
                    z=free(u+w);h=len(z)+len(w);total+=1
                    if h>15:counts[h]+=1
                    if h==16:first.add((u,w,z))
    assert b['normalized_candidates']==total==12384
    assert b['escape_heights']=={str(h):n for h,n in counts.items()}
    observed=set()
    for row in b['normalized_height16_exits']:
        u,v=row['before'];w,v2=row['after']
        assert v2==v and w==free(u+v) and len(w)+len(v)==16
        assert key((u,v))==key(tuple(row['source_fiber']))
        assert core(u)==core('xyxYXY')
        observed.add((u,v,w))
    assert observed==first and len(observed)==len(b['normalized_height16_exits'])==24
    assert b['first_exit_height']==16


def check_controls(c,second):
    assert c['global_height_bound'] is None
    assert c['complete_unrestricted_orbit_enumeration'] is False
    assert c['full_orbit_result']=='UNKNOWN'
    assert c['conjugator_bound']=='4*L**2+4*L+8'
    assert c['AK3_unconditional_height_lower_bound']==16 and c['free_lifting_height']==23
    assert c['second_certificate_sha256']==hashlib.sha256(second).hexdigest()
    old=json.loads(second)
    assert old['AK2_positive_path']['max_geodesic_sum']==15
    assert old['mixed_reorder_failure']['original_peak']==8
    assert old['mixed_reorder_failure']['reordered_peak']==11
    f=c['hidden_peak_counterexample']
    assert f['input']==['Xyx','x'] and f['height_cap']==4
    assert f['raw_output']==[free(f['input'][0]+f['input'][1]),f['input'][1]]
    assert f['cyclic_output']==[cyclic(w) for w in f['raw_output']]
    assert f['heights']==[sum(map(len,f[k])) for k in ('input','raw_output','cyclic_output')]==[4,5,3]
    p=c['one_cell_pants'];sym=set()
    for r in old['relators']:sym.update(rotations(r)|rotations(inv(r)))
    assert p['relator'] in sym and p['u']+p['v']+inv(p['w'])==p['relator']
    assert p['perimeter']==sum(len(p[k]) for k in ('u','v','w'))==61 and p['faces']==1
    assert all(cyclic(p[k])==p[k] for k in ('u','v','w'))
    # Annular rung bound8 plus girth61: these pairs cannot be nonfreely
    # conjugate because each pair's lengths+16 is below61.
    for a,b in ((p['u'],inv(p['v'])),(p['u'],p['w']),(p['v'],p['w'])):
        assert len(a)+len(b)+16<61 and b not in rotations(a)
    b=c['single_m_bounds_at_L15'];L=15;P=2*L;F=3*P+3;E=(61*F+P)//2;Q=4*E+4*P
    assert [b[k] for k in ('boundary_perimeter','area','edges','cut_path','derived_height','single_m_height')]==[P,F,E,Q,4*Q+2*L,3000*(L+1)]
    assert b['derived_height']<=b['single_m_height']


def check(folder):
    folder=Path(folder);raw=folder.joinpath('astra_third_strike.json').read_bytes();c=json.loads(raw)
    assert c['schema']=='acc-third-strike-v1' and c['height_shell']==15
    check_controls(c,folder.joinpath('astra_second_strike.json').read_bytes())
    check_boundary(c)
    z=folder.joinpath(c['standard']['file']).read_bytes()
    assert hashlib.sha256(z).hexdigest()==c['standard']['sha256']
    payload=gzip.decompress(z)
    assert hashlib.sha256(payload).hexdigest()==c['standard']['uncompressed_sha256']
    standard=json.loads(payload);assert standard['counts']==c['standard']['counts']
    akkeys=check_graph(c['AK3'],False)
    raw_control=check_ak3_raw(c['AK3'])
    standardkeys=check_graph(standard,True)
    assert not {gkey(s) for s in akkeys}&standardkeys
    return {'scope':'COMPLETE HEIGHT-15 SUBLEVEL; NO GLOBAL ORBIT CLAIM',
            'AK3_ordered_independent':raw_control,
            'AK3_cyclic_vertices':len(akkeys),'standard_symmetry_vertices':len(standardkeys),
            'frozen_counterexamples':'PASS','new_controls':'PASS',
            'certificate_sha256':hashlib.sha256(raw).hexdigest()}


if __name__=='__main__':
    start=time.perf_counter()
    result=check(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'certificates')
    result['runtime_seconds']=time.perf_counter()-start
    print(json.dumps(result,sort_keys=True))
