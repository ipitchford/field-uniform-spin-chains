"""Positive, negative and invalid-input controls for the stronger certifier."""
from __future__ import annotations
if not __debug__:
    raise SystemExit('REFUSED: assertion-based verification requires Python without -O or -OO')

import json
from pathlib import Path
from certify_field_uniform import certify

def diagonal(v):return {'coefficients':[[v[i] if i==j else 0 for j in range(8)] for i in range(8)]}

def run():
    cases={
      'original_witness':(diagonal(list(range(1,9))),'CERTIFIED_LOCAL_COMMUTANT_I_H'),
      'blind_cartan':(diagonal([1,2,24,4,5,6,7,8]),'CERTIFIED_LOCAL_COMMUTANT_I_H'),
      'blind_product':(diagonal([1,2,3,4,15,5,12,8]),'CERTIFIED_LOCAL_COMMUTANT_I_H'),
      'scalar_J':(diagonal(['1/2']*7+['1/6']),'INCONCLUSIVE'),
      'rank_deficient_general':(diagonal([0,2,3,4,5,6,7,8]),'INCONCLUSIVE'),
      'AKLT':({'kind':'blbq','u':1,'v':'1/3'},'CERTIFIED_NO_LOCAL_CHARGES_3_TO_HALF'),
      'Heisenberg':({'kind':'blbq','u':1,'v':0},'CERTIFIED_NO_LOCAL_CHARGES_3_TO_HALF'),
      'rank5':({'kind':'blbq','u':1,'v':2},'CERTIFIED_NO_LOCAL_CHARGES_3_TO_HALF'),
      'pure_biquadratic':({'kind':'blbq','u':0,'v':1},'ZERO_FIELD_THREE_SITE_CHARGE_EXISTS'),
      'ULS':({'kind':'blbq','u':1,'v':1},'ZERO_FIELD_THREE_SITE_CHARGE_EXISTS'),
      'TB':({'kind':'blbq','u':1,'v':-1},'ZERO_FIELD_THREE_SITE_CHARGE_EXISTS'),
      'zero':({'kind':'blbq','u':0,'v':0},'ZERO_INTERACTION')}
    out={}
    root=Path(__file__).resolve().parent/'evidence'
    for name,(data,status) in cases.items():
        ans=certify(data);assert ans['status']==status,(name,ans)
        out[name]=ans
        if name in ['blind_cartan','blind_product','AKLT','Heisenberg','rank5']:
            (root/f'{name}_input.json').write_text(json.dumps(data,indent=2)+'\n')
            (root/f'{name}_certificate.json').write_text(json.dumps(ans,indent=2)+'\n')
    bads=[{'kind':'blbq','u':1.0,'v':0},{'kind':'blbq','u':True,'v':0},
          {'kind':'blbq','u':'1/0','v':0},{'coefficients':[]},
          {'coefficients':[[1 if i<=j else 0 for j in range(8)] for i in range(8)]}]
    for bad in bads:
        try:certify(bad)
        except ValueError:pass
        else:raise AssertionError('Invalid input accepted')
    return {'status':'PASS','positive_and_inconclusive_cases':out,'invalid_cases_rejected':len(bads)}

if __name__=='__main__':print(json.dumps(run(),indent=2))
