"""Move-level controls for proposed Andrews--Curtis quantities.

The functions intentionally include *failed* candidate quantities.  Tests give
exact elementary-move witnesses for their failure, preventing them from being
reintroduced later as invariants.
"""
from __future__ import annotations

from fractions import Fraction
from random import Random
from typing import Iterable, Sequence

from .moves import Move, all_moves, apply_move, apply_path
from .presentation import Presentation
from .words import Word, cyclic_canonical, cyclic_reduce, inverse, reduce

Permutation = tuple[int, ...]


def compose_permutations(p: Permutation, q: Permutation) -> Permutation:
    """Composition p after q, with permutations stored by their images."""
    if len(p) != len(q):
        raise ValueError("permutation degrees differ")
    return tuple(p[q[i]] for i in range(len(p)))


def inverse_permutation(p: Permutation) -> Permutation:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    if sorted(p) != list(range(len(p))):
        raise ValueError("not a permutation")
    return tuple(out)


def evaluate_permutation_word(word: Word,
                              images: Sequence[Permutation]) -> Permutation:
    """Evaluate a free-group word exactly in a finite permutation group."""
    if not images or any(len(p) != len(images[0]) for p in images):
        raise ValueError("nonempty equal-degree images required")
    value = tuple(range(len(images[0])))
    for letter in word:
        image = images[abs(letter) - 1]
        if letter < 0:
            image = inverse_permutation(image)
        value = compose_permutations(value, image)
    return value


def generated_permutation_group(generators: Iterable[Permutation]
                                ) -> frozenset[Permutation]:
    """Exact closure, intended only for tiny witness groups in tests."""
    gens = tuple(generators)
    if not gens:
        raise ValueError("generators required")
    identity = tuple(range(len(gens[0])))
    seen = {identity}
    frontier = [identity]
    while frontier:
        a = frontier.pop()
        for b in gens:
            c = compose_permutations(a, b)
            if c not in seen:
                seen.add(c)
                frontier.append(c)
    return frozenset(seen)


def exponent_matrix(rels: Sequence[Word], rank: int) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(r.count(g) - r.count(-g) for g in range(1, rank + 1))
                 for r in rels)


def determinant_abs(rels: Sequence[Word], rank: int) -> Fraction:
    """Absolute determinant of the exponent matrix (square tuples only)."""
    matrix = exponent_matrix(rels, rank)
    if len(matrix) != rank:
        raise ValueError("determinant requires a balanced tuple")
    a = [[Fraction(x) for x in row] for row in matrix]
    det = Fraction(1)
    for col in range(rank):
        pivot = next((i for i in range(col, rank) if a[i][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        p = a[col][col]
        det *= p
        for j in range(col, rank):
            a[col][j] /= p
        for i in range(col + 1, rank):
            q = a[i][col]
            for j in range(col, rank):
                a[i][j] -= q * a[col][j]
    return abs(det)


def cyclic_length_multiset(rels: Sequence[Word]) -> tuple[int, ...]:
    """Failed candidate: changed by relator multiplication."""
    return tuple(sorted(len(cyclic_reduce(r)) for r in rels))


def individual_conjugacy_multiset(rels: Sequence[Word]) -> tuple[Word, ...]:
    """Failed candidate: independent conjugacy is safe, multiplication is not."""
    return tuple(sorted(cyclic_canonical(r) for r in rels))


def commutator(a: Word, b: Word) -> Word:
    return reduce(a + b + inverse(a) + inverse(b))


def commutator_conjugacy_class(rels: Sequence[Word]) -> Word:
    """Failed AC candidate: Nielsen-safe for pairs, but not AC-conjugacy-safe."""
    if len(rels) != 2:
        raise ValueError("pair required")
    return cyclic_canonical(commutator(rels[0], rels[1]))


def inverse_move(move: Move) -> Move:
    kind, i, j = move
    if kind == "I":
        return move
    if kind in {"M", "C"}:
        return kind, i, -j
    raise ValueError(move)


def inverse_path(path: Sequence[Move]) -> list[Move]:
    return [inverse_move(move) for move in reversed(path)]


def deterministic_ac_walk(
        p: Presentation, steps: int, seed: int,
        max_total_length: int = 160
) -> tuple[tuple[Word, ...], list[Move], list[tuple[Word, ...]]]:
    """Produce a bounded legal control orbit; this is not a reachability search."""
    rng = Random(seed)
    choices = all_moves(p.n, len(p.rels))
    rels = p.rels
    path: list[Move] = []
    states = [rels]
    attempts = 0
    while len(path) < steps:
        attempts += 1
        if attempts > 1000 * max(steps, 1):
            raise RuntimeError("walk could not satisfy the length cap")
        move = rng.choice(choices)
        nxt = apply_move(rels, move)
        if sum(map(len, nxt)) > max_total_length or nxt == rels:
            continue
        rels = nxt
        path.append(move)
        states.append(rels)
    return rels, path, states
