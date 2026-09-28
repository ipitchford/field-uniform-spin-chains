#!/usr/bin/env python3
"""Positive, inconclusive, and invalid-input controls for the public certifier."""
from __future__ import annotations
if not __debug__:
    raise SystemExit('REFUSED: assertion-based verification requires Python without -O or -OO')

import json
from pathlib import Path
from certify_interaction import certify


def diagonal(values: list) -> dict:
    return {'coefficients':[[values[i] if i == j else 0 for j in range(8)] for i in range(8)]}


def run() -> dict:
    checks = []
    original = diagonal(list(range(1,9)))
    a = certify(original)
    assert a['status'] == 'CERTIFIED_LOCAL_COMMUTANT_I_H'
    checks.append('integer witness receives the full local-commutant certificate')
    weak = certify(diagonal([1,1,3,4,5,6,7,8]))
    assert weak['status'] == 'CERTIFIED_NO_LOCAL_CHARGES_3_TO_HALF'
    checks.append('repeated squared eigenvalue correctly withholds short-charge classification')
    deficient = certify(diagonal([0,2,3,4,5,6,7,8]))
    assert deficient['nonzero_cubic_obstruction'] and not deficient['full_traceless_interaction_rank']
    assert deficient['status'] == 'INCONCLUSIVE'
    checks.append('nonzero obstruction without full interaction rank remains inconclusive')
    scalar = certify(diagonal(['1/2']*7+['1/6']))
    assert scalar['full_traceless_interaction_rank'] and not scalar['nonzero_cubic_obstruction']
    assert scalar['status'] == 'INCONCLUSIVE'
    checks.append('scalar orthonormal coupling gives zero obstruction and an inconclusive result')
    dense = {'coefficients':[[i+1 if i == j else '1/1000' for j in range(8)] for i in range(8)]}
    dense_result = certify(dense)
    assert dense_result['status'] == 'CERTIFIED_LOCAL_COMMUTANT_I_H'
    checks.append('fully dense symmetric rational coefficient matrix is certified')
    root = Path(__file__).parent/'evidence'
    (root/'dense_input.json').write_text(json.dumps(dense,indent=2)+'\n')
    (root/'dense_certificate.json').write_text(json.dumps(dense_result,indent=2)+'\n')
    bad = diagonal(list(range(1,9)))
    bad['coefficients'][0][1] = 1
    try:
        certify(bad)
        raise AssertionError('Asymmetric input was accepted')
    except ValueError:
        checks.append('asymmetric input is rejected')
    bad = diagonal(list(range(1,9)))
    bad['coefficients'][0][0] = 1.0
    try:
        certify(bad)
        raise AssertionError('Floating-point input was accepted')
    except ValueError:
        checks.append('floating-point input is rejected')
    return {'status':'PASS','checks':checks,
            'controls':{'witness':a['status'],'repeated_square':weak['status'],
                        'rank_deficient':deficient['status'],'scalar_interaction':scalar['status'],
                        'fully_dense':dense_result['status']}}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
