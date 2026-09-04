# ACC — fourth Astra strike

2026-09-04. Continued directly from a7f4adfd24983c5566e8e551ecb01b5fc760dd73.
**No global seam or height bound was obtained. The multi-seam route remains
open; no valid peak-minimal pump was found.**

```
ACC CE: NO
AK(3) F2 CONNECTING PATH: NO
H_SC SEPARATES AK(3): UNKNOWN
SEAM-LENGTH BOUND S(L): NONE
MULTIPLICATION BOUND N(L): NONE
GLOBAL HEIGHT BOUND B: NONE
CONJUGATOR BOUND: K(L)=4L^2+4L+8
ONE-M BOUND: Phi_1(L)=3000(L+1)
HEIGHT-16..23 SHELL COMPLETE: NO
PUMP FOUND: NO
COMPLETE COMPONENT ENUMERATION: NO
INDEPENDENT CERTIFICATE: PASS
```

The NO path fields mean no AK(3)-to-standard path was found, not a proof
that none exists. PASS covers finite controls and the independently replayed
capped transcript. There is no separating certificate. Stop condition **G**.

## What was proved

1. A height-first, then multiplication-count-minimal path has no repeated
   unordered pairs of signed conjugacy classes. If their minimum combined
   representative lengths are bounded by R, then m<=8R*3^(R-1). This is
   conditional on R and supplies no exterior-endpoint N(L).
2. A two-multiplication block whose target coordinate switches has central
   signed-conjugacy seam width <=2L. With the linked hypotheses it has a
   replacement of height <=3000(2L+1). The same-target central class is the
   first local boundary word absent from both exterior endpoints.
3. A seam-width bound R would give height <=3000(max(L,R)+1) by applying
   Phi_1 separately to linked pieces, without iterating it. Off-diagonal,
   non-loop seam edges automatically satisfy the linkage exclusions. Neither
   a bound on R nor diagonal avoidance is known for the fixed comparison.

## What the adversarial work found

An exact two-M block from an AK(3) fiber has a central class-width 23 and
external height <=15. Another two-M block reaches the same endpoint at
height 15. Both use the minimum M count in the liftable height-23 domain.
Thus M-minimality alone does not justify a seam bound; height minimality
must do real work. An infinite inflated raw-seam family also has short
replacements and is explicitly rejected as a pump.

Frozen exact moves can jump from 15 directly to 24, or from 13 to 25 by
macro conjugation. The old 24 height-16 exits are not compulsory gateways.
Uniform bounded cancellation also fails on a normally generating family;
the finite controls prove the stated exact cases and the written argument
proves unboundedness, without mistaking Dehn residues for geodesics.

## The positive-certificate attempt

One exact H=23 traversal was attempted under a predeclared two-million-event
cap. It discovered 4,063 signed cyclic fibers and fully processed 1,038,
without contact with the frozen standard height-15 component. It stopped at
the cap. A separate implementation reproduces every event and every stored
discovery edge. No negative inference or new height lower bound follows.

All **88 tests pass**, preserving the inherited 66. All prior campaign files
and manifests remain unchanged. See [HSC_MULTI_BLOCK.md](HSC_MULTI_BLOCK.md)
for proofs, [HSC_SEAM_4.md](HSC_SEAM_4.md) for exact failures and scope, and
[HSC_LIFTABLE_SHELL.md](HSC_LIFTABLE_SHELL.md) for the bounded computation.
No HSC_HEIGHT_BOUND.md is created because no global B is proved.

**Single strongest fifth strike: HSC-SAME-TARGET-5.** Analyze the central
signed conjugacy class in a height-minimal two-M block that changes the same
coordinate twice. Retain the second coordinate's copying/equality data in
the resulting four-boundary problem, and handle opposite multiplication
signs and diagonal seams explicitly. Prove a replacement bound or a precise
failure of the proposed local rule, using the frozen 13->23->15 example as
a required control. Another shell expansion is not the missing theorem.
