#!/usr/bin/env python3
"""Fail-closed publication controls, also safe under -O and -OO."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def check_manifest(root=ROOT):
    lines=(root/'SHA256SUMS.txt').read_text().splitlines()
    for line in lines:
        digest,name=line.split('  ',1)
        p=root/name
        if hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
            raise ValueError('Hash mismatch: '+name)
    return len(lines)

def main():
    scripts=['verify.py','verify_integer.py','verify_symbolic.py','test_certifier.py',
             'verify_extensions.py','verify_isotropic_independent.py','verify_dense_regression.py','test_field_uniform.py']
    for flag in ['-O','-OO']:
        for script in scripts:
            p=subprocess.run([sys.executable,flag,'-B',str(ROOT/script)],capture_output=True,text=True)
            if p.returncode==0 or 'REFUSED:' not in p.stderr+p.stdout:
                raise RuntimeError('Unsafe optimization handling: '+script)
    # Independent of assertions: exercise the portable verifier against retained witnesses.
    from portable_witness import verify
    for name in ['AKLT','blind_cartan','blind_product','charge_line']:
        w=json.loads((ROOT/'evidence'/f'{name}_witness.json').read_text())
        verify(w,w['input'])
        bad=dict(w);bad['inputSha256']='0'*64
        try:verify(bad,w['input'])
        except ValueError:pass
        else:raise RuntimeError('Input-binding tamper accepted')
    print(json.dumps({'status':'PASS','optimization_refusals':16,'witness_replays':4,'binding_negative_controls':4,
                      'optimized_meaning':'Legacy tests refuse; multiplication-based witness verifier remains active.'}))
if __name__=='__main__':main()
