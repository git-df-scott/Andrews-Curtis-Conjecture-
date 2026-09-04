# Candidate ledger

This ledger separates mathematical status, public certificates, and search labels. Only the first two can change the frontier.

## Rank-2 priority queue

| Priority | ID | Defining relators in repository convention | Length | Mathematical class | Public positive certificate | Next theorem-bearing test |
|---:|---|---|---:|---|---|---|
| 1 | `AK3` | `x^3 y^-4`, `x y x y^-1 x^-1 y^-1` | 13 | open; unique minimal potential CE | none to standard; receives Carreras certificates from `P3`,`P4` | decide thickenability; then infinite non-soluble rank-2 orbit invariants |
| 2 | `C1/P1` | `MS(2,x^-2 y^-1 x^2 y)`; classical Solitar `P1` up to rotation | 14 | block open; uncertified claimed link to `AK3` | `P1~P6`, 36 packaged / 58 classical | recover/prove `P1~AK3` or compare invariant on `C1` versus `AK3` |
| 3 | `C2/P2` | `MS(2,x^-2 y^-1 x^2 y^-1)` | 14 | block open; uncertified claimed link to `AK3` | `P5~P2`, 85 / 155 | recover/prove `P2~AK3` or compare invariant on `C2` versus `AK3` |
| 4 | `AK4` | `x^4 y^-5`, `x y x y^-1 x^-1 y^-1` | 15 | open; no reduction from current family theorem | none | same invariant suite after rank-2 method is proved |

`P3=MS(3,y x^2 y)` and `P4=MS(3,y^-1 x^2 y^-1)` are not independent candidates: their public certificates put them in the `AK3` block.

## Six-case length-14 benchmark

| ID | Presentation | Shehper et al. label | Audited 2026 status |
|---|---|---|---|
| `P1` | `MS(2,x^-2 y^-1 x^2 y)` | stated `~AK3`, no path | `~P6` certified; `~AK3` still uncertified |
| `P2` | `MS(2,x^-2 y^-1 x^2 y^-1)` | stated `~AK3`, no path | `~P5` certified; `~AK3` still uncertified |
| `P3` | `MS(3,y x^2 y)` | stated `~AK3`, no path | `~AK3` certified |
| `P4` | `MS(3,y^-1 x^2 y^-1)` | stated `~AK3`, no path | `~AK3` certified; shortest Carreras ledger used in tests |
| `P5` | `MS(2,y x^2 y x^-2)` | holdout | `~P2` certified; therefore belongs to an open MS(2) block |
| `P6` | `MS(2,y x^2 y^-1 x^-2)` | holdout | `~P1` certified; therefore belongs to an open MS(2) block |

The names “holdout” and “GS-unsolved” record a campaign history, not distinct mathematical AC components.

## Miller–Schupp routing rules

Before putting an `MS(n,w)` object in an unresolved queue, normalize `w` and check:

1. `n=1`: solved for every admissible `w`.
2. `w=y^-1 x y x^-1`: solved for every `n>0`.
3. `n=2` and `w=y^-k x^-1 y x y`: solved for every integer `k`.
4. General fixed-`n` `w_k=y^-k x^-1 y x y`: equivalent to `AK(n)`; route status to that AK object.
5. Match against a public certificate under cyclic relator rotation, inversion, relator order, and signed generator permutation.
6. Only then label it open. A timeout produces the separate label `search-unsolved`.

## Provenance fields required for additions

Every future entry must record:

- exact freely reduced relators and generator convention;
- total length after free reduction;
- a human proof or replayable certificate that the group is trivial;
- exact theorem/certificate hash for any AC-equivalence assertion;
- move vocabulary, classical expansion count, peak total and peak single-relator length;
- stable status with the entire rank-changing path checked;
- thickenability result plus certificate/tool version;
- search caps only in a separate experimental field.

## Negative labels forbidden

Do not enter `counterexample`, `non-AC`, or `separate component` because of:

- greedy, beam, PPO, MCTS, Prover9, or BFS failure;
- absence from AC-19 or another solved table;
- a restricted GS bottleneck;
- a large lower bound on distance;
- failure of this repository's current move set or canonicalizer;
- stable status in either direction.

## Sources

- Carreras, [arXiv:2607.23611](https://arxiv.org/abs/2607.23611).
- Shehper et al., [arXiv:2408.15332v2](https://arxiv.org/abs/2408.15332).
- Havas–Ramsay, [2003 paper](https://staff.itee.uq.edu.au/havas/2003hr.pdf).
