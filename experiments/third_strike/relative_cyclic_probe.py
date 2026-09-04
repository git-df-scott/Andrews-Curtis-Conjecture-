import signal,time
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup,coset_enumeration_r
from acsearch.hyperbolic import H_SC_RELATOR_STRINGS
start=time.perf_counter()
def stop(*args): raise TimeoutError('20 second bounded probe exhausted')
signal.signal(signal.SIGALRM,stop); signal.alarm(20)
F,x,y=free_group('x,y')
def word(s):
 w=F.identity
 for c in s: w*= {'x':x,'X':x**-1,'y':y,'Y':y**-1}[c]
 return w
try:
 G=FpGroup(F,[word('xyxYXY')]+[word(s) for s in H_SC_RELATOR_STRINGS])
 C=coset_enumeration_r(G,[x],max_cosets=512)
 C.compress();print('complete',C.is_complete(),'rows',len(C.table),'table',C.table[:3])
except (TimeoutError,ValueError) as e:print(type(e).__name__,str(e))
finally:signal.alarm(0);print('runtime',time.perf_counter()-start)
