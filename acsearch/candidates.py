"""Catalogue of potential counterexamples from the literature."""
from __future__ import annotations
from .presentation import Presentation
from .words import parse, reduce, inverse, Word


def AK(n: int) -> Presentation:
    """Akbulut-Kirby: <x,y | x^n = y^(n+1), xyx = yxy>."""
    return Presentation.from_strings(2, f"x^{n} y^-{n+1}", "x y x Y X Y")


def MS(n: int, w: str) -> Presentation:
    """Miller-Schupp: <x,y | x^-1 y^n x = y^(n+1), x = w>  (w has x-exponent sum 0)."""
    return Presentation.from_strings(2, f"X y^{n} x y^-{n+1}", "X " + w)


def gordon_classical() -> Presentation:
    """<x,y | x^-1 y^2 x = y^3, y^-1 x^2 y = x^3> (Miasnikov-Myasnikov (1))."""
    return Presentation.from_strings(2, "X y^2 x y^-3", "Y x^2 y x^-3")


def three_generator_classical() -> Presentation:
    """<x,y,z | y^-1 x y = x^2, z^-1 y z = y^2, x^-1 z x = z^2>."""
    return Presentation.from_strings(3, "Y x y x^-2", "Z y z y^-2", "X z x z^-2")


# The six length-14 Miller-Schupp presentations that resisted greedy search in
# Shehper et al. 2024 (as listed by Carreras 2026).
HARD_LENGTH_14 = {
    "MS(2, x^-2 y^-1 x^2 y)": MS(2, "x^-2 Y x^2 y"),
    "MS(2, x^-2 y^-1 x^2 y^-1)": MS(2, "x^-2 Y x^2 Y"),
    "MS(3, y x^2 y)": MS(3, "y x^2 y"),
    "MS(3, y^-1 x^2 y^-1)": MS(3, "Y x^2 Y"),
    "MS(2, y x^2 y x^-2)": MS(2, "y x^2 y x^-2"),
    "MS(2, y x^2 y^-1 x^-2)": MS(2, "y x^2 Y x^-2"),
}

CATALOGUE = {
    "AK(2)": AK(2), "AK(3)": AK(3), "AK(4)": AK(4), "AK(5)": AK(5),
    "classical_2gen": gordon_classical(),
    "classical_3gen": three_generator_classical(),
    **HARD_LENGTH_14,
}
