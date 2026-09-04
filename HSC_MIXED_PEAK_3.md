# HSC-MIXED-PEAK-3 execution ledger

2026-09-04. Base `ecaa80a263ce4ec739a953d1be0a69bdeafffb6c`; continuation
branch `astra/third-strike`. No old campaign file or frozen counterexample
was altered. The previous 48 tests remain part of the full test run.

## Results separated by status

| Status | Result | Scope |
|---|---|---|
| **PROVED** | Every H_SC path through height 23 from either endpoint lifts to F2 | Consequence of the inherited annular rung and girth bounds; no orbit verdict |
| **PROVED** | Complete retained-coordinate normal form for bounded multiplication edges | The cutoff comes from the input height; actual output height is checked before cyclic reduction |
| **PROVED** | Linked one-M block has Phi_1(L)=3000(L+1) | At most four conjugations and one multiplication, with neutral signs/order absorbed; does not cover arbitrarily many M moves |
| **PROVED** | Linked planar triple: F<=3P+3 and metric edges <=92P+91 | Explicit Euler/piece calculation; linked reduction is a stated external mathematical input |
| **PROVED** | Fixed-coordinate blocks equal conjugacy modulo that coordinate's normal closure | Exact algebraic equivalence; does not assert the relative quotient has a decision algorithm |
| **PROVED + COMPUTATIONALLY VERIFIED** | Complete height-15 components are disjoint; any full connecting path has height >=16 | Full sublevel completeness, no full-orbit separation |
| **COMPUTATIONALLY VERIFIED** | 26 AK(3) fibers, 23,774 standard symmetry vertices; exact ordered counts and exit predicates | Independent canonical and raw ordered controls; deterministic machine-readable graphs |
| **DISPROVED** | Testing cyclic output length suffices to bound the actual multiplication peak | New literal 4->5->3 witness; regression added |
| **DISPROVED AS A PROPOSED MECHANISM** | Uniformly bounded endpoints can have unbounded minimum connecting heights | Finitely many endpoint pairs; this does not supply a computable bound |
| **FAILED BOUNDED EXPERIMENT** | Fixed-braid relative presentation probes might produce a direct positive block certificate | KB capped at 20 seconds/1,000 rules; two coset probes capped at 512 rows; no positive certificate, no negative inference |
| **HEURISTIC** | Internal seam control might extend the one-M diagram bound | No invariance or completeness claim |
| **OPEN** | Arbitrary alternating-block bound, fixed AK(3) upper bound, full orbit comparison | Multiplication count and internal boundary lengths remain uncontrolled |

## What was actually computed

1. Loaded the three requested strike/proof files, code, all frozen controls,
   and ran the second-strike independent checker. No literature campaign or
   quotient selection was restarted.
2. Derived the fixed-coordinate theorem. Tried precisely its forced braid
   presentation, not a new separator. Scripts, hard limits, versions and
   exact observations are in `experiments/third_strike`. No proof resulted.
3. Proved the height-15 graph normalization before traversal. A plain pilot
   on the standard side hit its explicit cap; the proved order-eight action
   then made the **same** finite query complete. No height was increased.
4. Completed both sublevel components. Their full domains, normalization,
   counts, boundary predicates, runtimes and independent checks are in
   `HSC_HEIGHT_15_SHELL.md`. No raw 58-million-state enumeration was needed.
5. Derived the planar linked-diagram bound and explicit one-M height bound.
   The only narrow source check was the precise linked-boundary reduction
   hypothesis in the same McCammond source used by Strike #2.
6. Verified a literal one-cell pants control, the missing-output-height
   counterexample, all 24 normalized first exits at height 16, and the
   inherited AK(2)/mixed-reorder failures. All 66 tests pass.

No AK(3) connecting path was found. No global B was proved. Therefore the
conditional full-orbit enumeration and counterexample gates were not opened.
No `HSC_HEIGHT_BOUND.md` or `HSC_COMPLETE_COMPONENT.md` is created; the complete
**sublevel** result is named separately to prevent that ambiguity.

## Reproduction and certificate meaning

Production code is `acsearch/hsc_mixed.py`; the independent checker is
`scripts/check_third_strike.py`; regressions are `tests/test_third_strike.py`.
All use exact words and integers. The normal-form API remains explicitly
restricted; no long Dehn residue is used as a geodesic. The pants example's
length-40 written product equals its independently certified length-21
geodesic by a literal defining relator.

```sh
python -m acsearch.hsc_mixed
python scripts/check_third_strike.py
python -m pytest -q
sha256sum -c certificates/SHA256SUMS
sha256sum -c certificates/SECOND_STRIKE_SHA256SUMS
sha256sum -c certificates/THIRD_STRIKE_SHA256SUMS
```

The main producer regenerates complete height-15 graphs only. A target hit
stops before producing a noncontact certificate. The optional relative probes
are not test dependencies and are not rerun by this producer.

Independent verification means separate algorithms and code for finite
claims. The annular theorem remains inherited; the new planar and cut-path
arguments are written mathematics, not a Lean/Coq formalization or an
independent human review. No separation certificate is claimed.

## Stop condition and single fourth strike

Stop condition **F**. The finite one-M theorem does not satisfy the requested
full-path trigger B. Disproving the two shortcuts, correcting the pump test,
and locating the new local barrier do not satisfy global stop condition D.

**HSC-SEAM-4 — effective control of internal boundaries in a minimal mixed
block.** Use the proved one-M bound as a local module. Prove a bound on the
number and lengths of the internal boundary words, retaining the ordered
relator data when multiplication copies the retained coordinate. Treat
unlinked/degenerate triples explicitly. The theorem must apply to the fixed
AK(3)-to-standard comparison and must not substitute exterior perimeter for
uncontrolled interior seams. Start from the 26-fiber/24-exit certificate as
constraints; do not repeat height-15 enumeration or conduct a height sweep.
Only a well-founded global decrease or an explicit seam bound can open the
full finite-orbit gate.
