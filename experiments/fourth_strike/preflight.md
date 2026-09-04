# Fourth-strike preflight

Theorem 2 and Theorem 4 of HSC_MIXED_BLOCK_NORMAL_FORM.md certify the
endpoint-reachable free signed-cyclic graph for total height H<=23. Both
actual multiplication endpoint heights must pass before normalization.
Conjugators are not sampled: enumerate every reduced signed conjugate of
the changed core through H minus the retained core length. This is the
proved complete edge normalization, including both changed coordinates.

One positive-certificate attempt will use H=23 directly, not a radius sweep.
Start at the AK(3) fiber. A hit in the frozen complete standard height-15
component suffices; a hit must be expanded to a literal F2 move certificate.
The standard graph is reused, not recomputed. No symmetry identifies AK(3)
states in this traversal.

Hard work limits: 2,000,000 normalized multiplication candidates; 20,000
discovered fibers. These are resource stops, never conjugator cutoffs or
negative completeness claims. Stop immediately at a target. Every completed
vertex has all its normalized edges processed; a partly processed vertex
is recorded separately. The deterministic transcript contains discovery
parents and exact multiplication witnesses. Its independent replay proves
reachability and respects the height cap; it cannot certify global closure.

The trivial ambient word-pair bound at 23 is 1+8*23*3^22 =
5,774,114,968,057 ordered word pairs (including empty entries). It is only
an upper bound, not an estimate of either component. Direct complete raw
enumeration is not justified as practical by the height-15 result.

No global height upper bound is known. Even completion of this bounded
query could not establish full AC orbit separation.
