#!/usr/bin/env python3
"""Positive and tamper controls for portable exact quotient witnesses."""
import copy
import json
from pathlib import Path
from portable_witness import generate, verify

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def reject(w, data):
    try:
        verify(w, data)
    except (ValueError, TypeError):
        return
    raise RuntimeError('Tampered witness accepted')

def main():
    root = Path(__file__).resolve().parent
    cases = [('AKLT', {'kind':'blbq','u':1,'v':'1/3'}, 'inconsistent'),
             ('charge_line', {'kind':'blbq','u':1,'v':1}, 'consistent')]
    for name in ['blind_cartan', 'blind_product']:
        cases.append((name, json.loads((root/'evidence'/f'{name}_input.json').read_text()), 'inconsistent'))
    controls = 0
    for name, data, expected in cases:
        w = generate(data)
        require(w['kind'] == expected, 'Wrong consistency class')
        verify(w, data)
        (root/'evidence'/f'{name}_witness.json').write_text(json.dumps(w, indent=2)+'\n')
        bad = copy.deepcopy(w)
        field = 'weights' if expected == 'inconsistent' else 'coefficients'
        bad[field][0] = str(int(0)+999)
        reject(bad, data)
        bad = copy.deepcopy(w); bad['inputSha256'] = '0'*64; reject(bad, data)
        bad = copy.deepcopy(w); bad['coordinates'] = 'wrong'; reject(bad, data)
        bad = copy.deepcopy(w); bad[field] = bad[field][:-1]; reject(bad, data)
        controls += 4
    print(json.dumps({'status':'PASS','cases':len(cases),'semantic_negative_controls':controls,
                     'scope':'Quotient identities and tamper rejection; not universal theorem verification'}))

if __name__ == '__main__':
    main()
