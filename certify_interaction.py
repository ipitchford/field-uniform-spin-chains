#!/usr/bin/env python3
"""Apply the sufficient cubic-obstruction theorem to rational qutrit data.

Input: JSON {"coefficients": an 8x8 symmetric array of integers or rational
strings}, in the G basis of equation (7.1) of the manuscript. Floats are rejected.
Output: an exact certificate or INCONCLUSIVE, never an integrability verdict.
The certificate applies to all on-site fields, so there is no field input.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import sympy as s
from verify_symbolic import basis, comm, trace_middle


def rational(value: object) -> s.Rational:
    if isinstance(value,bool) or not isinstance(value,(int,str)):
        raise ValueError("Coefficients must be integers or rational strings; floats are not accepted")
    try:
        result = s.Rational(value)
    except (TypeError,ValueError,ZeroDivisionError) as exc:
        raise ValueError(f"Invalid rational coefficient: {value!r}") from exc
    if not result.is_finite:
        raise ValueError("Coefficients must be finite")
    return result


def certify(data: dict) -> dict:
    raw = data.get('coefficients')
    if not isinstance(raw,list) or len(raw) != 8 or any(not isinstance(row,list) or len(row) != 8 for row in raw):
        raise ValueError("Expected an 8x8 array in the 'coefficients' property")
    m = s.Matrix([[rational(x) for x in row] for row in raw])
    if m != m.T:
        raise ValueError("The rational coefficient matrix must be symmetric")
    g = basis()
    gram = s.diag(2,2,2,2,2,2,2,6)
    # m*gram is similar to the orthonormal coefficient matrix
    # sqrt(gram)*m*sqrt(gram), avoiding irrational intermediate entries.
    j_similar = m*gram
    determinant = s.factor(j_similar.det())
    t = s.Symbol('t')
    polynomial = (j_similar*j_similar).charpoly(t).as_expr()
    discriminant = s.factor(s.discriminant(polynomial,t))
    h = sum((m[a,b]*s.kronecker_product(g[a],g[b]) for a in range(8) for b in range(8)),s.zeros(9))
    a, b = s.kronecker_product(h,s.eye(3)), s.kronecker_product(s.eye(3),h)
    inner = comm(a,b).applyfunc(s.expand)
    obstruction = trace_middle(comm(a+b,inner).applyfunc(s.expand)).applyfunc(s.expand)
    assert obstruction == obstruction.conjugate().T
    norm2 = s.simplify(s.trace(obstruction*obstruction))
    full_rank, nonzero, simple_squares = determinant != 0, norm2 != 0, discriminant != 0
    if full_rank and nonzero and simple_squares:
        status = 'CERTIFIED_LOCAL_COMMUTANT_I_H'
        statement = 'For every periodic N >= 6 and arbitrary site-dependent on-site fields, every conserved quantity of range <= floor(N/2) is a linear combination of I and H.'
    elif full_rank and nonzero:
        status = 'CERTIFIED_NO_LOCAL_CHARGES_3_TO_HALF'
        statement = 'For every periodic N >= 6 and arbitrary site-dependent on-site fields, there is no conserved quantity of exact range 3 through floor(N/2); short-range charges are not classified by this certificate.'
    else:
        status = 'INCONCLUSIVE'
        statement = 'This sufficient certificate does not decide the interaction. Inconclusive is not an integrability verdict.'
    return {'status':status,'statement':statement,
            'assumptions':'Hermitian rational interaction; periodic chain; identical swap-symmetric bonds; arbitrary Hermitian on-site fields.',
            'normalization':'Input in unnormalized G basis; invariant tests use the orthonormal interaction matrix.',
            'full_traceless_interaction_rank':bool(full_rank),
            'nonzero_cubic_obstruction':bool(nonzero),
            'simple_spectrum_of_J_squared':bool(simple_squares),
            'determinant_J':str(determinant),
            'discriminant_characteristic_polynomial_J_squared':str(discriminant),
            'obstruction_frobenius_norm_squared':str(norm2),
            'obstruction_nonzero_entries_zero_based':[[i,j,str(obstruction[i,j])] for i in range(9) for j in range(9) if obstruction[i,j] != 0],
            'dependency':'Manuscript proofs and Hokkyo arXiv:2501.18400v3, Theorems 1 and 2.'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path,help='JSON file with rational 8x8 coefficients')
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding='utf-8'))
        if not isinstance(data,dict):
            raise ValueError('Input must be a JSON object')
        print(json.dumps(certify(data),indent=2))
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({'status':'INVALID_INPUT','error':str(exc)},indent=2),file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
