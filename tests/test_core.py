from acsearch import *
from acsearch.words import parse, unparse, reduce, inverse, mul, cyclic_canonical
from acsearch.moves import all_moves, apply_move, apply_path, cyclic_neighbors
from acsearch.presentation import Presentation, symmetry_canonical
from acsearch.search import greedy_search, bfs_closure
from acsearch.verify import verify_certificate, abelianization_is_trivial, presents_trivial_group
from acsearch.candidates import AK, MS, CATALOGUE


def test_words():
    assert parse("x y Y X") == ()
    assert parse("x^3 y^-4") == (1, 1, 1, -2, -2, -2, -2)
    assert unparse(parse("x^3 y^-4")) == "x^3 y^-4"
    assert mul((1, 2), (-2, 1)) == (1, 1)
    assert inverse((1, -2)) == (2, -1)
    assert cyclic_canonical((2, 1, -2)) == (-1,)  # min over w and w^-1
    assert cyclic_canonical((1, 2)) == cyclic_canonical((-2, -1))


def test_moves_roundtrip():
    p = AK(3)
    for mv in all_moves(2, 2):
        q = apply_move(p.rels, mv)
        assert len(q) == 2
    # inversion twice is identity; conjugation by x then X is identity
    assert apply_path(p.rels, [("I", 0, 0), ("I", 0, 0)]) == p.rels
    assert apply_path(p.rels, [("C", 1, 1), ("C", 1, -1)]) == p.rels


def test_symmetry_canonical():
    p = Presentation.from_strings(2, "x y", "y")
    q = Presentation.from_strings(2, "y x", "x")
    assert symmetry_canonical(p) == symmetry_canonical(q)


def test_abelianization():
    assert abelianization_is_trivial(AK(3))
    assert not abelianization_is_trivial(Presentation.from_strings(2, "x^2", "y"))


def test_trivial_group_check():
    assert presents_trivial_group(AK(2))
    assert presents_trivial_group(AK(3))
    assert not presents_trivial_group(Presentation.from_strings(2, "x^2 y^-3", "y"))


def test_greedy_easy():
    p = Presentation.from_strings(2, "x y x Y", "y x")     # easy
    path = greedy_search(p, max_rel_len=8)
    assert path is not None and verify_certificate(p, path)


def test_bfs_small_matches_slack():
    a = bfs_closure(((1,), (2,)), 2, 6, slack=0)
    b = bfs_closure(((1,), (2,)), 2, 6, slack=2)
    assert set(a) == set(b)
