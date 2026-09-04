# Hyperbolic-quotient invariant candidates

## The proof gate

Fix an epimorphism `q:F2->>H`.  A proposed computable label

```text
I_H : N_2(H) -> S
```

is admissible only if the following are theorems for every normally generating
pair `(a,b)` and every `h in H`:

```text
I(a,b) = I(a^-1,b) = I(a,b^-1)
I(a,b) = I(a b^e,b) = I(a,b a^e),       e in {+1,-1}
I(a,b) = I(h a h^-1,b) = I(a,h b h^-1).
```

Permutation and left-multiplication identities then follow from these moves,
but an implementation may check them redundantly.  Exact inequality

```text
I_H(q(r1),q(r2)) != I_H(q(x),q(y))
```

would prove non-AC-equivalence in `F2`.  A sampled equality, bounded search, or
floating-point difference has no such implication.

## Surviving objects

| Object | Invariance proof | Computability | Stabilization | Status |
|---|---|---|---|---|
| exact component `[a,b]_AC` in `pi_0(Delta_2(H))` | every elementary move is an edge; inverse moves give equality of components | paths are enumerable, so equality is semidecidable; no terminating inequality test is known for the selected `H` | genuinely rank-sensitive: the map to `Delta_3(H)` may merge components | **mathematically valid, computational gate open** |
| any proved block system / quotient of the exact AC action | if the label map is constant on each elementary generator, it factors through components | no nonconstant example survived this session | depends on the construction; must not take a stable direct limit | **research specification, not yet an invariant** |
| marked-epimorphism spectrum `S_H(R)={ [q(R)]_AC : q:F2->>H }` | AC moves act inside each component; simultaneous `Aut(F2)` merely reindexes epimorphisms by precomposition | infinite and not presently enumerable with an equality/inequality decision | rank-specific if defined only for `F2` | **valid set-valued object, not currently computable** |
| normal closure `<<a,b>>_H` | inversion, multiplication and independent conjugation preserve it in both directions | computable only in special classes; here its value is known | persists after stabilization | **valid but constant on the campaign domain** |
| abelian Nielsen class / absolute exponent determinant | induced moves are elementary integral row operations and conjugation vanishes | exact and tested | stable after adjoining an identity block | **valid but provably incapable** |

The first row is the strongest survivor.  It is deliberately not advertised as
a newly discovered numerical invariant: it is the exact target equivalence
relation.  The useful research problem is to construct a nonconstant computable
factor of it.

## Why normal generation is the correct domain

For every balanced trivial-group presentation, `(r1,r2)` normally generates
`F2`.  Hence `q(R)` normally generates every quotient `H`.  The image pair need
not generate `H` as an ordinary subgroup.  This invalidates a common shortcut:

```text
classification of Nielsen classes of generating pairs
        !=
classification of AC classes of normally generating pairs.
```

Independent coordinate conjugation is exactly what destroys the shortcut; an
explicit free-group witness is frozen in `tests/test_invariant_audit.py` and in
`INVARIANT_GRAVEYARD.md`.

## Candidate theorem programs

These are theorem programs, not claimed invariants.  Candidate evaluation is
forbidden until the stated proof is complete.

### A. Bass–Serre peak reduction in `C2*C3`

Construct a terminating confluent rewrite system for the AC action on normally
generating pairs in the virtually free group `C2*C3`.  A canonical irreducible
representative would be invariant because each rewrite preserves an AC
component and confluence makes the endpoint independent of choices.

- Required proof: termination, local/global confluence, and completeness for
  **independent conjugation**, not merely Nielsen moves.
- Positive outcome: two canonical forms give an exact separator and a template
  for triangle groups.
- Negative outcome: connectedness of `Delta_2(C2*C3)` closes the virtually-free
  calibration lane; nontermination closes only this rewrite orientation.
- Stabilization: do not add a third coordinate in the definition.

### B. Automatic-language component normal form in `H_SC`

Use the certified Dehn language of the fixed perfect torsion-free `C'(1/6)`
group to seek a finite-state peak-reduction theorem for locally minimal pairs.
The output is admissible only after proving every pair has an AC descent to a
canonical finite list and that all local minima in a component are joined by
proved plateau moves.

- Required proof: global completeness.  A finite ball or empirical peak bound
  is insufficient.
- Positive outcome: exact component labels for the mandatory controls, then
  the frontier.
- Negative outcome: an infinite family of critical peaks teaches that this
  automatic-language quotient is not finite-state; it says nothing about ACC.
- Stabilization: retain the ordered rank-two state and do not quotient by
  `(a,b)->(a,b,1)`.

### C. Orbifold/Bass–Serre component data in `Delta(2,3,7)`

Exploit the action on the hyperbolic plane and the rigid torsion conjugacy
classes to classify normally generating pairs modulo all AC generators.  Any
geometric label must be defined on the **whole pair orbit**; raw axes or lengths
do not work.

- Required proof: a finite list of normal forms and completeness under arbitrary
  coordinate conjugators.
- Positive outcome: exact distinct normal forms are a quotient obstruction.
- Negative outcome: transitivity closes this target, not the torsion-free
  small-cancellation targets.
- Stabilization: rank-two only.

### D. Equation-defined AC blocks

Gilman–Myasnikov prove that the AC transformation action is faithful using
equations over torsion-free hyperbolic groups.  One may look for a decidable
first-order or existential property `Phi(a,b)` fixed by every elementary AC
generator.  This would give a block system for the action.

The gate is severe: invariance must be a symbolic consequence for all `a,b,h`,
not a test on examples.  Faithfulness alone does not supply such a block.

## Exact certification target

A future successful quotient invariant should ship:

1. the finite presentation of `H` and a proof/certificate of all group
   hypotheses used by the algorithm;
2. the explicit epimorphism `q` (images of `x,y`);
3. a total algorithm computing `I_H` with exact serialized output;
4. proofs of the six identities in the proof gate;
5. stepwise equality on every mandatory control path;
6. exact unequal endpoint outputs;
7. an independent checker which rejects a corrupted group relation, move, and
   endpoint value.

Only that package would upgrade YELLOW to GREEN.  If the endpoint inequality
were then obtained for `AK(3)` and its trivial-group proof retained, it would be
a genuine counterexample certificate—not merely a candidate score.
