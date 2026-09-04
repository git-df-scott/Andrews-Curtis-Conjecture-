# Andrews-Curtis Conjecture: search framework and literature status

`acsearch` is a small Python package for studying balanced presentations of the
trivial group under Andrews-Curtis (AC) moves:

- `acsearch.words` - free-group words, reduction, cyclic canonical forms
- `acsearch.presentation` - presentations, canonical forms modulo signed
  generator permutations (a subgroup of Aut(F_n), under which AC-triviality is
  invariant)
- `acsearch.moves` - elementary AC moves (certificate moves) and the
  length-bounded cyclic-word move set used for exhaustive closure
- `acsearch.search` - greedy best-first search (Shehper et al. 2024 style) and
  breadth-first closure of the standard presentation within a length bound
- `acsearch.verify` - certificate replay and Todd-Coxeter check that a
  candidate really presents the trivial group (via sympy)
- `acsearch.candidates` - Akbulut-Kirby AK(n), Miller-Schupp MS(n,w), the
  classical two- and three-generator candidates, and the six length-14
  Miller-Schupp presentations that resisted greedy search
- `acsearch.hyperbolic` - exact `C'(1/6)` certificates and a Dehn word-problem
  reducer for the two fixed infinite hyperbolic laboratory groups
- `acsearch.invariant_audit` - bounded move-level controls and frozen
  counterexamples for quantities that fail AC invariance

Run the tests with `python3 -m pytest tests`.

Status of the conjecture itself (checked September 2026): open. No
counterexample or counterexample certificate is known. The audited campaign
documents are:

- [`STATUS.md`](STATUS.md) — executive status and bounded calibration
- [`FRONTIER_2026.md`](FRONTIER_2026.md) — canonical theorem-level frontier
- [`INVARIANT_LEDGER.md`](INVARIANT_LEDGER.md) — invariant proof gates and no-go results
- [`STABLE_VS_UNSTABLE.md`](STABLE_VS_UNSTABLE.md) — stabilization constraints and the corrected `AK(3)` status
- [`CANDIDATE_LEDGER.md`](CANDIDATE_LEDGER.md) — exact candidate routing
- [`ATTACK_MATRIX.md`](ATTACK_MATRIX.md) — ranked invariant-first attacks
- [`ASTRA_HANDOFF.md`](ASTRA_HANDOFF.md) — bounded high-compute handoff and CE/CEC criteria
- [`HYPERBOLIC_QUOTIENTS.md`](HYPERBOLIC_QUOTIENTS.md) — exact quotient action,
  finite blindness, concrete target families, and YELLOW verdict
- [`INVARIANT_CANDIDATES.md`](INVARIANT_CANDIDATES.md) — the surviving orbit
  object and theorem gates for a computable factor
- [`INVARIANT_GRAVEYARD.md`](INVARIANT_GRAVEYARD.md) — elementary-move
  counterexamples for rejected geometric/algebraic quantities
- [`CONTROL_RESULTS.md`](CONTROL_RESULTS.md) — bounded replay and
  small-cancellation validation
- [`AK_RESULTS.md`](AK_RESULTS.md) — frontier outputs after the invariant gate
- [`PEIFFER_FALLBACK.md`](PEIFFER_FALLBACK.md) — crossed-module collapse and
  the smallest justified based experiment

Search failure is never treated as evidence of non-equivalence.
