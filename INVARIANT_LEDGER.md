# Invariant battlefield

## Admission rule

An output is an ACC invariant only after all three obligations are discharged:

1. **Domain:** define `I(r1,...,rn)` for every normally generating `n`-tuple under consideration, including degenerate intermediate tuples.
2. **Elementary invariance:** prove, or mechanically verify from complete defining relations, invariance under
   - `ri -> ri^-1`,
   - `ri -> ri rj` and its inverse variants for `i != j`,
   - `ri -> g ri g^-1` for every `g` in the ambient free group.
3. **Endpoint computation:** compute the same rigorously specified object for the candidate and the standard basis. Floating-point separation, learned embeddings, and bounded orbit noncontact do not meet this obligation.

Relator permutation and cyclic rotation are harmless only because each is realizable by elementary moves; the code tests the rotation expansion. A quantity can be useful as a heuristic without being admitted as an invariant, but no heuristic value is counterexample evidence.

## Classification

| Mechanism | Class | AC-invariance audit | Stabilization behavior | Verdict |
|---|---|---|---|---|
| Abelianization matrix up to integral row operations | **PROVABLY INCAPABLE** | inversion and multiplication are unimodular row operations; conjugation disappears after abelianization | naturally stable after adding an identity block | every balanced trivial presentation has unimodular matrix; all controls and candidates agree |
| Images in finite quotient groups, including all finite representation images | **PROVABLY INCAPABLE** | tuple AC moves descend functorially | usually extends under a trivial coordinate | Borovik–Lubotzky–Myasnikov classify finite AC components by abelianization in the relevant range; cannot separate the free basis from a normally generating tuple |
| Nilpotent / `MN` quotient orbit data | **PROVABLY INCAPABLE** | functorial tuple orbit | generally stable | Myropolska gives the same abelianization control for the `MN` class, including finitely generated nilpotent groups |
| Finitely generated soluble quotient orbit data | **PROVABLY INCAPABLE** | functorial tuple orbit | generally stable | Guyot proves the relevant generalized AC property for soluble targets; no separator for a free-group candidate |
| Ordinary homology, homotopy type, Euler characteristic, Whitehead torsion | **PROVABLY INCAPABLE** | AC moves induce 2-deformations/simple equivalences | stabilization explicitly adds a cancelling pair / sphere in the corresponding models | every balanced trivial-group presentation complex is finite, simply connected, acyclic, hence contractible; `Wh(1)=0` |
| Augmented Fox matrix, determinant, Smith form | **PROVABLY INCAPABLE** in this form | augmentation converts moves to elementary integral row operations | identity-block stable | reduces to the abelianization matrix; determinant magnitude is 1 in every test case |
| Semisimple Quinn/Bobtcheva state-sum invariant | **PROVABLY INCAPABLE** | Bobtcheva–Quinn prove AC invariance | factors through homology for Euler characteristic at least 1 | their corollary explicitly says it cannot detect original-ACC counterexamples among contractible complexes |
| Raw word length, Whitehead length, curvature, small-cancellation score | **not an invariant** | elementary multiplication and conjugation change it | rank-dependent but irrelevant | search heuristic only |
| Neural embedding, policy value, neighborhood size, empirical hardness | **not an invariant** | no exact move invariance; data may only approximate it | uncontrolled | computational triage only; numerical separation is worthless for CE certification |
| Trace/character values of a chosen representation | **not an invariant as normally proposed** | `tr(r_i r_j)` need not equal `tr(r_i)`; conjugacy invariance alone is insufficient | varies by construction | must quotient by the *whole* AC action and prove well-definedness before any candidate computation |
| Raw Fox Jacobian over a noncommutative coefficient system | **KNOWN BUT INCOMPLETE** | multiplication gives elementary-looking operations, but conjugation, coefficient transport, choices and target equivalences must all be handled | often becomes a stable `K`-theory class and therefore loses unstable information | potentially useful only with rank-sensitive, non-stable target and a complete naturality proof |
| Relation modules / identities among relations / Peiffer data | **KNOWN BUT INCOMPLETE** | presentation transformations induce maps, but an ordered basis-sensitive quotient must be proved independent of choices | stable module invariants are automatically poor for unstable separation | higher data can survive collapse of the presented group; strongest algebraic opening if deliberately unstable |
| Sliced Quinn-model / Kaden state sums | **KNOWN BUT INCOMPLETE** | Kaden identifies a missing local slicing relation; satisfying a subset is not enough | a fully 3-deformation invariant is stable and may target stable rather than unstable ACC | do not compute candidates until every movie relation, including change-of-slicing, is verified |
| 4-thickening / handlebody quantum invariants | **KNOWN BUT INCOMPLETE** | normally invariant for a **chosen** thickening or trace; presentation-level independence and AC correspondence are separate obligations | many constructions normalize away handle stabilization | use the spectrum over all admissible thickenings or prove a canonical choice; raw single-thickening values are not ACC invariants |
| Thickenability | **COMPUTATIONALLY POSSIBLE** positive-pruning property | no presentation-level AC invariance is needed for the implication “this presentation is thickenable” | Lackenby's stable theorem applies; his Theorem 1.3 is already unstable | positive result proves AC-triviality; negative result is not a CE and not a separating invariant |
| Exact AC orbit in a computable infinite non-soluble quotient | **KNOWN BUT INCOMPLETE — YELLOW** | exact by functoriality: a free-group AC path maps to the target AC path | rank-specific components can merge after adding a trivial coordinate | the exact component is valid but not yet a computable separator; no general hyperbolic connectivity theorem kills it, and no terminating orbit algorithm was found |
| Unbased fundamental crossed module / Peiffer identities | **PROVABLY INCAPABLE** here | presentation moves induce crossed-module isomorphisms | homotopy-level object is stable | the balanced trivial-group presentation complex is contractible, so the boundary crossed module has zero kernel and trivial cokernel and is isomorphic to the free group |
| Based rank-sensitive crossed-module / Peiffer filtration | **KNOWN BUT INCOMPLETE** | must construct functorial basis maps for all three elementary moves and prove inverse laws | retain the free 1/2-cell basis so adding a cancelling pair remains visible | retaining the full basis restates the AC orbit; only a nonstable computable quotient with a nonfactorization theorem could help |
| Non-semisimple sliced-2-complex state sum with noninvertible bubble operator | **GENUINELY UNEXPLORED** at this frontier | verify the complete Kaden/Quinn movie presentation symbolically first | can be designed to record, rather than normalize, the stabilization operator | evades the semisimple homology-collapse theorem; no separator exists yet |
| AC-invariant substitution **groupoid spectrum** | **GENUINELY UNEXPLORED** | raw `u`-substitution groups fail well-definedness; use all decompositions and prove AC moves induce equivalences | likely rank-sensitive if objects remember the basis | McDermott's 2026 counterexamples to naive invariance define the gate, not a finished invariant |

## Mechanically checked baseline on the five required target types

`AK(2)` is the AC-trivial control. `P4` is used as the length-14 representative because its Carreras equivalence has the shortest packaged ledger.

| Object | Total length | Abelianization determinant magnitude | Todd–Coxeter order | Finite-quotient orbit | Ordinary complex invariants | Carreras ledger |
|---|---:|---:|---:|---|---|---|
| standard rank 2 | 2 | 1 | 1 | basis class | contractible | n/a |
| `AK(2)` control | 11 | 1 | 1 | same by theorem | contractible | historical trivialization, not recopied |
| `AK(3)` | 13 | 1 | 1 | same by theorem | contractible | endpoint of replayed equivalence |
| `AK(4)` | 15 | 1 | 1 | same by theorem | contractible | none |
| `P4=MS(3,y^-1 x^2 y^-1)` | 14 | 1 | 1 | same by theorem | contractible | `P4 ~ AK(3)` replay passes; corrupted ledger fails |

No approved invariant separates a candidate in this table. That is an audit result, not evidence for ACC.

## Why finite quotients are blind

Let `R=(r1,...,rn)` normally generate `F_n`, and let `phi:F_n -> G` be onto a finite group. Each elementary AC move on `R` maps to the same elementary move on `phi(R)`. The finitary theorem says the connected component in the relevant finite AC graph is controlled by the abelianized tuple. Since `F_n/<R>` is trivial, the exponent-sum matrix is unimodular, so `R` and the basis have the same abelianized orbit. Therefore their images cannot lie in different finite AC components. Enumerating more finite groups cannot change this theorem.

This does **not** kill every infinite representation. It does kill any purported algebraic separator whose inequality necessarily survives reduction to some finite specialization. Astra should try to prove that specialization lemma for each linear proposal before allocating candidate compute.

## Infinite quotient admission checklist

An infinite target `G` is eligible only if all of the following are supplied:

- exact normal forms or a decidable word problem;
- decidable conjugacy, or a proved complete approximation with certified one-sided conclusions;
- an exact `n`-tuple AC-orbit invariant or terminating orbit algorithm;
- proof that the chosen map `F_n -> G` is explicit and every candidate tuple normally generates its required image;
- proof that any reported difference cannot be an artifact of presentation, generating set, precision, or cutoff.

Torsion-free non-elementary hyperbolic groups are a live laboratory: Gilman–Myasnikov prove faithfulness of the full AC transformation action on every nontrivial orbit. Faithfulness is useful structure but **does not itself decide whether two tuples share an orbit**.

The focused strike in [HYPERBOLIC_QUOTIENTS.md](HYPERBOLIC_QUOTIENTS.md)
strengthens this warning. Ordinary Nielsen equivalence is not the needed
relation: independent AC conjugation can change the ordinarily generated
subgroup, and uniform Nielsen equivalence is undecidable even across
torsion-free hyperbolic/small-cancellation inputs. Exact move witnesses are in
[INVARIANT_GRAVEYARD.md](INVARIANT_GRAVEYARD.md).

## Source ledger

- Borovik–Lubotzky–Myasnikov, [The Finitary Andrews–Curtis Conjecture](https://arxiv.org/abs/1103.1295).
- Myropolska, [Andrews–Curtis and Nielsen equivalence relations on some infinite groups](https://arxiv.org/abs/1304.2668).
- Guyot, [On Andrews–Curtis conjectures for soluble groups](https://arxiv.org/abs/1612.06912).
- Bobtcheva–Quinn, [The reduction of quantum invariants of 4-thickenings](https://arxiv.org/abs/math/0012212).
- Kaden, [Considerations about Andrews–Curtis invariants based on sliced 2-complexes](https://arxiv.org/abs/1012.2228).
- Quinn, [Representation theory, topological field theory, and the Andrews–Curtis conjecture](https://arxiv.org/abs/hep-th/9202044).
- Gilman–Myasnikov, [Andrews–Curtis groups](https://arxiv.org/abs/2506.23031).
- Kapovich–Weidmann, [Nielsen equivalence in small cancellation groups](https://arxiv.org/abs/1011.5862).
- McDermott, [On u-substitutions for group presentations](https://arxiv.org/abs/2608.18929).
