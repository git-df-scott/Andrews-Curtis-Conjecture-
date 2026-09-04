"""Bounded certificate production. No AC reachability search or orbit decider."""
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from time import perf_counter

from .candidates import AK
from .hyperbolic import (
    _symmetrized, dehn_reduce_word, exponent_vector, parse_h_or_relator,
    parse_h_sc_relators, small_cancellation_certificate,
)
from .moves import apply_move
from .words import inverse, reduce


def letters(word):
    return ''.join({1: 'x', -1: 'X', 2: 'y', -2: 'Y'}[a] for a in word)


def modular_normal_form(word):
    """Unique free-product syllable form in <x,y | x^2,y^3>."""
    syllables = []
    for a in word:
        g, e = abs(a), 1 if a > 0 else -1
        modulus = 2 if g == 1 else 3
        if syllables and syllables[-1][0] == g:
            e += syllables.pop()[1]
        e %= modulus
        if e:
            syllables.append((g, e))
    return tuple(g for g, e in syllables for _ in range(e))


# Five moves reach (y,x), then five more reach the ordered pair (x,y).
MODULAR_PATH = (
    ('M', 1, -1), ('M', 1, -1), ('M', 0, -2), ('C', 0, 1),
    ('M', 1, -1), ('M', 0, 2), ('M', 1, -1), ('M', 0, 2),
    ('C', 0, -2), ('I', 1, 0),
)


def modular_certificate():
    state = tuple(modular_normal_form(w) for w in AK(3).rels)
    states = [list(map(letters, state))]
    for move in MODULAR_PATH:
        state = tuple(modular_normal_form(w) for w in apply_move(state, move))
        states.append(list(map(letters, state)))
    assert state == ((1,), (2,))
    return {'presentation': ['xx', 'yyy'], 'marking': ['x', 'y'],
            'candidate': list(map(letters, AK(3).rels)),
            'moves': list(MODULAR_PATH), 'states': states,
            'result': 'SAME_ORBIT', 'search_states': 0}


def short_dehn(word, sym):
    """Different rule order: leftmost minimal majority subword; record proof."""
    w = reduce(word)
    trace = []
    while True:
        hit = False
        for i in range(len(w)):
            for r in sym:
                k = len(r) // 2 + 1
                if w[i:i+k] == r[:k]:
                    trace.append({'offset': i, 'relator': letters(r), 'cut': k})
                    w = reduce(w[:i] + inverse(r[k:]) + w[i+k:])
                    hit = True
                    break
            if hit:
                break
        if not hit:
            return w, trace


def dehn_counterexample(rels):
    """Find one two-cell witness in a fixed finite construction domain.

    Domain: ordered symmetrized-relator pairs with common prefix >=5;
    every cyclic boundary offset; split one letter below the midpoint.
    Stop at the first positive witness. No exhaustion claim is made.
    """
    sym = _symmetrized(rels)
    tested = 0
    for r in sym:
        for s in sym:
            if r == s:
                continue
            k = 0
            while k < min(len(r), len(s)) and r[k] == s[k]:
                k += 1
            if k < 5:
                continue
            boundary = reduce(inverse(r[k:]) + s[k:])
            for offset in range(len(boundary)):
                z = boundary[offset:] + boundary[:offset]
                cut = len(z) // 2 - 1
                u, v = z[:cut], inverse(z[cut:])
                tested += 1
                if short_dehn(u, sym)[0] != u or short_dehn(v, sym)[0] != v:
                    continue
                end, trace = short_dehn(u + inverse(v), sym)
                assert not end and len(u) < len(v)
                # Cross-check with the pre-existing, longer-rule-first engine.
                assert dehn_reduce_word(u, rels) == u
                assert dehn_reduce_word(v, rels) == v
                assert not dehn_reduce_word(u + inverse(v), rels)
                return {'u': letters(u), 'v': letters(v),
                        'lengths': [len(u), len(v)], 'relator_a': letters(r),
                        'relator_b': letters(s), 'shared_prefix_length': k,
                        'boundary_rotation': offset, 'boundary_split': cut,
                        'equality_trace': trace, 'witnesses_tested': tested,
                        'result': 'EQUAL_IRREDUCIBLE_WORDS_OF_UNEQUAL_LENGTH'}
    raise RuntimeError('fixed finite witness construction produced no witness')


def run():
    started = perf_counter()
    result = {'schema': 'acc-first-strike-v1', 'base_commit':
              'b19113c5e507eaceb51aeb58f30c47433c85980b',
              'modular_ak3': modular_certificate(), 'laboratories': {}}
    for name, rels in [('H_SC', parse_h_sc_relators()),
                       ('H_OR', (parse_h_or_relator(),))]:
        cert = small_cancellation_certificate(rels)
        images = [letters(dehn_reduce_word(w, rels)) for w in AK(3).rels]
        result['laboratories'][name] = {
            'relators': list(map(letters, rels)), 'small_cancellation': asdict(cert),
            'overlap_pair_count': cert.symmetrized_size * (cert.symmetrized_size-1)//2,
            'exponent_vectors': [exponent_vector(r) for r in rels],
            'ak3_images': images, 'standard_images': ['x', 'y'],
            'orbit_result': 'UNKNOWN', 'dehn_counterexample': dehn_counterexample(rels),
        }
    root = Path(__file__).resolve().parents[1]
    target = root / 'certificates' / 'astra_first_strike.json'
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'certificate': str(target.relative_to(root)),
                      'runtime_seconds': perf_counter()-started,
                      'modular_moves': len(MODULAR_PATH), 'orbit_search_states': 0}))


if __name__ == '__main__':
    run()
