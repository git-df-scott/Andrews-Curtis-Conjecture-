"""Freeze new seam failure controls, not an AC component enumeration."""
from collections import deque
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path

from acsearch.words import parse,reduce,inverse
from acsearch.hsc_mixed import pair_key,normalized_edges
from acsearch.hsc_shortening import letters,symmetrized
from acsearch.hsc_seam import fiber_bridge,multiplication_events,word_pair_bound

ROOT=Path(__file__).resolve().parents[2]
folder=ROOT/'certificates'
old=json.loads(folder.joinpath('astra_third_strike.json').read_text())
nodes=[tuple(map(parse,n[0])) for n in old['AK3']['nodes']]
root=pair_key((parse('xxxYYYY'),parse('xyxYXY')))
lookup={s:i for i,s in enumerate(nodes)}
parents={root:None};todo=deque([root])
while todo:
    s=todo.popleft()
    for j in old['AK3']['nodes'][lookup[s]][1]:
        t=nodes[j]
        if t not in parents:parents[t]=s;todo.append(t)

# Load the already complete boundary domain; no larger graph is traversed.
jump=None
for s in sorted(nodes):
    for t,w in multiplication_events(s,15):
        if w['after_height']==24:
            jump=(s,w);break
    if jump:break
s,w=jump
route=[];cur=s
while parents[cur] is not None:route.append((parents[cur],cur));cur=parents[cur]
route.reverse()
path=fiber_bridge((parse('xxxYYYY'),parse('xyxYXY')),root)
for a,b in route:
    witness=normalized_edges(a,15)[0][b]
    before=(parse(witness['u']),parse(witness['b']))
    after=(parse(witness['product']),parse(witness['b']))
    path.extend(fiber_bridge(a,before))
    path.append({'move':['M',0,2],'after':[letters(z) for z in after]})
    path.extend(fiber_bridge(after,b))
before=(parse(w['u']),parse(w['b']))
path.extend(fiber_bridge(s,before))
path.append({'move':['M',0,2],'after':[w['product'],w['b']]})

families=[]
for n in range(2,15):
    g=parse('y'*n);state=(parse('x'),parse('y'));steps=[]
    for op in ('C','M','M','C'):
        if op=='C':
            z=g if not steps else inverse(g)
            state=(reduce(z+state[0]+inverse(z)),state[1]);mv=['C',0,letters(z)]
        else:
            state=(reduce(state[0]+state[1]),state[1]);mv=['M',0,2]
        steps.append({'move':mv,'after':[letters(z) for z in state]})
    families.append({'n':n,'initial':['x','y'],'steps':steps,
                     'raw_internal_seam_height':2*n+1,
                     'minimal_signed_seam_width':4,
                     'replacement':[
                         {'move':['M',0,2],'after':['xy','y']},
                         {'move':['M',0,2],'after':['xyy','y']} ]})

g='yyyyyy';r='xxxYYYY';s='xyxYXY'
macro={'initial':[r,s],'steps':[{'move':['C',0,g],
        'after':[letters(reduce(parse(g)+parse(r)+inverse(parse(g)))),s]}]}
counts=[sum(abs(a)==1 for a in R[:31]) for R in symmetrized()]
attempt_bytes=folder.joinpath('hsc_height23_attempt.json.gz').read_bytes()
attempt=json.loads(gzip.decompress(attempt_bytes));discovered=attempt['records']
types=Counter();maxima={};depths=[0]
for i,row in enumerate(discovered[1:],1):
    p=row['parent'];depths.append(depths[p]+1)
    if not p:continue
    same=pair_key((parse(row['witness']['b']),parse('x')))==pair_key((parse(discovered[p]['witness']['b']),parse('x')))
    kind='same_target' if same else 'switched_target'
    types[kind]+=1;g=discovered[p]['parent']
    L=max(sum(map(len,discovered[g]['pair'])),sum(map(len,row['pair'])))
    width=sum(map(len,discovered[p]['pair']))
    if kind not in maxima or width-L>maxima[kind]['excess']:
        maxima[kind]=dict(excess=width-L,indices=[g,p,i],external_L=L,seam_width=width)

def expand_fiber_edges(initial,edges):
    current=initial;out=[]
    for w in edges:
        before=(parse(w['u']),parse(w['b']))
        after=(parse(w['product']),parse(w['b']))
        out.extend(fiber_bridge(current,before))
        out.append({'move':['M',0,2],'after':[letters(z) for z in after]})
        current=pair_key(after);out.extend(fiber_bridge(after,current))
    return out

g,p,i=maxima['same_target']['indices'];assert g==0
high=expand_fiber_edges(root,[discovered[j]['witness'] for j in (p,i)])
target=tuple(map(parse,discovered[i]['pair']))
low_route=[];cur=target
while parents[cur] is not None:
    low_route.append((parents[cur],cur));cur=parents[cur]
low_route.reverse()
low=expand_fiber_edges(root,[normalized_edges(a,15)[0][b] for a,b in low_route])
record={
 'schema':'hsc-fourth-controls-v1',
 'seam_bound':None,'multiplication_bound':None,'global_height_bound':None,
 'scope':'CONDITIONAL THEOREMS AND FAILURE CONTROLS; NO SEPARATION',
 'inherited_sha256':{name:hashlib.sha256(folder.joinpath(name).read_bytes()).hexdigest()
     for name in ('astra_first_strike.json','astra_second_strike.json','astra_third_strike.json')},
 'conditional_seam_type_count':{'formula':'1+8*R*3**(R-1) for R>=1; 1 for R=0',
     'values':{str(R):word_pair_bound(R) for R in (0,1,2,3,4,15,23)}},
 'shell_sha256':hashlib.sha256(attempt_bytes).hexdigest(),
 'two_M_tree_analysis':{'type_counts':dict(types),'depth_counts':dict(Counter(depths)),
     'maximum_excess_examples':maxima,'scope':'DISCOVERY TREE ONLY; NOT PEAK-MINIMALITY'},
 'same_target_high_seam':{'initial':[letters(w) for w in root],
     'steps':high,'lower_replacement':low,'tree_indices':[g,p,i],
     'high_peak':23,'low_peak':15,'signed_internal_seam_width':23,
     'minimum_M_in_height23':2},
 'two_M_family':families,
 'family_infinite_distinctness':{'relator_windows':244,
     'minimum_x_letters_in_31_window':min(counts),'all_counts':counts},
 'unbounded_cancellation_controls':[
     {'n':n,'before':['x'+'y'*n,'Y'*n+'Xy'],
      'after':['y','Y'*n+'Xy'],'move':['M',0,2],
      'cancelled_pairs':n+1} for n in range(1,14)],
 'multiplication_jump_over_16':{'initial':['xxxYYYY','xyxYXY'],'steps':path},
 'macro_jump_over_liftable_shell':macro,
 'retained_class_is_not_a_seam_type':{
     'initial':['x','y'],'steps':[
       {'move':['M',0,2],'after':['x'+'y'*j,'y']} for j in range(1,22)],
     'distinct_seam_pairs':22,'height':23},
 'branching_word_failure':{
     'initial':['x','y'],'steps':[
       {'move':['M',0,2],'after':['xy','y']},
       {'move':['M',1,1],'after':['xy','yxy']}],
     'false_identity_word':letters(reduce(parse('xy')+inverse(parse('xy'))+inverse(parse('yxy'))))}
}
folder.joinpath('astra_fourth_strike.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print('height24 witness steps',len(path))
print('31-window minimum x letters',min(counts))
print('seam heights',[(r['n'],r['raw_internal_seam_height']) for r in families])
