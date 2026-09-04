from acsearch import *
from acsearch.words import parse, unparse, reduce, inverse, mul, cyclic_canonical
from acsearch.moves import all_moves, apply_move, apply_path, cyclic_neighbors
from acsearch.presentation import Presentation, symmetry_canonical
from acsearch.search import greedy_search, bfs_closure
from acsearch.verify import (verify_certificate, verify_equivalence_ledger,
                             apply_packaged_move, abelianization_is_trivial,
                             presents_trivial_group)
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


def test_packaged_cycle_is_elementary_conjugation():
    p = Presentation.from_strings(2, "x y X y", "y")
    cycled = apply_packaged_move(p.rels, ("cycle", 0, 1), p.n)
    elementary = apply_move(p.rels, ("C", 0, -p.rels[0][0]))
    assert cycled == elementary


def test_carreras_length14_ms3_to_ak3_certificate():
    """Carreras 2026, Theorem 4: 13 packaged / 22 classical moves.

    Source artifact: joe-carr-data/ac-certificates tag v1.0,
    cert_ms3_yinvx2yinv_equiv_ak3.json (MIT licensed).
    """
    p = MS(3, "Y x^2 Y")
    moves = [
        ("cycle", 0, 6), ("mul", 1, 0, -1), ("conj", 0, -2),
        ("mul", 1, 0, 1), ("cycle", 1, 2), ("conj", 0, 1),
        ("mul", 0, 1, -1), ("cycle", 0, 4), ("invert", 1),
        ("cycle", 1, 4), ("mul", 1, 0, 1), ("conj", 1, -1),
        ("mul", 1, 0, 1),
    ]
    assert verify_equivalence_ledger(p, AK(3), moves)
    broken = moves.copy()
    broken[-1] = ("mul", 1, 0, -1)
    assert not verify_equivalence_ledger(p, AK(3), broken)


def test_candidate_catalogue_lengths_and_trivial_groups():
    """Small positive calibration only; this is not an AC-orbit search."""
    expected_lengths = {
        "AK(2)": 11, "AK(3)": 13, "AK(4)": 15, "AK(5)": 17,
        "classical_2gen": 14, "classical_3gen": 15,
        "MS(2, x^-2 y^-1 x^2 y)": 14,
        "MS(2, x^-2 y^-1 x^2 y^-1)": 14,
        "MS(3, y x^2 y)": 14,
        "MS(3, y^-1 x^2 y^-1)": 14,
        "MS(2, y x^2 y x^-2)": 14,
        "MS(2, y x^2 y^-1 x^-2)": 14,
    }
    assert set(CATALOGUE) == set(expected_lengths)
    for name, p in CATALOGUE.items():
        assert p.total_length == expected_lengths[name]
        assert p.is_balanced()
        assert abelianization_is_trivial(p)
        assert presents_trivial_group(p)


def test_greedy_easy():
    p = Presentation.from_strings(2, "x y^2", "y")     # easy (my earlier example was not a trivial-group presentation)
    path = greedy_search(p, max_rel_len=8)
    assert path is not None and verify_certificate(p, path)


def test_bfs_small_matches_slack():
    a = bfs_closure(((1,), (2,)), 2, 6, slack=0)
    b = bfs_closure(((1,), (2,)), 2, 6, slack=2)
    assert set(a) == set(b)
