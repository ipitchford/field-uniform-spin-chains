"""Exact local algebra for field-uniform spin-chain certificates.

All computations use SymPy integers, rationals and Gaussian rationals. No
floating-point arithmetic, spectral tolerance, or finite-chain diagonalisation
is used. Site order and flattened coordinates are specified in the manuscript.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product
from typing import Sequence
import sympy as sp
from sympy.polys.matrices import DomainMatrix


def comm(a: sp.MatrixBase, b: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(a*b-b*a).applyfunc(sp.expand)


def tensor(*a: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(sp.kronecker_product(*a))


@lru_cache(maxsize=1)
def hermitian_basis() -> tuple[sp.ImmutableMatrix, ...]:
    def e(i: int, j: int) -> sp.Matrix:
        z=sp.zeros(3); z[i,j]=1; return z
    x=lambda i,j: e(i,j)+e(j,i)
    y=lambda i,j: -sp.I*e(i,j)+sp.I*e(j,i)
    return tuple(sp.ImmutableMatrix(z) for z in (
        x(0,1),y(0,1),sp.diag(1,-1,0),x(0,2),y(0,2),
        x(1,2),y(1,2),sp.diag(1,1,-2)))


def real_sl_basis(d: int=3) -> tuple[sp.Matrix, ...]:
    out=[]
    for i in range(d):
        for j in range(d):
            if i != j:
                z=sp.zeros(d); z[i,j]=1; out.append(z)
    for i in range(d-1):
        z=sp.zeros(d); z[i,i]=1; z[i+1,i+1]=-1; out.append(z)
    return tuple(out)


def pq(d: int=3) -> tuple[sp.Matrix,sp.Matrix]:
    p=sp.zeros(d*d); q=sp.zeros(d*d)
    for i,j in product(range(d),repeat=2):
        p[i*d+j,j*d+i]=1; q[i*d+i,j*d+j]=1
    return p,q


def partial_trace(x: sp.MatrixBase, d: int, n: int, site: int) -> sp.Matrix:
    """Unnormalised trace of one tensor factor; site is zero based."""
    if x.shape != (d**n,d**n) or not 0 <= site < n:
        raise ValueError('Inconsistent partial-trace dimensions.')
    inds=list(product(range(d),repeat=n-1))
    def idx(a: Sequence[int]) -> int:
        z=0
        for t in a: z=d*z+t
        return z
    out=sp.zeros(d**(n-1))
    for r,a in enumerate(inds):
        for c,b in enumerate(inds):
            out[r,c]=sum(x[idx(a[:site]+(t,)+a[site:]),
                           idx(b[:site]+(t,)+b[site:])] for t in range(d))
    return out


def endpoint_projection(x: sp.MatrixBase, d: int=3) -> sp.Matrix:
    """Orthogonal projection onto traceless first and last tensor factors."""
    i=sp.eye(d)
    t1=partial_trace(x,d,3,0); t3=partial_trace(x,d,3,2)
    t13=partial_trace(t1,d,2,1)
    return sp.Matrix(x-tensor(i,t1)/d-tensor(t3,i)/d+tensor(i,t13,i)/(d*d))


def local_data(h: sp.MatrixBase, d: int=3) -> tuple[sp.Matrix,...]:
    a=tensor(h,sp.eye(d)); b=tensor(sp.eye(d),h)
    c=comm(a,b); nested=comm(a+b,c)
    return a,b,c,nested,endpoint_projection(nested,d),partial_trace(nested,d,3,1)


def from_coefficients(m: sp.MatrixBase) -> sp.Matrix:
    if m.shape != (8,8): raise ValueError('Expected an 8 by 8 coefficient matrix.')
    g=hermitian_basis()
    return sum((m[a,b]*tensor(g[a],g[b]) for a,b in product(range(8),repeat=2)
                if m[a,b] != 0),sp.zeros(9))


def diagonal_interaction(j: Sequence[object]) -> sp.Matrix:
    if len(j) != 8: raise ValueError('Expected eight coefficients.')
    return from_coefficients(sp.diag(*map(sp.sympify,j)))


def real_vector(x: sp.MatrixBase) -> sp.Matrix:
    vals=[sp.expand(t) for t in x]
    return sp.Matrix([sp.re(t) for t in vals]+[sp.im(t) for t in vals])


def quotient_matrix(h: sp.MatrixBase) -> tuple[sp.Matrix,sp.Matrix]:
    """Return real-coordinate matrix 9*T and vector 9*Delta for d=3.

    28 correction columns (a<b, lexicographic), followed by the eight fields.
    Rows: real row-major matrix entries, then imaginary row-major entries.
    """
    i=sp.eye(3); g=hermitian_basis(); a,b,c,_,delta,_=local_data(h)
    cols=[]
    for r in range(8):
        for t in range(r+1,8):
            z=tensor(g[r],g[t])-tensor(g[t],g[r])
            cols.append(real_vector(9*sp.I*(comm(a,tensor(i,z))+comm(b,tensor(z,i)))))
    for f in g:
        ff=tensor(f,i,i)+tensor(i,f,i)+tensor(i,i,f)
        cols.append(real_vector(9*comm(ff,c)))
    return sp.Matrix.hstack(*cols),real_vector(9*delta)


def leading_pair_matrix(h: sp.MatrixBase) -> sp.Matrix:
    """729 x 128 complex-linear map, in the real matrix-unit sl_3 basis."""
    i=sp.eye(3); a=tensor(h,i); b=tensor(i,h)
    pairs=[tensor(x,y) for x in real_sl_basis() for y in real_sl_basis()]
    cols=[comm(tensor(z,i),b) for z in pairs]
    cols += [-comm(a,tensor(i,z)) for z in pairs]
    return sp.Matrix.hstack(*(sp.Matrix(list(z)) for z in cols))


def bond_stabilizer_matrix(h: sp.MatrixBase) -> sp.Matrix:
    """Real map (x,y) -> i[x tensor I+I tensor y,h], for Hermitian x,y."""
    i=sp.eye(3); g=hermitian_basis()
    return sp.Matrix.hstack(*(real_vector(sp.I*comm(z,h)) for z in
         [tensor(x,i) for x in g]+[tensor(i,x) for x in g]))


def rational_rank(a: sp.MatrixBase) -> int:
    """Rank over Q, with no numerical tolerance."""
    if any(t.is_Rational is not True for t in a):
        raise ValueError('Rank input must be exactly rational.')
    rows=[list(a.row(r)) for r in range(a.rows) if any(a.row(r))]
    if not rows: return 0
    dm=DomainMatrix.from_Matrix(sp.Matrix(rows)).convert_to(sp.QQ)
    _,pivots=dm.rref()
    return len(pivots)


def determinant_mod(a: sp.MatrixBase, prime: int) -> int:
    """A prime-field minor is a lower-rank certificate over characteristic zero."""
    if a.rows != a.cols: raise ValueError('Minor must be square.')
    vals=[]
    for r in range(a.rows):
        row=[]
        for x in a.row(r):
            x=sp.Rational(x)
            if int(x.q)%prime == 0: raise ValueError('Denominator vanishes modulo prime.')
            row.append(int(x.p)%prime*pow(int(x.q)%prime,-1,prime)%prime)
        vals.append(row)
    det=1; n=len(vals)
    for col in range(n):
        pivot=next((r for r in range(col,n) if vals[r][col]),None)
        if pivot is None:return 0
        if pivot != col: vals[pivot],vals[col]=vals[col],vals[pivot];det=-det
        v=vals[col][col];det=det*v%prime; inv=pow(v,-1,prime)
        for r in range(col+1,n):
            f=vals[r][col]*inv%prime
            if f:
                for k in range(col+1,n): vals[r][k]=(vals[r][k]-f*vals[col][k])%prime
                vals[r][col]=0
    return det%prime


def hilbert_schmidt_squared(x: sp.MatrixBase) -> sp.Expr:
    return sp.simplify(sum(sp.conjugate(t)*t for t in x))
