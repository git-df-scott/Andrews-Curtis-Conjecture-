"""Certified H_SC conjugacy and short-ball controls; never an AC component search.

Completeness arguments (not machine-formalized) are in HSC_PEAK_LEMMA.md.
Dehn outputs are equality witnesses, NOT canonical/geodesic normal forms.
"""
from collections import Counter
from functools import lru_cache
import hashlib
import json

from .hyperbolic import H_SC_RELATOR_STRINGS, _symmetrized, parse_h_sc_relators
from .words import reduce, inverse, rotations, cyclic_reduce, parse
from .moves import all_moves, apply_move


def letters(w):
    return ''.join({1:'x', -1:'X', 2:'y', -2:'Y'}[a] for a in w)


@lru_cache(None)
def symmetrized():
    return _symmetrized(parse_h_sc_relators())


@lru_cache(None)
def pieces():
    counts = Counter(r[:k] for r in symmetrized() for k in range(1, 61))
    return tuple(sorted((p for p, count in counts.items() if count >= 2),
                        key=lambda w: (len(w), w)))


@lru_cache(None)
def rule_index():
    return {r[:31]: r for r in symmetrized()}


def dehn(w):
    """Exact H_SC Dehn rewriting; output generally neither unique nor geodesic."""
    w = reduce(w)
    rules = rule_index()
    while True:
        for pos in range(len(w) - 30):
            r = rules.get(w[pos:pos+31])
            if r is None:
                continue
            k = 31
            while k < min(61, len(w)-pos) and w[pos+k] == r[k]:
                k += 1
            w = reduce(w[:pos] + inverse(r[k:]) + w[pos+k:])
            break
        else:
            return w


def equal(u, v):
    w = reduce(u + inverse(v))
    if len(w) < 61:  # certified girth, not a heuristic normal-form comparison
        return not w
    return not dehn(w)


def short_geodesic(w):
    """Unique exact geodesic for a freely reduced input of length <=30.

    Refuses longer inputs. In particular it never calls a Dehn residue geodesic.
    """
    w = reduce(w)
    if len(w) > 30:
        raise ValueError('outside the certified unique-geodesic ball of radius 30')
    return w


def piece_cover_certificate():
    pset = set(pieces())
    rows = []
    for r in symmetrized():
        ends = {0}
        maxima = []
        for _ in range(5):
            ends = {j+k for j in ends for k in range(1, 9)
                    if j+k <= 61 and r[j:j+k] in pset}
            maxima.append(max(ends, default=0))
        rows.append({'relator': letters(r), 'max_covered': maxima})
    return {'symmetrized_size': len(rows), 'piece_count': len(pset),
            'max_piece': max(map(len, pset)),
            'max_covered': [max(row['max_covered'][k] for row in rows)
                            for k in range(5)], 'rows': rows}


def cyclic_dehn(w):
    """Return (c,t) with c=t w t^-1, c cyclically Dehn-reduced.

    Input representative length N bounds |t| by 2*N*N+N. This is a witness,
    not a canonical conjugacy form. All cyclic rotations are checked.
    """
    w, t = reduce(w), ()
    while True:
        k = 0
        while 2*k+1 < len(w) and w[k] == -w[-k-1]:
            k += 1
        if k:
            t = reduce(inverse(w[:k]) + t)
            w = w[k:len(w)-k]
        for i in range(max(1, len(w))):
            rot = w[i:] + w[:i]
            d = dehn(rot)
            if len(d) < len(w):
                t = reduce(inverse(w[:i]) + t)
                w = d
                break
        else:
            return w, t


def conjugator_bound(L):
    if not isinstance(L, int) or L < 0:
        raise ValueError('L must be a nonnegative integer')
    return 4*L*L + 4*L + 8


def conjugacy_witness(u, v):
    """Complete individual conjugacy decision: g with v=g u g^-1, else None.

    Annular four-piece certificate gives rotations joined by one piece or 1.
    This routine does not enumerate AC states and does not decide AC orbits.
    """
    u, v = reduce(u), reduce(v)
    c, t = cyclic_dehn(u)
    d, h = cyclic_dehn(v)
    if not c or not d:
        return () if not c and not d else None
    # A cell would contribute >=15 edges to EACH boundary cycle.
    if min(len(c), len(d)) < 15:
        for i in range(len(c)):
            if c[i:]+c[:i] == d:
                return reduce(inverse(h) + inverse(c[:i]) + t)
        return None
    for i in range(len(c)):
        a, p = c[i:]+c[:i], c[:i]
        for j in range(len(d)):
            b, q = d[j:]+d[:j], d[:j]
            for z in ((),) + pieces():
                if equal(z+a+inverse(z), b):
                    g = reduce(inverse(h)+q+z+inverse(p)+t)
                    assert equal(g+u+inverse(g), v)
                    assert len(g) <= conjugator_bound(max(len(u), len(v)))
                    return g
    return None


def plateau_certificate(n):
    r, s = parse('x'*n+'Y'*(n+1)), parse('xyxYXY')
    a = sorted(set(rotations(r)) | set(rotations(inverse(r))))
    b = sorted(set(rotations(s)) | set(rotations(inverse(s))))
    rows = [{'a':letters(u), 'b':letters(v),
             'product':letters(reduce(u+v)),
             'cyclic_product':letters(cyclic_reduce(reduce(u+v)))}
            for u in a for v in b]
    minimum = min(len(row['cyclic_product']) for row in rows)
    return {'candidate':f'AK({n})', 'pair':[letters(r), letters(s)],
            'rotations_inversions':[len(a), len(b)], 'product_count':len(rows),
            'min_cyclic_product':minimum, 'rows':rows}


# Havas--Ramsay 2003, printed p.64, fixed positive certificate, NOT a search.
_HR_AK2 = [
 ('aBBBa','BAbabA'), ('aBBBa','BAbaBBa'), ('aBBBa','AbaBBaB'),
 ('aBBaBBaB','AbaBBaB'), ('aBBaBBaB','bAbbABa'),
 ('aBBaBBaB','abAbbAB'), ('aBBaBBaB','BabAbbA'),
 ('aBBaBBaB','BaBaB'), ('BBaBBaBa','BaBaB'),
 ('BBaBBaBa','bAbAb'), ('BBaBBaBa','AbAbb'),
 ('BBa','AbAbb'), ('BBa','Ab'), ('B','Ab'), ('B','A')]


def ak2_path_certificate():
    translation = str.maketrans('aAbB','xXyY')
    states = [tuple(parse(w.translate(translation)) for w in state)
              for state in _HR_AK2]
    steps = []
    for before, after in zip(states, states[1:]):
        matches = [mv for mv in all_moves(2,2) if apply_move(before,mv)==after]
        if not matches:
            raise AssertionError((before,after))
        steps.append({'move':list(matches[0]),'after':[letters(w) for w in after]})
    # Canonical AK(2) -> published start, by bounded free conjugacy/inversion.
    initial = (parse('xxYYY'), parse('xyxYXY'))
    prefix = []
    current = list(initial)
    for i in range(2):
        target = states[0][i]
        found = False
        for sign in (1,-1):
            a = current[i] if sign==1 else inverse(current[i])
            for k in range(len(a)):
                if a[k:]+a[:k] == target:
                    if sign == -1:
                        current[i] = inverse(current[i])
                        prefix.append({'move':['I',i,0], 'after':[letters(w) for w in current]})
                    g = inverse(a[:k])
                    # Expand g u g^-1 in reverse letter order.
                    for letter in reversed(g):
                        current = list(apply_move(tuple(current), ('C',i,letter)))
                        prefix.append({'move':['C',i,letter], 'after':[letters(w) for w in current]})
                    found = True
                    break
            if found:
                break
        assert current[i] == target
    suffix = []
    current = states[-1]
    for mv in [('I',0,0),('I',1,0)]:
        current = apply_move(current,mv)
        suffix.append({'move':list(mv),'after':[letters(w) for w in current]})
    current = (current[1],current[0])
    suffix.append({'move':['P',0,1],'after':[letters(w) for w in current]})
    full = prefix+steps+suffix
    assert current == (parse('x'),parse('y'))
    return {'source':'https://staff.itee.uq.edu.au/havas/2003hr.pdf',
            'initial':[letters(w) for w in initial], 'steps':full,
            'published_steps':len(steps),
            'max_geodesic_sum':max([11]+[sum(map(len,s['after'])) for s in full])}


def annular_example():
    """Freeze first deterministic single-cell conjugacy, not free conjugacy."""
    pset = set(pieces())
    for r in symmetrized():
        for k in range(1,9):
            z = r[:k]
            if z not in pset:
                continue
            for m in range(15,31):
                if r[k+m:k+m+k] != inverse(z):
                    continue
                b = r[k:k+m]
                a = inverse(r[2*k+m:])
                if not 15 <= len(a) <= 30:
                    continue
                if cyclic_reduce(a)!=a or cyclic_reduce(b)!=b:
                    continue
                if a in set(rotations(b)):
                    continue
                assert equal(z+b+inverse(z),a)
                return {'relator':letters(r),'u':letters(b),'v':letters(a),
                        'g':letters(z)}
    raise AssertionError('no one-cell example')


def bounded_walk_control():
    """128 prescribed walks, 48 moves, cap24; no component/noncontact claim."""
    import random
    rng = random.Random(26090402)
    checked, traps, transcript = 0, [], []
    moves = all_moves(2,2)
    for trial in range(128):
        state = (parse('x'),parse('y'))
        for step in range(48):
            choices = [(mv,apply_move(state,mv)) for mv in moves]
            choices = [(mv,t) for mv,t in choices if t!=state and sum(map(len,t))<=24]
            mv,state = rng.choice(choices)
            transcript.append([trial,step,list(mv),[letters(w) for w in state]])
            a,b = map(cyclic_reduce,state)
            if not a or not b or not 2 < len(a)+len(b) <=14:
                continue
            checked += 1
            minimum = min(len(cyclic_reduce(reduce(u+v)))
                          for aa in (a,inverse(a)) for u in rotations(aa)
                          for bb in (b,inverse(b)) for v in rotations(bb))
            if minimum > max(len(a),len(b)):
                traps.append([trial,step,letters(a),letters(b)])
    return {'seed':26090402,'walks':128,'moves_per_walk':48,'cap':24,
            'states_tested':checked,'traps':traps,
            'transcript_sha256':hashlib.sha256(json.dumps(transcript,separators=(',',':')).encode()).hexdigest(),
            'interpretation':'bounded diagnostic only; no orbit or completeness conclusion'}


def mixed_reorder_failure():
    """A shortest conjugator still makes the standard mixed reorder worse."""
    u,v,g=map(parse,('x','y','yxy'))
    b=reduce(g+u+inverse(g))
    c=reduce(b+v)
    a=reduce(inverse(g)+v+g)
    middle=reduce(u+a)
    original=[(u,v),(b,v),(c,v)]
    alternative=[(u,v),(u,a),(middle,a),(c,a),(c,v)]
    return {'g':letters(g),
            'original':[[letters(w) for w in state] for state in original],
            'reordered':[[letters(w) for w in state] for state in alternative],
            'original_peak':max(sum(map(len,state)) for state in original),
            'reordered_peak':max(sum(map(len,state)) for state in alternative),
            'conjugator_minimum_length':3,
            'scope':'this reorder fails; no claim that all peak lowering fails'}


def certificate():
    return {'schema':'hsc-second-strike-v1','relators':list(H_SC_RELATOR_STRINGS),
            'comparison':{'standard':['x','y'],'AK3':['xxxYYYY','xyxYXY']},
            'geodesic_radius':30, 'conjugator_bound':'4*L**2+4*L+8',
            'peak_upper_bound':None,'AK3_peak_lower_bound':15,
            'complete_component_enumeration':False,
            'piece_cover':piece_cover_certificate(),
            'plateaus':[plateau_certificate(2),plateau_certificate(3)],
            'AK2_positive_path':ak2_path_certificate(),
            'annular_positive':annular_example(),
            'bounded_walk_control':bounded_walk_control(),
            'mixed_reorder_failure':mixed_reorder_failure()}


if __name__ == '__main__':
    import sys
    json.dump(certificate(),sys.stdout,indent=2,sort_keys=True)
    print()
