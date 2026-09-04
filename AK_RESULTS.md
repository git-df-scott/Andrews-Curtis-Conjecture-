# Frontier results after the hyperbolic invariant gate

**Superseding first-strike result:** the AK(3) entry for the distinguished
`Delta(2,3,7)` marking is **SAME ORBIT**, not UNKNOWN. Ten elementary moves
already work in `C2*C3`, so the triangle result and the P3/P4 consequences
follow by functoriality. H_SC and H_OR remain UNKNOWN. The historical table
below records the earlier gate; current marked results and certificate are in
`QUOTIENT_LEDGER.md` and `certificates/astra_first_strike.json`.

## Outcome

No nonconstant computable AC invariant survived the move proof and controls.
Accordingly, no hyperbolic-target frontier score was produced.  This is the
required stop behavior: evaluating lengths, traces, axes, commutators or a
bounded component search on the candidates would create numbers with no
counterexample meaning.

For each distinguished epimorphism `q:F2->>H` to `H_SC`, `H_OR`, or
`Delta(2,3,7)`, the following exact statements do hold.

| Object | total length | `<<q(R)>>_H` | abelian AC class | exact comparison with `[q(x),q(y)]_AC` | inference |
|---|---:|---|---|---|---|
| standard `(x,y)` | 2 | `H` | basis | equal by definition | control |
| `AK(2)` | 11 | `H` | basis | equal because `AK(2)` is AC-trivial in `F2` | quotient control |
| `AK(3)` | 13 | `H` | basis | **UNKNOWN** | remains open |
| `P3=MS(3,yx^2y)` | 14 | `H` | basis | exactly the same unknown component question as `AK(3)` | public `P3~AK3` ledger |
| `P4=MS(3,y^-1x^2y^-1)` | 14 | `H` | basis | exactly the same unknown component question as `AK(3)` | public `P4~AK3` ledger, locally replayed |
| `P1=MS(2,x^-2y^-1x^2y)` / `P6` block | 14 | `H` | basis | **UNKNOWN** | block not publicly joined to `AK(3)` |
| `P2=MS(2,x^-2y^-1x^2y^-1)` / `P5` block | 14 | `H` | basis | **UNKNOWN** | block not publicly joined to `AK(3)` |
| `AK(4)` | 15 | `H` | basis | **UNKNOWN** | remains open |

The normal-closure column follows functorially: the relators of each listed
trivial-group presentation normally generate `F2`, so their images normally
generate every quotient.  The abelian column follows from the unimodular
exponent-sum matrix.  Neither column separates anything.

## What was deliberately not computed

- no bounded AC ball in `H_SC`, `H_OR`, or the triangle group;
- no finite quotient of those groups;
- no raw translation length, trace, scl, axis, boundary, centralizer or
  subgroup-geometry score on a frontier pair;
- no new word search for any free-group trivialization;
- no claim that a timeout or an `UNKNOWN` component comparison is negative.

## Required interpretation if a future difference appears

Before a difference may be called a serious CEC, all five gates remain:

1. independently verify the finite presentation of `H` and the epimorphism;
2. replay the exact invariant computation;
3. prove invariance under inversion, both multiplication directions, and
   independent conjugation by every element of `H`;
4. search for and replay a legal AC path contradicting the proposed label as a
   falsification test—not as evidence if none is found;
5. verify covariance under allowed presentation-coordinate changes, or freeze
   the marked quotient in a mathematically legitimate way.

No difference was observed because no unproved quantity was promoted to an
invariant.  Therefore:

- **CE: no**
- **CEC: no**
- **candidate status changed: none**
