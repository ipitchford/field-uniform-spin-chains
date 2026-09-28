#!/usr/bin/env python3
"""Run all release checks and record actual outputs, timings and environment.

Run on the untouched archive after checking SHA256SUMS.txt. Generated report
and certificate timestamps/timings may differ on a later run; this is expected.
"""
from __future__ import annotations
if not __debug__:
    raise SystemExit('REFUSED: assertion-based verification requires Python without -O or -OO')

import hashlib,json,platform,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
import sympy

ROOT=Path(__file__).resolve().parent
SUITES=[
 ('verify_integer.py','integer_report.json'),
 ('verify_symbolic.py','symbolic_report.json'),
 ('test_certifier.py','legacy_certifier_report.json'),
 ('verify_extensions.py','extensions_report.json'),
 ('verify_isotropic_independent.py','isotropic_independent_report.json'),
 ('verify_dense_regression.py','dense_regression_report.json'),
 ('test_field_uniform.py','new_certifier_report.json'),
 ('test_portable_witness.py','portable_witness_report.json')]

def main() -> int:
    began=time.perf_counter();reports=[]
    for script,outfile in SUITES:
        start=time.perf_counter()
        p=subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,capture_output=True,text=True,timeout=180)
        elapsed=time.perf_counter()-start
        try:data=json.loads(p.stdout)
        except json.JSONDecodeError:data={'status':'FAIL','stdout':p.stdout}
        ok=p.returncode==0 and data.get('status')=='PASS'
        data['runner_elapsed_seconds']=round(elapsed,6)
        if p.stderr:data['stderr']=p.stderr
        (ROOT/'evidence'/outfile).write_text(json.dumps(data,indent=2)+'\n')
        reports.append({'suite':script,'status':'PASS' if ok else 'FAIL','returncode':p.returncode,
                        'elapsed_seconds':round(elapsed,6),'report':'evidence/'+outfile})
        print(f'{script}: {reports[-1]["status"]} ({elapsed:.3f} s)',flush=True)
        if not ok:break
    passed=len(reports)==len(SUITES) and all(x['status']=='PASS' for x in reports)
    report={'status':'PASS' if passed else 'FAIL','date_utc':datetime.now(timezone.utc).isoformat(),
       'environment':{'python':sys.version,'sympy':sympy.__version__,'platform':platform.platform()},
       'suites':reports,'suite_count':len(reports),'total_elapsed_seconds':round(time.perf_counter()-began,6),
       'assurance':'Exact finite algebra and regression checks; not formal proof verification or independent specialist review.'}
    (ROOT/'evidence/verification_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return 0 if passed else 1

if __name__=='__main__':raise SystemExit(main())
