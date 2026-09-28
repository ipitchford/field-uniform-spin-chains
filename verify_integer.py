#!/usr/bin/env python3
"""Independent standard-library, exact-integer checker for the qutrit witness.

This checks the explicit local certificate, not Hokkyo's all-range theorem.
No floating-point operations, external dependencies, or network access are used.
"""
from __future__ import annotations
if not __debug__:
    raise SystemExit('REFUSED: assertion-based verification requires Python without -O or -OO')

import json

Matrix = list[list[int]]

H: Matrix = [
    [11,0,0,0,-1,0,0,0,-1],
    [0,5,0,3,0,0,0,0,0],
    [0,0,-16,0,0,0,9,0,0],
    [0,3,0,5,0,0,0,0,0],
    [-1,0,0,0,11,0,0,0,-1],
    [0,0,0,0,0,-16,0,13,0],
    [0,0,9,0,0,0,-16,0,0],
    [0,0,0,0,0,13,0,-16,0],
    [-1,0,0,0,-1,0,0,0,32],
]


def eye(n: int) -> Matrix:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("Incompatible matrix dimensions")
    bt = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def commutator(a: Matrix, b: Matrix) -> Matrix:
    ab, ba = multiply(a, b), multiply(b, a)
    return [[x-y for x, y in zip(ra, rb)] for ra, rb in zip(ab, ba)]


def kron(a: Matrix, b: Matrix) -> Matrix:
    return [[x*y for x in ra for y in rb] for ra in a for rb in b]


def trace_middle(a: Matrix, d: int = 3) -> Matrix:
    return [[sum(a[(i//d)*d*d+t*d+i%d][(j//d)*d*d+t*d+j%d]
                 for t in range(d)) for j in range(d*d)] for i in range(d*d)]


def run() -> dict:
    checks: list[str] = []
    assert H == [list(row) for row in zip(*H)], "Hermiticity failed"
    checks.append("integer witness is Hermitian")
    for a in range(3):
        for b in range(3):
            assert sum(H[3*a+t][3*b+t] for t in range(3)) == 0
            assert sum(H[3*t+a][3*t+b] for t in range(3)) == 0
    checks.append("both one-site partial traces vanish")
    perm = [3*(i%3)+i//3 for i in range(9)]
    assert all(H[i][j] == H[perm[i]][perm[j]] for i in range(9) for j in range(9))
    checks.append("inversion / swap symmetry")
    a, b = kron(H, eye(3)), kron(eye(3), H)
    obstruction = trace_middle(commutator(add(a,b), commutator(a,b)))
    diag = [0,3696,-3696,-3696,0,3696,3696,-3696,0]
    expected = [[diag[i] if i == j else 0 for j in range(9)] for i in range(9)]
    assert obstruction == expected, "Cubic partial-trace certificate failed"
    checks.append("27x27 double commutator gives the asserted 9x9 obstruction")
    norm2 = sum(x*x for row in obstruction for x in row)
    assert norm2 == 81962496
    checks.append("obstruction Frobenius norm squared is 81962496")
    # The correspondence with the Gell-Mann-basis interaction is checked by
    # verify_symbolic.py. These are its orthonormal interaction eigenvalues.
    eigenvalues = [2,4,6,8,10,12,14,48]
    assert all(x > 0 for x in eigenvalues)
    assert len(set(x*x for x in eigenvalues)) == 8
    checks.append("asserted interaction eigenvalues are nonzero with distinct squares")
    row_bound = max(sum(abs(x) for x in row) for row in H)
    assert row_bound == 34
    # For ||h-h_*||_F <= 1/10, the proven Lipschitz bound is 85704/10.
    lip_num = 8*3*(35*35+35*34+34*34)
    assert lip_num == 85704 and lip_num*lip_num < 100*norm2
    checks.append("rational radius 1/10 passes the stated robustness inequality")
    return {"status": "PASS", "arithmetic": "Python exact integers",
            "checks": checks, "obstruction_diagonal": diag,
            "obstruction_norm_squared": norm2,
            "orthonormal_interaction_eigenvalues": eigenvalues,
            "operator_norm_row_sum_bound": row_bound,
            "h_star": H}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
