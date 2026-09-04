import copy
import importlib.util
import json
from pathlib import Path

import pytest

from acsearch.candidates import AK
from acsearch.first_strike import MODULAR_PATH, modular_normal_form
from acsearch.moves import apply_move, cyclic_neighbors
from acsearch.presentation import Presentation
from acsearch.words import parse

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('independent_check',
                                             ROOT / 'scripts/check_first_strike.py')
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


def certificate():
    return json.loads((ROOT / 'certificates/astra_first_strike.json').read_text())


def test_independent_frozen_certificate_replay():
    CHECKER.check(certificate())


@pytest.mark.parametrize('mutation', ['path', 'overlap', 'word', 'trace'])
def test_corrupted_certificates_rejected(mutation):
    data = copy.deepcopy(certificate())
    if mutation == 'path':
        data['modular_ak3']['moves'][-1] = ['I', 0, 0]
    elif mutation == 'overlap':
        data['laboratories']['H_SC']['small_cancellation']['max_piece_length'] = 7
    elif mutation == 'word':
        data['laboratories']['H_OR']['dehn_counterexample']['v'] += 'x'
    else:
        data['laboratories']['H_SC']['dehn_counterexample']['equality_trace'][0]['offset'] = 999
    with pytest.raises(AssertionError):
        CHECKER.check(data)


def test_modular_path_does_not_claim_free_group_trivialization():
    state = AK(3).rels
    for operation in MODULAR_PATH:
        state = apply_move(state, operation)
    assert state != (parse('x'), parse('y'))
    assert tuple(map(modular_normal_form, state)) == (parse('x'), parse('y'))


def test_cyclic_shortening_edge_not_skipped_by_negative_budget():
    # Before this strike, the negative gmax silently skipped xy * X ~ y.
    start = Presentation.from_strings(2, 'x', 'xy').cyclic_key()
    standard = Presentation.from_strings(2, 'x', 'y').cyclic_key()
    assert standard in set(cyclic_neighbors(start, 2, max_total=3))
