"""Free group words as tuples of nonzero integers."""
from __future__ import annotations
from typing import Iterable, Tuple

Word = Tuple[int, ...]


def reduce(w: Iterable[int]) -> Word:
    """Freely reduce a word (cancel adjacent x x^-1 pairs)."""
    out: list[int] = []
    for a in w:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inverse(w: Word) -> Word:
    return tuple(-a for a in reversed(w))


def mul(a: Word, b: Word) -> Word:
    """Product of two freely reduced words; only cancels at the junction."""
    i = len(a)
    j = 0
    nb = len(b)
    while i > 0 and j < nb and a[i - 1] == -b[j]:
        i -= 1
        j += 1
    return a[:i] + b[j:]


def cyclic_reduce(w: Word) -> Word:
    """Cyclically reduce a freely reduced word."""
    i, j = 0, len(w)
    while j - i >= 2 and w[i] == -w[j - 1]:
        i += 1
        j -= 1
    return w[i:j]


def rotations(w: Word):
    """All cyclic rotations of w."""
    n = len(w)
    if n == 0:
        yield w
        return
    ww = w + w
    for k in range(n):
        yield ww[k:k + n]


def cyclic_canonical(w: Word, up_to_inverse: bool = True) -> Word:
    """Least representative of the conjugacy class of w (and of w^-1).

    The input is first cyclically reduced.  The result is the lexicographically
    minimal rotation of the cyclically reduced word (and of its inverse when
    up_to_inverse is set).  Inverting a relator and conjugating it are both
    AC-moves, so this is an invariant of the AC-class of a *single* relator.
    """
    w = cyclic_reduce(reduce(w))
    best = None
    cands = [w, inverse(w)] if up_to_inverse else [w]
    for c in cands:
        for r in rotations(c):
            if best is None or r < best:
                best = r
    return best if best is not None else ()


def length(w: Word) -> int:
    return len(w)


_LETTERS = "xyzuvw"


def parse(s: str, gens: str = _LETTERS) -> Word:
    """Parse strings like 'x^3 y^-4', 'xyxY' (capital = inverse), 'x y^-1'."""
    s = s.replace("*", " ")
    out: list[int] = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c.isspace():
            i += 1
            continue
        if c.lower() not in gens:
            raise ValueError(f"bad letter {c!r} in {s!r}")
        g = gens.index(c.lower()) + 1
        if c.isupper():
            g = -g
        i += 1
        e = 1
        if i < n and s[i] == "^":
            i += 1
            j = i
            if i < n and s[i] == "-":
                i += 1
            while i < n and s[i].isdigit():
                i += 1
            e = int(s[j:i])
        if e < 0:
            g, e = -g, -e
        out.extend([g] * e)
    return reduce(out)


def unparse(w: Word, gens: str = _LETTERS) -> str:
    if not w:
        return "1"
    parts = []
    i = 0
    while i < len(w):
        a = w[i]
        j = i
        while j < len(w) and w[j] == a:
            j += 1
        e = j - i
        s = gens[abs(a) - 1]
        if a < 0:
            e = -e
        parts.append(s if e == 1 else f"{s}^{e}")
        i = j
    return " ".join(parts)
