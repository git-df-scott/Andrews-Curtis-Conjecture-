# Live boundary and single next strike

## Latest: HSC-MIXED-PEAK-3 (after the second strike)

The new canonical continuation is [ASTRA_SECOND_STRIKE.md](ASTRA_SECOND_STRIKE.md).
Individual conjugacy in the fixed H_SC now has a complete rotation-and-piece
algorithm and the explicit bounded-output witness bound K(L)=4L²+4L+8.
The radius-30 geodesic ball is certified. AK(3) must reach sum height at least
15 to escape its short plateau. These results do not provide a peak upper bound.

**Single next strike: HSC-MIXED-PEAK-3.** Prove an effective replacement theorem
for alternating multiplication/conjugation blocks on a peak-minimal path
between the fixed AK(3) state and the standard pair, with an explicit
exceptional height B>=15. Require a well-founded decrease of peak height or
peak multiplicity. The theorem must survive the frozen AK(2) monotonicity
counterexample and the shortest-conjugator mixed reorder that raises height
8 to 11. Exact statements and proofs are in
[HSC_PEAK_LEMMA.md](HSC_PEAK_LEMMA.md). Do not rederive the single-conjugation
bound or enumerate an AC component before obtaining the block theorem.

The earlier second-strike instructions below are preserved as history. Their
conjugacy-algorithm obligation is now met; their peak-height obligation is not.

Date: 2026-09-04.

The strongest retained group is the fixed `H_SC`. Its exact group operations
are certified, but its AK(3) orbit comparison remains **UNKNOWN**. `H_OR` has
the same obstacle and is a secondary laboratory, not a reason to scale a family.
AK(3), AK(4), and the unresolved Miller–Schupp blocks retain their audited
free-group status. AK(3)'s stable triviality is not a supplied premise.

## Single strongest second strike: SC-AC-SHORTEN-2

**Prove a finite peak bound for the fixed H_SC comparison, using genuine
shortlex geodesics and arbitrary-conjugator equations.**

Freeze `A=(x^3 y^-4,xyxYXY)` and `B=(x,y)` in the same marking. The required
output is an explicit integer `L` and a proof of this implication:

```
A ~AC B in H_SC
  => a path exists whose every ordered pair has total geodesic length <= L.
```

Conjugation may be an arbitrary-element macro edge: do not demand that every
letter of its expansion stay below `L`. That macro convention still has the
same unrestricted components, but makes the height claim precise.

The proof must handle the infinite independent-conjugation family. Use
certified conjugacy or equations over `H_SC` to treat that family symbolically.
Begin with the exact two-cell Dehn witnesses as mandatory controls; a proof
that mistakes irreducibility for geodesicity fails immediately. Neither the
small-cancellation overlap bound nor a list of local minima is a peak bound.

**Why this would produce a finite attack.** There are finitely many group
elements of geodesic length at most `L`. Shortlex enumeration with the word
problem gives one representative each. For each pair of vertices, inversion
and multiplication edges are exact word comparisons, and a conjugation edge
is an exact conjugacy problem with the other coordinate fixed. Thus the entire
finite macro graph and its component relation can be decided. One may include
all pairs in this finite graph: starting from A, normal generation is preserved
automatically. A supplied peak theorem upgrades noncontact to separation; the
finite graph without that theorem does not.

**Certificate obligation.** Along with `L`, supply the proof covering every
peak type and a checker for exact group comparisons and conjugacy decisions
used to construct the graph. A positive path needs only equality proofs;
negative adjacency decisions need complete algorithms or replayable proofs.
No current implementation is claimed to provide that certificate.

**Stop before compute** if the bound depends on an unproved shortening lemma,
if arbitrary conjugators are replaced by a sampled ball, or if peak types
cannot be shown to reduce to a finite complete list. Do not start a radius
sweep while trying to discover `L`. This is a theorem task, not a proposal to
spend the old 96 CPU-hour allowance blindly.

The new no-go theorems clarify what any alternative separator must evade:
it must use more than a quantifier-free Boolean combination of group equations,
and more than a profinite-continuous label on the liftable tuples. Quantified
or nonalgebraic geometric information is not ruled out, but no particular new
invariant is promoted here.
