#!/usr/bin/env python3
"""Independent string verifier. No acsearch imports and no orbit verdict.

--replay additionally reconstructs the entire deterministic capped prefix.
Default verifies every discovery edge and every new finite failure control.
"""
from collections import deque,Counter
from functools import lru_cache
from itertools import product
from pathlib import Path
import gzip
import hashlib
import json
import sys
import time

ALPH='YXxy'
ORDER=str.maketrans(ALPH,'0123')


def inv(w):return w.swapcase()[::-1]


def free(w):
    assert set(w)<=set(ALPH)
    while True:
        z=w
        for p in ('xX','Xx','yY','Yy'):z=z.replace(p,'')
        if z==w:return z
        w=z


def cyclic(w):
    w=free(w)
    while len(w)>1 and w[0]==inv(w[-1]):w=w[1:-1]
    return w


@lru_cache(maxsize=8192)
def rots(w):
    return tuple(sorted({v[i:]+v[:i] for v in (w,inv(w))
                         for i in range(len(v))},key=lambda z:z.translate(ORDER)))


def core(w):
    w=cyclic(w)
    return rots(w)[0] if w else ''


def key(p):return tuple(sorted(map(core,p),key=lambda w:w.translate(ORDER)))


def move(state,mv):
    op,i,j=mv;s=list(state)
    if op=='P':s.reverse()
    elif op=='I':s[i]=inv(s[i])
    elif op=='C':s[i]=free(j+s[i]+inv(j))
    elif op=='M':
        assert abs(j)-1==1-i
        v=s[1-i];s[i]=free(s[i]+(v if j>0 else inv(v)))
    else:raise AssertionError('unknown move')
    return tuple(s)


def path(record):
    state=tuple(record['initial']);states=[state]
    for row in record['steps']:
        state=move(state,row['move']);assert state==tuple(row['after'])
        assert max(map(len,state),default=0)<=30  # unique geodesics inherited
        states.append(state)
    return states


def controls(c,folder):
    assert c['schema']=='hsc-fourth-controls-v1'
    assert c['seam_bound'] is c['multiplication_bound'] is c['global_height_bound'] is None
    for name,digest in c['inherited_sha256'].items():
        assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==digest
    # Independent convolution, not the closed formula used by the producer.
    def count_words(n):return 1 if not n else 4*3**(n-1)
    for r,n in c['conditional_seam_type_count']['values'].items():
        R=int(r)
        assert n==sum(count_words(i)*count_words(j)
                      for i in range(R+1) for j in range(R+1-i))
    first=json.loads((folder/'astra_first_strike.json').read_text())
    sym=set()
    for r in first['laboratories']['H_SC']['relators']:
        sym.update(rots(r))
    counts=[sum(a.lower()=='x' for a in r[:31])
            for r in sorted(sym,key=lambda z:z.translate(ORDER))]
    d=c['family_infinite_distinctness']
    assert len(sym)==d['relator_windows']==244
    assert counts==d['all_counts']
    assert min(counts)==d['minimum_x_letters_in_31_window']==10
    for row in c['two_M_family']:
        n=row['n'];states=path(row)
        assert states[-1]==('xyy','y')
        assert sum(map(len,states[2]))==row['raw_internal_seam_height']==2*n+1
        seams={key(states[j]) for j in (0,2,3)}
        assert len(seams)==3
        assert max(sum(map(len,s)) for s in seams)==row['minimal_signed_seam_width']==4
        assert sum(s['move'][0]=='M' for s in row['steps'])==2
        replacement=path({'initial':row['initial'],'steps':row['replacement']})
        assert replacement[-1]==states[-1]
        assert max(sum(map(len,s)) for s in replacement)==4
    assert [r['n'] for r in c['two_M_family']]==list(range(2,15))
    for row in c['unbounded_cancellation_controls']:
        a,b=row['before'];after=move((a,b),row['move'])
        assert after==tuple(row['after']) and after[0]=='y'
        assert (len(a)+len(b)-len(after[0]))//2==row['cancelled_pairs']==row['n']+1
        assert max(len(a),len(b))<=30
    jump=path(c['multiplication_jump_over_16'])
    assert max(sum(map(len,s)) for s in jump[:-1])==15
    assert sum(map(len,jump[-1]))==24
    assert c['multiplication_jump_over_16']['steps'][-1]['move'][0]=='M'
    macro=path(c['macro_jump_over_liftable_shell'])
    assert [sum(map(len,s)) for s in macro]==[13,25]
    chain=path(c['retained_class_is_not_a_seam_type'])
    assert len({key(s) for s in chain})==22
    assert len({core(s[1]) for s in chain})==1
    assert max(sum(map(len,s)) for s in chain)==23
    branch=path(c['branching_word_failure'])
    a,b=branch[0];u,v=branch[-1]
    residual=free(a+b+inv(u)+inv(v))
    assert residual==c['branching_word_failure']['false_identity_word']
    assert 0<len(residual)<61
    shell_bytes=(folder/'hsc_height23_attempt.json.gz').read_bytes()
    assert hashlib.sha256(shell_bytes).hexdigest()==c['shell_sha256']
    rows=json.loads(gzip.decompress(shell_bytes))['records']
    types=Counter();depths=[0];maxima={}
    for i,row in enumerate(rows[1:],1):
        p=row['parent'];depths.append(depths[p]+1)
        if p==0:continue
        b1=core(rows[p]['witness']['b']);b2=core(row['witness']['b'])
        mode='same_target' if b1==b2 else 'switched_target';types[mode]+=1
        g=rows[p]['parent'];L=max(sum(map(len,rows[g]['pair'])),sum(map(len,row['pair'])))
        width=sum(map(len,rows[p]['pair']))
        if mode=='switched_target':
            assert key((b1,b2))==tuple(rows[p]['pair']) and width<=2*L
        if mode not in maxima or width-L>maxima[mode]['excess']:
            maxima[mode]=dict(excess=width-L,indices=[g,p,i],external_L=L,seam_width=width)
    analysis=c['two_M_tree_analysis']
    assert dict(types)==analysis['type_counts']
    assert {str(k):v for k,v in Counter(depths).items()}==analysis['depth_counts']
    assert maxima==analysis['maximum_excess_examples']
    ex=c['same_target_high_seam'];hi=path(ex)
    lo=path({'initial':ex['initial'],'steps':ex['lower_replacement']})
    assert hi[-1]==lo[-1]
    assert max(sum(map(len,s)) for s in hi)==ex['high_peak']==23
    assert max(sum(map(len,s)) for s in lo)==ex['low_peak']==15
    assert sum(r['move'][0]=='M' for r in ex['steps'])==2
    assert sum(r['move'][0]=='M' for r in ex['lower_replacement'])==2
    q0,q1,q2=(tuple(rows[i]['pair']) for i in ex['tree_indices'])
    assert (q0,q2)==(key(hi[0]),key(hi[-1]))
    assert sum(map(len,q1))==ex['signed_internal_seam_width']==23
    assert len({q0,q1,q2})==3
    # Independent complete root neighborhood: rules out zero/one M at H<=23.
    assert ex['minimum_M_in_height23']==2 and q0!=q2
    for i in (0,1):
        for u,_,_ in representatives(q0[i],23-len(q0[1-i])):
            for b in rots(q0[1-i]):
                w=free(u+b)
                if len(w)+len(b)<=23:assert key((w,b))!=q2
    return {'two_M_controls':len(c['two_M_family']),
            'cancellation_controls':len(c['unbounded_cancellation_controls']),
            'jump24_steps':len(jump)-1,'relator_windows':len(counts),
            'two_M_type_counts':dict(types),'same_target_shortcut_verified':True}


MAPS=[str.maketrans('xXyY',a+inv(a)+b+inv(b))
      for a in ALPH for b in ALPH if a.lower()!=b.lower()]


def standard_targets(folder):
    data=folder.joinpath('hsc_standard_height15.json.gz').read_bytes()
    c=json.loads(gzip.decompress(data))
    targets={tuple(n[0]) for n in c['nodes']}
    def contact(s):
        return sum(map(len,s))<=15 and any(key(tuple(w.translate(m) for w in s)) in targets
                                           for m in MAPS)
    return data,contact


def discoveries(c,folder):
    assert c['schema']=='hsc-fourth-shell-v1'
    assert c['height']==23 and c['purpose']=='POSITIVE_PATH_ATTEMPT_ONLY'
    assert c['status']=='EVENT_CAP' and c['global_height_bound'] is None and c['contact'] is None
    assert c['candidate_events']==c['event_cap']==2000000
    assert c['discovered_vertices']==len(c['records'])<=c['state_cap']
    assert c['processed_vertices']+1+c['queued_vertices']==len(c['records'])
    assert c['partial_vertex']==c['processed_vertices']
    data,contact=standard_targets(folder)
    assert hashlib.sha256(data).hexdigest()==c['standard_graph_sha256']
    states=[]
    for i,row in enumerate(c['records']):
        s=tuple(row['pair']);assert key(s)==s and sum(map(len,s))<=23
        assert not contact(s)
        if i==0:
            assert row['parent'] is None and s==key(('xxxYYYY','xyxYXY'))
        else:
            assert 0<=row['parent']<i
            p=states[row['parent']];w=row['witness']
            a,b,g,u,v=(w[k] for k in ('a','b','g','u','product'))
            assert core(a)==p[w['target_index']]
            assert core(b)==p[1-w['target_index']]
            assert free(g+a+inv(g))==u and free(u+b)==v
            assert w['before_height']==len(u)+len(b)<=23
            assert w['after_height']==len(v)+len(b)<=23
            assert key((v,b))==s
        states.append(s)
    assert len(set(states))==len(states)
    return {'discovery_edges_verified':len(states)-1,'complete_shell':False}


@lru_cache(maxsize=4096)
def representatives(core,bound):
    # Independent route: enumerate free tail words, reject any boundary
    # cancellation, then sort the resulting literal conjugates.
    found=[]
    for n in range((bound-len(core))//2+1):
        for letters in product(ALPH,repeat=n):
            g=''.join(letters)
            if free(g)!=g:continue
            for a in rots(core):
                u=g+a+inv(g)
                if free(u)==u:found.append((u,g,a))
    return sorted(found,key=lambda t:tuple(w.translate(ORDER) for w in t))


def replay(c):
    states=[tuple(c['records'][0]['pair'])];index={states[0]:0}
    events=accepted=processed=0
    while True:
        s=states[processed]
        for i in (0,1):
            for u,g,a in representatives(s[i],23-len(s[1-i])):
                for b in rots(s[1-i]):
                    if events==c['event_cap']:
                        assert processed==c['processed_vertices']
                        assert accepted==c['accepted_events']
                        assert len(states)==c['discovered_vertices']
                        return {'replayed_events':events,'accepted':accepted,
                                'fully_processed_vertices':processed}
                    events+=1;v=free(u+b)
                    if len(v)+len(b)>23:continue
                    accepted+=1;t=key((v,b))
                    if t in index:continue
                    j=len(states);index[t]=j;states.append(t)
                    row=c['records'][j]
                    assert tuple(row['pair'])==t and row['parent']==processed
                    assert row['witness']==dict(target_index=i,a=a,b=b,g=g,u=u,product=v,
                        before_height=len(u)+len(b),after_height=len(v)+len(b))
        processed+=1


def check(folder,replay_prefix=False):
    folder=Path(folder)
    c=json.loads((folder/'astra_fourth_strike.json').read_text())
    p=json.loads(gzip.decompress((folder/'hsc_height23_attempt.json.gz').read_bytes()))
    result={'controls':controls(c,folder),'discoveries':discoveries(p,folder)}
    if replay_prefix:result['prefix_replay']=replay(p)
    return result


if __name__=='__main__':
    start=time.perf_counter()
    print(json.dumps(check(Path(__file__).resolve().parents[1]/'certificates',
                           '--replay' in sys.argv),sort_keys=True))
    print('runtime_seconds',round(time.perf_counter()-start,6))
