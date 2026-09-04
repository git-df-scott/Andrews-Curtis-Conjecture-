# Mixed blocks: exact normal forms and their limits

Third strike, 2026-09-04, based on `ecaa80a`. The ambient group, generator
marking, and ordered pair A=(xxxYYYY,xyxYXY) are unchanged. Complexity is
C(u,v)=|u|+|v| for the ordinary four-letter geodesic metric. Conjugation is
g u g^-1 and is an arbitrary-element macro move. Signed left multiplication
is simulated by I-M-I without extra height, as proved in Strike #2.

The inherited conjugator theorem is used with its original hypotheses:
**both source and output elements have length <=L**, then a witness has
length <=K(L)=4L²+4L+8. It does not bound an unknown path's height.

## 1. A bounded shell in which the graph lifts to F2

**Lemma 1 (short total boundary).** Two nonidentity cyclically Dehn-reduced
words c,d with |c|+|d|+16<61 are conjugate in H_SC exactly when they are freely
conjugate. In particular this holds when both lengths are <=22.

**Proof.** Strike #2 gives cyclic rotations c1,d1 and a rung z of length <=8
satisfying z c1 z^-1 d1^-1=1 for every positive conjugacy answer. Its written
length is <61. The inherited girth lemma forces free triviality, so c,d are
free cyclic rotations. The reverse implication is automatic. ∎

This is a corollary of the existing annular theorem, not a replacement for
its hypotheses. Words of length <=22 are cyclically Dehn-reduced after free
cyclic reduction. The old 30/29 conjugacy control has total length 59 and is
correctly outside this corollary.

**Theorem 2 (free lifting through height 23).** Every H_SC macro AC path of
height <=23 starting at either A or S=(x,y) lifts to a free-group AC path
with the same endpoint representatives and height bound. Conversely free
paths in that sublevel descend unchanged.

**Proof.** Every word of length <=30 is a unique geodesic by Strike #2.
Inductively maintain that the two unique representatives normally generate
F2. Both are nonempty: an identity entry in a normally generating pair of
F2 is impossible by abelianization. Each length is therefore <=22.
Inversion and interchange lift literally. A multiplication starts with
combined length <=23, so the freely reduced product is already a unique
geodesic; it lifts literally. For a conjugation edge, freely cyclically
reduce its source and output. Their lengths are <=22 and Lemma 1 shows
that they are freely conjugate. Use a free conjugation witnessing that edge.
Normal generation in F2 persists, completing the induction. ∎

A free conjugation between bounded freely reduced words can also be expanded
into generator conjugations without raising the maximum endpoint length:
strip the source's cyclic tails, rotate the cyclic core, then build the
output's tails. Thus the generator-conjugation and macro sublevel components
coincide in this range. This statement is local; it does not assert that
arbitrary H_SC macro edges have height-preserving expansions.

**Consequence:** a connecting H_SC path of height <=23 would give an actual
free AC trivialization of AK(3). This is not an unconditional lower bound 24:
free AC triviality of AK(3) remains unknown. No height-16-to-23 graph was run.

## 2. Retained-coordinate normal form for bounded multiplication edges

For a nonempty word w, let [w] denote its signed free cyclic class (rotations
and inversion). A vertex is an unordered pair of such classes, with canonical
representatives obtained by cyclic reduction, inversion/rotation minimization,
and sorting. In the code, integer alphabet order is Y<X<x<y. These classes
are fibers of ordered states, not a new invariant of multiplication.

**Lemma 3 (connected fibers).** All ordered representatives of a fiber with
C<=H are connected by inversion, permutation and conjugation within C<=H.

**Proof.** Reduce each entry to a minimal cyclic representative, decreasing
its length, then choose signs/order, then grow the desired conjugation tails.
The pair height never exceeds the larger of the two endpoint heights. ∎

**Theorem 4 (complete normalized M-edges for H<=23).** On either endpoint
component of the bounded graph, all multiplication edges between fibers are
represented by the following finite list. For a source ([a],[b]), choose
signed cyclic rotations a,b and a freely reduced word p with

```
|p| <= floor((H-|a|-|b|)/2).
```

Form u=free(p a p^-1) and w=free(u b). Retain the edge exactly when

```
|u|+|b| <= H    and    |w|+|b| <= H.
```

Its output fiber is ([w],[b]); include both choices of changed coordinate.
The executable implementation deliberately accepts H<=15 only.

**Proof of completeness.** Start with any actual bounded edge
(u,v)->(uv,v). Write v=q b q^-1 freely, with b cyclic and
|v|=|b|+2|q|. Simultaneously conjugate the algebraic edge by q^-1:

```
(q^-1 u q,b) -> (q^-1 uv q,b).
```

Both pair heights are no larger than their original heights: the changed
entry grows by at most 2|q| and the retained entry shrinks by exactly 2|q|.
Now freely cyclically reduce q^-1u q, writing it as p a p^-1. Its exact
length is |a|+2|p|, giving the cutoff. The list therefore includes a witness
between the original two fibers. This normalizes a whole edge; it does not
use the false mixed reorder from Strike #2.

**Proof of soundness.** Move from the canonical source to the displayed
(u,b) using fiber moves, perform the actual multiplication, then move to the
canonical output. Lemma 3 and the two height tests keep this entire block
within H. Inversion, permutation and height-preserving left multiplication
supply the other orientations. ∎

The output height test must precede cyclic normalization. The new frozen
failure is (Xyx,x)->(Xyxx,x), with heights 4->5, although cyclic reduction of
the output gives (yx,x), height 3. Testing only the latter conceals a peak.
This is a counterexample to that test, not to all paths between these fibers.

**Exact ordered-state representation.** For a cyclic core a of length alpha,
let c(a) be the number of distinct signed cyclic rotations. Its number of
freely reduced signed conjugates at length alpha+2t is

```
c(a),                              t=0,
c(a) * 2 * 3^(t-1),                t>=1.
```

There are two admissible final tail letters and 3 choices for every preceding
letter. Free cyclic reduction uniquely recovers the tail and cyclic word.
For two distinct signed classes, convolve these counts under the total-height
cap and multiply by 2 for order. All reachable endpoint fibers have distinct
classes, since their exponent determinant in F2 is ±1. This grammar describes
all ordered states without listing tens of millions of words.

## 3. A genuine single-multiplication height theorem

This section supplies a bound for **one multiplication surrounded by any
number of independent conjugations**, with the linked-boundary hypothesis
below. It does not bound arbitrarily many multiplications.

For oriented cycles (c,d,e^-1), call the triple linked if no nonempty proper
sublist bounds a relation diagram. For three nonidentity cycles this is
exactly the exclusion of c~d^-1, c~e, and d~e. These are decidable by the
inherited complete conjugacy algorithm. The orientation matters.

**Lemma 5 (explicit planar area bound).** A linked triple of cyclically
reduced boundary words of total length P admitting a planar H_SC relation
diagram admits a reduced such diagram with

```
F <= 3P+3,
E_metric <= floor((61(3P+3)+P)/2) <= 92P+91.
```

Here F is the number of defining-relator cells and E_metric counts unit
letter edges. The complement has exactly three components.

**Proof.** The external input is the reduction theorem for linked boundaries
and the fact that internal arcs of a reduced diagram are pieces: Lemmas 7.15
and 9.1 in [McCammond, A General Small Cancellation Theory](https://web.math.ucsb.edu/~jon.mccammond/papers/gsct.pdf),
printed pp.81 and 90. These are the same diagram framework used in Strike #2;
we checked the linked-boundary requirement specifically for this new use.

There are no vertices of degree 1 because every region boundary is cyclically
reduced. Suppress vertices of degree 2, counting an arc as one edge for the
following Euler calculation. A connected graph with three complementary
regions in addition to its relator cells is not a single circle, so all
remaining vertices have degree >=3. Write V,E for these compressed counts,
P' for the total exterior boundary degree, and F_b for the number of relator
cells incident to an exterior edge. An interior cell has at least eight arcs:
its 61 letters cannot be covered by seven pieces of length <=8. Thus

```
V-E+F = -1,       3V <= 2E,       E <= 3F+3,
2E >= 8(F-F_b)+F_b+P',           F_b <= P' <= P.
```

Combining gives 2F<=7F_b-P'+6<=6P'+6, hence F<=3P+3.
Counting unit-edge incidences instead gives 2E_metric=61F+P, including
self-bordering edges and shared boundary edges with their multiplicities.
This proves the metric bound. ∎

**Elementary cut-path bound used below.** In a connected planar map with
three marked boundary cycles and E_metric unit edges, one can base the
boundary product using cut paths of length at most

```
Q = 4 E_metric + 4P.
```

To obtain this deliberately loose bound, choose an embedded spanning tree
and use parallel sides of its boundary tour (length at most 2 E_metric) to
join the boundary components. Prune the cut tree to the three boundaries.
Move its attachment points to the prescribed marked points along the
boundary cycles; at most two tours of the boundary words cost 2P. Parallel
copies give noncrossing cuts; doubling both allowances yields the displayed
bound, covering shared edges, repeated vertices and either side of a cut.
Cutting opens a disk. Its boundary identity reads the outer cycle as a product
of the two conjugated inner cycles, in one of the two orders. Filling the
relator cells makes this an equality in H_SC. Either order is an allowed
left/right multiplication, so no order-swapping conjecture is needed.

**Theorem 6 (linked one-M normal form).** Suppose endpoint pairs (u,v) and
(w,z) have C<=L, z is conjugate to v (signs/order can be absorbed), and a
block with one multiplication and otherwise only independent conjugations
connects them. Cyclically Dehn-reduce u,v,w to c,d,e. If their oriented triple
(c,d,e^-1) is linked, there is such a block of at most four conjugations and
one signed left/right multiplication, with height at most

```
Phi_1(L) = 3000(L+1).
```

All its conjugators can consequently be chosen of length <=K(Phi_1(L)).

**Proof.** Absorbing the existing conjugations gives an equation expressing a
conjugate of w as a product of conjugates of u and v, and hence a planar
three-boundary diagram. Cyclic Dehn reduction tracks conjugacy without
increasing these word lengths. The total boundary length satisfies P<=2L:
|c|+|d|<=L and |e|<=L. Lemma 5 and the cut construction supply a,b of length
at most Q=4E_metric+4P such that

```
e = (a c a^-1)(b d b^-1)
```

or the product in the other order. Move u to a c a^-1 and v to b d b^-1 by
two conjugations, multiply, then conjugate e to w and b d b^-1 to z. The
maximum height is at most 4Q+2L. Since

```
E_metric <= 184L+91,
Q <= 744L+364,
4Q+2L <= 2978L+1456 <= 3000(L+1),
```

the claimed bound follows. Apply K only now, to endpoints already bounded
by Phi_1. A signed left multiplication costs I-M-I in the original convention;
the two neutral inversions do not raise height. ∎

This theorem is restricted. A loop on both conjugacy classes needs no
multiplication and is already controlled by conjugation. Identity and other
unlinked cases are not silently included in Theorem 6. In particular equal
coordinate conjugacy classes can occur on arbitrary H_SC normally generating
pairs; F2's abelianization cannot exclude them globally. The linked hypothesis
is checkable and holds for the frozen nondegenerate short controls.

**Controls.** Both inherited counterexamples remain unchanged. Phi_1 allows
positive excess, and Theorem 6 replaces an entire one-M block, rather than
asserting that the old reorder with its chosen conjugator lowers height. A
new literal one-cell diagram has boundary lengths 20,20,21 and P=61. Its
three linkage tests are exact: each tested pair has total length plus 16
below 61, and is not freely conjugate, so Lemma 1 applies. The independent
checker verifies the defining-relator word and these exclusions. It checks
finite data and arithmetic, not a machine-formalized topological proof.

## 4. Fixed-coordinate blocks and a bounded positive-certificate probe

**Theorem 7.** Keep v fixed. Allow arbitrary conjugations of u and signed
multiplication of u by v. Then (u,v) reaches (w,v) by these moves exactly when
u and w are conjugate in H_SC / normal_closure(v).

**Proof.** The moves descend to conjugation or identity in that quotient.
Conversely, a positive conjugacy gives, in H_SC,

```
w = g u g^-1 * product_j h_j v^(epsilon_j) h_j^-1.
```

After conjugating u by g, append each factor using C(h_j^-1), M(v^epsilon_j),
C(h_j) on the changing coordinate. This restores the old prefix and appends
exactly the desired conjugate. Every step fixes v. ∎

This is an exact mixed-block characterization. It is not a decision algorithm
unless the forced relative quotient's conjugacy problem is solved. It does
not pick a new separator quotient. A certificate with m factors, conjugators
of length <=D, and initial conjugator length <=D yields, for endpoint/input
lengths <=L, the coarse constructive height bound

```
2L + 4D + m(2D+L).
```

The fixed braid coordinate suggests the specific presentation
<x,y | xyxYXY,R1,R2>. Three tightly capped exact rewriting/coset probes did
not produce a positive certificate. Their limits and outputs are preserved
in `experiments/third_strike`; nothing is inferred from those failures.

## 5. Why these local bounds do not solve the alternating block

Choose a hypothetical path lexicographically minimizing height, number of
maximum-height states, path length, then total shortest-conjugator length.
This minimum exists if a connecting path exists. Repeated ordered states
can be deleted. Consecutive same-target conjugations merge; different-target
conjugations can be reordered with decreases first. Inversions and permutations
are transported using the proved left/right symmetries. These statements
survive the frozen controls.

But Theorem 6 bounds one pants diagram using **its own three boundary words**.
Gluing many multiplication diagrams introduces internal boundaries whose
lengths are precisely the missing quantities. The retained coordinate is also
copied into a multiplication and passed to subsequent moves: discarding this
information loses the ordered AC derivation. There is no proof that the
result is one linked planar diagram with only four short exterior boundaries.
If handles are present, the Euler term itself becomes

```
F <= 3P + 3(b-2+2g),
```

rather than a bound from P alone. Neither genus/branching complexity nor the
number or lengths of seams is bounded here. A short van Kampen proof of an
endpoint normal-closure identity is not automatically an AC path.

Likewise, K(H), the bound on simple-path length
(2*3^H-1)^2-1, and Phi_1(H) all remain conditional on H. Substituting these
functions into one another does not give an upper bound on H.

**Logical correction to the proposed pump test.** For every fixed L, there
are finitely many endpoint pairs with C<=L. Each connected pair has some
finite path and hence a finite minimum peak. Taking a maximum over the
finitely many connected pairs gives a finite bound. Thus an infinite family
of uniformly short endpoints with unbounded *minimum* peaks cannot exist
in this finitely generated group. For one fixed comparison a finite-bound
implication always exists classically (vacuously if disconnected). The task
is to exhibit an integer and prove it works, not to disprove bare finiteness.

More generally, with effective word/conjugacy decisions, a computable uniform
height bound for all endpoint pairs is equivalent to deciding AC connectivity:
a bound gives a finite graph; conversely decide which finitely many short
pairs connect, find paths for those positive pairs, and take their maximum
height. This does not prove undecidability in H_SC. It identifies the missing
algorithmic content of an unrestricted mixed-block normal form.

**OPEN:** effective control of internal seams or multiplication depth on a
minimal path for the fixed A,S comparison. No global mixed-peak theorem, fixed
height upper bound, new separating invariant, or full orbit verdict follows.
