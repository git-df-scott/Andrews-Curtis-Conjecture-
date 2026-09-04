from acsearch.candidates import AK, MS
from acsearch.hyperbolic import (
    dehn_reduce_word, dehn_word_is_identity, exponent_vector,
    parse_h_or_relator, parse_h_sc_relators, small_cancellation_certificate,
)
from acsearch.invariant_audit import (
    commutator_conjugacy_class, cyclic_length_multiset,
    determinant_abs, deterministic_ac_walk, individual_conjugacy_multiset,
    evaluate_permutation_word, generated_permutation_group, inverse_path,
)
from acsearch.moves import apply_move, apply_path
from acsearch.presentation import Presentation
from acsearch.verify import apply_packaged_move
from acsearch.words import parse


def test_fixed_small_cancellation_laboratories():
    sc = parse_h_sc_relators()
    cert = small_cancellation_certificate(sc)
    assert cert.relator_lengths == (61, 61)
    assert cert.symmetrized_size == 244
    assert cert.max_piece_length == 8
    assert cert.c_prime and cert.torsion_free_by_power_test
    assert tuple(exponent_vector(r) for r in sc) == ((-7, -10), (2, 3))
    assert (-7) * 3 - (-10) * 2 == -1  # perfect abelianization

    one = parse_h_or_relator()
    one_cert = small_cancellation_certificate((one,))
    assert one_cert.relator_lengths == (61,)
    assert one_cert.symmetrized_size == 122
    assert one_cert.max_piece_length == 7
    assert one_cert.c_prime and one_cert.torsion_free_by_power_test
    assert exponent_vector(one) == (-14, -7)


def test_dehn_word_problem_controls():
    rels = parse_h_sc_relators()
    for relator in rels:
        assert dehn_word_is_identity(relator, rels)
    for word in (parse("x"), parse("y"), parse("x y X Y")):
        assert dehn_reduce_word(word, rels) == word
        assert not dehn_word_is_identity(word, rels)


def test_length_and_individual_conjugacy_die_under_multiplication():
    rels = (parse("x"), parse("y"))
    moved = apply_move(rels, ("M", 0, 2))
    assert cyclic_length_multiset(rels) == (1, 1)
    assert cyclic_length_multiset(moved) == (1, 2)
    assert individual_conjugacy_multiset(rels) != individual_conjugacy_multiset(moved)


def test_commutator_class_dies_under_independent_conjugation():
    rels = (parse("x"), parse("y"))
    # Conjugate the first coordinate successively by y and x.  This is a legal
    # AC path from a normally generating pair.
    moved = apply_path(rels, [("C", 0, 2), ("C", 0, 1)])
    assert len(commutator_conjugacy_class(rels)) == 4
    assert len(commutator_conjugacy_class(moved)) == 12
    assert commutator_conjugacy_class(rels) != commutator_conjugacy_class(moved)

    # The moved pair does not even generate F2: under x->(23), y->(12) in S3,
    # its two entries both map to (12), whereas x,y generate all of S3.  It
    # still normally generates F2 because it was reached by legal AC moves.
    assert moved == (parse("x y x Y X"), parse("y"))
    x_image = (0, 2, 1)  # (23)
    y_image = (1, 0, 2)  # (12)
    original_images = tuple(evaluate_permutation_word(w, (x_image, y_image))
                            for w in rels)
    moved_images = tuple(evaluate_permutation_word(w, (x_image, y_image))
                         for w in moved)
    assert len(generated_permutation_group(original_images)) == 6
    assert moved_images == (y_image, y_image)
    assert len(generated_permutation_group(moved_images)) == 2


def test_determinant_survives_long_bounded_control_orbits():
    controls = [Presentation.from_strings(2, "x", "y"), AK(2),
                Presentation.from_strings(2, "x y^2", "y")]
    for i, p in enumerate(controls):
        end, path, states = deterministic_ac_walk(p, 128, 20260904 + i)
        assert len(path) == 128
        assert len(states) == 129
        assert all(determinant_abs(state, 2) == 1 for state in states)
        assert apply_path(end, inverse_path(path)) == p.rels


def test_determinant_survives_carreras_p4_to_ak3_ledger():
    rels = MS(3, "Y x^2 Y").rels
    moves = [
        ("cycle", 0, 6), ("mul", 1, 0, -1), ("conj", 0, -2),
        ("mul", 1, 0, 1), ("cycle", 1, 2), ("conj", 0, 1),
        ("mul", 0, 1, -1), ("cycle", 0, 4), ("invert", 1),
        ("cycle", 1, 4), ("mul", 1, 0, 1), ("conj", 1, -1),
        ("mul", 1, 0, 1),
    ]
    values = [determinant_abs(rels, 2)]
    for move in moves:
        rels = apply_packaged_move(rels, move, 2)
        values.append(determinant_abs(rels, 2))
    assert values == [1] * 14
    assert Presentation(2, rels).cyclic_key() == AK(3).cyclic_key()
