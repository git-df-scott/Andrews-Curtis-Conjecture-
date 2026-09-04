# Andrews–Curtis campaign status — 2026-09-04

## Executive status

- **ACC:** open. No counterexample is known.
- **CEC (counterexample certificate):** none.
- **Unconditional rank-2 census:** every balanced trivial-group presentation of total relator length at most 12 is AC-trivial.
- **First unresolved object:** `AK(3)`, total length 13. Every length-13 case is AC-trivial or AC-equivalent to `AK(3)`.
- **Length 14:** there has never been an exhaustive classification of the whole stratum. In the six-case Miller–Schupp benchmark, the published certificates give exactly three connected blocks; only the `MS(3,...)` block is publicly joined to `AK(3)`.
- **Stable status of `AK(3)`:** **not established in the corrected record**. The 2024/2025 claim used a misprinted Wirtinger relator; the corrected v2 paper explicitly says the resulting presentations are not necessarily stably AC-trivial. The unstable status remains open as before.
- **Thickenable class:** Lackenby proves both stable and unstable ACC for every thickenable balanced presentation of the trivial group. Thickenability of the named frontier candidates was not established in the audited primary sources.
- **Finite quotients:** incapable of separating a normally generating tuple of a free group from the basis under AC moves. Soluble and broad nilpotent/`MN` quotient variants are also dead ends.
- **Search interpretation:** a path is a positive certificate; failure to find one is not evidence of non-equivalence.

The canonical object table is in [FRONTIER_2026.md](FRONTIER_2026.md). The proof obligations for any invariant are in [INVARIANT_LEDGER.md](INVARIANT_LEDGER.md), and the compute program is in [ATTACK_MATRIX.md](ATTACK_MATRIX.md).

## What this audit changed

1. It narrows Carreras's result correctly: the result certifies four equivalences inside the named six-case Miller–Schupp benchmark, not all balanced presentations of length 14.
2. It preserves the two uncertified links `P1 ~ AK(3)` and `P2 ~ AK(3)` as claims, not theorems with public ledgers.
3. It withdraws the formerly repeated statement that `AK(3)` is known stably AC-trivial. The revised Shehper et al. paper documents the defect that invalidates the cited route.
4. It separates the statement “`AK(n)` is length-reducible for `n >= 5`” from “`AK(n)` is AC-trivial.” Only the former is proved.
5. It places thickenability ahead of brute force as a theorem-backed positive-pruning test.

## Repository audit

The pre-existing implementation was preserved. It has:

- exact free-group words and free reduction;
- elementary inversion, multiplication, and generator-conjugation moves;
- cyclic and signed-generator-permutation canonicalization;
- exact positive-certificate replay;
- a Todd–Coxeter order-one check, where enumeration terminates;
- bounded greedy/BFS experiments whose negative output is explicitly non-evidentiary.

This audit added exact replay for Carreras's packaged ledger vocabulary and froze the 13-packaged/22-classical-move certificate

`MS(3, y^-1 x^2 y^-1) ~ AK(3)`

as a regression test, including rejection of a corrupted last move. Dependencies are now pinned in `requirements.txt` and `requirements-dev.txt`.

## Calibration results

The bounded calibration run checked:

| Check | Result | Meaning |
|---|---:|---|
| Existing unit tests | pass | word operations, moves, canonicalization, positive certificates and group checks agree internally |
| Carreras 13-move ledger | pass | exact endpoint agrees with `AK(3)` up to certified AC-realizable terminal symmetries |
| Corrupted Carreras ledger | rejected | replay is not merely accepting the expected label |
| `AK(2)`–`AK(5)` Todd–Coxeter order | 1 | independent finite coset enumeration terminates with the trivial group for these controls |
| Six length-14 MS cases, order | 1 | each named benchmark passes the same positive group-order check |
| Known `AK(2)` greedy attempt | no path in small cap | **no mathematical inference**; Havas–Ramsay's known optimum requires 14 essential moves and peak total length 15 |

Todd–Coxeter termination at order one is a useful positive group check, not a general decision procedure for triviality. The literature supplies the actual family-level trivial-group arguments.

The independent verifier in Carreras's release tag `v1.0` (commit
`d347fc4764ee55de6fc779fe697769127dde48e3`) was also run directly:

| Public ledger | Replay |
|---|---:|
| `cert_sym_equiv_orphan1.json` | PASS — 36 packaged / 58 classical |
| `cert_idx0_equiv_mirror.json` | PASS — 85 / 155 |
| `bottleneck_ak_f3_cert.json` | PASS — 66 / 101 |
| `cert_ms3_yx2y_equiv_ak3.json` | PASS — 71 / 106 |
| `cert_ms3_yinvx2yinv_equiv_ak3.json` | PASS — 13 / 22 |
| release verifier honest/corrupt/malformed self-tests | PASS |

Only the compact 13-move ledger is duplicated as a permanent local regression;
the release remains the canonical source for all five artifacts.

## Stop rule honored

No open-ended `AK(3)` search, exhaustive length census, RL training, million-state closure, or overnight job was launched.

## Primary sources

- J. Carreras, [Machine-checkable equivalence certificates at the length-14 Andrews–Curtis frontier](https://arxiv.org/abs/2607.23611), 2026; [archived certificate release](https://github.com/joe-carr-data/ac-certificates/releases/tag/v1.0).
- A. Shehper et al., [What makes math problems hard for reinforcement learning: a case study, v2](https://arxiv.org/abs/2408.15332), 2025 revision.
- M. Lackenby, [The stable Andrews–Curtis conjecture and thickenable presentations of the trivial group](https://arxiv.org/abs/2606.06122), 2026.
- G. Havas and C. Ramsay, [Breadth-first search and the Andrews–Curtis conjecture](https://staff.itee.uq.edu.au/havas/2003hr.pdf), 2003.

## Bottom line

- **CE:** no
- **CEC:** no
- **Smallest genuinely unresolved objects:** `AK(3)` at length 13; at length 14, the certified `AK(3)/MS(3)` block and the two still-unjoined `MS(2)` blocks; then `AK(4)` at length 15.
- **Strongest remaining invariant avenue:** a rank-sensitive orbit invariant in a computable infinite non-soluble quotient, with an exact proof of invariance and a terminating orbit-separation theorem.
- **Three best Astra attacks:** infinite hyperbolic-quotient orbit invariants; unstable crossed-module/Peiffer invariants; non-semisimple sliced-2-complex state sums.
- **Do not repeat:** finite quotients; abelian/nilpotent/soluble representations; semisimple Quinn invariants; unproved neural scores; raw Fox/trace/determinant differences; raw substitution groups; bounded-search noncontact; exhaustive short censuses; or any overnight direct search for `AK(3)`.
