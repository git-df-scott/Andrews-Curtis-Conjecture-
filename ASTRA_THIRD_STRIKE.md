# ACC — third Astra strike

2026-09-04. Continued from `ecaa80a` in the unchanged H_SC marking.
**A linked one-multiplication block now has an explicit height bound.
The unrestricted alternating-block theorem remains open.**

```
ACC CE: NO
H_SC SEPARATES AK(3): UNKNOWN
MIXED-PEAK THEOREM: OPEN
EXPLICIT HEIGHT BOUND B: NONE
CONJUGATOR BOUND: K(L)=4L^2+4L+8
COMPLETE COMPONENT ENUMERATION: NO
CONNECTING AC PATH FOUND: NO
FROZEN COUNTEREXAMPLES SURVIVE: YES
INDEPENDENT CERTIFICATE: PASS
```

COMPLETE COMPONENT ENUMERATION refers to an enumeration deciding the full
orbit comparison under a proved global B. Both requested **height-15 induced
components** were completely determined; their noncontact is a local barrier.
PASS covers those finite certificates and controls, not AK(3) separation or
an independently formalized global theorem. Stop condition **F**.

## Main results

- **One-M theorem:** for linked cyclic boundary triples, one multiplication
  surrounded by arbitrary independent conjugations has a replacement of
  height at most **Phi_1(L)=3000(L+1)**. The explicit planar bounds are
  F<=3P+3 and E_metric<=92P+91. K is applied only after the height is bounded.
- **Exact shell:** AK(3)'s component has 26 signed cyclic fibers representing
  **13,728 ordered states**. The standard component has 23,774 symmetry
  vertices, expanding to 185,713 cyclic fibers and **58,487,624 ordered
  states**, represented by a finite grammar. They are disjoint.
- **Stronger local barrier:** every connecting H_SC path must reach height
  **at least 16**. All 24 normalized height-16 exits change the braid
  coordinate. This is not a full-orbit separator.
- **Free lifting:** every H_SC path from either endpoint with height <=23
  lifts to F2. A connecting path there would settle AK(3)'s free AC status.
  No graph at heights 16–23 was enumerated.
- **Adversarial controls:** both frozen counterexamples remain byte-for-byte
  unchanged. A new 4->5->3 witness rejects testing multiplication height only
  after cyclic normalization. The proposed uniformly short-endpoint pump is
  impossible by finiteness; computable height control is the real question.
- **Verification:** **66 tests passed in 28.75 seconds**, including all prior
  48. A separate ordered-state algorithm reproduces AK(3)'s full 13,728-state
  shell, and the independent checker verifies every standard orbit-graph edge.

The missing proof is precise: a single diagram's bound depends on its own
boundary words. Alternating multiplication introduces internal words and
copies retained coordinates. Neither their lengths nor their number is
controlled by the short exterior endpoints. The one-M theorem cannot be
iterated into a global B by replacing those unknown lengths with L.

Proofs: [HSC_MIXED_BLOCK_NORMAL_FORM.md](HSC_MIXED_BLOCK_NORMAL_FORM.md).
Complete local result: [HSC_HEIGHT_15_SHELL.md](HSC_HEIGHT_15_SHELL.md).
Work ledger: [HSC_MIXED_PEAK_3.md](HSC_MIXED_PEAK_3.md).
Exact graph and controls: [astra_third_strike.json](certificates/astra_third_strike.json).
Older canonical files and both earlier hash manifests are preserved intact;
this document is the newest continuation record.

**Single strongest fourth strike: HSC-SEAM-4.** Prove effective internal
boundary control for a minimal mixed block in the fixed comparison, using
the one-M theorem and frozen first-switch constraints. No further radius
sweep is a substitute for that proof.
