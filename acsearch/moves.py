"""Andrews-Curtis moves.

Two views of the same equivalence relation are provided.

1. ``ac_neighbors``: relators are ordered, freely reduced words and the moves
   are the classical elementary ones
     (I)  r_i <- r_i^-1
     (M)  r_i <- r_i r_j^{+-1},  i != j
     (C)  r_i <- g r_i g^-1,      g a generator or its inverse.
   These are exactly the moves whose sequences form a *certificate*.

2. ``cyclic_neighbors``: relators are cyclic words up to inversion.  Since
   conjugation and inversion are AC moves, a presentation is determined up to
   those moves by the multiset of conjugacy classes {[r_i]^{+-1}}, and the only
   remaining move is
        [r_i] <- [ rot(r_i) . g . rot(r_j)^{+-1} . g^-1 ]
   for a bounded conjugator g. This implementation enumerates a finite
   collection of legal moves. Its residual-conjugator cutoff is not a
   certified completeness theorem for the full length-bounded AC graph.
"""
from __future__ import annotations
from itertools import product
from typing import Iterator, List, Tuple
from .words import Word, reduce, inverse, mul, cyclic_reduce, rotations, cyclic_canonical

# ---------------------------------------------------------------- ordered moves

Move = Tuple[str, int, int]   # (kind, i, j)  kind in {"I","M","C"}
# "I": invert relator i (j ignored)
# "M": r_i <- r_i * r_j^sign, encoded j = +-(index+1)
# "C": r_i <- g r_i g^-1 with g = j (signed generator)


def all_moves(n: int, m: int, include_inverse: bool = True) -> List[Move]:
    mv: List[Move] = []
    for i in range(m):
        if include_inverse:
            mv.append(("I", i, 0))
        for j in range(m):
            if i != j:
                mv.append(("M", i, j + 1))
                mv.append(("M", i, -(j + 1)))
        for g in range(1, n + 1):
            mv.append(("C", i, g))
            mv.append(("C", i, -g))
    return mv


def apply_move(rels: Tuple[Word, ...], mv: Move) -> Tuple[Word, ...]:
    kind, i, j = mv
    r = list(rels)
    if kind == "I":
        r[i] = inverse(r[i])
    elif kind == "M":
        other = rels[abs(j) - 1]
        if j < 0:
            other = inverse(other)
        r[i] = mul(r[i], other)
    elif kind == "C":
        r[i] = reduce((j,) + r[i] + (-j,))
    else:
        raise ValueError(mv)
    return tuple(r)


def apply_path(rels: Tuple[Word, ...], path) -> Tuple[Word, ...]:
    for mv in path:
        rels = apply_move(rels, mv)
    return rels


def ac_neighbors(rels: Tuple[Word, ...], n: int, max_rel_len: int | None = None,
                 include_inverse: bool = True) -> Iterator[Tuple[Move, Tuple[Word, ...]]]:
    for mv in all_moves(n, len(rels), include_inverse):
        new = apply_move(rels, mv)
        if max_rel_len is not None and len(new[mv[1]]) > max_rel_len:
            continue
        yield mv, new


# ---------------------------------------------------------------- cyclic moves

def words_up_to(n: int, k: int) -> List[Word]:
    """All freely reduced words of length <= k in F_n (including empty)."""
    out: List[Word] = [()]
    layer: List[Word] = [()]
    letters = [g for g in range(1, n + 1)] + [-g for g in range(1, n + 1)]
    for _ in range(k):
        nxt = []
        for w in layer:
            for a in letters:
                if w and w[-1] == -a:
                    continue
                nxt.append(w + (a,))
        out.extend(nxt)
        layer = nxt
    return out


def cyclic_neighbors(rels: Tuple[Word, ...], n: int, max_total: int,
                     slack: int = 0) -> Iterator[Tuple[Word, ...]]:
    """Neighbours of a presentation in the cyclic-word model, restricted to
    total length <= max_total.  ``rels`` must be a sorted tuple of cyclic
    canonical words; the output is likewise canonical.

    Output edges are sound. Completeness of the residual-conjugator cutoff
    is not certified here; noncontact is not an orbit-separation certificate.
    """
    m = len(rels)
    total = sum(len(r) for r in rels)
    for i in range(m):
        ri = rels[i]
        budget = max_total - (total - len(ri))     # allowed length of new r_i
        for j in range(m):
            if i == j:
                continue
            rj = rels[j]
            # Even when the uncancelled product exceeds budget, g=1 can
            # produce a shortening edge. Never skip that case.
            gmax = max(0, (budget - len(ri) - len(rj)) // 2 + slack)
            seen = set()
            rots_i = list(rotations(ri))
            rots_j = list(rotations(rj)) + list(rotations(inverse(rj)))
            for g in words_up_to(n, gmax):
                gi = inverse(g)
                for a in rots_i:
                    ag = mul(a, g)
                    for b in rots_j:
                        w = cyclic_reduce(mul(mul(ag, b), gi))
                        if len(w) > budget:
                            continue
                        c = cyclic_canonical(w)
                        if c in seen:
                            continue
                        seen.add(c)
                        new = list(rels)
                        new[i] = c
                        yield tuple(sorted(new))
