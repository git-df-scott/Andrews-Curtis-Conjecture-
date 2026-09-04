# SC-AC-SHORTEN-2 execution ledger

Date: 2026-09-04. Base: `82fe261d3ef925db37bdc293210005aa63d8eb7d`.
Branch: `astra/second-strike`. First-strike work was pushed first as requested;
the remote first-strike branch was already up to date. No token is retained
in repository files or the remote URL.

## Results by epistemic status

| Status | Result | Evidence / precise scope |
|---|---|---|
| **PROVED** | Girth 61 and unique geodesics through radius 30 | HSC_PEAK_LEMMA, Lemma 1; Dehn exactness plus last-rewrite argument |
| **PROVED** | Annular rotation-and-piece reduction in this H_SC | Four consecutive pieces cover <=23<31; annular C(6)-map lemma; not a C'(1/8) assumption |
| **PROVED** | K(L)=4L²+4L+8 | Source and conjugation output both bounded by L; identities and arbitrary conjugators included |
| **PROVED** | Complete individual conjugacy algorithm | Cyclic Dehn reduction; all cyclic rotations; all 202 pieces and empty rung; exact word decisions |
| **PROVED** | Every connecting AK(3) path has sum peak >=15 | Short-conjugacy classification plus all 168 local products; a lower bound only |
| **COMPUTATIONALLY VERIFIED** | Required finite overlap and product facts | Independent string checker; frozen JSON and digest |
| **COMPUTATIONALLY VERIFIED** | AK(2) -> standard | Fixed published chain, 23 fully replayed moves including normalization; maximum sum 15, maximum component 8 |
| **COMPUTATIONALLY VERIFIED** | Quotient-specific conjugacy of distinct short geodesics | One literal defining relator; cyclic lengths 30 and 29; rung Y |
| **DISPROVED** | Connected endpoints always admit a path at endpoint height | AK(2) plateau, for both sum and maximum complexity; positive path certifies connectedness |
| **DISPROVED** | The displayed mixed reorder always lowers a strict peak when its conjugator is shortest | u=x,v=y,g=yxy: peak 8 becomes 11; shortest conjugator length 3 |
| **DISPROVED** | Conjugator bound depending only on source length | Infinitely many outputs y^n x y^-n; distinguishes this false claim from the proved bounded-output lemma |
| **HEURISTIC / FAILED DIAGNOSTIC** | Random short walks might supply a simple cyclic local trap | Prescribed bounded sample found none; no inference follows |
| **OPEN** | Fixed AK(3) peak upper bound; general mixed-peak shortening; AK(3) orbit in H_SC | No component enumeration and no separation claim |

No stronger invariant survived arbitrary multiplication/conjugation in this
strike. Only two complexity choices were assessed: geodesic sum and maximum.
Both zero-excess claims fail on the same certified control. No heuristic score
was tuned. H_OR was left unchanged because the missing upper-bound theorem
has not been obtained for H_SC.

## Finite computation specifications

| Task | Domain and normalization | Completeness / state count |
|---|---|---|
| Piece extraction | Two inherited length-61 words, all rotations/inverses | 244 words; 29,646 distinct unordered pairs in independent checker; 202 pieces |
| Consecutive-piece test | Each cyclic relator start, k=1,...,5 pieces | All 244*5 maximum-cover entries; endpoints/recursive cuts 0..61; no sampled overlaps |
| AK(2), AK(3) local multiplication | Cyclic rotations and inversions of the two prescribed words | 120 and 168 products; all signs, targets and handedness follow from cyclic/inversion symmetry |
| Published AK(2) positive control | One fixed ledger; free reduction only | 24 ordered states, 23 verified transitions; no search |
| Annular positive control | First single-relator decomposition R=z u z^-1 v^-1 in the fixed finite symmetrized order; rung length 1..8, boundary lengths 15..30 | Stops on first positive witness; no claim of exhaustive nonexistence; one frozen literal relation is sufficient |
| Mixed-reorder negative control | Two prescribed short paths, g=yxy | 3 and 5 state occurrences, 6 transitions in total; a failure of that replacement rule only |
| Bounded walk diagnostic | Seed 26090402; 128 walks from (x,y), 48 steps each; legal nonidentity elementary moves, freely reduced total <=24 | 6,144 prescribed moves; 3,232 sampled states satisfy the local-test filter; no cyclic strict traps; sampling is not exhaustive |
| Complete H_SC AC component | **Not run** | No B; zero component states enumerated |

All displayed local state lengths are exact by Lemma 1. The walk diagnostic
also examines cyclic free reductions of states with sum <=24; their product
lengths are within the unique-geodesic range. Its lack of traps has no
negative force. The deterministic transcript digest is in the JSON; the
independent mathematical certificates do not rely on this diagnostic.

Producer: `acsearch/hsc_shortening.py`. Independent checker:
`scripts/check_second_strike.py`, stdlib-only, importing no producer code.
The checker verifies finite hypotheses and explicit witnesses; it is not an
independent human review or a formalized proof of the cited annular theorem.
Its PASS is not an ACC separation certificate.

The new exact conjugacy API returns a witness or a complete negative answer
for **one element pair**. Its general branch is tested with both quotient
conjugate positives and negatives. Geodesic normalization is deliberately
scoped in the executable API: longer inputs raise instead of using a Dehn
residue as a geodesic. The abstract full shortlex procedure is specified in
the proof document, not silently approximated in code.

Run records, measured runtimes and hashes are in
`certificates/second_strike_validation.txt` and
`certificates/SECOND_STRIKE_SHA256SUMS`. Old history and hashes are preserved.

```sh
python -m acsearch.hsc_shortening > /tmp/astra_second_strike.json
cmp /tmp/astra_second_strike.json certificates/astra_second_strike.json
python scripts/check_first_strike.py
python scripts/check_second_strike.py
python -m pytest -q
sha256sum -c certificates/SHA256SUMS
sha256sum -c certificates/SECOND_STRIKE_SHA256SUMS
```

## Stop and next proof obligation

Stop condition **F**: the bounded high-value local tasks have been completed.
Conditions A, B, C and E were not reached. Condition D was reached only for
specific proposed shortcuts, not for the full peak architecture, so it is
not used as the strike's global stopping verdict.

A bound for a conjugation whose output is already short cannot bound an
unknown AC path's output lengths. The decisive unresolved case is a block
of multiplications interleaved with independent conjugations, rather than
a pair of conjugation moves. The AK(2) control proves that any theorem must
permit positive excess above endpoint height. The explicit mixed control
proves that shortest conjugators do not repair the obvious reorder.

**Single strongest third strike: HSC-MIXED-PEAK-3.** Prove a replacement theorem
for high alternating multiplication/conjugation blocks along a peak-minimal
path from the fixed AK(3) plateau to (x,y), with an explicit exceptional
height B>=15. It must control relative conjugation in products, survive the
two frozen counterexamples, and lower either height or the number of states
at the maximal height. The annular rung algorithm is now proved infrastructure;
do not repeat the quotient selection, conjugacy audit, or local product tables.
No component enumeration until the block theorem yields a terminating,
explicit height bound.
