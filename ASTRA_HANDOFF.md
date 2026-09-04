# Astra handoff — hyperbolic-quotient feasibility strike

## Decision

**HYPERBOLIC ROUTE: YELLOW.**

The quotient argument is rigorous, and no theorem located forces rank-2 AC
graphs of infinite torsion-free hyperbolic groups to be connected. The
remaining obstacle is explicit: construct a nonconstant computable factor of
the AC-component relation for normally generating pairs, or prove a terminating
component algorithm. Word/conjugacy solutions, faithful action of the AC
transformation group, and ordinary Nielsen classifications do not supply it.

There is no counterexample and no counterexample certificate.

## Canonical frontier retained from `47596ab`

1. `AK(3)` is the smallest unresolved rank-2 object, total length 13.
2. Its corrected stable status is open; stable triviality is not established.
3. The six named length-14 Miller–Schupp cases form the certified blocks
   `C0={AK3,P3,P4}`, `C1={P1,P6}`, and `C2={P2,P5}`. Only `C0` is publicly
   connected to `AK(3)`.
4. Carreras did not classify the whole length-14 stratum.
5. `AK(4)` remains open at length 15; `AK(n>=5)` is length-reducible, not thereby
   AC-trivial.
6. Search failure has no CE weight.

Nothing in this strike changes an object-level frontier status.

## What the strike established

### Exact functorial obstruction

For an epimorphism `q:F2->>H`, every elementary AC path maps to the identical
sequence on the image pair. Therefore

```text
q(R) and q(x,y) in different components of Delta_2(H)
    =>
R and (x,y) in different components of Delta_2(F2).
```

This is the complete soundness theorem. Quotients may merge orbits, so the
reverse implication is unavailable.

### Finite images remain unusable

Borovik–Lubotzky–Myasnikov identify finite AC components with their
abelianized components in the relevant rank. A balanced trivial-group
presentation has a unimodular exponent matrix, so its image pair and the basis
image agree in every finite quotient. This includes non-soluble finite groups
and all finite images of an infinite target.

### Hyperbolicity is not a solution by itself

- exact word, conjugacy and centralizer algorithms are infrastructure;
- the image pair normally generates but may not ordinarily generate;
- ordinary Nielsen classes fail independent relator conjugation;
- Gilman–Myasnikov's faithfulness theorem concerns transformations, not
  transitivity or point-orbit decidability;
- uniform Nielsen equivalence is already undecidable across torsion-free
  hyperbolic/small-cancellation inputs.

### Failed quantities

Raw word/translation length, individual conjugacy, axes and boundary data,
commutator conjugacy, centralizer configuration, ordinary Nielsen/Whitehead
class, ordinary subgroup geometry, scl and bounded-cohomology evaluations,
marked traces/representation values, and bounded orbit balls all fail a move
or fail to define useful information. Exact witnesses are frozen in
`INVARIANT_GRAVEYARD.md` and the test suite.

## Ranked target groups

| Rank | Target | Reason | Main obstacle |
|---:|---|---|---|
| 1 | `H_SC`, the repository's perfect torsion-free two-relator `C'(1/6)` group | exact Dehn word problem, cyclic centralizers, trivial abelianization, non-elementary, no finite theorem collapse at `H` itself | no AC-component algorithm |
| 2 | `H_OR`, the repository's torsion-free one-relator `C'(1/6)` group | simpler presentation and exact algorithms; non-elementary certified via `H_ab=Z+Z/7` | abelian noise and same orbit gate |
| 3 | `Delta(2,3,7)` | perfect, two-generated, geometric and algorithmically manageable | torsion; ordinary Nielsen/orbifold results are insufficient |

Use `C2*C3` only as a cheap Bass–Serre implementation calibration. Do not
mistake a calibration success for evidence that the torsion-free targets are
decidable.

## Strongest surviving invariant

```text
I_H(a,b) = [a,b]_AC in pi_0(Delta_2(H)).
```

It is exactly invariant under every move and rank-sensitive under
stabilization. Equality is semidecidable by enumerating paths. Inequality is
not presently decidable or finitely certifiable for the selected targets.
Thus the surviving item is the target relation, not yet the required
computable separator.

The only acceptable upgrade is a total computable label constant on all AC
edges, or a terminating orbit decider, with exact unequal values. No numerical
proxy qualifies.

## Exact first Astra experiment: `SC-AC-PEAK-1`

### Input

- repository commit containing this handoff;
- the fixed marked group `H_SC` from `HYPERBOLIC_QUOTIENTS.md`;
- elementary moves exactly as implemented in `acsearch.moves`;
- rank fixed at two.

### Task

Attempt a **theorem-bearing peak-reduction completion**, not a reachability
search:

1. independently replay the exhaustive `C'(1/6)` and proper-power certificate;
2. add independently tested exact conjugacy and centralizer routines for this
   fixed group;
3. define a well-founded exact complexity on Dehn-geodesic ordered pairs;
4. orient only AC transformations that provably decrease that complexity;
5. enumerate symbolic critical-peak *types* using the `C'(1/6)` overlap bound;
6. prove termination and either confluence, or a finite plateau theorem giving
   a canonical finite component label;
7. make arbitrary independent conjugation part of the proof, not a sampled
   generator bound;
8. emit a standalone checker for every critical type and normal-form equality.

### Pass criterion

A paper-level proof plus checker that the resulting canonical label is total
and constant under inversion, both signed multiplication directions, and
independent conjugation by every element of `H_SC`.

Only after that pass, run in order:

1. standard presentation;
2. `AK(2)` and `<x,y|xy^2,y>`;
3. the three 128-move-and-inverse synthetic paths;
4. every state of the Carreras `P4~AK3` ledger;
5. `AK(3)`, then `AK(4)`, then one representative of `C1` and `C2`.

### Exact stop condition

Stop `SC-AC-PEAK-1` immediately if any elementary move changes the proposed
label, if completeness requires an unproved global peak bound, or if symbolic
critical types cannot be proved finite. In all cases stop after **96 CPU-hours
or 32 GiB peak RAM**, archive `UNKNOWN`, and do not convert the cap into a pair
reachability run. Do not compute frontier values before the pass criterion.

### Result meanings

- **Canonical labels differ after all gates:** freeze the artifacts and seek an
  independent mathematical proof/replay; this is a serious CEC candidate.
- **Labels agree:** this closes only this target/label.
- **Peak theorem fails or remains unknown:** this teaches that Dehn normal forms
  do not automatically lift to AC-orbit normal forms. It has no implication
  for `AK(3)`.

## Peiffer fallback disposition

For a balanced trivial-group presentation the presentation complex is
contractible. Its free crossed-module boundary has zero kernel and trivial
cokernel, hence is an isomorphism. The unbased crossed module is therefore
structurally incapable. Retaining its distinguished 2-cell generators restores
the original relator-basis orbit problem.

The only bounded fallback worth attempting is a degree-at-most-3 nonabelian
based Peiffer filtration with a prior nonfactorization test. Stop if it factors
through the augmented Fox matrix, a nilpotent/soluble boundary quotient, or a
stable module. Do not increase the degree automatically.

## Counterexample standard

A genuine CE still requires:

1. a proof that the presentation group is trivial; and
2. a proof that its relator tuple is outside the standard elementary AC orbit.

For a quotient attack, item 2 requires the explicit epimorphism, a total exact
invariant/decision theorem in `H`, proofs for every move, exact unequal values,
and independent replay. There is no known general finite certificate for
non-AC-equivalence. A path is a positive finite certificate; absence of a path
is not a negative certificate.

## Astra must not repeat

- any open-ended `AK(3)` trivialization search;
- any rank-2 short census;
- finite-group, finite-image, soluble, nilpotent or `MN` quotient sweeps;
- raw trace, character, Fox, determinant or substitution values;
- raw lengths, axes, boundary pictures, centralizers, commutators, scl or
  subgroup geometry;
- ordinary Nielsen classification presented as AC classification;
- semisimple TQFT/state-sum invariants already known to collapse;
- bounded component noncontact, learned embeddings, hardness scores or search
  lower bounds as CE evidence;
- candidate evaluation before the move theorem and controls;
- automatic expansion of the Peiffer degree or the Astra resource cap.

## Final handoff state

- **Hyperbolic route verdict:** YELLOW
- **Strongest surviving invariant:** exact rank-2 AC component in `H_SC`; valid
  but not yet computably separable
- **Exact first Astra experiment:** `SC-AC-PEAK-1` above
- **Exact stop condition:** first invariance/completeness failure, nonfinite
  symbolic peak family, or 96 CPU-hours / 32 GiB; no frontier computation before
  theorem pass
- **What was learned:** infinite torsion-free hyperbolic quotients escape the
  finite blindness theorem, but their familiar geometry is destroyed by
  independent coordinate conjugation and multiplication; the actual bottleneck
  is AC-orbit decidability on normally generating pairs
- **CE:** no
- **CEC:** no
