"""Verification utilities: certificates and trivial-group checks.

Search is never evidence of non-equivalence.  The routines in this module only
certify positive claims by exact replay (or, separately, prove that a presented
group has order one when Todd--Coxeter enumeration completes).
"""
from __future__ import annotations
from typing import Sequence, Tuple
from .words import Word, cyclic_canonical, reduce, unparse
from .moves import apply_path, Move
from .presentation import Presentation, standard_key


PackagedMove = tuple


def verify_certificate(p: Presentation, path: Sequence[Move]) -> bool:
    """Replay ``path`` from ``p`` and check that the result is the standard
    presentation up to conjugating / inverting / permuting relators."""
    end = apply_path(p.rels, path)
    return tuple(sorted(cyclic_canonical(r) for r in end)) == standard_key(p.n)


def apply_packaged_move(rels: Tuple[Word, ...], move: PackagedMove,
                        n: int) -> Tuple[Word, ...]:
    """Apply the public Carreras ledger vocabulary exactly.

    Supported moves are ``("invert", i)``, ``("conj", i, g)``,
    ``("mul", i, j, sign)``, and ``("cycle", i, k)``.  A cycle is a
    packaged AC move: left rotation by one letter ``a`` is conjugation by
    ``a^-1`` followed by free reduction.  Indices are zero-based.

    This routine deliberately performs no canonicalization between steps.
    Certificate replay must follow the recorded representatives, not merely a
    quotient graph.
    """
    if not isinstance(move, (tuple, list)) or not move:
        raise ValueError("malformed packaged move")
    op = move[0]
    out = list(rels)
    if op == "invert" and len(move) == 2:
        i = move[1]
        if not isinstance(i, int) or not 0 <= i < len(out):
            raise ValueError(move)
        out[i] = tuple(-a for a in reversed(out[i]))
    elif op == "conj" and len(move) == 3:
        i, g = move[1:]
        if (not isinstance(i, int) or not 0 <= i < len(out)
                or not isinstance(g, int) or g == 0 or abs(g) > n):
            raise ValueError(move)
        out[i] = reduce((g,) + out[i] + (-g,))
    elif op == "mul" and len(move) == 4:
        i, j, sign = move[1:]
        if (not all(isinstance(x, int) for x in (i, j, sign))
                or not 0 <= i < len(out) or not 0 <= j < len(out)
                or i == j or sign not in (-1, 1)):
            raise ValueError(move)
        rhs = out[j] if sign == 1 else tuple(-a for a in reversed(out[j]))
        out[i] = reduce(out[i] + rhs)
    elif op == "cycle" and len(move) == 3:
        i, k = move[1:]
        if (not isinstance(i, int) or not 0 <= i < len(out)
                or not isinstance(k, int) or not out[i]):
            raise ValueError(move)
        k %= len(out[i])
        out[i] = reduce(out[i][k:] + out[i][:k])
    else:
        raise ValueError(move)
    return tuple(out)


def apply_packaged_ledger(p: Presentation,
                          moves: Sequence[PackagedMove]) -> Tuple[Word, ...]:
    rels = p.rels
    for move in moves:
        rels = apply_packaged_move(rels, move, p.n)
    return rels


def verify_equivalence_ledger(p: Presentation, target: Presentation,
                              moves: Sequence[PackagedMove]) -> bool:
    """Certify that a ledger reaches the target's AC-realizable orbit.

    The terminal comparison allows relator order, inversion, and cyclic
    rotation, all of which are realizable by elementary AC moves.
    """
    if p.n != target.n:
        return False
    end = apply_packaged_ledger(p, moves)
    return tuple(sorted(cyclic_canonical(r) for r in end)) == target.cyclic_key()


def describe_path(p: Presentation, path: Sequence[Move]) -> str:
    lines = [str(p)]
    rels = p.rels
    from .moves import apply_move
    for mv in path:
        rels = apply_move(rels, mv)
        lines.append(f"{mv[0]}({mv[1]},{mv[2]}) -> " + ", ".join(unparse(r) for r in rels))
    return "\n".join(lines)


def abelianization_is_trivial(p: Presentation) -> bool:
    """Necessary condition: the relator exponent matrix is unimodular."""
    from fractions import Fraction
    M = [[Fraction(v) for v in row] for row in p.abelianization_matrix()]
    n = len(M)
    if n != p.n:
        return False
    det = Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return False
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return abs(det) == 1


def group_order(p: Presentation, max_cosets: int = 200000):
    """Order of the group presented by p via Todd-Coxeter (sympy).  Returns
    None if enumeration does not complete within max_cosets."""
    from sympy.combinatorics.free_groups import free_group
    from sympy.combinatorics.fp_groups import FpGroup
    names = "xyzuvw"[: p.n]
    F, *gens = free_group(", ".join(names))
    def to_elt(w):
        e = F.identity
        for a in w:
            g = gens[abs(a) - 1]
            e = e * (g if a > 0 else g ** -1)
        return e
    G = FpGroup(F, [to_elt(r) for r in p.rels])
    try:
        return G.order(strategy="relator_based") if False else _order(G, max_cosets)
    except Exception:
        return None


def _order(G, max_cosets):
    from sympy.combinatorics.coset_table import CosetTable
    from sympy.combinatorics.fp_groups import coset_enumeration_r
    C = coset_enumeration_r(G, [], max_cosets=max_cosets)
    C.compress()
    return len(C.table)


def presents_trivial_group(p: Presentation, max_cosets: int = 200000) -> bool:
    return abelianization_is_trivial(p) and group_order(p, max_cosets) == 1
