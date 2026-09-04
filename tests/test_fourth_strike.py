import copy
import gzip
import importlib.util
import json
from pathlib import Path

import pytest

from acsearch.words import parse
from acsearch.hsc_mixed import pair_key,normalized_edges,representatives
from acsearch.hsc_seam import (word_pair_bound,tail_representatives,
    multiplication_events,fiber_bridge,bounded_attack,switched_two_m_bounds)

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('fourth_independent',ROOT/'scripts/check_fourth_strike.py')
CHECK=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(CHECK)


def frozen():return json.loads((ROOT/'certificates/astra_fourth_strike.json').read_text())


def test_independent_fourth_controls_and_every_discovery():
    result=CHECK.check(ROOT/'certificates')
    assert result['discoveries']['discovery_edges_verified']==4062
    assert result['discoveries']['complete_shell'] is False
    assert result['controls']['two_M_type_counts']=={'same_target':3378,'switched_target':180}


@pytest.mark.parametrize('change',['global','count','window','jump','family','cancellation','seam','scope'])
def test_corrupted_fourth_control_rejected(change):
    c=copy.deepcopy(frozen())
    if change=='global':c['global_height_bound']=23
    elif change=='count':c['conditional_seam_type_count']['values']['23']-=1
    elif change=='window':c['family_infinite_distinctness']['all_counts'][0]=0
    elif change=='jump':c['multiplication_jump_over_16']['steps'][-1]['after'][0]='x'
    elif change=='family':c['two_M_family'][0]['raw_internal_seam_height']=4
    elif change=='cancellation':c['unbounded_cancellation_controls'][0]['cancelled_pairs']=0
    elif change=='seam':c['same_target_high_seam']['signed_internal_seam_width']=15
    else:c['same_target_high_seam']['minimum_M_in_height23']=1
    with pytest.raises(AssertionError):CHECK.controls(c,ROOT/'certificates')


def test_capped_prefix_cannot_be_relabelled_complete():
    c=json.loads(gzip.decompress((ROOT/'certificates/hsc_height23_attempt.json.gz').read_bytes()))
    c['status']='COMPLETE_SUBLEVEL'
    with pytest.raises(AssertionError):CHECK.discoveries(c,ROOT/'certificates')


def test_raw_seam_growth_has_low_replacement_and_is_not_a_minimal_pump():
    for row in frozen()['two_M_family']:
        states=CHECK.path(row)
        assert max(sum(map(len,s)) for s in states)>4
        short=CHECK.path({'initial':row['initial'],'steps':row['replacement']})
        assert short[-1]==states[-1]
        assert max(sum(map(len,s)) for s in short)==4


def test_fiber_bridge_changes_decreasing_coordinate_first():
    source=tuple(map(parse,('yyyxYYY','y')))
    target=tuple(map(parse,('x','xxxyXXX')))
    steps=fiber_bridge(source,target)
    states=CHECK.path({'initial':['yyyxYYY','y'],'steps':steps})
    assert states[-1]==('x','xxxyXXX')
    assert max(sum(map(len,s)) for s in states)==8
    assert steps[0]['move'][1]==0


def test_fiber_bridge_includes_signs_permutation_and_arbitrary_conjugators():
    source=tuple(map(parse,('XXyxx','Yxxxxy')))
    target=tuple(map(parse,('XXXX','Y')))
    states=CHECK.path({'initial':['XXyxx','Yxxxxy'],
                       'steps':fiber_bridge(source,target)})
    assert states[-1]==('XXXX','Y')
    assert max(sum(map(len,s)) for s in states)<=11


def test_one_retained_class_does_not_allow_seam_excision():
    with pytest.raises(ValueError):
        fiber_bridge(tuple(map(parse,('x','y'))),tuple(map(parse,('xyy','y'))))


def test_new_excision_does_not_resurrect_either_frozen_counterexample():
    c=json.loads((ROOT/'certificates/astra_second_strike.json').read_text())
    e=c['mixed_reorder_failure']
    assert e['original_peak']==8<e['reordered_peak']==11
    with pytest.raises(ValueError):
        fiber_bridge(tuple(map(parse,e['original'][0])),tuple(map(parse,e['original'][-1])))
    with pytest.raises(ValueError):
        fiber_bridge(tuple(map(parse,c['AK2_positive_path']['initial'])),tuple(map(parse,('x','y'))))


@pytest.mark.parametrize('words,H',[(('x','xy'),3),(('xxYYY','xyxYXY'),15),(('xxxYYYY','xyxYXY'),15)])
def test_extended_edge_domain_agrees_with_inherited_exact_domain(words,H):
    s=pair_key(tuple(map(parse,words)));old,count=normalized_edges(s,H)
    events=[(t,w) for t,w in multiplication_events(s,H) if t is not None]
    assert {t for t,w in events}==set(old) and len(events)==count
    assert all(w['before_height']<=H and w['after_height']<=H for t,w in events)


def test_inside_out_conjugates_match_prior_complete_generator_enumeration():
    a=parse('xyXy')
    assert {u for u,g,a in tail_representatives(a,10)}=={u for u,g,a in representatives(a,10)}


def test_height_scope_and_resource_caps_are_explicit():
    s=pair_key(tuple(map(parse,('xxxYYYY','xyxYXY'))))
    with pytest.raises(ValueError):list(multiplication_events(s,24))
    c=bounded_attack(ROOT/'certificates',event_cap=10,state_cap=20)
    assert c['status']=='EVENT_CAP' and c['candidate_events']==10
    assert c['global_height_bound'] is None


def test_local_switched_target_bound_is_not_global_height_control():
    for L in (0,1,15,23,1000):
        b=switched_two_m_bounds(L)
        assert b['signed_seam_width']==2*L
        assert b['linked_replacement_height']==3000*(2*L+1)
        assert b['global_height_bound'] is None and 'ONLY' in b['scope']


def test_conditional_word_pair_count_includes_empty_coordinates():
    assert [word_pair_bound(r) for r in range(4)]==[1,9,49,217]
    assert word_pair_bound(23)==5774114968057
    with pytest.raises(ValueError):word_pair_bound(-1)
