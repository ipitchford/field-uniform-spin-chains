#!/usr/bin/env python3
"""Exact coordinate witnesses for the field-eliminated quotient; MIT.

This checker verifies only the finite linear identity, not leading rigidity,
the residual commutant, the all-range reduction or formal proof correctness.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp
from spin1_algebra import from_coefficients, quotient_matrix, pq

CONVENTION = '9T,9Delta; row-major real then imaginary; 28 lexicographic swap-odd G pairs then 8 G fields'

def matrices(data):
    from certify_field_uniform import rational
    if not isinstance(data, dict):
        raise ValueError('Input must be an object')
    if data.get('kind') == 'blbq':
        u, v = rational(data.get('u')), rational(data.get('v'))
        p, q = pq()
        h = u*p + (v-u)*q - v*sp.eye(9)/3
    else:
        raw = data.get('coefficients')
        if not isinstance(raw, list) or len(raw) != 8 or any(not isinstance(r, list) or len(r) != 8 for r in raw):
            raise ValueError('Expected 8x8 rational coefficients')
        m = sp.Matrix([[rational(x) for x in r] for r in raw])
        if m != m.T:
            raise ValueError('Coefficients must be symmetric')
        h = from_coefficients(m)
    return quotient_matrix(h)

def fingerprint(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def generate(data):
    t, d = matrices(data)
    _, cols = t.rref()
    b = t[:, list(cols)]
    augmented = b.row_join(d)
    _, rows = augmented.T.rref()
    out = {'schema': 'field-uniform-quotient-witness/v1', 'input': data,
           'inputSha256': fingerprint(data), 'coordinates': CONVENTION,
           'scope': 'Finite quotient identity only; consistency is not exact conservation or integrability.'}
    if len(rows) > len(cols):
        selected = augmented[list(rows), :]
        target = sp.zeros(len(cols)+1, 1)
        target[-1] = 1
        weights = selected.T.inv()*target
        out.update(kind='inconsistent', rows=list(rows), weights=[str(x) for x in weights])
    else:
        solution, parameters = b.gauss_jordan_solve(-d)
        solution = solution.subs({x: 0 for x in parameters})
        x = sp.zeros(t.cols, 1)
        for j, value in zip(cols, solution):
            x[j] = value
        out.update(kind='consistent', coefficients=[str(v) for v in x])
    verify(out, data)
    return out

def verify(witness, expected_input):
    from certify_field_uniform import rational
    if witness.get('schema') != 'field-uniform-quotient-witness/v1' or witness.get('coordinates') != CONVENTION:
        raise ValueError('Unsupported witness schema or coordinates')
    if witness.get('input') != expected_input or witness.get('inputSha256') != fingerprint(expected_input):
        raise ValueError('Witness input binding mismatch')
    t, d = matrices(expected_input)
    if witness.get('kind') == 'inconsistent':
        rows, weights = witness.get('rows'), witness.get('weights')
        if not isinstance(rows, list) or not isinstance(weights, list) or not rows or len(rows) != len(weights):
            raise ValueError('Invalid sparse functional')
        if any(type(r) is not int or r < 0 or r >= t.rows for r in rows) or len(set(rows)) != len(rows):
            raise ValueError('Invalid row selection')
        y = sp.Matrix([rational(v) for v in weights]).T
        if y*t[rows, :] != sp.zeros(1, t.cols) or (y*d[rows, :])[0] != 1:
            raise ValueError('Dual identity failed')
    elif witness.get('kind') == 'consistent':
        raw = witness.get('coefficients')
        if not isinstance(raw, list) or len(raw) != t.cols:
            raise ValueError('Wrong coefficient dimension')
        x = sp.Matrix([rational(v) for v in raw])
        if t*x+d != sp.zeros(t.rows, 1):
            raise ValueError('Consistency identity failed')
    else:
        raise ValueError('Unknown witness kind')
    return {'status': 'PASS', 'kind': witness['kind'], 'inputSha256': fingerprint(expected_input),
            'assurance': 'Exact multiplication with reconstructed matrices; shares the matrix-construction module, not independent implementation.'}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('witness', type=Path)
    p.add_argument('input', type=Path, help='Trusted intended interaction; never infer solely from witness')
    args = p.parse_args()
    try:
        print(json.dumps(verify(json.loads(args.witness.read_text()), json.loads(args.input.read_text())), indent=2))
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)}))
        return 1
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
