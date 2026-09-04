# Stable versus unstable information

## Definitions

Unstable AC equivalence fixes the rank and uses relator inversion, multiplication by another relator, and conjugation. Stable equivalence additionally permits adding or deleting a generator together with its matching trivial relator.

Unstable triviality implies stable triviality. The converse is exactly the gap that makes stable data potentially useless for the original conjecture.

## The `AK(3)` premise is not currently available

The campaign's former premise “`AK(3)` is stably AC-trivial” must not be used as a theorem. The chain was:

1. A misprinted presentation `W'` was treated as a Wirtinger presentation of the unknot.
2. Deleting a relator and adding a word was therefore claimed to produce stably trivial presentations.
3. One such presentation was reduced unstably to `AK(3)`.
4. The stable conclusion for `AK(3)` was then repeated and independently automated downstream.

Shehper et al. v2, Remark 14 and Appendix F, correct step 1: `W'` is not a Wirtinger presentation, and deleting different relators can even yield different groups. They retain the exact AC path from a length-25 presentation to `AK(3)` but explicitly state that those presentations are not necessarily stably AC-trivial. An unstable equivalence cannot supply the missing stable premise.

Accordingly:

- `AK(3)` unstable status: **open**;
- `AK(3)` stable status: **open in the corrected record**;
- any claimed stable certificate must be audited from its actual starting presentation through every stabilization and destabilization, not merely from the length-25 intermediate to `AK(3)`.

## Conditional design constraint

The intended design constraint remains mathematically decisive for **any** presentation `P` once a valid stable trivialization is proved.

Suppose `I_n` is an unstable AC invariant in rank `n`, and suppose it is coherently stable:

`I_{n+1}(P + <z|z>) = s(I_n(P))`

for an injective comparison `s`, with the same rule for the standard presentation. If `P` is stably AC-trivial, AC invariance along the stable path forces

`s^a(I_n(P)) = s^a(I_n(standard))`

after enough stabilizations. Injectivity then gives equality already in rank `n`. Such an invariant cannot prove that `P` is an unstable counterexample.

Even without injectivity, any invariant explicitly unchanged by stabilization is immediately blind to a stably trivial `P`.

## Automatically stabilization-blind constructions

| Construction | Why it survives stabilization | Consequence if a candidate is proved stably trivial |
|---|---|---|
| Stable homotopy type / simple-homotopy data | adding a cancelling 1/2-cell pair is precisely the equivalence built into the theory | cannot separate the unstable orbit |
| Stable module class, `K_0`, stabilized Fitting ideal | adjoining a free identity summand is quotiented out | cannot separate |
| Invariants of the 4-dimensional 2-handlebody after cancelling-handle stabilization | handle cancellation is normalized away | cannot separate |
| Any TQFT required to be invariant under all 3-deformations | stabilization is part of the move calculus | targets stable ACC, not a known-stably-trivial unstable candidate |
| Direct limits of rank-`n` AC orbit sets | the colimit intentionally identifies tuples after adding trivial coordinates | cannot recover a distinction killed in the colimit |
| Morita-stable / matrix-stable representation invariants | identity blocks vanish under stable equivalence | cannot separate |

## Genuinely unstable information to seek

The desired object must retain the fixed rank, the ordered free basis, or the precise number of 1/2-cell pairs. Viable patterns include:

- an AC-orbit invariant in `G^n` that has no injective stabilization map;
- a based crossed module in which adjoining `<z|z>` adds visible data rather than a zero summand;
- a non-semisimple state sum with a noninvertible bubble operator, reported before stabilization quotient;
- a spectrum over all thickenings that records handle number/framing rather than normalizing cancelling handles;
- a rank-graded obstruction that may vanish after one stabilization but is exact at rank 2.

“Unstable” does not excuse failure of AC invariance. It means invariant under all rank-fixed AC moves but intentionally **not** invariant under stabilization.

## Quinn's nilpotence warning

Quinn records the stabilization phenomenon: a simple homotopy equivalence of finite 2-complexes becomes a 2-deformation after wedging enough 2-spheres. Traditional invariants recoverable from stabilized data therefore cannot detect the missing 2-deformation. This is the conceptual reason that ordinary homotopy and stable algebra repeatedly collapse.

## Lackenby's additional pruning

If a candidate presentation complex is thickenable, Lackenby's Theorem 1.3 proves its **unstable** AC-triviality. Therefore a genuine counterexample must be non-thickenable. This is a necessary condition for a CE, not a sufficient one, and thickenability need not be promoted to an orbit invariant to use the positive implication.

## Required regression if a corrected stable `AK(3)` proof appears

Before changing the status, require:

1. a complete source presentation with the corrected Wirtinger relator;
2. an exact ledger including all rank changes and generator substitutions;
3. a verifier whose state includes the current generator alphabet and checks legal destabilization;
4. corrupted-ledger rejection;
5. independent replay from `AK(3)` to a standard presentation.

Then reclassify every invariant in [INVARIANT_LEDGER.md](INVARIANT_LEDGER.md): all stabilization-invariant rows become formally incapable of separating `AK(3)` from the trivial pair.

## Sources

- Shehper et al., [arXiv:2408.15332v2](https://arxiv.org/abs/2408.15332), Remark 14 and Appendix F.
- Lisitsa, [arXiv:2501.18601v1](https://arxiv.org/abs/2501.18601), the downstream claim that must be read with the correction.
- Quinn, [arXiv:hep-th/9202044](https://arxiv.org/abs/hep-th/9202044).
- Lackenby, [arXiv:2606.06122](https://arxiv.org/abs/2606.06122), Theorems 1.2–1.3.
