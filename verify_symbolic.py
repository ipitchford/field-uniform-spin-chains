#!/usr/bin/env python3
"""Exact symbolic checks for the spin-1 cubic-obstruction research draft.

Dependencies: SymPy 1.14.0 (tested); standard-library modules otherwise.
The all-range conclusion uses the cited theorem and the manuscript's proofs;
finite matrix checks alone do not certify that conclusion.
"""
from __future__ import annotations
if not __debug__:
    raise SystemExit('REFUSED: assertion-based verification requires Python without -O or -OO')

import json
from pathlib import Path
import sympy as s
from verify_integer import H


def comm(a: s.Matrix, b: s.Matrix) -> s.Matrix:
    return a*b-b*a


def matrix_unit(i: int, j: int) -> s.Matrix:
    a = s.zeros(3)
    a[i,j] = 1
    return a


def basis() -> list[s.Matrix]:
    e, z = matrix_unit, s.I
    return [e(0,1)+e(1,0), -z*e(0,1)+z*e(1,0), s.diag(1,-1,0),
            e(0,2)+e(2,0), -z*e(0,2)+z*e(2,0),
            e(1,2)+e(2,1), -z*e(1,2)+z*e(2,1), s.diag(1,1,-2)]


def trace_middle(a: s.Matrix) -> s.Matrix:
    return s.Matrix(9,9,lambda i,j: sum(a[(i//3)*9+3*t+i%3,
                                         (j//3)*9+3*t+j%3] for t in range(3)))


def det_mod(a: list[list[int]], p: int) -> int:
    n = len(a)
    b = [[x % p for x in row] for row in a]
    result = 1
    for k in range(n):
        pivot = next((i for i in range(k,n) if b[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            result = -result % p
        value = b[k][k]
        result = result*value % p
        inverse = pow(value,-1,p)
        for i in range(k+1,n):
            factor = b[i][k]*inverse % p
            if factor:
                for j in range(k+1,n):
                    b[i][j] = (b[i][j]-factor*b[k][j]) % p
            b[i][k] = 0
    return result


def pair_certificate() -> dict:
    """Verify an explicit rank-127 minor and the identity-pair null vector."""
    e = matrix_unit
    g = [e(0,1),e(1,0),e(0,2),e(2,0),e(1,2),e(2,1),
         s.diag(1,-1,0),s.diag(0,1,-1)]
    def coords(x: s.Matrix) -> list[int]:
        return [int(v) for v in [x[0,1],x[1,0],x[0,2],x[2,0],
                                 x[1,2],x[2,1],x[0,0],-x[2,2]]]
    c = [[coords(comm(x,y)) for y in g] for x in g]
    a = [[0]*128 for _ in range(512)]
    for x in range(8):
        for y in range(8):
            for z in range(8):
                row = (x*8+y)*8+z
                for t in range(8):
                    a[row][t*8+x] += c[t][y][z]
                    a[row][64+t*8+y] -= c[x][t][z]
    identity_pair = [int(i//8 == i%8) for i in range(64)]*2
    assert all(sum(x*y for x,y in zip(row,identity_pair)) == 0 for row in a)
    certificate = json.loads((Path(__file__).parent/'evidence'/'pair_certificate.json').read_text())
    rows, cols = certificate['row_indices'], certificate['column_indices']
    assert len(rows) == len(set(rows)) == len(cols) == len(set(cols)) == 127
    assert certificate['prime'] == 101
    minor = [[a[i][j] for j in cols] for i in rows]
    determinant = det_mod(minor,101)
    assert determinant == 32
    return {"rows":512, "columns":128, "rank_over_Q":127,
            "minor_order":127,"prime":101,"minor_determinant_mod_prime":determinant,
            "kernel_vector":"(Id,Id)"}


def run() -> dict:
    checks: list[str] = []
    g = basis()
    norms = [s.trace(x*x) for x in g]
    assert norms == [2]*7+[6]
    assert all(s.trace(g[a]*g[b]) == (norms[a] if a == b else 0)
               for a in range(8) for b in range(8))
    assert all(x == x.conjugate().T and s.trace(x) == 0 for x in g)
    checks.append("rational Hermitian traceless orthogonal basis and its Gram matrix")
    h = sum((s.Integer(a+1)*s.kronecker_product(g[a],g[a]) for a in range(8)),s.zeros(9))
    assert h == s.Matrix(H)
    checks.append("Gell-Mann interaction (1,...,8) equals the integer witness")
    assert [int(norms[a]*(a+1)) for a in range(8)] == [2,4,6,8,10,12,14,48]
    checks.append("orthonormal interaction eigenvalues follow from exact Gram normalization")
    variables = s.symbols('j1:9',real=True)
    coefficients: dict[tuple[int,int],s.Expr] = {}
    # Expand Tr_2([h12+h23,[h12,h23]]) directly in tensor factors.
    # The trace-cyclicity contractions here are independent of the full
    # 27x27 integer implementation in verify_integer.py.
    for a in range(8):
        for c in range(8):
            middle = comm(g[a],g[c])
            for f in range(8):
                t = s.trace(g[f]*middle)
                if t == 0:
                    continue
                left, right = comm(g[f],g[a]), comm(g[f],g[c])
                for r in range(8):
                    v = s.trace(g[r]*left)/norms[r]
                    if v != 0:
                        key = (r,c)
                        coefficients[key] = coefficients.get(key,s.S.Zero)+variables[a]*variables[c]*variables[f]*t*v
                    v = s.trace(g[r]*right)/norms[r]
                    if v != 0:
                        key = (a,r)
                        coefficients[key] = coefficients.get(key,s.S.Zero)+variables[a]*variables[c]*variables[f]*t*v
    result = {key:s.factor(v) for key,v in coefficients.items() if s.expand(v) != 0}
    j1,j2,j3,j4,j5,j6,j7,j8 = variables
    value = 4*(j3-3*j8)*(j4*j5-j6*j7)
    assert set(result) == {(2,7),(7,2)}
    assert s.expand(result[(2,7)]-value) == 0
    assert s.expand(result[(7,2)]+value) == 0
    assert value.subs(dict(zip(variables,range(1,9)))) == 1848
    checks.append("complete eight-variable symbolic cubic identity; all other coefficients zero")
    a, b = s.kronecker_product(h,s.eye(3)), s.kronecker_product(s.eye(3),h)
    c = comm(a,b)
    for x in g:
        for onsite in [s.kronecker_product(x,s.eye(3),s.eye(3)),
                       s.kronecker_product(s.eye(3),x,s.eye(3)),
                       s.kronecker_product(s.eye(3),s.eye(3),x)]:
            assert trace_middle(comm(onsite,c)) == s.zeros(9)
    checks.append("24 single-site basis commutators have zero middle trace at the witness")
    for x in g:
        for y in g:
            q = s.kronecker_product(x,y)
            assert trace_middle(comm(s.kronecker_product(q,s.eye(3)),b)) == s.zeros(9)
            assert trace_middle(comm(a,s.kronecker_product(s.eye(3),q))) == s.zeros(9)
    checks.append("128 overlapping two-site basis corrections have zero middle trace")
    pair = pair_certificate()
    checks.append("independent rank-127 certificate for the sl_3 pair-rigidity lemma")
    return {"status":"PASS", "sympy_version":s.__version__, "arithmetic":"exact symbolic",
            "checks":checks, "symbolic_coefficient":str(s.factor(value)),
            "nonzero_basis_pairs_one_based":[[3,8],[8,3]],"pair_rigidity":pair}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
