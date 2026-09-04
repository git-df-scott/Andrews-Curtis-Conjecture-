# Multi-seam minimality: what is bounded and what remains open

Fourth strike, based on `a7f4adfd24983c5566e8e551ecb01b5fc760dd73`.
The group, marking, AK(3) words, geodesic metric and macro moves are exactly
those in HSC_PEAK_LEMMA.md. Put C(u,v)=|u|+|v|. Conjugation means g u g^-1.
All assertions below concern this full conjugation convention.

## 1. Seams retain both signed conjugacy classes

Write a block as C0 M1 C1 ... Mm Cm, where each C portion may also contain
inversions and permutations. Track coordinate labels through permutations;
signed left multiplication uses the inherited I-M-I simulation. For g in
H_SC, write [g]± for its conjugacy class together with that of g^-1, and

    lambda(g) = min{|h| : h belongs to [g]±}.

This minimum is computable using the inherited conjugacy decision: enumerate
words up to the length of a supplied representative, in shortlex order.
Choose a shortest representative for each class, then sort the two choices.
No long Dehn residue is called a geodesic or a canonical representative.

The seam type q is the unordered **pair, with multiplicity** {[u]±,[v]±}; its width is
rho(q)=lambda(u)+lambda(v). Let q0 be the initial type and qi the type just
after Mi. Then qm is the final type. A raw seam also records the ordered
geodesic words, the changed slot, signs, and the multiplication witnesses.
Those data are necessary to replay a path. The two-class type is sufficient
only for the excision theorem below. One retained class alone is insufficient.

## 2. Excision and a conditional multiplication count

**Lemma 1 (height-preserving fiber bridge).** If two ordered states have the
same type q, they are connected by at most five I/P/C macro moves at height
at most the larger endpoint height.

**Proof.** Permute to match the classes. Invert coordinates as necessary.
Replace each coordinate by the required conjugate, doing all length decreases
before increases. With two coordinates, the sum during these replacements
is at most the larger original/final sum. Inversions and permutation preserve
length. Identity coordinates need no conjugation. Each nontrivial conjugation
has both endpoint element lengths <=H, so the inherited K(H) supplies a
conjugator if a bounded witness is wanted. We do not bound H this way. ∎

**Minimality convention.** Among hypothetical paths between the fixed
endpoints choose a lexicographic minimum of

    (maximum height, number of M moves, total macro moves,
     sum of shortest conjugator lengths).

This is a tuple of natural numbers; every nonempty set of such tuples has a
least member. Shortest conjugator lengths exist. This deliberately puts M
count before path length and omits peak multiplicity as an earlier tie-break.
We do not silently claim the same excision proof for a different ordering
that first minimizes the number of maximum-height states.

**Theorem 2 (no repeated seam types).** Such a minimal path has qi!=qj for
all 0<=i<j<=m.

**Proof.** Replace the subpath between the two equal types by Lemma 1's
bridge. Height does not rise and j-i>0 multiplications disappear. This
strictly improves one of the first two coordinates of the minimality tuple,
regardless of the number of new conjugations. ∎

**Theorem 3 (conditional count).** If all these seam types have width <=R,
then

    m <= T(R)-1,
    T(0)=1,   T(R)=1+8R*3^(R-1) for R>=1.

**Proof.** A class pair of width <=R has a canonical ordered pair of freely
reduced shortest representative words with combined length <=R. This gives
an injection into the set of such word pairs; including identities, signs
and ordered duplicates in the upper bound is harmless. There are a0=1 and
an=4*3^(n-1) freely reduced words of length n>=1. Thus

    T(R)=sum_{i+j<=R} ai*aj = 1+8R*3^(R-1).

There are m+1 distinct types by Theorem 2. ∎

This is **not N(L)** in terms of external endpoint length. Substituting the
unknown peak H for R is circular. The exact count is independently checked
by convolution. At R=23 it is 5,774,114,968,057, an ambient upper bound,
not the size or an estimate of either component.

## 3. Off-diagonal seams make the linked hypothesis explicit

Call a type diagonal if its two signed classes agree. On a nonidentity,
non-diagonal path with no repeated successive types, every one-M triple
satisfies the inherited linked hypothesis.

Indeed, write the changing, retained and new classes as [a]±,[b]±,[c]±.
The forbidden oriented conjugacies a~b^-1, a~c, b~c would respectively give
a diagonal source, a loop on the seam type, or a diagonal output. Their
exclusion is exactly what the linked one-M theorem needs. Signs and order
do not affect this sufficient test. A first identity coordinate cannot
appear away from a diagonal source: u v^epsilon=1 implies [u]±=[v]±.

**Conditional gluing theorem.** Suppose a connecting path has seam width
<=R and every one-M piece is linked. If its external endpoints have C<=L,
it has a replacement of height

    3000(max(L,R)+1).

Insert shortest seam representatives using Lemma 1. Each one-M piece now
has endpoints bounded by max(L,R), so apply the inherited Phi_1 to each
piece separately. Every replacement starts and ends at the chosen common
seam representatives. Concatenate them. There is no iterated Phi_1 and no
dependence on m in the maximum height. K applies after this height bound.

For a minimal off-diagonal path, the preceding paragraph supplies linkage
automatically. For a path crossing a diagonal, it does not. Neither avoidance
of diagonals nor a bound on R is established for the fixed AK(3) comparison.
No unconditional global height file or enumeration follows.

## 4. A genuine local two-M seam bound

**Theorem 4 (switched target, two M moves).** Consider exactly two
multiplications with arbitrary C portions and neutral moves, with external
states of height <=L. If the second multiplication changes the other
coordinate lineage, the central seam has width <=2L.

**Proof.** Its class pattern, after tracking permutations, is

    (a,b) -> (c,b) -> (c,d).

The central seam contains the initial retained class b and the final
retained class c. Hence rho<=lambda(b)+lambda(c)<=2L. No conjugator is
bounded or discarded in this argument. ∎

More precisely the bound is the sum of those two particular exterior
coordinate lengths. If successive seam types are distinct and all three
types are non-diagonal/nonidentity, Section 3 and Phi_1 give a two-M
replacement at height <=3000(2L+1), with K of that height. This is a **local
two-M theorem only**, not S(L) for an arbitrarily long mixed region.

For the same target, the pattern is instead

    (a,b) -> (c,b) -> (d,b),

and c is absent from both exterior pairs. That is the first genuinely
uncontrolled canonical seam in this decomposition. In longer switched-target
runs the neighboring external data of a two-M subblock are themselves
internal seams; Theorem 4 does not turn them into the global endpoint L.

## 5. Exact cancellation and the diagram obstruction

In the inherited liftable domain, all multiplication words are free geodesics.
If k letters cancel at each side of u v^epsilon, then

    k=(|u|+|v|-|u v^epsilon|)/2,
    C_after-C_before=|v|-2k.

There is no constant bound on k even on normally generating H_SC pairs.
Let un=x y^n and vn=Y^n X y. They form a free basis: first replace x by
x y^n, then left-multiply y by un^-1. Their product is y. Since y has
infinite order, |un| tends to infinity, and |vn|>=|un|-1. The geodesic
Gromov product (|un|+|vn|-1)/2 is therefore unbounded. Finite n=1..13
controls have exact unique-geodesic words and cancellation n+1. This does
not contradict a bound depending on an already bounded state or prove a
minimal-path pump.

The inherited relator-window certificate independently proves y has infinite
order: every defining 31-letter window contains at least ten x/X letters;
no nonzero power of y admits a Dehn rewrite or represents identity.

Two successive switched multiplications already demonstrate the copying
issue: (a,b)->(ab,b)->(ab,bab). A pants piece uses b as an input boundary
while the AC operation also retains b for the next state. Gluing that
boundary simultaneously to the next piece and to a retained-coordinate
cylinder is branched, not an ordinary surface gluing. Separate copies need
equality labels and extra boundary/corridor data. The frozen x,y example
also rejects the literal identity ab=(ab)(bab). It does not purport to
exclude every possible four-boundary surface in H_SC.

Thus the three-boundary Euler estimate cannot be applied to the whole
derivation with only its short exterior words until copying constraints
and internal boundaries are controlled. An arbitrary small-area equality
diagram need not retain an AC derivation with the required seam data.

## 6. Pumps and the remaining statement

The frozen families in HSC_SEAM_4.md grow seams but have lower replacements.
They are not peak-minimal pumps. For fixed exterior length L there are only
finitely many endpoint states. Each connected pair has a finite minimum
peak, a finite minimum M count at that peak, and a finite chosen path. Taking
maxima over those finitely many pairs proves bare finite bounds exist.
It supplies no integer or computable function witnessing the bounds.

Consequently an endlessly inflated block with fixed endpoints cannot disprove
bare existence of a bound for peak-minimal paths. A valid obstruction would
need to refute a specified proposed bound/shortening rule or establish an
effective impossibility theorem. Neither has been obtained for the full
architecture. The fixed AK(3) comparison, its canonical seam-width bound,
and its global height upper bound remain **OPEN**.
