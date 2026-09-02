"""Balanced presentations and canonical forms."""
from __future__ import annotations
from dataclasses import dataclass
from itertools import permutations, product
from typing import Tuple
from .words import Word, reduce, cyclic_canonical, parse, unparse, inverse

Relators = Tuple[Word, ...]


@dataclass(frozen=True)
class Presentation:
    """A presentation <x_1..x_n | r_1..r_m> with freely reduced relators."""
    n: int
    rels: Relators

    @staticmethod
    def from_strings(n: int, *rels: str) -> "Presentation":
        return Presentation(n, tuple(parse(r) for r in rels))

    def __str__(self) -> str:
        return "<" + ",".join("xyzuvw"[i] for i in range(self.n)) + " | " + \
            ", ".join(unparse(r) for r in self.rels) + ">"

    @property
    def total_length(self) -> int:
        return sum(len(r) for r in self.rels)

    def is_balanced(self) -> bool:
        return self.n == len(self.rels)

    def cyclic_key(self) -> Relators:
        """Sorted tuple of cyclic canonical forms of the relators.

        This is invariant under conjugating / inverting / reordering relators,
        all of which are AC moves (reordering is a composition of AC moves).
        """
        return tuple(sorted(cyclic_canonical(r) for r in self.rels))

    def apply_map(self, images: Tuple[Word, ...]) -> "Presentation":
        """Apply the endomorphism x_i -> images[i-1] to all relators."""
        def img(w):
            out = []
            for a in w:
                out.extend(images[a - 1] if a > 0 else inverse(images[-a - 1]))
            return reduce(out)
        return Presentation(self.n, tuple(img(r) for r in self.rels))

    def is_trivial_standard(self) -> bool:
        """True iff the cyclic key is that of <x_1..x_n | x_1, ..., x_n>."""
        return self.cyclic_key() == standard_key(self.n)

    def abelianization_matrix(self):
        return [[sum(1 if a == g else -1 if a == -g else 0 for a in r)
                 for g in range(1, self.n + 1)] for r in self.rels]


def standard_key(n: int) -> Relators:
    """Cyclic key of the standard presentation <x_1..x_n | x_1..x_n>."""
    return tuple(sorted(cyclic_canonical((g,)) for g in range(1, n + 1)))


def _signed_permutations(n: int):
    for perm in permutations(range(1, n + 1)):
        for signs in product((1, -1), repeat=n):
            yield tuple(s * p for s, p in zip(signs, perm))


def symmetry_canonical(p: Presentation) -> Relators:
    """Canonical form under the finite group of signed permutations of the
    generators (2^n n! automorphisms) combined with the cyclic key.

    AC-triviality is invariant under all of Aut(F_n) (automorphisms commute
    with AC moves and carry the standard tuple to a basis, which is Nielsen
    equivalent to the standard tuple), so this is a legitimate quotient.
    """
    best = None
    for sp in _signed_permutations(p.n):
        rels = tuple(cyclic_canonical(tuple((1 if a > 0 else -1) * sp[abs(a) - 1]
                                            for a in r)) for r in p.rels)
        key = tuple(sorted(rels))
        if best is None or key < best:
            best = key
    return best
