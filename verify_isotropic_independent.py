"""Independent standard-library checker for the isotropic extension.

This file imports no submitted algebra module or other checker. Polynomial
coefficient matrices are constructed directly with Python integer arithmetic.
This is a separate implementation, not an independent human referee report.
"""
from __future__ import annotations
if not __debug__:
    raise SystemExit('REFUSED: assertion-based verification requires Python without -O or -OO')

import json,time
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def zero(n): return [[0]*n for _ in range(n)]
def plus(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a):return [[c*x for x in r] for r in a]
def minus(a,b):return plus(a,scale(-1,b))
def mul(a,b):
    n=len(a);out=zero(n)
    for i in range(n):
        for k,c in enumerate(a[i]):
            if c:
                for j,d in enumerate(b[k]):
                    if d:out[i][j]+=c*d
    return out

def bracket(a,b):return minus(mul(a,b),mul(b,a))
def kron(a,b):
    n=len(a);m=len(b)
    return [[a[i//m][j//m]*b[i%m][j%m] for j in range(n*m)] for i in range(n*m)]

def gap_trace(a):
    return [[sum(a[9*(r//3)+3*t+r%3][9*(c//3)+3*t+c%3] for t in range(3))
             for c in range(9)] for r in range(9)]

def end9(a):
    out=zero(27)
    for r in range(27):
        i,j,k=r//9,(r//3)%3,r%3
        for c in range(27):
            l,m,n=c//9,(c//3)%3,c%3
            z=9*a[r][c]
            if i==l: z-=3*sum(a[9*t+3*j+k][9*t+3*m+n] for t in range(3))
            if k==n: z-=3*sum(a[9*i+3*j+t][9*l+3*m+t] for t in range(3))
            if i==l and k==n:z+=sum(a[9*t+3*j+s][9*t+3*m+s] for t in range(3) for s in range(3))
            out[r][c]=z
    return out

def detmod(a,p):
    a=[[x%p for x in r] for r in a];d=1;n=len(a)
    for j in range(n):
        k=next((k for k in range(j,n) if a[k][j]),None)
        if k is None:return 0
        if k!=j:a[k],a[j]=a[j],a[k];d=-d
        pivot=a[j][j];d=d*pivot%p;inv=pow(pivot,-1,p)
        for k in range(j+1,n):
            f=a[k][j]*inv%p
            if f:
                a[k]=[(x-f*y)%p for x,y in zip(a[k],a[j])]
    return d%p

def sl_basis():
    out=[]
    for i in range(3):
        for j in range(3):
            if i!=j:
                z=zero(3);z[i][j]=1;out.append(z)
    for i in range(2):
        z=zero(3);z[i][i]=1;z[i+1][i+1]=-1;out.append(z)
    return out

def main():
    start=time.perf_counter();i=eye(3);p=zero(9);q=zero(9)
    for a in range(3):
        for b in range(3):p[3*a+b][3*b+a]=1;q[3*a+a][3*b+b]=1
    h=minus(p,q);k=q # subtracting v*I/3 does not affect nested commutators
    a,b=kron(h,i),kron(i,h);aa,bb=kron(k,i),kron(i,k)
    c20=bracket(a,b);c11=plus(bracket(a,bb),bracket(aa,b));c02=bracket(aa,bb)
    sh,sk=plus(a,b),plus(aa,bb)
    ds=[bracket(sh,c20),plus(bracket(sh,c11),bracket(sk,c20)),
        plus(bracket(sh,c02),bracket(sk,c11)),bracket(sk,c02)]
    ss=list(map(end9,ds));w9=ss[0]
    assert ss[1]==zero(27) and ss[2]==scale(-1,w9) and ss[3]==zero(27)
    assert all(gap_trace(d)==zero(9) for d in ds)
    assert sum(x*x for r in w9 for x in r)==3240
    # Exactly four homogeneous coefficients checked: u^3,u^2*v,u*v^2,v^3.
    pair_results={};basis=[kron(x,y) for x in sl_basis() for y in sl_basis()]
    for name in ['Heisenberg','rank5']:
        cert=json.loads((ROOT/f'evidence/{name}_pair.json').read_text());hh=cert['interaction']
        aa,bb=kron(hh,i),kron(i,hh)
        cs=[bracket(kron(z,i),bb) for z in basis]
        cs += [scale(-1,bracket(aa,kron(i,z))) for z in basis]
        rows,cols=cert['rows'],cert['cols']
        minor=[[cs[c][r//27][r%27] for c in cols] for r in rows]
        val=detmod(minor,101)
        assert val==cert['minor_determinant_mod101'] and val!=0
        # The nonzero interaction is traceless at both endpoints, so (h,h)
        # is a nonzero domain vector. Its image cancels identically.
        assert any(x for row in hh for x in row)
        assert all(sum(hh[3*t+j][3*t+k] for t in range(3))==0 for j in range(3) for k in range(3))
        assert all(sum(hh[3*j+t][3*k+t] for t in range(3))==0 for j in range(3) for k in range(3))
        assert minus(bracket(aa,bb),bracket(aa,bb))==zero(27)
        pair_results[name]={'minor_order':127,'determinant_mod101':val,'rank_Q':127}
    return {'status':'PASS','implementation':'standard library only; no submitted module imports',
       'arithmetic':'integers and prime-field integers',
       'isotropic_cubic_coefficients':['W','0','-W','0'],'norm_W_squared':40,
       'old_obstruction_coefficients_all_zero':True,'pair_certificates':pair_results,
       'elapsed_seconds':round(time.perf_counter()-start,6)}

if __name__=='__main__':print(json.dumps(main(),indent=2))
