#!/usr/bin/env python3
"""Certify field-uniform absence of strictly local charges using exact algebra.

Input JSON either has an 8x8 symmetric `coefficients` array in the manuscript's
unnormalised G basis, or {"kind":"blbq", "u":..., "v":...}. Values must be
integers or rational strings. No on-site fields need be supplied: exclusion is
uniform over all Hermitian fields. INCONCLUSIVE never means integrable.
"""
from __future__ import annotations
import argparse,json,sys,time
from pathlib import Path
import sympy as sp
from spin1_algebra import (from_coefficients,local_data,quotient_matrix,
        rational_rank,bond_stabilizer_matrix,hilbert_schmidt_squared)


def rational(x: object) -> sp.Rational:
    if isinstance(x,bool) or not isinstance(x,(int,str)):
        raise ValueError('Use integers or rational strings; floats are rejected.')
    try:y=sp.Rational(x)
    except (ValueError,TypeError,ZeroDivisionError) as exc:
        raise ValueError(f'Invalid rational: {x!r}') from exc
    if y.is_finite is not True:raise ValueError('Rationals must be finite.')
    return y


def certify(data: dict) -> dict:
    started=time.perf_counter()
    common={'evidence_kind':'exact recomputation report; optional portable witness proves only the quotient identity',
            'range':'3 <= k <= floor(N/2), every periodic N >= 6',
            'fields':'arbitrary site-dependent Hermitian on-site potentials, with no norm bound',
            'arithmetic':'exact rational','dependency':'Hokkyo arXiv:2501.18400v3, Theorems 1 and 2, with hypotheses proved in the manuscript'}
    if data.get('kind')=='blbq':
        u,v=rational(data.get('u')),rational(data.get('v'));factor=u*(u-v)*(u+v)
        out={**common,'u':str(u),'v':str(v),'isotropic_factor':str(factor),
             'Delta_norm_squared':str(40*factor**2)}
        if factor!=0:
            out.update(status='CERTIFIED_NO_LOCAL_CHARGES_3_TO_HALF',
                local_commutant='span{I,H} plus uniform total-spin generators commuting with every on-site field')
        elif u!=0 or v!=0:
            out.update(status='ZERO_FIELD_THREE_SITE_CHARGE_EXISTS',
                statement='At zero fields the nonzero charge sum_i [h_i,h_{i+1}] is conserved. This does not classify arbitrary fields on this line.')
        else:
            out.update(status='ZERO_INTERACTION',statement='The interaction vanishes; the exclusion theorem does not apply.')
    else:
        raw=data.get('coefficients')
        if not isinstance(raw,list) or len(raw)!=8 or any(not isinstance(r,list) or len(r)!=8 for r in raw):
            raise ValueError("Expected an 8x8 'coefficients' array or kind='blbq'.")
        m=sp.Matrix([[rational(x) for x in row] for row in raw])
        if m!=m.T:raise ValueError('Coefficient matrix must be symmetric.')
        det=sp.factor((m*sp.diag(2,2,2,2,2,2,2,6)).det())
        out={**common,'determinant_J':str(det)}
        if det==0:
            out.update(status='INCONCLUSIVE',reason='Automatic leading-rigidity hypotheses require full rank. Use kind=blbq for the separately certified rank-deficient isotropic lines.')
        else:
            h=from_coefficients(m);*_,delta,old=local_data(h)
            out['old_gap_norm_squared']=str(hilbert_schmidt_squared(old))
            if old!=sp.zeros(9):
                excluded=True;out['route']='identity-middle-site projection'
            else:
                t,d=quotient_matrix(h);rt=rational_rank(t);ra=rational_rank(t.row_join(d))
                excluded=ra>rt
                out.update(route='field-eliminated three-site quotient',rank_T=rt,rank_augmented=ra)
            if excluded:
                br=rational_rank(bond_stabilizer_matrix(h))
                out['bond_stabilizer_rank']=br
                out['status']='CERTIFIED_LOCAL_COMMUTANT_I_H' if br==16 else 'CERTIFIED_NO_LOCAL_CHARGES_3_TO_HALF'
                out['statement']='Exclusion holds for every chain length and all fields in the stated range.'
            else:
                out.update(status='INCONCLUSIVE',reason='A uniform-field almost-conserved three-site candidate exists. Exact local conservation and integrability are not decided.')
    out['elapsed_seconds']=round(time.perf_counter()-started,6)
    return out


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--witness', type=Path, help='Export exact quotient dual or consistency vector; does not certify other proof obligations')
    args=parser.parse_args()
    try:
        data=json.loads(args.input.read_text())
        if not isinstance(data,dict):raise ValueError('Input must be a JSON object.')
        result=certify(data)
        if args.witness:
            from portable_witness import generate
            witness=generate(data)
            args.witness.write_text(json.dumps(witness,indent=2)+'\n')
            result['portable_witness']={'path':str(args.witness),'kind':witness['kind'],'scope':witness['scope']}
        print(json.dumps(result,indent=2))
    except (OSError,ValueError,TypeError) as exc:
        print(json.dumps({'status':'INVALID_INPUT','error':str(exc)}),file=sys.stderr)
        return 2
    return 0

if __name__=='__main__':raise SystemExit(main())
