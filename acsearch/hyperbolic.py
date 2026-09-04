"""Exact, bounded utilities for the hyperbolic-quotient feasibility audit.

This module does not search AC orbits.  It certifies elementary small-
cancellation facts for two fixed laboratory groups and supplies a Dehn word
reducer.  A Dehn-reduced representative is not advertised as a unique normal
form; for a C'(1/6) presentation, however, the reducer gives an exact word-
problem decision.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, Sequence

from .words import Word, cyclic_reduce, inverse, parse, reduce, rotations


# A deterministic two-relator laboratory found during this audit.  Both
# relators have length 61, their exponent-sum determinant is -1, and their
# symmetrized set has maximum piece length 8.  Hence this is a perfect,
# torsion-free C'(1/6) group, and therefore a non-elementary hyperbolic group.
H_SC_RELATOR_STRINGS = (
    "YXyXXXYxYxyxyyxYYXXyXXyyxyXyXYYYYXYXYYXYYXXYYYxyxyxYXYxyXYYxY",
    "xYXXYXyyxyyyyyyyyxYXyxYxyyxyyXyXYxxYYYXyXyXYXYxyXYYYxxxYXYxYx",
)

# A one-relator torsion-free C'(1/6) laboratory.  Its abelianization is
# Z + Z/7 (the exponent vector is (-14,-7)), so it cannot be cyclic; together
# with torsion-freeness this also rules out elementary hyperbolicity.
H_OR_RELATOR_STRING = (
    "yXYYxYYXyXyXYxxxYYXXyyyXyyXXYYxyyXXXyXYYYXYYYxYxYXYXyxYXXXXXX"
)


@dataclass(frozen=True)
class SmallCancellationCertificate:
    relator_lengths: tuple[int, ...]
    symmetrized_size: int
    max_piece_length: int
    denominator: int
    c_prime: bool
    proper_power_flags: tuple[bool, ...]

    @property
    def torsion_free_by_power_test(self) -> bool:
        return self.c_prime and not any(self.proper_power_flags)


def _symmetrized(relators: Sequence[Word]) -> tuple[Word, ...]:
    return tuple(sorted({s for r in relators
                         for z in (r, inverse(r)) for s in rotations(z)}))


def _lcp(a: Word, b: Word) -> int:
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i
    return min(len(a), len(b))


def is_proper_power(word: Word) -> bool:
    """Whether a nonempty cyclically reduced word is a literal proper power."""
    w = cyclic_reduce(reduce(word))
    if not w:
        return False
    return any(len(w) % d == 0 and w == w[:d] * (len(w) // d)
               for d in range(1, len(w)))


def small_cancellation_certificate(
        relators: Sequence[Word], denominator: int = 6
) -> SmallCancellationCertificate:
    """Exhaustively certify the C'(1/denominator) overlap inequality.

    The longest common prefix among a sorted set of words occurs between two
    adjacent entries.  We nevertheless retain the pairwise length test because
    relators need not all have the same length.
    """
    if denominator < 2 or not relators:
        raise ValueError("need relators and denominator >= 2")
    raw = tuple(tuple(r) for r in relators)
    if any(not r for r in raw):
        raise ValueError("relators must be nonempty")
    if any(r != reduce(r) or (len(r) > 1 and r[0] == -r[-1]) for r in raw):
        raise ValueError("relators must be cyclically reduced")
    clean = raw

    sym = _symmetrized(clean)
    max_piece = 0
    valid = True
    # At these audit sizes (<=244 words), the explicit pair audit is preferable
    # to a clever implementation: it is transparent and runs in milliseconds.
    for a, b in combinations(sym, 2):
        piece = _lcp(a, b)
        max_piece = max(max_piece, piece)
        if denominator * piece >= min(len(a), len(b)):
            valid = False
    return SmallCancellationCertificate(
        tuple(map(len, clean)), len(sym), max_piece, denominator, valid,
        tuple(is_proper_power(r) for r in clean),
    )


def exponent_vector(word: Word, rank: int = 2) -> tuple[int, ...]:
    return tuple(word.count(g) - word.count(-g) for g in range(1, rank + 1))


def parse_h_sc_relators() -> tuple[Word, Word]:
    return tuple(parse(s) for s in H_SC_RELATOR_STRINGS)  # type: ignore[return-value]


def parse_h_or_relator() -> Word:
    return parse(H_OR_RELATOR_STRING)


def _dehn_rules(relators: Sequence[Word]) -> tuple[tuple[Word, Word], ...]:
    rules: dict[Word, Word] = {}
    for s in _symmetrized(tuple(relators)):
        for k in range(len(s) // 2 + 1, len(s) + 1):
            rules[s[:k]] = inverse(s[k:])
    return tuple(sorted(rules.items(), key=lambda item: -len(item[0])))


def dehn_reduce_word(word: Iterable[int], relators: Sequence[Word]) -> Word:
    """Apply length-decreasing Dehn rewrites until none applies."""
    w = reduce(word)
    rules = _dehn_rules(relators)
    while True:
        changed = False
        for lhs, rhs in rules:
            width = len(lhs)
            for i in range(len(w) - width + 1):
                if w[i:i + width] == lhs:
                    w = reduce(w[:i] + rhs + w[i + width:])
                    changed = True
                    break
            if changed:
                break
        if not changed:
            return w


def dehn_word_is_identity(word: Iterable[int], relators: Sequence[Word]) -> bool:
    """Exact for the certified C'(1/6) laboratories in this module."""
    cert = small_cancellation_certificate(tuple(relators), 6)
    if not cert.c_prime:
        raise ValueError("exact decision requires a certified C'(1/6) presentation")
    return not dehn_reduce_word(word, relators)
