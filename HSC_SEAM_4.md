# HSC-SEAM-4 execution ledger

2026-09-04. Continuation of astra/third-strike at a7f4adf on branch
astra/fourth-strike. All files from Strikes 1–3, their frozen counterexamples,
certificates and hash manifests are preserved unchanged.

## Status by claim

| Status | Result | Limitation |
|---|---|---|
| **PROVED** | Same signed two-class fiber admits a bridge of at most five neutral macro moves without exceeding the larger endpoint height | Uses arbitrary conjugation; K applies only once endpoint lengths are bounded |
| **PROVED** | A height-first, then M-count-minimal path has no repeated seam types | The minimality order is specified; retained-class repetition alone does not suffice |
| **PROVED** | If seam width is <=R, then m<=8R*3^(R-1) for R>=1 | Conditional on R; no N(L) for exterior length L |
| **PROVED** | With linked one-M pieces and seam width <=R, height <=3000(max(L,R)+1) suffices | No unknown seam bound is supplied; diagonal exceptions remain explicit |
| **PROVED** | Two M moves with switched targets have central signed seam width <=2L | Local two-M statement, not a bound for an arbitrarily long region |
| **PROVED** | Non-diagonal distinct successive seam types give the linked one-M exclusions | No diagonal-avoidance theorem for AK(3) |
| **COMPUTATIONALLY VERIFIED** | The entire capped 2,000,000-event height-23 transcript, 4,062 discovery witnesses and target checks | Incomplete search; zero contact has no negative force |
| **COMPUTATIONALLY VERIFIED** | 180 switched-target and 3,378 same-target two-M tree segments | Tree observations only, not a census of minimal blocks |
| **DISPROVED** | M-minimality and distinct seam types alone force seams below exterior height | A two-M AK(3)-fiber block has seam width 23 and a two-M height-15 replacement |
| **DISPROVED** | Fixed M count and distinct class pairs bound raw seams in arbitrary representatives | The n-parameter two-M family below has short replacements |
| **DISPROVED** | Every first departure from the low component lands at 16 | Frozen exact jumps 15->24 by M and 13->25 by macro C |
| **DISPROVED** | Legal multiplication has a uniform cancellation constant independent of its input states | A normally generating free-basis family has unbounded cancellation |
| **HEURISTIC** | Marked corridor reduction might control a same-target two-M seam | No diagram simplification theorem or global decrease is claimed |
| **OPEN** | S(L), N(L), global B, diagonal avoidance, AK(3) F2 and H_SC comparison | No counterexample gate or full component enumeration is opened |

## A finite certificate for an infinite raw-seam phenomenon

For n>=2, take the following free AC block:

    (x,y)
      C0(y^n): (y^n x Y^n, y)
      M0:      (y^n x Y^(n-1), y)
      M0:      (y^n x Y^(n-2), y)
      C0(Y^n): (x y^2, y).

Its seam classes are ([x]±,[y]±), ([xy]±,[y]±),
([xyy]±,[y]±), all distinct, of maximum width 4. The displayed raw internal
seam has unbounded geodesic length in H_SC. Indeed every defining 31-letter
window has at least ten x/X letters, checked over all 244 symmetrized
relators. A nonempty freely reduced y^k x Y^k X has only two such letters,
so is Dehn-irreducible and nontrivial for k!=0. Thus all y^n x Y^n, and
therefore all y^n x Y^(n-1), are distinct. Finiteness of balls proves their
lengths tend to infinity. No long-word geodesic formula is assumed.

For n=2..14 every displayed coordinate is <=30 letters, so the raw seam
height is exactly 2n+1; all thirteen instances are frozen. In every case
the two direct multiplications (x,y)->(xy,y)->(xyy,y) give height 4.
The inflated family is therefore **not a pump against peak-minimality**.
Its M count is minimal in F2 by exponent vectors, but the minimum number
of M moves in unrestricted H_SC is not inferred from abelianization.

The additional AK(3)-fiber 13->23->15 example is stronger for canonical
seams. Both its high path and low replacement use two multiplications;
two is independently proved minimal within H<=23 by complete root-edge
normalization. It likewise fails height-first minimality and cannot kill
the route. Exact ledgers are in certificates/astra_fourth_strike.json.

## Preserved hypotheses and adversarial checks

K(L)=4L^2+4L+8 bounds an individual conjugator when **both element endpoints**
have geodesic representatives of length <=L. It is not an unknown path-height
bound. Phi_1(L)=3000(L+1) remains restricted to a **linked, one-M** block.
The new non-diagonal criterion is a sufficient linkage test, not permission
to ignore unlinked cases.

The old AK(2) height obstruction and shortest-conjugator mixed-reorder failure
remain byte-identical. A fiber bridge refuses their differing endpoint types;
it cannot simulate a multiplication for free. The old raw-output-height
counterexample remains part of the extended edge tests. The new checks also
reject false global-bound labels, missing cancellation, altered seam heights,
corrupt relator-window data and relabelling a capped prefix as complete.

The four requested reports, new producer, independent string checker, tests,
exact positive ledgers, compressed discovery transcript and run logs are
the complete new work. No older quotient experiment or failed relative probe
was rerun. Required baseline tests replay their frozen controls only.

## Reproduce and interpret verification

    python -m acsearch.hsc_seam
    python -m experiments.fourth_strike.make_controls
    python scripts/check_fourth_strike.py --replay
    python -m pytest -q
    sha256sum -c certificates/SHA256SUMS
    sha256sum -c certificates/SECOND_STRIKE_SHA256SUMS
    sha256sum -c certificates/THIRD_STRIKE_SHA256SUMS
    sha256sum -c certificates/FOURTH_STRIKE_SHA256SUMS

The independent route imports no acsearch code. It reconstructs the complete
capped prefix using a different conjugate generator, verifies every literal
failure witness and checks arithmetic by direct convolution. It independently
replays the complete root neighborhood used for the new two-M lower bound.
PASS is about these finite artifacts, not a machine formalization or an
independent human review of the written mathematics, and not AK(3) separation.

All 66 inherited tests plus 22 new tests pass. Exact runtimes are in the
validation log. Stop condition **G**: the bounded high-value seam tasks of
this strike are exhausted. The local switched-target bound is not the
unrestricted S(L) required by stop condition B.
