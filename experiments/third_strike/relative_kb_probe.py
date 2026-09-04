import signal,time,json
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup
from acsearch.hyperbolic import H_SC_RELATOR_STRINGS
start=time.perf_counter()
def stop(*args): raise TimeoutError('20 second bounded probe exhausted')
signal.signal(signal.SIGALRM,stop);signal.alarm(20)
F,x,y=free_group('x,y')
def word(s):
 w=F.identity
 for c in s: w*= {'x':x,'X':x**-1,'y':y,'Y':y**-1}[c]
 return w
G=None
try:
 G=FpGroup(F,[word('xyxYXY')]+[word(s) for s in H_SC_RELATOR_STRINGS])
 G._rewriting_system.maxeqns=1000
 print('initial_rules',len(G._rewriting_system.rules),flush=True)
 G._rewriting_system.make_confluent()
 print('completed',len(G._rewriting_system.rules), 'x=',G.reduce(x),'y=',G.reduce(y))
except (TimeoutError,RuntimeError) as e:
 print(type(e).__name__,str(e),flush=True)
 if G is not None: print('rules',len(G._rewriting_system.rules),flush=True)
finally:
 signal.alarm(0)
 print('runtime',time.perf_counter()-start)
