# Complete height-15 shell, not a full-orbit certificate

Third strike, 2026-09-04. Section 12 of the strike explicitly requested this
bounded shell. Completeness of its normalization and transitions was proved
before traversal; see `experiments/third_strike/height15_preflight.txt` and
Theorems 2–4 in `HSC_MIXED_BLOCK_NORMAL_FORM.md`.

No theorem says a hypothetical full connecting path stays here. Consequently
these finite components do not separate the unrestricted H_SC AC orbits.

## Exact components

| Domain | AK(3) component | Standard component |
|---|---:|---:|
| Computed canonical vertices | 26 signed cyclic fibers | 23,774 orbits of fibers under eight generator maps |
| Directed canonical adjacency edges, loops included | 76 | 210,008 |
| Accepted normalized multiplication events at the computed representatives | 168 | 940,574 |
| Signed cyclic fibers after undoing generator symmetry | 26 | 185,713 |
| Ordered, geodesically normalized states represented by the fibers | 13,728 | 58,487,624 |
| Other endpoint present | NO | NO |

The eight maps are signed permutations of the **free generators**. They are
isometries of the bounded graph proved to lift to F2, and fix the standard
signed cyclic vertex. Thus paths in the orbit graph lift, and applying all
eight maps recovers exactly the standard component. This does not assert
that these maps extend to automorphisms of H_SC, and it does not treat a
generator map as a relator AC move. It is not used to identify the 26 AK(3)
fibers with additional fibers.

The original unsymmetrized standard pilot reached its explicit 50,000-state
cap. It was replaced by this mathematically justified finite symmetry
calculation, which completed in 20.611 seconds. The cap failure had no
negative significance. The AK(3) traversal took 0.0131 seconds.

The ordered states are given **exactly**, not sampled: take each recorded
cyclic pair, expand the eight maps on the standard side, and apply the finite
free-tail grammar in Theorem 4 under the total cap 15. No 58-million-state
raw traversal was performed. Heights and full counts are in the JSON.

AK(3) has two fibers of cyclic sum 13 and 24 of cyclic sum 15. All retain the
signed conjugacy class of `xyxYXY`. Their ordered expansion has 672 states
at height 13 and 13,056 at height 15; there are no even-height states in it.
The standard component contains the independently certified AK(2) control,
so it still refutes endpoint-height monotonicity.

**Theorem.** Any H_SC connecting path from AK(3) to standard has maximum
height at least **16**.

**Proof.** The graph is the entire induced height-15 component by the
normal-form theorem, and its complete adjacency list excludes standard.
The independent raw-state verification below reproduces the same component.
Since height is integral, every connecting path must leave through >=16. ∎

This is a local barrier. It does not imply AC non-equivalence.

## Boundary and first switches

Every represented ordered state is a boundary state with respect to
**arbitrary conjugation**: both entries are nonidentity, their conjugacy
classes in the non-elementary torsion-free H_SC are infinite, and the allowed
output ball is finite. Thus some conjugations leave the shell from every
state. No finite sample of conjugator words is substituted for this fact.

For an ordered state (u,v), all staying conjugation outputs on the first
coordinate are exactly the freely reduced conjugates of u of length
<=15-|v|, with the correct orientation (without the optional inversion).
The tail grammar lists them. For any supplied g, test g u g^-1 against this
finite list with the exact H_SC word decision: membership means it stays;
nonmembership means it escapes. This is a complete predicate for **all**
conjugation exits, even when the written conjugator is arbitrarily long.
The same rule applies to the other coordinate.

Inversion and permutation never escape. A multiplication escapes exactly
when

```
length(free(u v^epsilon)) + length(v) > 15
```

or the corresponding other-coordinate formula. These are exact geodesic
lengths because each product starts with at most 15 written letters. Together
with the stored fibers and tail grammar, these predicates specify every
staying/escaping legal transition at every ordered state on either side.

For the 26 AK(3) fibers, the finite normalized multiplication boundary has
12,384 candidate events: 168 stay and 12,216 escape. Their exit heights are:

| Height | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 24 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Normalized events | 24 | 376 | 288 | 1,256 | 576 | 4,392 | 1,416 | 3,888 |

All 24 normalized height-16 exits are frozen as literal moves. They change
the braid coordinate and retain the other coordinate. For example:

```
(YXyxyX, xYYYYxx) -> (YXyxYYYxx, xYYYYxx)
         13                         16
```

The source belongs to AK(3)'s fiber; the arrow is one right multiplication.
The braid-changing assertion also holds for any first exit of height exactly
16: source states have odd total height; conjugation preserves parity in
this short free range; retaining the braid coordinate (length 6 or 8) under
multiplication also preserves parity. Only multiplying the braid coordinate
by the odd-length other entry can give height 16. This is a necessary local
pattern, not a proof that any such exit eventually reaches standard.

## Independent verification and files

`certificates/astra_third_strike.json` includes all 26 AK(3) vertices, their
adjacency, counts, all 24 first-exit witnesses, and the new diagram controls.
`certificates/hsc_standard_height15.json.gz` contains the full standard orbit
graph, not only its statistics. Both compressed and uncompressed hashes are
included in the main certificate. Compression is deterministic (`mtime=0`).

`scripts/check_third_strike.py` imports no `acsearch` code. It reconstructs
conjugates by wrapping letters from the inside out instead of enumerating
conjugators. It checks every canonical adjacency and proves connectivity of
the supplied finite graphs. It additionally runs a completely different
**ordered elementary-move BFS** from AK(3):

```
ordered states:                 13,728
literal moves tested:           205,920
accepted directed moves:         96,768
ordered-state digest:
a1b47ff7fd7eb88da79ddc909b6e51d0dec5db97668911e8fa87ee1517369582
```

The generator-conjugation completeness needed for that second implementation
is proved after Theorem 2. Its signed cyclic image is exactly the producer's
26-vertex set. The standard graph is independently recomputed under its
proved normalization; the entire raw standard component is not redundantly
expanded. Certificate PASS concerns these bounded graphs and explicit
controls, not an independent formal proof of a global mixed-peak theorem.
