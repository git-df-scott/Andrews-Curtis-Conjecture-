# H_SC: proved conjugator shortening and the remaining peak lemma

Second strike, 2026-09-04. This document proves a bound on individual
conjugation edges and short-level barriers. It does **not** prove an upper
bound on the height of an AK(3)-to-standard AC path.

## 1. Fixed group, metric, and moves

The presentation is exactly the one in `acsearch/hyperbolic.py` at `82fe261`:

```
H_SC = <x,y | R1,R2>
R1 = YXyXXXYxYxyxyyxYYXXyXXyyxyXyXYYYYXYXYYXYYXXYYYxyxyxYXYxyXYYxY
R2 = xYXXYXyyxyyyyyyyyxYXyxYxyyxyyXyXYxxYYYXyXyXYXYxyXYYYxxxYXYxYx
```

Capital letters denote inverses. The epimorphism F(x,y) -> H_SC sends each
free generator to its named image. Ordered comparison states are

```
A = (xxxYYYY, xyxYXY)    # canonical AK(3), not a reconstructed convention
S = (x,y).
```

Let |w| denote **group geodesic length** for {x,X,y,Y}, and put
C(u,v)=|u|+|v|. The abstract normal form is the first minimum-length
representative in shortlex order x<X<y<Y. It is computable: enumerate words
up to the length of a supplied representative and use the Dehn word decision
to compare them. This existence algorithm is finite but can be expensive.
The implementation returns exact, unique representatives in the proved
radius-30 ball and explicitly refuses to call longer Dehn residues geodesic.
No general long-word geodesic computation was needed for the local controls.

Edges: invert one coordinate; right-multiply one coordinate by the other or
its inverse; interchange coordinates; or replace u by g u g^-1 for arbitrary
g in H_SC, keeping v fixed (and symmetrically for v). Conjugations here are
**macro edges**. Their expansion into generator conjugations need not preserve
the same height bound. Both conventions have the same unrestricted orbits.
Left multiplication is height-preservingly redundant: v u is obtained from
u by inversion, right multiplication by v^-1, and inversion again. Thus one
may include signed left multiplication in peak classifications without
changing any sublevel component.

Both relators have length 61; the symmetrized set has 244 distinct words;
maximum piece length is 8; neither relator is a proper power. The first-strike
C'(1/6) certificate and standard small-cancellation consequences therefore
still apply: the Dehn algorithm solves the word problem, and the group is
torsion-free and hyperbolic. Nonidentity x follows also from Lemma 1 below.
Its exponent matrix has determinant -1, so it is perfect and noncyclic;
a nontrivial torsion-free elementary hyperbolic group would be cyclic.
No new quotient has been selected.

## 2. Exact local geometry

**Lemma 1 (girth 61; unique geodesics through radius 30).** No nonempty freely
reduced word of length less than 61 is identity in H_SC. Every freely reduced
word of length at most 30 is the unique geodesic for its element.

**Proof.** If a shorter nonempty null word existed, exact length-decreasing
Dehn rewriting would take it to the empty word. Consider the last rewrite,
on a freely reduced word p A q, using a cyclic relator R=A B of length 61.
Its replacement p B^-1 q freely reduces to 1. In the free group, q=B p^-1,
so the preceding word is freely equal to p R p^-1. A conjugate of a cyclically
reduced word of length 61 has freely reduced length at least 61, contradicting
the strictly decreasing sequence. For the second statement, two distinct
freely reduced representatives, each of length at most 30, would give a
nonempty freely reduced null word of length at most 60. A shorter competing
representative for any such word is excluded in the same way. ∎

This does not assert that every Dehn-reduced word is geodesic. The inherited
53/55 witness remains a regression control. In particular C(A)=13 and C(S)=2
are exact, not heuristic word lengths.

A piece is a nonempty common prefix of two distinct symmetrized relators.
For each cyclic relator start, partition an initial segment into k consecutive
pieces. The exhaustive maxima for k=1,...,5 are

| k | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| maximum covered letters | 8 | 13 | 17 | **23** | 28 |

There are 202 pieces. The certificate records all 244 rows; its independent
checker uses pairwise prefix extraction and recursive partitioning instead
of the producer's prefix counts and sets of reachable cut positions.
These are finite combinatorial facts about two fixed words.
**Ordinary C'(1/8) is false**: 8*8 >= 61. The next proof uses the four-piece
condition, not a misapplication of the C'(1/8) conjugacy theorem.

**Lemma 2 (annular rung reduction).** If nonidentity cyclically Dehn-reduced
words c,d are conjugate in H_SC, there are cyclic rotations c1,d1 and a piece
z, or z=1, with d1=z c1 z^-1. One may choose |z|<=8. Every cell of the
reduced annular diagram used here meets each boundary in one arc of length
at least 15 and at most 30.

**Proof.** Use a reduced annular diagram for the conjugacy, allowing coincident
boundary portions, bridges, and self-bordering cells. Its internal arcs are
pieces, and its underlying map is a C(6)-map. An exposed cell has one external
arc. Cyclic Dehn reduction bounds this arc by 30 letters. Its internal
complement has at least 31 letters and is a consecutive concatenation of its
internal arcs. Four or fewer pieces cover at most 23 letters (the table also
covers k<4), so the internal degree is greater than 4.

Apply the annular C(6)-map lemma: exposed degrees >4 on both boundaries imply
that every cell has two boundary arcs, one on each boundary, and at most two
internal arcs. This is the precise external combinatorial input, Lemma 7.3
in [McCammond, *A General Small Cancellation Theory*, printed p.73](https://web.math.ucsb.edu/~jon.mccammond/papers/gsct.pdf).
The internal-arc justification is Lemma 9.1, printed p.90; this argument
specializes the proof of Lemma 9.4 while replacing its C'(1/8) assumption.

The resulting annulus consists of ladders and possibly shared boundary arcs.
Cut across a rung, or at a common boundary vertex if present, and choose the
corresponding basepoints on c,d. The rung is a piece of length <=8; a common
vertex gives the empty word. A diagram with no cells gives ordinary free
cyclic conjugacy. This yields the claimed equation. For any cell, the two
rungs contribute at most 16, and the opposite side at most 30. Its remaining
side consequently has length at least 61-16-30=15. Both sides are subarcs
of cyclically Dehn-reduced boundary cycles and so are at most 30. ∎

**Corollary 2a (short conjugacy).** If one of c,d above has length <15, the
annulus has no cells; c,d are free cyclic rotations. Thus any cyclically
reduced word of length <15 is of minimum length in its entire H_SC conjugacy
class: a shorter representative could be freely cyclically reduced and would
fall under this corollary. If a freely reduced conjugate also has length <15,
its free cyclic core is a rotation of the original word.

This is more information than ball injectivity: short words can in general
be conjugate by long elements through quotient relations. The annular proof
is needed to exclude that phenomenon in this particular range.

## 3. Complete conjugacy and an explicit conjugator bound

**Theorem 3 (bounded endpoints, arbitrary original conjugator).** For elements
u,v with |u|,|v|<=L, if v=g u g^-1 for any g in H_SC, then the same equality
has a witness g' with

```
|g'| <= K(L) = 4*L^2 + 4*L + 8.
```

Individual conjugacy in H_SC is decidable by a finite rotation-and-piece
algorithm. The implementation `conjugacy_witness` either returns a witness
in the stipulated direction or returns `None` after the complete decision.

**Proof.** Choose representatives of u,v of length at most L. Freely cyclically
reduce each, and repeatedly rotate to expose a Dehn rewrite, perform the
length-decreasing rewrite, and cyclically reduce again. Track the conjugation
basepoint, obtaining c=t u t^-1 and d=h v h^-1. Each successful iteration
strictly reduces the current word length, so there are at most L iterations.
The initial cyclic strip costs at most L letters of conjugator. A rotation
and a subsequent strip cost at most 2L per iteration. Consequently

```
length(t), length(h) <= 2*L^2 + L.
```

This coarse estimate also permits gratuitous free cancellation and shorter
input representatives. No step asserts that the resulting words are geodesic.
If either cyclically Dehn-reduced word is empty, conjugacy holds exactly when
both are empty, with g'=1. Otherwise use Lemma 2. Write c=p c_tail,
d=q d_tail and choose rotations c1=p^-1 c p, d1=q^-1 d q. For a rung z,

```
d1 = z c1 z^-1,
g' = h^-1 q z p^-1 t,
v  = g' u g'^-1.
```

There are finitely many rotations and just 203 candidate rungs (including 1).
Check each equation using the exact Dehn word decision. Lemma 2 proves
completeness of a negative answer. Since |p|,|q|<=L and |z|<=8, the displayed
K(L) follows. Freely reducing g' only improves the estimate. ∎

**Centralizers and exceptions.** For a particular original witness g, the
element g'^-1 g belongs to C_H_SC(u). Infinite centralizer powers therefore
do not have to be enumerated: they give the same conjugation output. For
u=1 the centralizer is the whole group and the witness 1 suffices. There is
no torsion case in this group. Short elements are handled by Corollary 2a,
not discarded as exceptional inputs. The proof does not require finding
primitive roots or generators of centralizers.

**Scope.** The bound applies when the source **and the output** of the
conjugation are bounded. In an AC graph restricted to C<=L this includes
every internal conjugation edge. It says nothing about the height reached
by some unknown connecting path. Enumerating words of length K(L) is also
unnecessary: one can test conjugacy between candidate vertices directly.
A complete algorithm for edges is not an algorithm for unrestricted components.

**Concrete quotient-specific control.** The JSON includes a symmetrized
relator R=z u z^-1 v^-1 with z=Y, |u|=30, |v|=29. Both u,v are cyclically
reduced unique geodesics (Lemma 1), yet conjugate. The producer returns z=Y;
the independent checker verifies the literal relator decomposition. This
rejects the false substitution of free conjugacy for H_SC conjugacy outside
the short range. It also shows geodesic conjugate lengths need not have the
same parity globally; parity below 15 comes from Corollary 2a alone.

## 4. What is proved about peaks

**Theorem 4 (AK(3) first-exit barrier).** Every AC path from A to a state with
C<13, if one exists, visits a state with C>=15. In particular any eventual
peak bound for A to S must be at least 15.

**Proof.** The components of A have cyclic lengths 7 and 6, each <15. By
Corollary 2a neither can be shortened by conjugation. Inversion and permutation
preserve the lengths. As long as no multiplication or length increase has
occurred, the state consists of independent cyclic rotations and inversions
of these two words, possibly interchanged. There are 14 and 12 choices.
For all 168 products a b the minimum **cyclically** freely reduced length is
9 (frozen exact product table). Actual freely reduced product length is no
smaller; it is at most 13, hence is an exact geodesic by Lemma 1. Right/left
products, both signs, and interchanged target are covered: ab and ba are
cyclic conjugates, and inversion reverses their order. A multiplication
therefore produces total length at least 9+6=15.

A conjugation taking one of these words outside its current minimum length
cannot increase its length by just one while the new total is <=14: the new
component has length at most 8, so its freely reduced geodesic has the same
free cyclic core and differs in length by an even number. Thus a first exit
by conjugation also has total length at least 15. Neutral steps alone cannot
reach C<13. ∎

This proof is a finite local product computation plus a conjugacy theorem,
not an AC component enumeration. It gives no upper bound and no separation.

**Theorem 5 (counterexample to endpoint-height/monotone reduction).** The
assertion that every pair of connected states admits a path of height at
most the maximum endpoint complexity is false in this exact H_SC, even on
normally generating pairs. It is false for both C=sum and C_max=max.

**Proof.** Use the explicit AK(2) pair T=(xxYYY,xyxYXY). Its component lengths
are 5 and 6. The analogous 120-product table has minimum cyclic product
length 7. At sum <=11, arbitrary conjugation cannot leave a component's
minimum length without exiting the sublevel, and multiplication produces
total at least 7+5=12. Thus T cannot reach any shorter state within sum 11.
At maximum <=6, the length-5 component cannot move to length 6 (Corollary 2a),
the length-6 component cannot grow, and multiplication forces a component
of length at least 7. Thus maximum 6 also traps the short conjugacy plateau.

Nevertheless T is connected to S: the certificate replays the prescribed
14-move chain on printed p.64 of
[Havas–Ramsay (2003)](https://staff.itee.uq.edu.au/havas/2003hr.pdf), with six
initial inversion/conjugation moves and three endpoint cleanup moves.
All 23 steps are verified as free-group identities, so they descend to H_SC.
The maximum sum is 15 and the maximum individual length is 8, all inside the
unique-geodesic ball. No path search was used. ∎

No claim of smallest possible obstruction is made. Theorem 5 disproves a
specific zero-excess peak claim, **not** an arbitrary computable excess bound,
not the fixed AK(3) peak theorem, and not H_SC's suitability as a separator.
There must be a minimal-height AK(2) path whose peak cannot be reduced to
endpoint height; the certificate does not claim each two-edge peak in the
published path is locally irreducible.

## 5. Peak cases and the exact unresolved step

Signed inversions and permutation are isometries. Permutation transports
move targets; coordinate inversions transport right to left multiplication
or reverse signs. The height-preserving left-multiplication simulation from
Section 1 makes these valid symmetries. These neutral moves cannot be one
side of a **strict** two-edge peak. They must still be handled on plateaus.

| Adjacent types, up to reversal/symmetry | Exact reduction / limitation |
|---|---|
| I-I, I-P, P-P | Neutral; no strict peak |
| I-C, P-C, I-M, P-M | Neutral edge; transport using the above isometries when moving along a plateau |
| C-C, same target | Compose the two conjugators into one macro edge; removes the intermediate state |
| C-C, different targets | Commute them; perform the decreasing coordinate first at a strict peak |
| M-M | Opposite multiplications on the same target cancel; other cases need further analysis |
| C-M or M-C | Algebraic reorder exists, but its intermediate height is uncontrolled |

For different-target conjugations, write the original segment as
(u,v)->(u',v)->(u',v'). A strict peak means |u'|>|u| and |v|>|v'|.
The alternative intermediate (u,v') is below the peak (indeed below both
endpoints). For same-target conjugations the composition is legal with no
restriction on the conjugator. Theorem 3 gives bounded witnesses for either
replacement **once their endpoint heights are bounded**.

Here is the precise mixed obstruction to the tempting proof:

```
(u,v) -> (gug^-1,v) -> (gug^-1 v,v)
```

has an algebraically valid reorder

```
(u,v)
 -> (u,g^-1 v g)
 -> (u g^-1 v g,g^-1 v g)
 -> (g u g^-1 v,g^-1 v g)
 -> (g u g^-1 v,v).
```

The replacement exposes g^-1 v g, whose length is not bounded by Theorem 3
unless its output length is already bounded. Applying that theorem here to
infer a height bound is circular. The finite positive identities in this
reorder are tested; no height assertion is attached to them. This is a gap
in that proposed argument, not proof that every alternative reorder fails.

**Explicit failure of this reorder, even with a shortest conjugator.** Take
u=x, v=y, g=yxy. The original three states have complexities 2,8,7. The
reordered five states have complexities 2,6,11,11,7. All words have length
at most 7, so these are exact geodesic complexities. Moreover |g x g^-1|=7
forces every conjugator producing that output to have length at least 3;
the displayed g is shortest. Thus merely choosing a shortest conjugator
does not make this particular mixed reorder lower peaks. The certificate
checks the two paths and the lower bound. It does not assert that some other
path between these endpoints cannot avoid the peak.

For perspective, no finite conjugator bound can depend on the source length
alone in this group. The family y^n x y^-n contains infinitely many distinct
outputs. In a torsion-free hyperbolic group centralizers of nonidentity
elements are cyclic (for example, the preliminaries of
[Bogopolski–Ventura, *On endomorphisms of torsion-free hyperbolic groups*](https://archive.mpim-bonn.mpg.de/id/eprint/3335/1/preprint_2008_136.pdf)): if a nonzero power of y commuted with x, x,y would both
lie in its cyclic centralizer and commute, contrary to Lemma 1 applied to
their length-4 commutator. Hence the outputs are distinct. Finitely many
bounded conjugators cannot realize them all. This standard centralizer fact
is not needed for the constructive bound in Theorem 3.

**OPEN:** an explicit B for the fixed A,S comparison; peak reduction of
alternating multiplication/conjugation blocks; a complete AC-orbit algorithm;
a separating invariant. Neither Theorem 3 nor the local barrier resolves
any of these. No component enumeration is authorized by the current results.
