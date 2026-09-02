"""acsearch: tools for studying the Andrews-Curtis conjecture.

Words in a free group F_n are tuples of nonzero ints: generator k is +k,
its inverse is -k (k = 1..n).  A presentation is a tuple of relators.
"""
from .words import (reduce, inverse, mul, cyclic_reduce, rotations,
                    cyclic_canonical, parse, unparse, length)
from .presentation import Presentation, symmetry_canonical
from .moves import ac_neighbors, cyclic_neighbors
