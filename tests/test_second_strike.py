"""Regressions for the proved scope; no component search is performed."""
import copy
import importlib.util
import json
from pathlib import Path

import pytest

from acsearch.hsc_shortening import (
    annular_example, bounded_walk_control, certificate, conjugacy_witness,
    conjugator_bound, cyclic_dehn, dehn, equal, letters, pieces,
    short_geodesic, symmetrized,
)
from acsearch.words import inverse, parse, reduce

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('second_independent_checker',ROOT/'scripts/check_second_strike.py')
CHECKER=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


def frozen():
    return json.loads((ROOT/'certificates/astra_second_strike.json').read_text())


def test_independent_second_certificate():
    CHECKER.verify(frozen())


@pytest.mark.parametrize('mutation',['cover','missing_row','product','path','annulus','false_bound'])
def test_corruption_is_rejected(mutation):
    c=copy.deepcopy(frozen())
    if mutation=='cover':
        c['piece_cover']['max_covered'][3]=22
    elif mutation=='missing_row':
        c['piece_cover']['rows'].pop()
    elif mutation=='product':
        c['plateaus'][1]['rows'][0]['product']='x'
    elif mutation=='path':
        c['AK2_positive_path']['steps'][8]['move']=['I',0,0]
    elif mutation=='annulus':
        c['annular_positive']['g']='x'
    else:
        c['peak_upper_bound']=15
    with pytest.raises(AssertionError):
        CHECKER.verify(c)


def test_producer_reproduces_frozen_data():
    assert certificate()==frozen()


def test_geodesic_scope_rejects_long_dehn_residues():
    # First-strike failure is replayed, not rediscovered; neither long residue
    # may be advertised as a geodesic by the new short-ball API.
    old=json.loads((ROOT/'certificates/astra_first_strike.json').read_text())
    w=old['laboratories']['H_SC']['dehn_counterexample']
    u,v=map(parse,(w['u'],w['v']))
    assert dehn(u)==u and dehn(v)==v and equal(u,v)
    for a in (u,v):
        with pytest.raises(ValueError):
            short_geodesic(a)
    assert short_geodesic(parse('x'*30))==parse('x'*30)


@pytest.mark.parametrize('u,v,answer',[('','',True),('','x',False),('x','',False),
                                       ('x','y',False),('x','X',False),
                                       ('xy','yx',True),('xy','yyxY',True)])
def test_short_conjugacy_including_identity(u,v,answer):
    a,b=parse(u),parse(v)
    g=conjugacy_witness(a,b)
    assert (g is not None)==answer
    if g is not None:
        assert equal(g+a+inverse(g),b)


def test_identity_represented_by_defining_relator():
    assert conjugacy_witness(symmetrized()[0],())==()
    assert conjugacy_witness(symmetrized()[0],parse('x')) is None


def test_annular_conjugacy_cannot_be_replaced_by_free_conjugacy():
    e=annular_example()
    u,v=parse(e['u']),parse(e['v'])
    g=conjugacy_witness(u,v)
    assert g is not None and equal(g+u+inverse(g),v)
    assert len(g)<=conjugator_bound(max(len(u),len(v)))
    assert len(short_geodesic(u))!=len(short_geodesic(v))


def test_cyclic_dehn_tracks_basepoint_and_wraparound_rewriting():
    r=symmetrized()[17]
    # Defining relation split across a chosen linear basepoint; add conjugating
    # tails and a nonidentity letter to test every bookkeeping operation.
    a=reduce(parse('yxy')+r[20:]+parse('x')+r[:20]+parse('YXY'))
    c,t=cyclic_dehn(a)
    assert equal(c,t+a+inverse(t))
    assert len(t)<=2*len(a)**2+len(a)
    assert c
    assert all(dehn(c[i:]+c[:i])==c[i:]+c[:i] for i in range(len(c)))


def test_centralizer_powers_do_not_have_to_be_enumerated():
    u=parse('x')
    g=parse('yyy'+'x'*40)
    v=reduce(g+u+inverse(g))
    short=conjugacy_witness(u,v)
    assert short is not None and len(short)==3
    assert equal(short+u+inverse(short),v)
    # Source length 1 does not mean a length-1 conjugator suffices.
    assert len(v)==7 and len(short)>len(u)


def test_conjugator_direction_and_composition_after_dehn_rewrite():
    e=annular_example()
    u,v=parse(e['u']),parse(e['v'])
    left,right=parse('xy'),parse('YYx')
    a=reduce(left+u+inverse(left))
    b=reduce(right+v+inverse(right))
    g=conjugacy_witness(a,b)
    assert g is not None and equal(g+a+inverse(g),b)


def test_mixed_move_reordering_is_algebraically_correct_only():
    # This identity does NOT assert a peak bound on the intermediate states.
    u,v,g=map(parse,('xyx','yXX','yxy'))
    a=reduce(inverse(g)+v+g)
    b=reduce(u+a)
    c=reduce(g+b+inverse(g))
    assert c==reduce(g+u+inverse(g)+v)
    assert reduce(g+a+inverse(g))==v


def test_short_geodesic_does_not_confuse_ball_injectivity_with_conjugacy():
    assert not equal(parse('xy'),parse('yx'))
    assert conjugacy_witness(parse('xy'),parse('yx')) is not None


def test_negative_conjugacy_uses_complete_piece_rung_branch():
    assert conjugacy_witness(parse('x'*15),parse('y'*15)) is None


def test_shortest_conjugator_does_not_force_mixed_peak_lowering():
    from acsearch.hsc_shortening import mixed_reorder_failure
    f=mixed_reorder_failure()
    assert f['original_peak']==8 and f['reordered_peak']==11
    assert f['conjugator_minimum_length']==3
    assert f['original'][-1]==f['reordered'][-1]
