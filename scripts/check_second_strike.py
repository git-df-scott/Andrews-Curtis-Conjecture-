#!/usr/bin/env python3
"""Independent stdlib certificate checker. Imports NO acsearch implementation.

Certifies finite combinatorics and positive paths, not the cited annular theorem,
not a formal proof of peak reduction, and not orbit separation.
"""
from functools import lru_cache
from itertools import combinations
import hashlib
import json
from pathlib import Path
import sys

RELATORS = [
 'YXyXXXYxYxyxyyxYYXXyXXyyxyXyXYYYYXYXYYXYYXXYYYxyxyxYXYxyXYYxY',
 'xYXXYXyyxyyyyyyyyxYXyxYxyyxyyXyXYxxYYYXyXyXYXYxyXYYYxxxYXYxYx']


def inv(s):
    return s.swapcase()[::-1]


def free(s):
    assert set(s) <= set('xXyY')
    while True:
        t = s
        for p in ('xX','Xx','yY','Yy'):
            t = t.replace(p,'')
        if t == s:
            return s
        s = t


def cyclic(s):
    s = free(s)
    while len(s)>1 and s[0]==inv(s[-1]):
        s = s[1:-1]
    return s


def rots(s):
    return {s[i:]+s[:i] for i in range(len(s))} if s else {''}


def verify(c):
    assert c['schema']=='hsc-second-strike-v1'
    assert c['relators']==RELATORS
    assert c['comparison']=={'standard':['x','y'],'AK3':['xxxYYYY','xyxYXY']}
    assert c['geodesic_radius']==30
    assert c['conjugator_bound']=='4*L**2+4*L+8'
    assert c['peak_upper_bound'] is None
    assert c['AK3_peak_lower_bound']==15
    assert c['complete_component_enumeration'] is False
    assert all(len(r)==61 and cyclic(r)==r for r in RELATORS)
    sym = sorted(set().union(*(rots(r)|rots(inv(r)) for r in RELATORS)))
    pieces = set()
    # Independent pairwise common-prefix extraction, vs producer histogram.
    for a,b in combinations(sym,2):
        k = 0
        while k<min(len(a),len(b)) and a[k]==b[k]:
            k += 1
        pieces.update(a[:j] for j in range(1,k+1))
    assert len(sym)==244 and max(map(len,pieces))==8 and 6*8<61
    assert all(not any(r==r[:k]*(61//k) for k in range(1,61) if 61%k==0)
               for r in RELATORS)
    cover = c['piece_cover']
    assert cover['symmetrized_size']==244 and cover['piece_count']==len(pieces)==202
    assert cover['max_piece']==8
    rows = {row['relator']:row['max_covered'] for row in cover['rows']}
    assert len(rows)==len(cover['rows'])==244 and set(rows)==set(sym)
    for r in sym:
        @lru_cache(None)
        def reach(pos,k):
            if k==0:
                return pos
            return max((reach(pos+j,k-1) for j in range(1,9)
                        if pos+j<=61 and r[pos:pos+j] in pieces), default=-1)
        assert rows[r]==[reach(0,k) for k in range(1,6)]
    assert cover['max_covered']==[max(row[k] for row in rows.values()) for k in range(5)]
    assert cover['max_covered']==[8,13,17,23,28]
    assert len(c['plateaus'])==2
    for n,p in zip((2,3),c['plateaus']):
        r,s='x'*n+'Y'*(n+1),'xyxYXY'
        assert p['candidate']==f'AK({n})' and p['pair']==[r,s]
        aa,bb=rots(r)|rots(inv(r)),rots(s)|rots(inv(s))
        assert p['rotations_inversions']==[len(aa),len(bb)]
        observed={(row['a'],row['b']):row for row in p['rows']}
        assert len(observed)==len(p['rows'])==len(aa)*len(bb)==p['product_count']
        assert set(observed)=={(a,b) for a in aa for b in bb}
        for (a,b),row in observed.items():
            assert row['product']==free(a+b)
            assert row['cyclic_product']==cyclic(a+b)
        assert p['min_cyclic_product']==min(len(cyclic(a+b)) for a in aa for b in bb)
        assert p['min_cyclic_product']=={2:7,3:9}[n]
    # Full literal replay of the published AK2 control, including endpoint setup.
    path=c['AK2_positive_path']
    assert path['initial']==['xxYYY','xyxYXY'] and path['published_steps']==14
    assert len(path['steps'])==23
    state=path['initial'].copy()
    lengths=[sum(map(len,state))]
    for step in path['steps']:
        op,i,j=step['move']
        assert type(i) is int and i in (0,1)
        if op=='I':
            assert j==0
            state[i]=inv(state[i])
        elif op=='M':
            assert type(j) is int and abs(j) in (1,2) and abs(j)-1!=i
            s=state[abs(j)-1]
            state[i]+=s if j>0 else inv(s)
        elif op=='C':
            assert j in (1,-1,2,-2)
            g={1:'x',-1:'X',2:'y',-2:'Y'}[j]
            state[i]=g+state[i]+inv(g)
        elif op=='P':
            assert (i,j)==(0,1)
            state=[state[1],state[0]]
        else:
            raise AssertionError('unknown move')
        state=list(map(free,state))
        assert state==step['after']
        assert all(len(s)<=30 for s in state)
        lengths.append(sum(map(len,state)))
    assert state==['x','y']
    assert path['max_geodesic_sum']==max(lengths)==15
    e=c['annular_positive']
    assert e['relator'] in sym and e['g'] in pieces
    assert e['g']+e['u']+inv(e['g'])+inv(e['v'])==e['relator']
    assert 15<=len(e['u'])<=30 and 15<=len(e['v'])<=30
    assert cyclic(e['u'])==e['u'] and cyclic(e['v'])==e['v']
    assert e['v'] not in rots(e['u'])
    f=c['mixed_reorder_failure']
    assert f['g']=='yxy'
    g=f['g']
    u,v='x','y'
    b=free(g+u+inv(g)); end=free(b+v)
    a=free(inv(g)+v+g)
    original=[[u,v],[b,v],[end,v]]
    reordered=[[u,v],[u,a],[free(u+a),a],[end,a],[end,v]]
    assert f['original']==original and f['reordered']==reordered
    assert f['original_peak']==max(sum(map(len,t)) for t in original)==8
    assert f['reordered_peak']==max(sum(map(len,t)) for t in reordered)==11
    assert all(len(w)<=30 for state in original+reordered for w in state)
    # 7=|g x g^-1| <= 2|g|+1 proves any witness has length >=3.
    assert len(b)==7 and f['conjugator_minimum_length']==len(g)==3
    return {'piece_cover':'PASS (pairwise prefixes / recursive partitions)',
            'short_plateau_products':'PASS (all 120+168 products)',
            'AK2_positive_path':'PASS (23 moves in F2; maximum sum 15)',
            'nonfree_conjugacy':'PASS (literal single-relator annulus)',
            'mathematical_scope':'finite certificate checks; annular implications require written proof',
            'AK3_orbit_separation':'NOT CLAIMED',
            'mixed_reorder_counterexample':'PASS (peak 8 becomes 11)'}


if __name__=='__main__':
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'certificates/astra_second_strike.json'
    raw=path.read_bytes()
    result=verify(json.loads(raw))
    result['certificate_sha256']=hashlib.sha256(raw).hexdigest()
    print(json.dumps(result,sort_keys=True))
