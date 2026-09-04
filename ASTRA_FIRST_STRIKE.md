# ACC — first Astra strike

2026-09-04. Inherited the repository's default branch
`claude/curtis-conjecture-counterexample-iodu6j` at
`b19113c5e507eaceb51aeb58f30c47433c85980b` (there was no `main` branch).
Stop condition **F**: bounded high-value proof/certificate tasks completed;
the remaining global orbit/peak theorem is unresolved. Conditions A–E were
not achieved for the unrestricted target architecture.

```
ACC CE: NO
AK(3) SEPARATED: NO
QUOTIENT-SEPARATOR THEOREM: PROVED
USEFUL INFINITE QUOTIENT: NO
EXACT ORBIT ALGORITHM: NO
NEW AC INVARIANT: NO
```

Here “useful” means a quotient with a proved separating mechanism or complete
attack algorithm. Two certified infinite laboratories remain live. The ten-move
positive result below is an exact answer for one marked pair, not a general
orbit algorithm. No negative inference is drawn from an unfinished theorem.

## What changed

1. **Theorem:** the exact quotient separator is proved with the full move set,
   rank, normal-generation, marking, and surjectivity conventions. It agrees
   with the prior one-way theorem; it is not presented as a new discovery.
2. **Theorem + computation:** AK(3) reaches the standard pair in ten elementary
   moves in `C2*C3`, using only `x^2=y^3=1`. This closes every further quotient
   in that marking, including the previously UNKNOWN standard
   `Delta(2,3,7)` row. Independent normal-form and integer matrix replays pass.
3. **Theorem, new to campaign:** quantifier-free group-equation/inequation
   predicates cannot distinguish normally generating AC orbits in a
   non-elementary torsion-free hyperbolic group. The proof derives from the
   no mixed identity property, a finite-avoidance lemma, and injective
   independent-conjugate substitution. No literature-priority claim is made.
4. **Theorem, sharpened formulation:** all quotient images of free normally
   generating pairs have AC orbits with the same profinite closure.
   Profinite-continuous Hausdorff-valued invariant labels are consequently
   blind. This is a consequence of the inherited finite theorem, not a new
   invariant or a prohibition on every finite automaton.
5. **Computation:** independently recertified the two small-cancellation
   laboratories and evaluated the literal AK(3) words. Both entries remain
   nonidentity in each group. Their AC component comparisons remain UNKNOWN.
6. **Failed implementation premise:** equal Dehn-irreducible representatives
   of lengths 53/55 (`H_SC`) and 55/57 (`H_OR`) disprove the shortcut from Dehn
   reduction to geodesic/canonical forms. Both equalities have two-step
   rewrite proofs. This closes the shortcut, not all peak reduction.
7. **Audit repair:** `cyclic_neighbors` skipped a legal shortening edge for
   `(x,xy)` when its conjugator budget was negative. The empty-conjugator
   case is repaired, with a regression test. Unsupported completeness language
   is withdrawn; the remaining cutoff is not certified here.

Full proofs: [HYPERBOLIC_QUOTIENT_THEOREM.md](HYPERBOLIC_QUOTIENT_THEOREM.md).
Targets: [QUOTIENT_LEDGER.md](QUOTIENT_LEDGER.md).

## Chronological reconciliation and internal map

| Commit | Record | Treatment |
|---|---|---|
| `cf3f0e0` | Initial word/move/search/verifier/catalogue implementation | Preserved; audit found one bounded-neighbor omission and overstatement |
| `fabca19` | Replaced the erroneous easy test with a genuine trivial presentation | Retained |
| `47596ab` | Frontier and invariant audit; stable-status and length-14 corrections | Retained; critical source passages rechecked |
| `b19113c` | Hyperbolic feasibility, explicit laboratories, graveyard, controls, peak handoff | Inherited as newest canonical record; changes above supersede only named claims |

| Classification | Binding state after this strike |
|---|---|
| **VERIFIED** | Canonical AK(3) words and length; direct family-level triviality proof; separator mechanism; finite blindness hypotheses; explicit marked modular/triangle equality; both C'(1/6)/power certificates; positive Carreras local ledger; complete current tests |
| **CONDITIONALLY VERIFIED** | Historical external ledgers other than the locally embedded Carreras P4 path remain inherited external-replay reports, not newly replayed artifacts here; any peak or full orbit algorithm remains conditional on its missing completeness theorem |
| **UNKNOWN** | AK(3) unstable status; corrected stable status; AK(3) AC components in H_SC and H_OR; useful terminating rank-2 AC algorithm for either laboratory |
| **CLOSED** | Old finite/soluble and audited invariant lanes; marked x²=y³ quotient route for AK(3); quantifier-free invariant predicates; profinite-continuous labels; Dehn-normal-form shortcut |
| **LIVE** | H_SC with a theorem-proved geodesic peak bound or another nonconstant exact invariant escaping the two new no-go formulations |

The bounded source check confirmed the AK frontier and faithfulness/orbit
distinction in [Gilman–Myasnikov](https://arxiv.org/html/2506.23031v1), the
stable correction in [Shehper et al., Appendix F](https://arxiv.org/html/2408.15332v2#A6),
and the six-case scope in [Carreras](https://arxiv.org/html/2607.23611v1).
The two certified MS(2) blocks are not proved separate AC components. No stable
AK(3) premise or exhaustive length-14 classification was imported.
The older semisimple/Fox/substitution closures were retained, not re-audited.

The campaign description “strongest surviving architecture” is a research
ranking, not a mathematical theorem. This strike narrows that architecture;
it does not prove every infinite hyperbolic quotient incapable.

## Computational record

| Task | Domain / normalization / completeness | Count | Result |
|---|---|---:|---|
| H_SC overlap certificate | Full symmetrized relator set; all distinct unordered word pairs. Prefix overlap definition exactly characterizes pieces | 244 words; 29,646 pairs | Max piece 8; 6*8<61; no proper powers |
| H_OR overlap certificate | Same | 122 words; 7,381 pairs | Max piece 7; 6*7<61; no proper power |
| AK(3) marked modular path | One prescribed path; unique free-product syllable forms. Positive proof requires no exhaustive search | 10 moves; 11 ordered states | Standard ordered endpoint |
| Dehn shortcut falsification | Fixed ordered symmetrized pairs sharing >=5 letters; cyclic rotations of the two-cell boundary; split one letter below midpoint; stop at first witness | 26 candidate splits for H_SC; 28 for H_OR | Equal irreducible words of unequal length |
| Existing and new controls | pytest, exact word operations, local Carreras honest/corrupt path, tiny existing BFS test, catalogue group checks, 3x128 legal walks and inverse replays; independent new certificates and four corruptions | 16 before; 23 after | PASS |
| AC orbit exploration | None | 0 search states | No search-failure inference |

Certificate producer runtime on this host: **0.466 seconds** for the first
recorded run. Post-change test run: **23 passed in 0.90 seconds**. Runtime is
observational, not part of the deterministic certificate bytes. The frozen
JSON is reproducible; hashes and the latest exact run records are in
`certificates/SHA256SUMS` and `certificates/first_strike_validation.txt`.

The certificate checker is stdlib-only and imports no `acsearch` routines.
It uses a prefix histogram instead of the producer's pairwise LCP check,
string rewriting instead of its syllable stack, and an additional PSL(2,Z)
matrix route for the ten-move path. It checks every recorded Dehn rewrite.
This is independent implementation verification, not an independent human
review of the written theorems. No counterexample certificate is claimed.

Reproduce from the repository root:

```sh
python -m pip install -r requirements-dev.txt
python -m acsearch.first_strike
python scripts/check_first_strike.py
python -m pytest -q
sha256sum -c certificates/SHA256SUMS
```

## Why the primary orbit target remains unresolved

Hyperbolic equations decide any fixed macro-depth path template, including
arbitrary conjugators, but not an unbounded disjunction over all depths.
Ordinary Nielsen, simultaneous conjugacy, and automorphism orbit problems
still omit permitted AC transformations. The new quantifier-free theorem
rules out an especially tempting algebraic compression of that gap.

No global peak theorem, finite complete orbit automaton, or nonconstant exact
label was obtained. It would be incorrect to claim stop condition C or D.
No other candidate was promoted: the missing theorem affects the mechanism,
so computing additional hard presentations would add no valid separator.

**Single strongest second strike:** `SC-AC-SHORTEN-2`, specified in
[OPEN_LANES.md](OPEN_LANES.md): prove an explicit geodesic peak bound for this
fixed H_SC comparison, treating arbitrary conjugation exactly. Only that
proof authorizes a finite component computation with negative force.
