# Astra handoff

## Mission

Astra is not being handed a longer word search. It is being handed a sequence of theorem gates whose successful endpoint is a checkable AC-orbit separator.

## Ground truth to load

1. `AK(3)` is the smallest unresolved rank-2 object (length 13).
2. At length 14, use three **certified connected blocks**, not six independent candidates:
   - `C0={AK3,P3,P4}`;
   - `C1={P1,P6}`;
   - `C2={P2,P5}`.
3. `C1~AK3` and `C2~AK3` are not public theorems with replayable ledgers. They remain possible equivalences.
4. The full length-14 stratum has not been classified.
5. `AK(4)` (length 15) is open. `AK(n>=5)` is length-reducible, not known trivializable.
6. Corrected stable status of `AK(3)` is open; do not encode stable triviality as a fact.
7. Any thickenable named candidate is AC-trivial by Lackenby.

## First 72 compute-hours

These are bounded gates, not a search launch.

| Budget | Task | Required artifact | Stop/pass criterion |
|---:|---|---|---|
| 2 h | Reproduce repository tests in a pinned environment | test log with commit SHA | all tests pass, including corrupted-ledger rejection |
| 6 h | Implement stepwise invariant harness interface | value recorded after every elementary/packaged move | known controls constant; otherwise reject implementation |
| 16 h | Prototype Neuwirth thickenability encoding for rank 2 | independently checkable rotation-system or obstruction record | positive settles candidate; negative only routes onward |
| 24 h | Survey 2–3 explicit torsion-free hyperbolic targets and exact normal-form libraries | target dossier with proofs of word/conjugacy decidability and explicit maps | reject any target whose proposed separator reduces to bounded BFS |
| 24 h | Formalize the algebraic-specialization preflight | theorem statement plus mechanized tests on trace/Fox proposals | prune all proposals satisfying the finite-specialization hypotheses |

Do not automatically consume unused hours. Stop after producing the artifacts and request mathematical review.

## Invariant harness contract

Every module must expose logically equivalent operations:

```text
value(presentation) -> exact serialized object
check_invert(state, relator_index) -> proof/check result
check_multiply(state, target, source, sign) -> proof/check result
check_conjugate(state, relator_index, conjugator) -> proof/check result
compare(value_a, value_b) -> exact equal / exact unequal / unknown
stabilize(value) -> exact value or explicit unsupported
```

The result `unknown` is valid. A timeout must map to `unknown`, never `unequal`.

## Mandatory five-object test suite

For each invariant candidate, compute only after the move proof passes:

| Role | Object |
|---|---|
| trivial endpoint | `<x,y|x,y>` |
| AC-trivial control | `AK(2)` plus a one-move synthetic control |
| primary frontier | `AK(3)` |
| next frontier | `AK(4)` |
| length-14 control/frontier | `P4=MS(3,y^-1 x^2 y^-1)` along all 13 packaged Carreras moves; then representatives `P1` and `P2` |

`P4` and `AK(3)` **must** have equal output because an exact certificate is present. If they differ, the object is not an invariant or the implementation is wrong.

## What would constitute a genuine counterexample

For a balanced presentation `P=<x1,...,xn|r1,...,rn>`, a counterexample proof needs both:

1. a rigorous proof that the normal closure of `(r1,...,rn)` is all of `F_n`, equivalently that `P` presents the trivial group; and
2. a rigorous proof that `(r1,...,rn)` is not in the elementary AC orbit of `(x1,...,xn)`.

Acceptable forms for item 2 are:

- an explicitly defined invariant `I`, a proof that every elementary AC move preserves `I`, exact computations of `I(P)` and `I(standard)`, and a proof those values differ; or
- a terminating, proved-correct decision procedure for AC orbit equivalence that returns “different,” with a replayable proof object.

A **CEC** should package the presentation, trivial-group proof, invariant/decision theorem in a proof-checkable form, exact endpoint computations, tool versions/hashes, and an independent verifier that rejects corrupted inputs.

There is currently no known general finite certificate format for non-AC-equivalence. A positive path has an obvious finite certificate; nonexistence of all finite paths does not. Consequently there is no CEC now. A new invariant theorem or a complete orbit-decision theorem is required.

The following are not item 2:

- a hard or famous presentation;
- BFS/beam/greedy/RL/ATP failure;
- non-membership in a published solved table;
- a lower bound on AC distance, however large;
- separation in a restricted move graph;
- stable triviality or failure to find a stable path;
- a numerical feature not proved invariant.

## Decision tree

1. **Thickenability positive?** Mark the object AC-trivial by Lackenby; archive the certificate; stop work on it.
2. **Proposed invariant fails a single frozen move?** Reject the invariant; do not tune it on candidates.
3. **Proposed quotient is finite, nilpotent/`MN`, or soluble?** Reject as a separator by theorem.
4. **Proposed invariant is unchanged by stabilization?** It targets stable ACC; retain only if the candidate's stable status remains genuinely open and the theorem is otherwise sound.
5. **Exact unequal values after all gates?** Freeze code/data, obtain independent replay, and turn the invariance argument into a formal theorem before using “counterexample.”
6. **Equal or unknown?** Record which invariant/target was ruled out. Do not increase word-search depth as a fallback.

## Data and reproducibility requirements

- Pin the repository commit, Python packages, algebra system and target-group implementation.
- Hash every presentation after parsing and every certificate ledger.
- Store exact integers, rationals, algebraic numbers, finite presentations or normal forms—never only floating-point summaries.
- Record whether equality is proved, disproved, or unknown.
- Separate mathematical theorems from experimental search observations in every schema.
- Expand packaged moves to elementary moves for final proof artifacts.
- Make corrupted-value, corrupted-move and wrong-endpoint tests mandatory.

## Recommended program order

1. Thickenability positive-pruning on `AK3`, `C1`, `C2`, `AK4`.
2. Algebraic-specialization no-go theorem to prune linear representation ideas.
3. Hyperbolic-quotient orbit invariant prototype.
4. Based crossed-module degree/truncation prototype.
5. Non-semisimple sliced-state-sum movie-relation verifier.
6. Only after one of 3–5 passes its theorem gate, allocate high compute to the five-object suite.

## Approaches Astra must not repeat

- open-ended direct search for an `AK(3)` trivialization;
- the rank-2 length-at-most-12 census or a broad length-13 census;
- finite-group/finite-quotient enumeration for separation;
- abelian, nilpotent, metabelian, or soluble representation sweeps;
- semisimple Quinn/Bobtcheva state sums on contractible complexes;
- raw augmented Fox determinants or Smith forms;
- raw trace/character values without invariance under relator multiplication;
- one arbitrarily chosen 4-thickening presented as an invariant of the presentation;
- raw `u`-substitution groups without a functorial all-choice construction;
- neural embeddings, t-SNE clusters, policy values, neighborhood sizes, or hardness labels as CE evidence;
- treating Carreras's GS bottleneck 27 as a full-AC lower bound;
- treating absent or private Shehper ledgers as published proof;
- treating the invalidated stable `AK(3)` premise as settled;
- converting spare compute into overnight BFS, beam, MCTS, PPO, or Prover9 runs.

## Final handoff state

- **CE: no**
- **CEC: no**
- **Smallest genuinely unresolved objects:** `AK(3)` (length 13); the `C0` class at length 14 is the same question, while the `C1` and `C2` MS(2) blocks are not yet publicly connected to it; `AK(4)` follows at length 15.
- **Strongest remaining invariant avenue:** exact rank-2 AC-orbit information in computable infinite non-soluble, preferably torsion-free hyperbolic, quotient groups.
- **Three best Astra attacks:** (1) hyperbolic-quotient orbit invariant, (2) based crossed-module/Peiffer invariant, (3) non-semisimple sliced-2-complex state sum.
- **Astra MUST NOT waste time repeating:** finite/soluble quotient sweeps, semisimple TQFTs, unproved numeric features, naive Fox/trace/substitution values, known censuses, restricted-graph noncontact, or longer direct search.
