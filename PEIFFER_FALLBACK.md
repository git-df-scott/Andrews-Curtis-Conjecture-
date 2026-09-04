# Based crossed-module / Peiffer fallback

## Verdict on the fallback

The **unbased fundamental crossed module is structurally dead** for balanced
presentations of the trivial group.  Keeping distinguished 2-cell generators
avoids that immediate collapse, but then their orbit under basis changes is
essentially the original AC problem.  A useful finite truncation would need a
new theorem showing that it retains based information without factoring through
the boundary, abelianization, a relation module, or stabilization.

This is a bounded structural result, not a computational failure.

## Exact object

For `P=<X|R>`, let `F=F(X)` and let

```text
partial : C(R) -> F
```

be the free crossed `F`-module on symbols `rho_i`, with

```text
partial(rho_i)=r_i,
partial({}^g c)=g partial(c) g^-1,
{}^{partial(c)} d = c d c^-1.
```

One concrete pre-quotient uses symbols `{}^g rho_i` and their inverses;
Peiffer commutators impose the second crossed-module identity.  The kernel of
`partial` is `pi_2(K_P)` and the cokernel is `pi_1(K_P)` for the presentation
2-complex.

The ordered based enhancement is

```text
(partial:C(R)->F ; rho_1,...,rho_n ; X).
```

It remembers the chosen 1-cell and 2-cell bases rather than only the homotopy
2-type.

## Relationship to elementary AC moves

With the displayed convention, the boundary identities lift as

| relator move | crossed-module basis move |
|---|---|
| `r_i -> r_i^-1` | `rho_i -> rho_i^-1` |
| `r_i -> r_i r_j` | `rho_i -> rho_i rho_j` |
| `r_i -> g r_i g^-1` | `rho_i -> {}^g rho_i` |

Inverse basis moves give isomorphisms back.  Thus an isomorphism class of a
based quotient of this object can be AC-invariant—but only if the quotient
construction is functorial for all three rows and its equality notion does not
forget the distinguished basis prematurely.

Ordinary group quotienting applies only `partial` and remembers the boundary
words `q(r_i)`.  It discards the lifts, Peiffer identities, and 2-cell basis;
that explains what the proposed fallback hoped to retain.

## Structural collapse for trivial-group presentations

For a balanced trivial-group presentation with `n` generators and `n`
relators, the finite presentation complex `K_P` has Euler characteristic 1.
It is simply connected.  Therefore `H_1(K_P)=0`, and the Euler characteristic
gives `H_2(K_P)=0`.  Hurewicz gives `pi_2(K_P)=0`; equivalently, the acyclic
simply connected CW complex is contractible.

Consequently

```text
ker(partial)=pi_2(K_P)=0,
coker(partial)=pi_1(K_P)=1.
```

The boundary map is therefore an isomorphism `C(R) ~= F`.  After forgetting
the distinguished `rho_i`, the crossed module contains no extra information.
After retaining them, `partial(rho_i)=r_i` identifies the based tuple with the
original relator tuple.  Deciding whether that based tuple can be changed to
the standard basis by the three displayed operations is the AC-orbit problem,
not a simpler invariant supplied for free by crossed-module language.

## Peiffer sequences

An identity among relations is a product

```text
(g_1 r_{i_1}^{e_1} g_1^-1) ...
(g_m r_{i_m}^{e_m} g_m^-1) = 1 in F.
```

Peiffer exchanges and insertion/deletion of inverse pairs change its expression
without changing the crossed-module element.  Because `pi_2(K_P)=0`, ordinary
identity classes do not yield a nonzero second-homotopy label here.  Lengths,
minimal Peiffer areas, or bounded simplification failures also are not
automatically AC-invariant: an AC basis change changes the generating
expressions themselves.

## Truncation audit

| Proposed representation | What it retains | Failure risk | Gate |
|---|---|---|---|
| abelianized crossed module / relation module | linear identities and Fox data | factors through the already-dead stable/module information | reject if an explicit factorization is obtained |
| nilpotent quotient of `C(R)` and `F` | bounded commutator depth | likely falls into nilpotent/soluble quotient blindness after applying `partial` | prove nonfactorization before candidates |
| bounded Peiffer word length | computational complexity of one expression | not invariant under basis changes; nontermination/noncontact has no force | do not use as separator |
| based automorphism groupoid of free crossed-module bases | exact unstable basis data | may simply restate the full AC orbit | require a finite complete presentation or a decidable quotient |
| degree-`d` nonabelian Peiffer filtration | potentially retains interactions among lifts | no current proof it is nonconstant or move-functorial | only live experimental gate |

## Smallest useful experiment

Use degree at most 3 and no frontier search:

1. implement formal words `{}^g rho_i` with boundary words in `F2`;
2. encode the three basis isomorphisms above and their inverses;
3. derive the induced maps on a degree-3 Peiffer-commutator filtration
   symbolically;
4. prove whether the resulting object factors through the augmented Fox matrix,
   a nilpotent boundary quotient, or the stabilization colimit;
5. only if nonfactorization is proved, replay the standard, `AK(2)`, synthetic
   128-move, and Carreras controls.

### Stop condition

Stop immediately if the degree-3 object is determined by `partial` plus the
abelianized exponent matrix, becomes a stable module class, or fails one basis
move.  Such a result closes that truncation.  It does not justify increasing
the degree automatically and does not say anything negative about `AK(3)`.

## Net lesson

Crossed modules explain exactly what ordinary quotienting forgets, but for a
contractible balanced presentation the unbased crossed module itself collapses.
Any surviving Peiffer attack must live in a **based orbit or non-stable
filtration of presentations**, and it must demonstrate real compression of the
AC problem rather than rename it.

## Sources

- Huebschmann, [Crossed modules](https://arxiv.org/abs/2403.15900), for the
  free crossed module, Peiffer identities, and identities among relations.
- Brown–Razak Salleh, [Free crossed resolutions of groups and presentations of
  modules of identities among relations](https://arxiv.org/abs/math/9812132),
  for `ker(partial)=pi_2(K(P))` in the presentation setting.
