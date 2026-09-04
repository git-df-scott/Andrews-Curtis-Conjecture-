# Astra invariant-first attack matrix

No attack below earns candidate compute until its “AC gate” is proved. Costs are for the first theorem-bearing prototype, not an open-ended run.

## Hyperbolic-strike disposition

The focused audit leaves the hyperbolic route **YELLOW**. Its exact orbit is a
valid invariant, but no nonconstant computable factor is known. The old generic
hyperbolic prototype is replaced by the fixed `SC-AC-PEAK-1` experiment in
`ASTRA_HANDOFF.md`. The unbased crossed-module lane is now structurally closed;
only a based degree-at-most-3 nonfactorization gate remains.

## Ranked matrix

| Rank | Attack | Why it might separate | Why no-go results do not kill it | Stabilization behavior | Exact computation | Positive result | Negative result | First-gate cost |
|---:|---|---|---|---|---|---|---|---|
| **1** | `SC-AC-PEAK-1` in fixed `H_SC` | a global `C'(1/6)` peak-reduction theorem could compress exact rank-2 AC components without finite images | finitary, `MN`, and soluble theorems do not cover this perfect non-elementary torsion-free hyperbolic target; AC faithfulness does not imply transitivity | keep `H_SC^2` rank-specific; do not pass to a stable direct limit | prove termination plus confluence or a finite plateau theorem for exact Dehn-geodesic pair rewrites, including arbitrary independent conjugation; then run controls | different canonical labels give a rigorous quotient obstruction | equality closes this target/label; nonfinite peak types kill the scheme, not ACC | hard cap 96 CPU-hours / 32 GiB for the theorem prototype; no frontier evaluation before proof |
| **2** | Based crossed-module / Peiffer degree-3 gate | a nonstable based filtration might retain 2-cell-basis information | only the **unbased** crossed module is now proved to collapse; a based nonfactorizing quotient is not ruled out | adjoining `<z|z>` must remain visible | derive all three basis maps symbolically and first test factorization through boundary/Fox/nilpotent/stable data | a nonfactorizing exact functor earns controls, not yet a CE | factorization or one failed move closes degree 3; do not auto-increase depth | 1–3 CPU-days, bounded |
| **3** | Non-semisimple sliced-2-complex state sum | noninvertible/nilpotent sectors may retain 2-deformation data that semisimple theories collapse to homology | Bobtcheva–Quinn's impossibility result assumes the semisimple setting; Kaden identifies the full local-relation issue rather than proving all theories trivial | record the bubble/stabilization operator; do not normalize it to the identity; rank-2 value may vanish after stabilization | implement the complete Quinn/Kaden movie generators and relations; use exact tensors over a number field/finite characteristic as algebra (not a finite group quotient); mechanically verify every movie relation before evaluating five controls | differing exact values after all relations give a CE certificate | equality for a theory closes that theory; failure of a movie relation rejects the theory before candidate use | relation gate 10–500 CPU-hours; candidate tensor contraction potentially GPU-days |
| 4 | Algebraic-specialization no-go theorem | does not directly separate, but can eliminate enormous families of futile trace/character/determinant attacks | it extends rather than conflicts with the finite-quotient theorem; analytic, nonalgebraic, or non-specializable objects may escape | classify whether stabilization commutes with specialization | formalize: an AC-invariant difference over a finitely generated ring that persists under some maximal-ideal specialization induces forbidden finite-image separation; check hypotheses for proposed representation schemes using Gröbner/elimination certificates | a proof prunes a broad class and isolates exact loopholes | a failed hypothesis identifies the non-specializable feature Astra should exploit | 20–100 CPU-hours plus algebraic proof |
| 5 | Spectrum of all admissible 4-thickenings with Floer/gauge labels | a set-valued spectrum removes the arbitrary choice of one thickening while retaining boundary/framing information | known reductions concern chosen thickenings or semisimple invariants; a presentation-level spectrum with non-semisimple labels is not covered | keep handle number and cancelling-pair action explicit; do not stable-normalize connected sums | enumerate rotation systems/framing data for rank-2 complexes; prove AC moves biject spectra; compute exact boundary 3-manifolds and certified Floer/correction-term packages | disjoint spectra certify non-AC | overlapping spectra close only the chosen label; enumeration blow-up quantifies infeasibility | high/extreme: weeks to months; proof gate before Floer compute |
| 6 | AC-invariant `u`-substitution groupoid spectrum | all substitution decompositions may carry structure even though a single substituted group is choice-dependent | McDermott's 2026 examples kill the raw derived group, not the groupoid of all choices with AC-induced functors | remember rank/basis in objects; study explicit effect of adding a trivial pair | enumerate bounded symbolic decompositions only after proving a finite complete presentation of the groupoid or a functorial quotient; replay move-induced equivalences | differing complete spectra certify non-AC | equivalence closes the chosen quotient and prevents re-running naive substitutions | 2–10 CPU-days for formal gate; weeks if a finite quotient survives |
| 7 | Neuwirth thickenability certification | a positive answer invokes Lackenby and proves unstable AC-triviality without finding a move path | not an invariant-separation attempt; it is theorem-backed positive pruning | Lackenby separately proves stable and unstable conclusions | implement/validate the combinatorial thickenability decision; emit rotation-system/3-manifold certificate; test `AK3`, both MS(2) blocks, then `AK4` | candidate removed from CE queue by theorem | non-thickenable remains open; it only becomes eligible for other attacks | 1–10 CPU-days after locating a trusted implementation; no search expansion |

## Required control order

Every surviving invariant implementation must run in this order:

1. standard rank-2 presentation;
2. `AK(2)` and at least one second known AC-trivial control;
3. every intermediate state of the frozen Carreras `P4 ~ AK(3)` ledger—value must be identical step by step;
4. `AK(3)`;
5. `AK(4)`;
6. one representative each of `C1` and `C2`.

A mismatch on step 2 or 3 is an implementation/theorem failure, not a discovery. Only exact inequality after those gates is admissible.

## Astra top three

### 1. `SC-AC-PEAK-1`

Run the exact theorem-gated peak-reduction experiment in the fixed perfect
torsion-free `C'(1/6)` target. This is the most direct attempt to construct the
missing computable factor of the true quotient AC orbit.

### 2. Bass–Serre classifier in `C2*C3`

Use exact virtually-free normal forms to seek a terminating complete AC
classifier for normally generating pairs. It is a cheaper calibration and a
possible separator in its own right; transitivity would close only this target.

### 3. Orbifold classifier in `Delta(2,3,7)`

Exploit the perfect hyperbolic triangle group and its orbifold normal forms.
Torsion requires fresh move proofs, and ordinary generating-pair Nielsen results
cannot be substituted for normally generating AC classes.

The based Peiffer degree-3 test is fallback only. Non-semisimple sliced state
sums remain an independent longer-term avenue, not one of the top three for this
hyperbolic strike.

## Hard stop conditions

Stop an attack immediately if:

- its value changes along the Carreras certificate;
- invariance is shown only for conjugation but not relator multiplication;
- the implementation uses numeric tolerance where equality is the theorem;
- its separation necessarily descends to a finite, nilpotent, or soluble quotient;
- it factors through ordinary homology, simple homotopy type, or a stable module class;
- its “negative result” is only failure to connect within a resource cap.

## Sources

- Gilman–Myasnikov, [arXiv:2506.23031](https://arxiv.org/abs/2506.23031).
- Bobtcheva–Quinn, [arXiv:math/0012212](https://arxiv.org/abs/math/0012212).
- Kaden, [arXiv:1012.2228](https://arxiv.org/abs/1012.2228).
- McDermott, [arXiv:2608.18929](https://arxiv.org/abs/2608.18929).
- Lackenby, [arXiv:2606.06122](https://arxiv.org/abs/2606.06122).
