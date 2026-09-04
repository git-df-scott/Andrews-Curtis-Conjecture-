# Astra invariant-first attack matrix

No attack below earns candidate compute until its “AC gate” is proved. Costs are for the first theorem-bearing prototype, not an open-ended run.

## Ranked matrix

| Rank | Attack | Why it might separate | Why no-go results do not kill it | Stabilization behavior | Exact computation | Positive result | Negative result | First-gate cost |
|---:|---|---|---|---|---|---|---|---|
| **1** | Infinite non-soluble hyperbolic-quotient orbit invariant | rank-2 tuple orbits can contain geometric/dynamical information absent from abelianization | finitary, `MN`, and soluble theorems do not cover non-elementary torsion-free hyperbolic targets; Gilman–Myasnikov show the AC action is faithful on nontrivial orbits | keep `G^2` rank-specific; do not pass to a stable direct limit | choose explicit automatic hyperbolic `G` and maps `F2->G`; compute exact normal forms, normal generation, and a *complete* orbit invariant/decision procedure (e.g. certified canonical JSJ/boundary/current data); prove all three AC moves preserve it | different values give a rigorous ACC counterexample | equality rules out that target/invariant only; use it to prune a target class | 1–4 CPU-weeks plus proof work; prototype controls in 10–100 CPU-hours |
| **2** | Based crossed-module / Peiffer orbit invariant | retains identities among relators and the chosen 1/2-cell basis even though the presentation complex is contractible | ordinary homotopy and stable module no-go results discard precisely this based higher data | adjoining `<z|z>` must add a visible generator-relation pair, not a zero/stable summand | construct finite truncations of the free crossed module; derive explicit maps for inversion, multiplication and conjugation; quotient only by proved Peiffer relations; canonicalize rank-2 objects and compare controls/candidates | unequal exact based objects, plus the naturality theorem, certify non-AC | collapse at truncation `d` sets a lower bound on useful depth and may prove a whole family of module invariants blind | symbolic prototype 1–3 CPU-days; deep truncations 1–4 CPU-weeks and heavy RAM |
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

### 1. Hyperbolic-quotient orbit invariants

Best balance of relevance and formal cleanliness. Functoriality supplies elementary AC invariance at the orbit level, word and conjugacy problems are decidable, and recent work supplies nontrivial action structure. The missing theorem is a computable complete-enough orbit obstruction.

### 2. Based crossed modules

Best algebraic route to genuinely unstable information. It explicitly refuses the stable module quotient that makes familiar invariants blind. Begin by proving the move functor on a tiny nilpotent/degree truncation and run the Carreras stepwise gate.

### 3. Non-semisimple sliced state sums

Best topological route. The semisimple family is dead, but the precise Kaden movie-relation list gives a concrete proof harness. Candidate tensors come only after that harness is green.

The specialization no-go project should run as a cheap preflight alongside attacks 1–3: its purpose is to kill attractive but doomed linear variants before they consume Astra time.

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
