# Canonical 2026 frontier

Status date: **2026-09-04**. “Open” means mathematically unresolved, not “unsolved by this repository.” Total length is the sum of freely reduced relator lengths.

## Canonical table

| Presentation or family | Total length | Why the group is trivial | Unstable AC status | Stable AC status | Best published path / reduction | Thickenable? | Governing result | What is genuinely unknown |
|---|---:|---|---|---|---|---|---|---|
| Standard rank-2 `<x,y | x,y>` | 2 | immediate | AC-trivial | stably trivial | 0 moves | yes | definition | nothing |
| `AK(2)` | 11 | Akbulut–Kirby family argument; also order-one enumeration here | **AC-trivial** | stably trivial | Havas–Ramsay: 14 essential moves, peak total length 15; no proof exists with fewer essential moves | not needed for status; not separately audited | Havas–Ramsay (2003) | nothing about AC status |
| `AK(3)` | 13 | standard AK family argument; order-one enumeration here | **open** | **open / prior claim invalidated** | no unstable trivialization; length-13 cases reduce to it or trivial cases | not established in audited sources | Havas–Ramsay; Shehper et al. v2 correction | both unstable and corrected stable AC-triviality; thickenability |
| `AK(4)` | 15 | standard AK family argument; order-one enumeration here | **open** | **open** | no length reduction from Theorem A (`n+11=15`) | not established | Shehper et al., Theorem A | unstable/stable status and thickenability |
| `AK(n)`, `n >= 5` | `2n+7` | standard AK family argument | **open**; length-reducible is not trivializable | open | AC-equivalent to a presentation of length `n+11` | not established | Shehper et al., Theorem A | all AC/stable statuses; further reductions/trivializations |
| `P1 = MS(2,x^-2 y^-1 x^2 y)` (classical Solitar candidate) | 14 | Miller–Schupp construction; order-one enumeration here | in certified block `{P1,P6}`; link to `AK(3)` remains uncertified | open | `P1 ~ P6`: 36 packaged / 58 classical, peak 27 | not established | Carreras, Thm. 1 | whether its block joins `AK(3)`; stable status; thickenability |
| `P2 = MS(2,x^-2 y^-1 x^2 y^-1)` | 14 | Miller–Schupp construction; order-one enumeration here | in certified block `{P2,P5}`; link to `AK(3)` remains uncertified | open | `P5 ~ P2`: 85 / 155, peak 33 | not established | Carreras, Thm. 2 | whether its block joins `AK(3)`; stable status; thickenability |
| `P3 = MS(3,y x^2 y)` | 14 | Miller–Schupp construction; order-one enumeration here | **equivalent to `AK(3)`**, hence unresolved exactly with it | same unresolved status as `AK(3)` | 66 / 101, peak 24; alternative 71 / 106, peak 22 | not established | Carreras, Thm. 3 | `AK(3)` status and thickenability |
| `P4 = MS(3,y^-1 x^2 y^-1)` | 14 | Miller–Schupp construction; order-one enumeration here | **equivalent to `AK(3)`**, hence unresolved exactly with it | same unresolved status as `AK(3)` | 13 / 22, peak 23 | not established | Carreras, Thm. 4 | `AK(3)` status and thickenability |
| `P5 = MS(2,y x^2 y x^-2)` (2024 holdout) | 14 | Miller–Schupp construction; order-one enumeration here | **equivalent to `P2`**; block unresolved | open | `P5 ~ P2`: 85 / 155, peak 33 | not established | Carreras, Thm. 2 | same as `P2` block |
| `P6 = MS(2,y x^2 y^-1 x^-2)` (2024 holdout) | 14 | Miller–Schupp construction; order-one enumeration here | **equivalent to `P1`**; block unresolved | open | `P1 ~ P6`: 36 / 58, peak 27 | not established | Carreras, Thm. 1 | same as `P1` block |
| `MS(1,w)` | varies | Miller–Schupp construction | **AC-trivial for all admissible `w`** | stably trivial | constructive proof | not needed | Shehper et al., Thm. B(i) / Thm. 2 | nothing about AC status |
| `MS(n,w*)`, `w*=y^-1 x y x^-1`, `n>0` | varies | Miller–Schupp construction | **AC-trivial** | stably trivial | constructive proof | not needed | Shehper et al., Thm. B(ii) | nothing about AC status |
| `MS(2,w_k)`, `w_k=y^-k x^-1 y x y`, `k in Z` | varies | Miller–Schupp construction | **AC-trivial** | stably trivial | constructive equivalence to `AK(2)` | not needed | Shehper et al., Thm. B(iii) | nothing about AC status |
| `MS(n,w_k)`, fixed `n>0`, `k in Z` | varies | Miller–Schupp construction | all equivalent to `AK(n)`; therefore open for `n>=3` | follows the corresponding `AK(n)` status | explicit family equivalence | not established | Shehper et al., Thms. 6–7 / Prop. 5 | exactly the relevant `AK(n)` question |
| General admissible `MS(n,w)` outside solved subfamilies | varies | Miller–Schupp construction | mixed: some certified trivial; many merely search-unsolved | generally open | case-dependent | not established | Shehper et al.; Two-Hump; Carreras | must be stated case by case; a search label is not a theorem |

## What “the length-14 frontier” means

Carreras does **not** prove a census of all balanced rank-2 presentations of length 14. The whole length-14 stratum has never been exhaustively classified. The 2026 theorem concerns the six presentations left by the Shehper et al. Miller–Schupp benchmark and proves four exact equivalences:

| Published connected block | Certificate status | Remaining link |
|---|---|---|
| `C0={P3,P4,AK(3)}` | unconditional, public ledgers replayed | trivial iff `AK(3)` is trivial |
| `C1={P1,P6}` | unconditional, public ledger replayed | `C1 ~ AK(3)` was stated for `P1`, but no public ledger/proof was located |
| `C2={P5,P2}` | unconditional, public ledger replayed | `C2 ~ AK(3)` was stated for `P2`, but no public ledger/proof was located |

Carreras also proves in the **restricted substitution-move graph** that `P3` reaches `AK(3)` with exact bottleneck 19, while paths from the searched `P1` or `P2` representatives to `AK(3)` or to each other must reach total length at least 27. This is not a lower bound in the full elementary AC graph and is not counterexample evidence.

## The stable `AK(3)` correction

Lisitsa's January 2025 paper and the first version of Shehper et al. report a stable trivialization. The revised Shehper et al. paper records that the source presentation had a misprinted 13th Wirtinger relator and was not a Wirtinger presentation. Its Appendix F states that the length-25 presentation is AC-equivalent to `AK(3)` but is **not necessarily stably AC-trivial**. Thus the unstabilized equivalence into `AK(3)` does not repair the missing stable premise.

Until a corrected stable ledger begins at `AK(3)`, ends at a standard presentation, and replays with legal stabilization/destabilization moves—or a new proof supplies the same implication—the canonical stable status is open. Lackenby's 2026 introduction independently continues to list the AK family for parameters at least 3 among potential stable counterexamples.

## Thickenability

Lackenby's Theorem 1.3 says every thickenable balanced trivial-group presentation satisfies **unstable** ACC. Theorem 1.2 gives a double-exponential stable-move bound `2^(2^(c*l^2))`, `c=2*10^6`. Neuwirth's algorithm decides thickenability. A positive thickenability certificate for any named candidate settles that candidate positively; a negative test does not prove it is a counterexample.

No primary source audited here assigns a definitive thickenability value to `AK(3)`, `AK(4)`, or the three length-14 blocks. These are high-value theorem-backed tests, not values to guess from the relator words.

## Sources

- Carreras, [arXiv:2607.23611](https://arxiv.org/abs/2607.23611), especially §§1, 3–5.
- Shehper et al., [arXiv:2408.15332v2](https://arxiv.org/abs/2408.15332), especially Theorems A/B and Appendix F.
- Lackenby, [arXiv:2606.06122](https://arxiv.org/abs/2606.06122), Theorems 1.2–1.3 and §6.2.
- Havas–Ramsay, [2003 paper](https://staff.itee.uq.edu.au/havas/2003hr.pdf).
- Lisitsa, [arXiv:2501.18601v1](https://arxiv.org/abs/2501.18601), retained as the superseded claim whose premise must not be imported without the v2 correction.
