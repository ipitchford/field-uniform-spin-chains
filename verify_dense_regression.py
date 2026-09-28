"""Dense structure-constant regression and spin-half negative controls.

The contraction uses the unnormalised Gram matrix to cancel normalisation
radicals analytically. It is exactly the normalised [J,K(J)] formula.
"""
from __future__ import annotations
if not __debug__:
    raise SystemExit('REFUSED: assertion-based verification requires Python without -O or -OO')

import json,time
from functools import lru_cache
import sympy as sp
from spin1_algebra import hermitian_basis,from_coefficients,tensor,comm,local_data

@lru_cache(maxsize=4)
def structure_data(g):
    norms=[sp.trace(x*x) for x in g];m=len(g);triples=[]
    for r in range(m):
        tt=[]
        for a in range(m):
            for b in range(m):
                x=sp.expand(sp.trace(g[r]*comm(g[a],g[b]))/sp.I)
                if x:tt.append((a,b,x))
        triples.append(tt)
    return norms,triples

def structure_obstruction(m,g):
    norms,triples=structure_data(g);n=len(g)
    # L_rc = sqrt(n_r*n_c) K_rc, with J_ab=sqrt(n_a*n_b) M_ab.
    ell=sp.Matrix(n,n,lambda r,c:sum(fr*fc*m[a,b]*m[e,t]
            for a,e,fr in triples[r] for b,t,fc in triples[c]))
    ni=sp.diag(*[1/x for x in norms]);coeff=m*ell*ni-ni*ell*m
    out=sum((coeff[a,b]*tensor(g[a],g[b]) for a in range(n) for b in range(n)
             if coeff[a,b]),sp.zeros(g[0].rows**2)).applyfunc(sp.expand)
    return out,ell,coeff

def run():
    start=time.perf_counter();g=hermitian_basis();checks=[]
    for seed in [1,2,3]:
        m=sp.Matrix(8,8,lambda a,b:(a+2*seed+1) if a==b else
                    sp.Rational(1+((a+b+seed)%5),7+seed))
        assert m==m.T and all(m)
        h=from_coefficients(m);direct=local_data(h)[5].applyfunc(sp.expand)
        via,ell,coeff=structure_obstruction(m,g)
        assert via==direct and ell==ell.T and coeff==-coeff.T
        assert direct==direct.H and direct!=sp.zeros(9)
        checks.append({'seed':seed,'coefficient_formula_matches_direct':True,
                        'obstruction_norm_squared':str(sp.expand(sp.trace(direct*direct)))})
    sx=sp.ImmutableMatrix([[0,1],[1,0]]);sy=sp.ImmutableMatrix([[0,-sp.I],[sp.I,0]]);sz=sp.ImmutableMatrix(sp.diag(1,-1))
    controls=[]
    for j in [sp.diag(1,2,3),sp.Matrix([[2,1,3],[1,5,2],[3,2,7]]),sp.Matrix([[0,1,2],[1,0,3],[2,3,4]])]:
        gg=(sx,sy,sz);m=j/2
        h=sum((m[a,b]*tensor(gg[a],gg[b]) for a in range(3) for b in range(3)),sp.zeros(4))
        direct=local_data(h,2)[5].applyfunc(sp.expand);via,ell,_=structure_obstruction(m,gg)
        assert direct==via==sp.zeros(4) and ell/2==4*j.adjugate()
        controls.append({'J':[[int(x) for x in j.row(r)] for r in range(3)],'old_obstruction_zero':True})
    return {'status':'PASS','dense_qutrit_checks':checks,'spin_half_controls':controls,
            'elapsed_seconds':round(time.perf_counter()-start,6),'arithmetic':'exact Gaussian rationals; Gram-corrected structure constants'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
