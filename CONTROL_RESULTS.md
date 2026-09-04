# Hyperbolic-invariant control results

## Scope

This was a bounded invariance/calibration run.  It did not enumerate a short
census, search for an `AK(3)` trivialization, sweep finite/soluble quotients, or
infer anything from noncontact.

## Frozen control suite

| Control | Why it is known | What was checked |
|---|---|---|
| `<x,y|x,y>` | standard trivial presentation | exact elementary move semantics and failed-statistic witnesses |
| `<x,y|xy^2,y>` | one multiplication away after elementary reductions | positive certificate replay in the pre-existing suite; bounded walk below |
| `AK(2)` | Havas–Ramsay AC-trivial control | pre-existing trivial-group check; bounded legal orbit walk |
| three 128-move synthetic controls based at the preceding presentations | each has its complete legal path and inverse path by construction | 129 states per control; inverse replay returns byte-for-byte to the start; determinant remains 1 at every state |
| `P4=MS(3,y^-1 x^2 y^-1)` through the Carreras ledger | public 13-packaged/22-classical-move certificate to `AK(3)` | determinant is 1 at all 14 packaged states; the pre-existing endpoint and corrupted-ledger tests remain green |

The 128-move controls supply deliberately long *known* paths without asking a
search procedure to discover them.  They test move application and replay, not
AC distance.

## Move-level kill tests

| Quantity | Control move/path | Result |
|---|---|---|
| cyclic word-length multiset | `(x,y)->(xy,y)` | changes `(1,1)` to `(1,2)`; rejected |
| individual conjugacy-class multiset | same move | changes; rejected |
| commutator conjugacy class | independently conjugate first coordinate by `y`, then `x` | cyclic length changes 4 to 12; rejected |
| ordinary generated subgroup / Nielsen class | same two-conjugation path plus exact map to `S3` | original images generate `S3`; moved images generate order 2; rejected |
| abelian determinant magnitude | all 384 generated control moves and all Carreras packaged states | exactly 1; invariant but incapable |
| exact AC component | every listed legal path | constant by the path itself; valid but no computable component label yet |

No rejected statistic was evaluated on `AK(3)`, `AK(4)`, or the unresolved
length-14 blocks.

## Fixed hyperbolic laboratories

The two target presentations in `acsearch.hyperbolic` have machine-checked
small-cancellation certificates:

| Target | relator lengths | symmetrized set | longest piece | strict `C'(1/6)` | proper power | abelianization check |
|---|---:|---:|---:|---:|---:|---|
| `H_SC` | `61,61` | 244 | 8 | `6*8<61` | neither | determinant `-1`, hence perfect |
| `H_OR` | `61` | 122 | 7 | `6*7<61` | no | exponent vector `(-14,-7)`, hence `Z + Z/7` |

The certificate enumerates the complete symmetrized relator set and every pair
of distinct relators, rather than sampling overlaps.  The Dehn reducer then
checks each defining relator as the identity and checks `x`, `y`, and `[x,y]`
as nonidentity short controls.  A Dehn-reduced representative is not described
as a canonical normal form; the identity decision is the exact claim used.

## Replay commands

From the repository root:

```bash
python3 -m pytest tests/test_invariant_audit.py -q
python3 -m pytest -q
```

Expected result at this handoff:

```text
6 passed
16 passed
```

The first count is the focused file; the full suite includes the ten prior
frontier/certificate tests.  A future count may rise as tests are added, but no
failure may be waived as “numerical noise.”

## Interpretation

- Passing controls proves the implementations do what the tests state.
- The overlap certificate proves the two fixed presentations satisfy the
  stated `C'(1/6)` inequalities.
- It does not prove that an AC component algorithm exists.
- A failed bounded orbit computation would have no counterexample meaning and
  is not part of this suite.
