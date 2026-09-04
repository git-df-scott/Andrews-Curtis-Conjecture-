import copy
import importlib.util
import json
from pathlib import Path
import pytest

from acsearch.hsc_mixed import (pair_key,normalized_edges,representatives,
    generator_orbit,GENERATOR_MAPS,fiber_height_counts,pants_bounds)
from acsearch.hsc_shortening import conjugacy_witness
from acsearch.words import parse,inverse,cyclic_reduce,reduce

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('third_independent',ROOT/'scripts/check_third_strike.py')
CHECK=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(CHECK)


def frozen():return json.loads((ROOT/'certificates/astra_third_strike.json').read_text())


def test_complete_shell_independent_checker():
    result=CHECK.check(ROOT/'certificates')
    assert result['AK3_ordered_independent']['ordered_states']==13728
    assert result['standard_symmetry_vertices']==23774


@pytest.mark.parametrize('change',['global_bound','second_digest','hidden_peak','pants','boundary','adjacency'])
def test_corrupted_third_certificate_rejected(change):
    c=copy.deepcopy(frozen());second=(ROOT/'certificates/astra_second_strike.json').read_bytes()
    if change=='global_bound':c['global_height_bound']=15
    elif change=='second_digest':c['second_certificate_sha256']='0'*64
    elif change=='hidden_peak':c['hidden_peak_counterexample']['heights']=[4,4,3]
    elif change=='pants':c['one_cell_pants']['w']+='x'
    elif change=='boundary':c['AK3_boundary']['normalized_height16_exits'].pop()
    else:c['AK3']['nodes'][0][1].pop()
    with pytest.raises(AssertionError):
        CHECK.check_controls(c,second)
        CHECK.check_boundary(c)
        CHECK.check_graph(c['AK3'],False)


def test_macro_height_test_precedes_cyclic_canonicalization():
    # New failure witness: raw multiplication leaves4 although its cyclic
    # output has height3. Such a witness must not be admitted at cap4.
    source=pair_key((parse('y'),parse('x')))
    targets,_=normalized_edges(source,4)
    for witness in targets.values():
        assert witness['before_height']<=4 and witness['after_height']<=4
    assert sum(map(len,(parse('Xyxx'),parse('x'))))==5
    assert sum(map(len,pair_key((parse('Xyxx'),parse('x')))))==3


def test_input_slack_cutoff_includes_shortening_edges():
    state=pair_key((parse('x'),parse('xy')))
    targets,_=normalized_edges(state,3)
    assert pair_key((parse('x'),parse('y'))) in targets


def test_all_short_conjugates_are_generated_without_heuristic_cutoff():
    a=pair_key((parse('xy'),parse('x')))[0]
    words={u for u,_,_ in representatives(a,len(a)+4)}
    independent=CHECK.all_conjugates(''.join({1:'x',-1:'X',2:'y',-2:'Y'}[n] for n in a),len(a)+4)
    assert words=={parse(w) for w in independent}


def test_generator_action_fixes_standard_only_locally():
    s=pair_key((parse('x'),parse('y')))
    assert len(set(GENERATOR_MAPS))==8
    assert generator_orbit(s)==(s,)
    # We never apply these maps to defining relators or assert H_SC symmetry.
    a=pair_key((parse('xxxYYYY'),parse('xyxYXY')))
    assert len(generator_orbit(a))>1


def test_ordered_fiber_formula_against_explicit_small_words():
    s=pair_key((parse('x'),parse('xy')));bound=7
    counts={h:0 for h in range(3,bound+1,2)}
    for a,_,_ in representatives(s[0],bound-len(s[1])):
        for b,_,_ in representatives(s[1],bound-len(s[0])):
            if len(a)+len(b)<=bound:counts[len(a)+len(b)]+=2
    assert fiber_height_counts(s,bound)==counts


def test_short_total_boundary_threshold_is_strict():
    assert 22+22+16<61
    assert not 23+22+16<61
    old=json.loads((ROOT/'certificates/astra_second_strike.json').read_text())
    e=old['annular_positive']
    assert len(e['u'])+len(e['v'])+16>=61
    assert conjugacy_witness(parse(e['u']),parse(e['v'])) is not None


def test_one_m_theorem_survives_every_published_ak2_multiplication():
    old=json.loads((ROOT/'certificates/astra_second_strike.json').read_text())
    state=tuple(map(parse,old['AK2_positive_path']['initial']))
    checked=0
    for step in old['AK2_positive_path']['steps']:
        after=tuple(map(parse,step['after']));op,i,j=step['move']
        if op=='M':
            a=cyclic_reduce(state[i]);b=state[abs(j)-1]
            b=cyclic_reduce(b if j>0 else inverse(b));w=cyclic_reduce(after[i])
            assert conjugacy_witness(a,inverse(b)) is None
            assert conjugacy_witness(a,w) is None
            assert conjugacy_witness(b,w) is None
            L=max(sum(map(len,state)),sum(map(len,after)))
            assert L<=pants_bounds(L)['single_m_height']
            checked+=1
        state=after
    assert checked>0


def test_one_m_theorem_does_not_resurrect_the_frozen_reorder():
    old=json.loads((ROOT/'certificates/astra_second_strike.json').read_text())
    e=old['mixed_reorder_failure'];start=e['original'][0];end=e['original'][-1]
    L=max(sum(map(len,start)),sum(map(len,end)))
    assert e['original_peak']==8<e['reordered_peak']==11
    assert pants_bounds(L)['single_m_height']>=11
    a,b=map(parse,start);w=cyclic_reduce(parse(end[0]))
    assert all(conjugacy_witness(u,v) is None for u,v in ((a,inverse(b)),(a,w),(b,w)))


def test_pants_constants_cover_euler_and_cut_estimates():
    for L in (0,1,2,7,15,23,1000):
        b=pants_bounds(L)
        assert b['derived_height']<=b['single_m_height']
        assert b['area']==6*L+3
        assert b['edges']<=184*L+91
        assert 'ONLY' in b['scope']


def test_literal_one_cell_pants_has_certified_short_geodesic_output():
    p=frozen()['one_cell_pants']
    from acsearch.hsc_shortening import equal,short_geodesic
    u,v,w=map(parse,(p['u'],p['v'],p['w']))
    assert equal(u+v,w)
    assert [len(short_geodesic(z)) for z in (u,v,w)]==[20,20,21]


def test_first_height16_exits_change_the_braid_coordinate():
    c=frozen();CHECK.check_boundary(c)
    assert len(c['AK3_boundary']['normalized_height16_exits'])==24
    assert all(CHECK.core(row['before'][0])==CHECK.core('xyxYXY')
               for row in c['AK3_boundary']['normalized_height16_exits'])
