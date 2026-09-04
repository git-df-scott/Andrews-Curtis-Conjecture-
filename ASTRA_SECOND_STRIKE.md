# ACC — second Astra strike

2026-09-04. Continued directly from first strike `82fe261` in the same H_SC.
**The conjugator bound is proved. The requested fixed-endpoint peak upper
bound remains open, so no AC component was enumerated.**

```
ACC CE: NO
H_SC SEPARATES AK(3): UNKNOWN
PEAK-REDUCTION THEOREM: OPEN
EXPLICIT PEAK BOUND: NONE
EXPLICIT CONJUGATOR BOUND: K(L)=4L^2+4L+8
COMPLETE COMPONENT ENUMERATION: NO
CONNECTING AC PATH FOUND: NO
INDEPENDENT CERTIFICATE: PASS
```

The final PASS covers finite overlap/product certificates, the AK(2) positive
control, and explicit failure witnesses, **not an AK(3) separation certificate**.
CONNECTING AC PATH FOUND refers to AK(3) in H_SC; the AK(2) control is connected.
K(L) bounds a conjugator when its source and output both have geodesic length
at most L. It is not a bound on the height of an unknown AC path.
Stop condition **F**, not a proof that H_SC or all peak reduction is incapable.

## What this strike established

- **Exact geometry:** no nonempty reduced null word has length below 61.
  Freely reduced words through length 30 are unique geodesics. Longer Dehn
  residues remain unsafe; the inherited counterexample is a regression test.
- **Conjugator theorem:** four consecutive pieces cover at most 23 letters
  of a length-61 relator. The annular C(6)-map lemma therefore gives a
  rotation-and-piece conjugacy algorithm with rung length at most 8.
  Tracking cyclic reduction gives the explicit K(L) above, including arbitrary
  conjugators, identities, and centralizer ambiguity. Ordinary C'(1/8) is
  false here and was not assumed.
- **AK(3) barrier:** any path to the standard pair must first reach total
  geodesic length at least **15**. This is a lower bound, not separation.
- **Genuine counterexamples to shortcuts:** AK(2) is connected to standard by
  a checked 23-move ledger, but cannot be connected at its starting sum 11
  or starting maximum 6. Also the standard mixed reorder with a shortest
  conjugator can increase a peak from 8 to 11. Neither fact disproves an
  upper bound with a larger, explicitly allowed excess.
- **Implemented and independently checked:** exact individual conjugacy;
  literal non-free conjugacy via one relator; all 120+168 plateau products;
  AK(2) ledger and mixed-reorder witness. The old 23-test suite and all new
  regressions pass: **48 passed in 1.53 seconds**. Exact run records are in
  the validation log.

The unresolved step is multiplication interleaved with independent
conjugation. The tempting reorder exposes g^-1 v g; controlling g u g^-1
does not control that second output. A bound conditional on both outputs
being short cannot prove that a connecting AC path stays short.

Proofs: [HSC_PEAK_LEMMA.md](HSC_PEAK_LEMMA.md).
Exact work ledger and reproduction: [SC_AC_SHORTEN_2.md](SC_AC_SHORTEN_2.md).
Frozen certificate: [certificates/astra_second_strike.json](certificates/astra_second_strike.json).
No `HSC_COMPONENT_CERTIFICATE.md` is produced because enumeration never became
legitimate. H_OR and the previously closed quotient markings were not reopened.
Only the specifically required existing tests replay their frozen controls.

**Single strongest third strike:** `HSC-MIXED-PEAK-3`: prove an explicit
exceptional height for alternating multiplication/conjugation blocks in the
fixed AK(3) comparison, using the now-certified annular conjugacy machinery.
The replacement must survive both frozen counterexamples and give a
well-founded peak-lowering argument before any component enumeration.
