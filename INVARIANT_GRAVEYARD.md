# Invariant graveyard: move-level failure certificates

Every entry here failed before frontier evaluation.  The witnesses live in the
free group `F(x,y)`, which is itself a torsion-free hyperbolic group, so a
quantity that claims universal hyperbolic-target AC invariance must survive
them.  Several witnesses are executable in `tests/test_invariant_audit.py`.

Write `C_h^i` for independent conjugation of coordinate `i` by `h` and `M_ij`
for multiplication of coordinate `i` on the right by coordinate `j`.

## Exact elementary witnesses

Start with `U=(x,y)`.

1. `M_12` gives `U1=(xy,y)`.
2. `C_y^1` followed by `C_x^1` gives
   `U2=(x y x y^-1 x^-1, y)`.

Both are in the same AC orbit as `U`; in particular both normally generate
`F2`.

For `U2`, use the homomorphism to `S3`

```text
x -> (23),     y -> (12).
```

The two entries of `U2` both map to `(12)`, so their ordinary generated image
has order 2.  The entries of `U` generate all of `S3`.  Thus `U2` does not
generate `F2`, even though it normally generates it.  This is a compact exact
certificate that AC independent conjugation can leave the ordinary Nielsen
domain.

Also,

```text
|cyclic([x,y])| = 4,
|cyclic([x y x y^-1 x^-1, y])| = 12.
```

Conjugate elements of a free group have equal cyclically reduced length, so the
two commutators are neither conjugate nor inverse-conjugate.

## Rejected quantities

| Proposal | Move that kills it | Proof / counterexample | Disposition |
|---|---|---|---|
| individual word or cyclic length | multiplication | `(x,y)->(xy,y)` changes length multiset `(1,1)` to `(1,2)` | heuristic only |
| individual conjugacy classes | multiplication | `x` and `xy` are not conjugate in `F2` (different cyclic length) | conjugacy invariance is only one AC move |
| translation-length multiset | multiplication | in the Cayley tree, stable translation lengths change from `(1,1)` to `(2,1)` | dead |
| axes / endpoints / marked boundary dynamics | multiplication; relative data also independent conjugation | the axis/endpoints of `x` are replaced by those of `xy`; separately conjugating one coordinate moves only its axis | dead unless quotiented by the entire AC action |
| marked length spectrum built from `a,b` | multiplication | the marked word `a` acquires the length of `ab`; re-marking is exactly the Nielsen/AC action one is trying to classify | dead in raw form |
| simultaneous conjugacy class of the pair | independent conjugation | `U` ordinarily generates `F2`, while `U2` does not; simultaneous conjugacy preserves the generated subgroup up to conjugacy | dead |
| ordinary Nielsen class | independent conjugation | same `S3` witness: Nielsen moves preserve the ordinary generated subgroup, while `U~AC U2` | dead |
| Whitehead-minimal length / Whitehead graph of the tuple | independent conjugation and multiplication | it is an ordinary Nielsen-orbit tool; `U,U2` are outside one Nielsen orbit despite being AC-equivalent | useful subroutine, not an AC invariant |
| subgroup geometry of `<a,b>`: index, quasiconvexity, core graph, limit set | independent conjugation | `<U>=F2`, but `<U2>` is proper by the `S3` witness | dead; normal closure is the preserved subgroup notion |
| commutator conjugacy class `[a,b]` up to inverse | independent conjugation | cyclic lengths 4 and 12 for `U,U2`; the familiar rank-2 Nielsen theorem does not extend to independent AC conjugation | dead |
| centralizer/axis **configuration** of the two entries | independent conjugation | each centralizer is conjugated by an independently chosen element, so relative position/intersection data has no diagonal equivariance; coarsenings that retain only “cyclic/noncommensurable” are constant on normally generating pairs in a non-elementary torsion-free target | raw configurations dead |
| stable commutator length of the coordinates | domain failure and multiplication | ACC image coordinates need not lie in `[H,H]`; on unrestricted `H^2`, `(c,c)->(c^2,c)` changes `scl(c)` whenever `scl(c)>0` | dead as a total pair invariant |
| `scl([a,b])` | independent conjugation | in `F(x,y)`, `(x,x)` has trivial commutator and scl 0; conjugating only the first entry by `y` gives `(yxy^-1,x)`, whose commutator is nontrivial and has scl `1/2` by the free-group gap theorem | dead as a universal `H^2` invariant; a restriction to `N_2(H)` would require a new target-specific proof |
| bounded-cohomology / homogeneous-quasimorphism evaluations on coordinates | multiplication | `phi(ab)` is not generally `phi(a)`; even a genuine homomorphism such as exponent sum gives an immediate change | dead raw; a block invariant needs a new symbolic identity |
| unmarked representation variety `Hom(H,K)//K` | none—constant for the wrong reason | it depends only on `H`, not on `(a,b)` | valid but useless |
| marked trace/character/representation evaluations | multiplication | `tr(r_i r_j)` is not determined by `tr(r_i)` and need not equal it; conjugacy invariance alone is insufficient | dead raw; also subject to finite-specialization no-go arguments |
| `Aut(H)`-orbit of the pair | multiplication | a coordinate Nielsen move need not be induced by an automorphism of `H`, especially when the pair only normally generates | dead unless a target-specific extension theorem is proved |
| finite quotients or finite representations of `H` | all moves descend, but components collapse | BLM: rank-2 normally generating components of every finite image are controlled by abelianization; the candidate and basis agree | provably incapable |
| soluble, nilpotent or `MN` quotient shadows | components collapse by the existing generalized-AC theorems | already audited in `INVARIANT_LEDGER.md` | provably incapable; not rerun |
| finite-radius AC balls, hashes, neighborhood counts | boundary of the ball | applying one move changes which vertices lie within radius `R`; two balls failing to meet proves only distance `>2R` | search diagnostic only |
| random-walk distributions / learned embeddings | no exact move equality | distribution depends on start, generators, time and sampling error | never CE evidence |
| Dehn-reduced word representatives | multiplication and independent conjugation | they solve equality in a chosen `H`; they are not constant under pair moves | infrastructure only |
| normal-closure membership samples | incomplete and usually constant | both the basis image and every ACC relator image normally generate `H`; bounded sampling cannot certify unequal closures | valid closure invariant, no separation here |

## What survived these failures

Only the exact AC component, or a genuinely new function proved constant on
that component, survives all moves without becoming constant for an obvious
reason.  In particular:

- “geometric” does not imply “AC-invariant”;
- ordinary Nielsen classification does not solve the normally generating
  problem;
- exact group normal forms make move evaluation rigorous but do not turn a
  changing statistic into an invariant;
- quotient-specific equalities can merge proposed values and lose information,
  never justify skipping a move proof.

Any attempt to revive a graveyard entry must include a new formula and prove
the complete identities in `INVARIANT_CANDIDATES.md`; renaming or aggregating
the same raw numbers is not sufficient.

For the scl witness, see Calegari, [scl](https://arxiv.org/abs/math/0605354),
for the free-group gap theorem used in the exact `0` versus `1/2` comparison.
