#!/usr/bin/env python3
"""Standalone stdlib-only checker: deliberately imports no acsearch code.

Checks finite combinatorics and positive equality/path certificates. The
small-cancellation implications and no-go theorems require the written proofs.
This is implementation independence, not an independent human mathematical review.
"""
import json
import sys
from pathlib import Path


def inv(s):
    return s.swapcase()[::-1]


def free(s):
    assert set(s) <= set('xXyY')
    while True:
        t = s
        for pair in ('xX', 'Xx', 'yY', 'Yy'):
            t = t.replace(pair, '')
        if t == s:
            return s
        s = t


def symmetrize(rels):
    return sorted({w[i:] + w[:i] for r in rels for w in (r, inv(r))
                   for i in range(len(w))})


def modular(s):
    """String rewriting, independent of the producer's syllable stack."""
    s = s.replace('X', 'x').replace('Y', 'yy')
    while True:
        t = s.replace('xx', '').replace('yyy', '')
        if t == s:
            return s
        s = t


def matrix_mul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def matrix(s):
    generators = {'x': (0, -1, 1, 0), 'y': (0, -1, 1, 1)}
    m = (1, 0, 0, 1)
    for c in s:
        a = generators[c.lower()]
        if c.isupper():
            a = (a[3], -a[1], -a[2], a[0])
        m = matrix_mul(m, a)
    return min(m, tuple(-v for v in m))  # PSL(2,Z), quotient by +/-I


def move(state, operation):
    kind, i, j = operation
    assert type(i) is int and i in (0, 1) and type(j) is int
    new = state.copy()
    if kind == 'I':
        assert j == 0
        new[i] = inv(state[i])
    elif kind == 'M':
        assert abs(j) in (1, 2) and abs(j)-1 != i
        word = state[abs(j)-1]
        new[i] += word if j > 0 else inv(word)
    elif kind == 'C':
        assert j in (1, -1, 2, -2)
        g = {1: 'x', -1: 'X', 2: 'y', -2: 'Y'}[j]
        new[i] = g + state[i] + inv(g)
    else:
        raise AssertionError('invalid move')
    return new


def check_modular(c):
    assert c['presentation'] == ['xx', 'yyy']
    assert c['marking'] == ['x', 'y']
    assert c['candidate'] == ['xxxYYYY', 'xyxYXY']
    assert c['result'] == 'SAME_ORBIT' and c['search_states'] == 0
    assert len(c['states']) == len(c['moves'])+1
    state = list(map(modular, c['candidate']))
    assert state == c['states'][0]
    for operation, expected in zip(c['moves'], c['states'][1:]):
        raw = move(state, operation)
        assert [matrix(w) for w in raw] == [matrix(w) for w in expected]
        state = list(map(modular, raw))
        assert state == expected
    assert state == ['x', 'y']


def irreducible(s, sym):
    return free(s) == s and not any(r[:len(r)//2+1] in s for r in sym)


def check_lab(c):
    rels = c['relators']
    assert all(r and free(r) == r and r[0] != inv(r[-1]) for r in rels)
    sym = symmetrize(rels)
    # A prefix occurs in two distinct symmetrized words iff it is a piece.
    # This prefix histogram is independent of the producer's pairwise LCP.
    prefixes = {}
    for r in sym:
        for k in range(1, len(r)+1):
            prefixes.setdefault(r[:k], []).append(len(r))
    pieces = {p: lengths for p, lengths in prefixes.items() if len(lengths) > 1}
    maximum = max(map(len, pieces), default=0)
    valid = all(6*len(p) < min(lengths) for p, lengths in pieces.items())
    powers = [any(len(r) % k == 0 and r == r[:k]*(len(r)//k)
                  for k in range(1, len(r))) for r in rels]
    observed = {'relator_lengths': list(map(len, rels)),
                'symmetrized_size': len(sym), 'max_piece_length': maximum,
                'denominator': 6, 'c_prime': valid, 'proper_power_flags': powers}
    assert observed == c['small_cancellation'] and valid and not any(powers)
    assert c['overlap_pair_count'] == len(sym)*(len(sym)-1)//2
    assert c['exponent_vectors'] == [[r.count('x')-r.count('X'),
                                    r.count('y')-r.count('Y')] for r in rels]
    assert c['standard_images'] == ['x', 'y']
    assert c['ak3_images'] == ['xxxYYYY', 'xyxYXY']
    assert all(irreducible(w, sym) and w for w in c['ak3_images'])
    assert c['orbit_result'] == 'UNKNOWN'
    w = c['dehn_counterexample']
    r, s, k = w['relator_a'], w['relator_b'], w['shared_prefix_length']
    assert r in sym and s in sym and r != s
    assert 0 < k < min(len(r), len(s)) and r[:k] == s[:k]
    assert r[k] != s[k]
    boundary = free(inv(r[k:]) + s[k:])
    offset, cut = w['boundary_rotation'], w['boundary_split']
    assert 0 <= offset < len(boundary) and 0 < cut < len(boundary)
    z = boundary[offset:] + boundary[:offset]
    u, v = z[:cut], inv(z[cut:])
    assert [u, v] == [w['u'], w['v']]
    assert [len(u), len(v)] == w['lengths'] and len(u) < len(v)
    assert irreducible(u, sym) and irreducible(v, sym)
    current = free(u + inv(v))
    for step in w['equality_trace']:
        i, r, cut = step['offset'], step['relator'], step['cut']
        assert r in sym and len(r)//2 < cut <= len(r)
        assert 0 <= i <= len(current)-cut and current[i:i+cut] == r[:cut]
        current = free(current[:i] + inv(r[cut:]) + current[i+cut:])
    assert current == ''
    assert w['result'] == 'EQUAL_IRREDUCIBLE_WORDS_OF_UNEQUAL_LENGTH'


def check(c):
    assert c['schema'] == 'acc-first-strike-v1'
    check_modular(c['modular_ak3'])
    assert set(c['laboratories']) == {'H_SC', 'H_OR'}
    assert c['laboratories']['H_SC']['relators'] == [
        'YXyXXXYxYxyxyyxYYXXyXXyyxyXyXYYYYXYXYYXYYXXYYYxyxyxYXYxyXYYxY',
        'xYXXYXyyxyyyyyyyyxYXyxYxyyxyyXyXYxxYYYXyXyXYXYxyXYYYxxxYXYxYx']
    assert c['laboratories']['H_OR']['relators'] == [
        'yXYYxYYXyXyXYxxxYYXXyyyXyyXXYYxyyXXXyXYYYXYYYxYxYXYXyxYXXXXXX']
    for lab in c['laboratories'].values():
        check_lab(lab)
    return {'modular_path': 'PASS (normal forms and PSL matrices)',
            'small_cancellation': 'PASS (independent prefix counts)',
            'dehn_witnesses': 'PASS (literal rewrite proofs)',
            'separation_claim': 'NONE'}


if __name__ == '__main__':
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else (
        Path(__file__).resolve().parents[1] / 'certificates/astra_first_strike.json')
    print(json.dumps(check(json.loads(p.read_text())), sort_keys=True))
