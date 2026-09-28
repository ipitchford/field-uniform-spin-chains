"""Exact symbolic and modular checks for the new version-1 theorems."""
from __future__ import annotations
if not __debug__:
    raise SystemExit('REFUSED: assertion-based verification requires Python without -O or -OO')

import json,time
from pathlib import Path
import sympy as sp
from spin1_algebra import *

ROOT=Path(__file__).resolve().parent

def check(condition: bool, message: str) -> None:
    if not condition: raise AssertionError(message)


def run() -> dict:
    started=time.perf_counter(); checks={}
    p,q=pq(); u,v=sp.symbols('u v',real=True)
    h=u*p+(v-u)*q-v*sp.eye(9)/3
    _,_,c,nested,delta,old=local_data(h)
    delta=delta.applyfunc(sp.factor)
    w=local_data(p-q)[4]
    check(delta.applyfunc(sp.expand)==(u*(u-v)*(u+v)*w).applyfunc(sp.expand),'Isotropic cubic identity')
    check(old.applyfunc(sp.expand)==sp.zeros(9),'Isotropic old-obstruction vanishing')
    check(hilbert_schmidt_squared(w)==40,'Isotropic norm')
    saved=sp.Matrix([[sp.Rational(x) for x in row] for row in json.loads((ROOT/'evidence/isotropic_W.json').read_text())])
    check(w==saved,'Stored isotropic certificate')
    check(hilbert_schmidt_squared(delta.subs({u:1,v:sp.Rational(1,3)}))==sp.Rational(2560,81),'AKLT exact norm')
    # The coefficient operator has the claimed eigenvalues on the symmetric
    # traceless and antisymmetric transpose-parity spaces in Cartesian basis.
    g=hermitian_basis(); ns=[sp.trace(x*x) for x in g]
    j=sp.Matrix(8,8,lambda a,b:sp.simplify(sp.trace(tensor(g[a],g[b])*h)/sp.sqrt(ns[a]*ns[b])))
    expected=sp.diag(v,2*u-v,v,v,2*u-v,v,2*u-v,v)
    check(j==expected,'Isotropic coupling eigenspaces and multiplicities')
    check(sp.factor(j.det())==v**5*(2*u-v)**3,'Isotropic determinant')
    checks['isotropic_polynomial']={'identity':'Delta = u*(u-v)*(u+v)*W','norm_W_squared':40,
        'old_obstruction':'identically zero','AKLT_Delta_norm_squared':'2560/81',
        'det_J':'v^5*(2*u-v)^3'}
    # Check all four cubic coefficient matrices separately against symmetry.
    # T has degree one (corrections) or two (fields) in u,v. Since W is fixed,
    # its exact pairing must vanish as a polynomial in both variables.
    i=sp.eye(3);h12=tensor(h,i);h23=tensor(i,h)
    for a in range(8):
        for b in range(a+1,8):
            z=tensor(g[a],g[b])-tensor(g[b],g[a])
            tz=sp.I*(comm(h12,tensor(i,z))+comm(h23,tensor(z,i)))
            check(sp.expand(sp.trace(w*tz))==0,'Isotropic dual correction annihilation')
    for f in g:
        tf=comm(tensor(f,i,i)+tensor(i,f,i)+tensor(i,i,f),c)
        check(sp.expand(sp.trace(w*tf))==0,'Isotropic dual field annihilation')
    checks['isotropic_dual']={'correction_polynomials_checked':28,'field_polynomials_checked':8}
    # Local endpoint projection zero on each integrable ray; verify the full
    # Reshetikhin telescoping form rather than relying on zero projection alone.
    positive=[]
    for uu,vv in [(0,1),(1,1),(1,-1)]:
        hh=h.subs({u:uu,v:vv});_,_,cc,dd,de,oo=local_data(hh)
        # Trace site 1 gives d*X23 up to one-site terms. Solve X23-X12 exactly.
        # For these canonical isotropic densities, Tr_{1,2}D = 0, so this is X.
        xx=partial_trace(dd,3,3,0)/3
        check(dd==tensor(i,xx)-tensor(xx,i),'Reshetikhin identity on integrable ray')
        check(cc!=sp.zeros(27),'Nonzero range-three charge density')
        positive.append({'u':uu,'v':vv,'Reshetikhin':True,'C_nonzero':True})
    checks['integrable_positive_controls']=positive
    pair_results={}
    for name in ['Heisenberg','rank5']:
        cert=json.loads((ROOT/f'evidence/{name}_pair.json').read_text())
        hh=sp.Matrix(cert['interaction']);mm=leading_pair_matrix(hh)
        minor=mm.extract(cert['rows'],cert['cols'])
        val=determinant_mod(minor,101)
        check(val==cert['minor_determinant_mod101'] and val!=0,'Leading pair minor')
        # The known kernel (h,h) is verified by reconstructing h exactly in the
        # real tensor basis, then checking all 729 equations.
        b2=[tensor(x,y) for x in real_sl_basis() for y in real_sl_basis()]
        bmat=sp.Matrix.hstack(*(sp.Matrix(list(x)) for x in b2))
        coeff=bmat.gauss_jordan_solve(sp.Matrix(list(hh)))[0]
        check(mm*coeff.col_join(coeff)==sp.zeros(729,1),'Known pair kernel')
        left=sp.Matrix.hstack(*(sp.Matrix(list(comm(tensor(x,i),hh))) for x in real_sl_basis()))
        right=sp.Matrix.hstack(*(sp.Matrix(list(comm(tensor(i,x),hh))) for x in real_sl_basis()))
        check(rational_rank(left)==rational_rank(right)==8,'Boundary injectivity')
        pair_results[name]={'matrix_shape':[729,128],'minor_order':127,
                           'prime':101,'minor_determinant':val,'rank_Q':127,
                           'boundary_ranks':[8,8],'exact_kernel':'(h,h)'}
    checks['rank_deficient_leading_hypotheses']=pair_results
    quotient_results={}
    for name in ['gapzero_cartan','gapzero_product']:
        cert=json.loads((ROOT/f'evidence/{name}_minor.json').read_text())
        hh=diagonal_interaction(cert['input_diagonal_G'])
        mat,dv=quotient_matrix(hh);aug=mat.row_join(dv)
        val=determinant_mod(aug.extract(cert['row_indices'],cert['column_indices']),101)
        check(val==cert['det_mod_prime'] and val!=0,'Augmented quotient minor')
        check(local_data(hh)[5]==sp.zeros(9),'Old certificate must be blind')
        check(rational_rank(mat)==36 and rational_rank(aug)==37,'Exact quotient ranks')
        check(bond_stabilizer_matrix(hh).cols==16,'Bond map dimensions')
        brank=rational_rank(bond_stabilizer_matrix(hh))
        check(brank==16,'No short-range bond stabilizer')
        quotient_results[name]={'input_diagonal_G':cert['input_diagonal_G'],'old_obstruction':0,
           'rank_T_Q':36,'rank_augmented_Q':37,'minor_order':37,
           'minor_determinant_mod101':val,'bond_stabilizer_rank_Q':brank}
    checks['blind_hypersurface_witnesses']=quotient_results
    return {'status':'PASS','arithmetic':'exact rational / Gaussian rational / polynomial / prime field',
            'elapsed_seconds':round(time.perf_counter()-started,6),'checks':checks}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
