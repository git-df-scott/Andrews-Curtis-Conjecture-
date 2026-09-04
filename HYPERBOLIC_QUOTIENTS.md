# Hyperbolic-quotient feasibility audit — 2026-09-04

## Verdict

**YELLOW.** Infinite hyperbolic quotients are not ruled out, and quotienting
gives an exact one-way obstruction: different Andrews–Curtis components in a
quotient imply different components in the free group.  The unresolved gate is
not the word or conjugacy problem.  It is an exact, terminating method—or a
strictly weaker proved obstruction—for AC components of **normally generating**
pairs.  No such method was found in the audited literature.

Gilman–Myasnikov prove that the full AC transformation group acts faithfully on
every nontrivial orbit for a non-elementary torsion-free hyperbolic group.  This
does **not** say that there is one orbit, that two given pairs are in the same
orbit, or that orbit equivalence is decidable.  Thus their theorem neither kills
nor completes this route.

## Exact target and induced moves

Let

```text
P = <x,y | r1,r2>,       R=(r1,r2) in F2^2,
q : F2 ->> H,            q(R)=(a,b).
```

The classical elementary AC moves and their images in `H^2` are

| free-group move | induced move in `H^2` |
|---|---|
| `r1 -> r1^-1` | `(a,b) -> (a^-1,b)` |
| `r2 -> r2^-1` | `(a,b) -> (a,b^-1)` |
| `r1 -> r1 r2^e`, `e=+-1` | `(a,b) -> (a b^e,b)` |
| `r2 -> r2 r1^e`, `e=+-1` | `(a,b) -> (a,b a^e)` |
| `ri -> w ri w^-1`, `w in F2` | `q(ri) -> q(w)q(ri)q(w)^-1` |

Because `q` is onto, the last line permits independent conjugation of either
coordinate by every `h in H`.  If a homomorphism is not onto, the honest target
is its image `q(F2)`, and only conjugators in that image are induced.

Left multiplication is not additional information: for example, right-multiply
`a` by `b`, then conjugate the result by `b`, obtaining `ba`.  Relator
permutations are likewise products of inversion and multiplication moves (or
may harmlessly be included as redundant generators).  Consequently every free
AC path maps edge-for-edge to an AC path in `H`:

```text
R ~AC S in F2  ==>  q(R) ~AC q(S) in H.                 (1)
```

The contrapositive of (1) is the desired certificate theorem.  The converse is
false in general: a quotient can merge free-group orbits.

### Simultaneous automorphisms are different

A simultaneous `alpha in Aut(F2)` sends

```text
(r1,r2) -> (alpha(r1),alpha(r2)).
```

This is not one elementary relator move.  AC-triviality is covariant under it:
apply `alpha` to every word in a path, and note that the basis
`(alpha(x),alpha(y))` is Nielsen—and hence AC—equivalent to `(x,y)`.  A **fixed**
quotient map does not give the equality
`q(alpha(ri))=q(ri)`; it gives evaluation under `q o alpha`.  Therefore:

- one explicit fixed epimorphism `q` is enough for a sound separation;
- a presentation-coordinate-independent *survey* must transform `q` by
  precomposition, or take a proved orbit/spectrum over marked epimorphisms;
- quotient automorphisms may be used only as an additional coarsening after
  proving how they act.  They can merge components and therefore lose power,
  though they cannot manufacture a valid separation.

The exact object is the component

```text
[q(R)]_AC in pi_0(Delta_2(H)),
```

where vertices of `Delta_2(H)` are normally generating pairs.  This component
label is invariant by definition.  Calling it *computable* requires more: a
terminating equality test or a computable coarser label constant on every edge.

## Finite-quotient blindness, in the needed form

Since `P` presents the trivial group, the exponent-sum matrix of `(r1,r2)` is in
`GL(2,Z)`.  Hence in every abelian target the image pair is related to the image
of `(x,y)` by integral elementary Nielsen operations.

Borovik–Lubotzky–Myasnikov prove that if `G` is finite and
`k >= max(d_G(G),2)`, two normally generating `k`-tuples are AC-equivalent in
`G` exactly when their images are AC-equivalent in `G_ab`.  Taking `k=2` and an
epimorphism `F2 ->> G` therefore gives

```text
q(R) ~AC (q(x),q(y)) in every finite G.                 (2)
```

This covers non-soluble finite groups as well as soluble ones.  It also means
that passing a proposed infinite-target invariant through any finite quotient
of `H` cannot restore separating power.  Residual finiteness of `H` does not
help: individual unequal group elements can be separated finitely, but the two
AC components in (2) cannot.

An infinite target must therefore have an AC-component obstruction which:

1. does not factor through abelianization or through finite images;
2. is sensitive to rank-two, normally generating tuples rather than merely
   ordinary generating tuples;
3. is invariant under independent conjugation as well as Nielsen operations;
4. admits exact equality/inequality certificates;
5. preferably does not become a stable invariant after adding a trivial
   coordinate.

Word, conjugacy, normal-form and centralizer algorithms are necessary
infrastructure, not an orbit invariant.

## Quotient-family audit

| Family | Typical presentation / status | Exact algorithms | Aut/Nielsen information | Maps from `F2` | Blindness and cost |
|---|---|---|---|---|---|
| finite `C'(1/6)` small-cancellation presentations | hyperbolic; torsion-free when no defining relator is a proper power | Dehn word algorithm; conjugacy and cyclic centralizers in the torsion-free non-elementary case | no uniform Nielsen algorithm: Nielsen equivalence is undecidable across torsion-free hyperbolic/small-cancellation inputs | distinguished 2-generator presentations give an epimorphism; all epimorphisms form an infinite set | finite-image collapse remains, but not at `H`; cheap word operations, very hard AC orbit gate |
| closed orientable surface groups | `<a_i,b_i | product [a_i,b_i]>`, hyperbolic for genus at least 2 | excellent automatic/geometry algorithms | minimal generating tuples are strongly classified | **ineligible** for genus at least 2: abelianization rank `2g>2`, so no `F2` epimorphism; punctured-torus group is just `F2` | no useful rank-2 quotient obtained |
| free products / virtually free groups | calibration target `C2*C3=<s,t|s^2,t^3>` | exact reduced normal forms, conjugacy, centralizers and Bass–Serre tree | comparatively tractable; AC on normally generating pairs is still broader than Nielsen equivalence | obvious 2-generator epimorphism | not covered by the finite theorem; low/medium proof cost; likely too rigid, so use as a feasibility control |
| two-generator one-relator torsion groups | `<a,b|W^m>`, `m>1`, hyperbolic | word/conjugacy algorithms; `Out(H)` computable in the classified family | Pride/Logan classify ordinary **generating-pair** Nielsen classes; this does not classify normally generating AC pairs | obvious when the presentation uses two generators | infinite target avoids (2), but torsion complicates axes/centralizers; medium cost |
| torsion-free one-relator `C'(1/6)` groups | `<x,y|W>` with certified overlaps and `W` not a proper power | Dehn word and conjugacy algorithms; centralizers controlled | no complete AC-orbit machinery; general hyperbolic algorithms for `Aut(H)` are heavy | obvious | strong exact laboratory; medium group-operation cost, high orbit-theorem cost |
| hyperbolic triangle/orbifold groups | `Delta(2,3,7)=<s,t|s^2,t^3,(st)^7>` | automatic/Dehn algorithms; geometric conjugacy and centralizers | orbifold automorphisms manageable; ordinary Nielsen results do not automatically extend to AC | obvious | perfect and infinite, so no abelian signal; torsion is the tradeoff; medium cost |
| random groups at density `<1/2` | finite random presentations, hyperbolic with overwhelming probability | algorithms apply after a deterministic hyperbolicity/small-cancellation certificate | random groups can have multiple stabilized Nielsen classes, but that is not an AC classification | meaningful only after fixing a 2-generator certified sample | probability is not a proof for a chosen `H`; sample generation cheap, exact orbit theorem expensive |

Kapovich–Weidmann explicitly note that Nielsen equivalence is undecidable
uniformly even among torsion-free word-hyperbolic groups, via subgroup
membership, and that the obstruction persists for finitely presented
torsion-free small-cancellation groups.  Conversely, locally quasiconvex
subfamilies have finiteness results.  Neither statement decides the AC problem
for one fixed laboratory.  Also, a quotient image of an ACC relator pair is
known to **normally** generate `H`; it need not generate `H`.  Algorithms and
theorems restricted to generating tuples cannot silently be applied.

## Three ranked concrete targets

### 1. `H_SC`: perfect torsion-free `C'(1/6)` laboratory

Use the distinguished quotient on `x,y`:

```text
H_SC = <x,y |
 YXyXXXYxYxyxyyxYYXXyXXyyxyXyXYYYYXYXYYXYYXXYYYxyxyxYXYxyXYYxY,
 xYXXYXyyxyyyyyyyyxYXyxYxyyxyyXyXYxxYYYXyXyXYXYxyXYYYxxxYXYxYx >.
```

Here capitals denote inverses.  The repository exhaustively certifies:

- both cyclically reduced relators have length 61;
- the full symmetrized set has 244 distinct words;
- the longest piece has length 8, and `6*8 < 61`;
- neither relator is a proper power;
- exponent vectors are `(-7,-10)` and `(2,3)`, determinant `-1`.

Thus `H_SC` is `C'(1/6)`, torsion-free and perfect.  The checked nontrivial
generator plus perfectness rules out an elementary torsion-free hyperbolic
group, so it is non-elementary.  It supplies exact Dehn word decisions and the
centralizer structure used by Gilman–Myasnikov.  Its weakness is precisely the
missing AC-orbit algorithm.  Expected cost: milliseconds per short word,
hours–days to validate an automatic/conjugacy implementation, and unbounded
research risk for the orbit theorem.

### 2. `H_OR`: torsion-free one-relator `C'(1/6)` laboratory

```text
H_OR = <x,y |
 yXYYxYYXyXyXYxxxYYXXyyyXyyXXYYxyyXXXyXYYYXYYYxYxYXYXyxYXXXXXX >.
```

The checked relator has length 61, longest symmetrized piece 7, is not a proper
power, and has exponent vector `(-14,-7)`.  Hence `H_OR` is torsion-free
`C'(1/6)` and has abelianization `Z + Z/7`; it is not cyclic, so it is
non-elementary hyperbolic.  It is simpler than `H_SC`, but its nontrivial
abelianization provides a possible source of irrelevant signals.  Expected cost
is similar at word level and high at AC-orbit level.

### 3. `Delta(2,3,7)`: perfect hyperbolic orbifold group

```text
Delta(2,3,7) = <s,t | s^2, t^3, (st)^7>.
```

It is an infinite non-elementary hyperbolic triangle group.  Its abelianization
is trivial because the `2x2` minors `6,14,21` have gcd 1.  Normal forms and
orbifold geometry make it more tractable than a random group, and its
automorphisms are tightly constrained.  Torsion prevents direct use of the
torsion-free centralizer/faithfulness theorem and requires separate proofs for
axis-based arguments.  Expected cost: low for exact group operations; medium to
high for a complete rank-2 AC analysis.

`C2*C3` is retained immediately below these as the Bass–Serre calibration
target.  It is not promoted as a separator until a nontrivial AC component is
proved.

## What the current theorems do and do not say

- The finite theorem proves (2); it does not extend merely because an infinite
  group is residually finite.
- The hyperbolic faithfulness theorem distinguishes AC **transformations** as
  permutations; it does not distinguish the **orbits of two points**.
- Hyperbolic word and conjugacy algorithms do not decide reachability under a
  finitely generated group of transformations.
- Ordinary Nielsen equivalence preserves the generated subgroup.  AC allows
  independent conjugation and preserves only normal closure, so Nielsen
  invariants are generally invalid.
- No primary theorem located in this bounded audit proves generalized AC for
  all torsion-free hyperbolic groups or forces `Delta_2(H)` to be connected.

## Sources

- Borovik–Lubotzky–Myasnikov, [The Finitary Andrews–Curtis Conjecture](https://arxiv.org/abs/1103.1295), Theorem 1.1 and Corollary 1.3.
- Gilman–Myasnikov, [Andrews–Curtis Groups](https://arxiv.org/abs/2506.23031), Theorem 2 and its corollary.
- Kapovich–Weidmann, [Nielsen equivalence in small cancellation groups](https://arxiv.org/abs/1011.5862), especially the algorithmic warning and Theorem 1.1.
- Kapovich–Weidmann, [Freely indecomposable groups acting on hyperbolic spaces](https://arxiv.org/abs/math/0203015).
- Logan, [The outer automorphism groups of two-generator, one-relator groups with torsion](https://arxiv.org/abs/1206.2765), Proposition 2.1 and Corollary B.
- Dahmani–Guirardel, [The isomorphism problem for all hyperbolic groups](https://arxiv.org/abs/1002.2590), including the hyperbolic-group Whitehead problem.
- Kapovich–Weidmann, [Nielsen equivalence in a class of random groups](https://arxiv.org/abs/1309.7458).
