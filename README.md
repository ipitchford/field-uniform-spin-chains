# Field-uniform nonintegrability of spin chains

**Evidence Press — version 1.0.1-candidate — 28 September 2026**

The main manuscript is `paper.pdf`; its editable source is `paper.tex`. This
release supersedes *A field-independent cubic obstruction to local conservation
in general spin-1 chains*, version 0.1. The supplied referee report concerns that
earlier version, not the new theorems.

## Candidate results

For a leading-rigid, Hermitian, swap-symmetric nearest-neighbour interaction,
an exact local quotient eliminates all on-site fields and two-site corrections
from the three-site almost-conservation test. For qutrits it has 36 real
unknowns. A nonzero residual excludes every conserved quantity of exact
contiguous range 3 through floor(N/2), for every periodic N >= 6 and every
site-dependent Hermitian field. Full traceless interaction rank automatically
supplies the leading-rigidity hypotheses.

A multiplicity-free symmetry theorem makes this quotient equal to the full
three-site obstruction for invariant interactions. Applied to the complete
spin-1 bilinear–biquadratic family

    h(u,v) = u B + v (B^2 - 4I/3),  B = Sx⊗Sx + Sy⊗Sy + Sz⊗Sz,

it gives the exact factor `u*(u-v)*(u+v)`. No choice of fields admits the stated
higher-range charges when that factor is nonzero. On its three zero lines,
zero fields admit a nonzero conserved three-site current. Both rank-deficient
lines required in the proof have exact rank certificates. Outside the three
charge-admitting lines, the entire local commutant is identity, energy and the uniform
spin generators commuting with every field.

The quotient also certifies generic exclusion on each of the two blind
hypersurfaces of the earlier eight-parameter diagonal family. The unrestricted
generic theorem, explicit cubic witness, perturbation ball and all-dimension
extension from version 0.1 are retained.

## Reproduce

Python 3.13.5 and SymPy 1.14.0 were used for the recorded run. The code requires
modern Python (3.10 or later) and the pinned dependency; other Python versions
have not been run in this release environment.

```sh
python -m pip install -r requirements.txt
python verify.py
python certify_field_uniform.py evidence/AKLT_input.json
python certify_field_uniform.py evidence/blind_cartan_input.json
```

`verify_isotropic_independent.py` and `verify_integer.py` require only the Python
standard library. The new independent integer checker imports none of the other
submitted modules. It constructs all four homogeneous cubic coefficient
matrices and verifies both rank-deficient pair minors.

The original seven-suite clean run is historical. The publication revision has eight suites; fresh exact-version replay is recorded in the separate release REPLAY_RECEIPT.json asset. `evidence/verification_report.json` records
the actual results and environment; `BENCHMARKS.md` gives the timings. No
floating-point rank threshold is used. Nonzero modular minors establish lower
bounds over characteristic zero; known kernel vectors establish the complementary
upper bounds for the two 127-dimensional pair ranks.

The general input is an 8×8 symmetric `coefficients` array in the unnormalised G
basis in the paper. Values must be integers or rational strings. The separate
`{"kind":"blbq","u":1,"v":"1/3"}` input invokes the complete isotropic-family
theorem, including rank-deficient cases. Invalid inputs are rejected.

## Navigation

| File or directory | Purpose |
|---|---|
| `paper.pdf`, `paper.tex` | Final manuscript and editable source |
| `review/response_to_referee.md` | Point-by-point action on the supplied review |
| `review/referee_report_v0_1.txt` | Supplied earlier report, retained without rewriting |
| `evidence/claim_ledger.json` | Precise theorem claims, dependencies and limits |
| `evidence/source_audit.md` | Inspected sources, literature boundary and metadata correction |
| `evidence/*_pair.json` | Exact rank-deficient local pair certificates |
| `evidence/gapzero_*_minor.json` | New augmented rank certificates on the old blind locus |
| `evidence/isotropic_W.json` | Exact 27×27 rational isotropic obstruction |
| `certify_field_uniform.py` | Stronger field-uniform certifier |
| `certify_interaction.py` | Compatibility implementation of the old cubic quick test |
| `verify.py` | Reproduction runner for eight suites |
| `RELEASE_METADATA.json` | Release status, no invented archive identifier |
| `SHA256SUMS.txt` | Integrity manifest for the final bundle |

Check the checksum manifest before reproducing the calculations:

```sh
sha256sum -c SHA256SUMS.txt
```

A rerun regenerates timing-bearing reports and example certificates. Those
regenerated files can differ in timing fields, so checksum differences after a
rerun are not evidence of a changed mathematical result. Code and certificate
inputs remain fixed.

## Boundaries

The quotient is complete for an **almost-conservation** test, not an integrability
classification. A vanishing quotient is reported as inconclusive for actual
conserved quantities. The complete isotropic result classifies **existence of a
field choice**, not every field configuration on the three charge-admitting lines.
General rank-deficient qutrit interactions and the full exceptional locus are
not classified. Theorems do not imply thermalisation, chaotic level statistics,
absence of quasilocal tails, or exclusion beyond the stated range.

The all-range implication depends on Hokkyo, arXiv:2501.18400v3, Theorems 1 and 2.
The present work proves their interaction hypotheses and the remaining local
obstructions. Exact computations are not formal proof verification. The new
results have not received a fresh independent specialist review, and the limited
literature search does not certify historical priority. No REF grade is asserted
for this revised manuscript.

Scholarly creator: Anonymous. Original prose/data CC0-1.0 and original code MIT, with third-party exceptions in LICENSES.md. Version DOI: https://doi.org/10.5281/zenodo.23021227. Provider publication is confirmed by public readback, not merely this metadata.

## Publication revision

[AI_INDEX.md](AI_INDEX.md) is the claim-level agent entry point. [REVISION_RESPONSE_V101.md](REVISION_RESPONSE_V101.md) records review actions. Optional portable quotient witness:

```sh
python certify_field_uniform.py evidence/AKLT_input.json --witness result.json
python portable_witness.py result.json evidence/AKLT_input.json
python -OO -B publication_controls.py
```

The default certifier returns an exact-computation report. The portable witness verifies a finite linear identity, not the all-range theorem or general integrability. Assertion-based legacy suites explicitly refuse optimized Python. The supplied historical review and generated computation reports are not external human peer review.
