# Response to the version-0.1 referee report

**Revised manuscript:** *Field-uniform nonintegrability of spin chains*, v1.0.
**Date:** 28 September 2026.

The supplied report recommended minor revisions and assessed the earlier output
as strong 3* overall, with 4*-level rigour. This response records revisions and
new research. It does not extend that report's assessment to the new theorems.

## 4.1 — Reshetikhin positioning: addressed

Section 1.2 now distinguishes the full identity `D=X23-X12`, its full
endpoint-traceless projection `Delta`, the partial trace `O`, and actual local
conservation. It explicitly gives the implication from the full identity to
both projections and an exact counterexample to the converse from `O=0`.
Hokkyo's 2026 conservation-law result and Sanatani–Shiraishi–Ishii's July 2026
sufficiency theorem are now cited and delimited. The latter's diagonalisability
hypothesis is stated. Neither is silently substituted for the actual all-range
dependency, Hokkyo's revised 2025 Theorems 1 and 2.

## 4.2 — Isotropic blind spot: addressed and extended

The paper retains, explains and exactly checks `O(h(u,v))=0`, including full-rank
isotropic interactions. The AKLT regression gives determinant `125/6561` and
old obstruction zero. It also reproduces the full obstruction norm `2560/81`.

New research in Sections 3–5 addresses this limitation rather than suppressing
it. The field-eliminated quotient is exact for the three-site almost-conservation
test. A multiplicity-free symmetry theorem evaluates the quotient as the full
endpoint-traceless obstruction. It gives

    Delta(h(u,v)) = u*(u-v)*(u+v)*W,    ||W||_F^2 = 40.

Both rank-deficient rays are now closed by independently reconstructed exact
127-minors, so the arbitrary-field exclusion covers every nonzero interaction
with `u*(u-v)*(u+v) != 0`, without a residual full-rank proviso. On the other
three rays, zero fields give a conserved three-site current. Section 5 also
classifies every residual local charge as identity, energy and uniform spin
components commuting with each field.

This is a classification of **whether some field choice can admit a charge**,
not of every field choice on the three positive rays. The earlier field-free
classification is credited, not presented as new.

## 4.3 — Quasicentroid attribution: addressed

Section 2 attributes the scalarity mechanism to established quasicentroid and
centroid theory, with Leger–Luks cited through the inspected formulation in
Andruszkiewicz–Brzeziński–Radziszewski, p. 8. Appendix A retains the self-contained
matrix-unit proof and identifies the present use in the leading-charge equations.
No priority claim is made for the abstract scalarity lemma.

## Minor comments

**Author correction.** The bibliography and source audit now use Naoto Shiraishi
and Mizuki Yamaguchi for the published isotropic dichotomy. The publisher record
and arXiv HTML v4 agree; the differing arXiv abstract metadata is recorded rather
than silently reconciled.

**Coefficient terminology.** Section 6.1 explicitly distinguishes a real
skew-symmetric coefficient matrix from the Hermitian, exchange-odd tensor
operator that it represents.

**Measurable algorithmic claims.** The old unqualified “inexpensive” language has
been replaced by fixed local matrix sizes, explicit rational bit-length limits
on the complexity claim, and measured timings in `BENCHMARKS.md`. Both public
certifiers give calibrated inconclusive results. Exact expansion of the old
certifier's finite commutators replaces unnecessary symbolic simplification;
this preserves its checks and improves reproducibility time.

**Regression strengthening.** The new dense regression compares the
structure-constant contraction against direct nested commutators on three
fully dense rational inputs. It handles Gram normalisation algebraically.
Three independent qubit matrices and the full isotropic family are negative
controls for the old gap projection. The three isotropic positive rays are
checked against the full telescoping identity, not merely zero projection.

**Licence and archive metadata.** The software has an explicit MIT licence.
Release and citation metadata, proof-dependency and claim ledgers, and a checksum
manifest are included. No persistent archive identifier has yet been assigned:
creating local files cannot mint a DOI or establish an external repository
deposit. This administrative requirement is recorded as pending actual archival
deposit, not falsely marked completed.

## Additional coverage beyond the required revisions

Section 7 gives exact 37-minors on each irreducible hypersurface
`j3=3*j8` and `j4*j5=j6*j7` in the eight-parameter diagonal-G family. Their
nonzero residues prove that the new quotient is nontrivial relatively generically
on each component that the old obstruction entirely misses. A strengthened
short-charge lemma permits abelian degenerate eigenspaces of `J^2`, so even the
forced two-dimensional Cartan degeneracy on the first component does not prevent
classification of the full local commutant.

These results strengthen the originality and significance case with actual new
coverage. More checks alone would not have answered the report's 4* concern.
A fresh specialist assessment must decide the revised output's quality.

## Assurance carried forward, and assurance not carried forward

The original report is retained as supplied. Its independent reviewer code was
not provided as a mounted bundle in this turn and has not been represented as
rerun here. All new calculations were reconstructed in the current environment.
The independent integer implementation is separate code within this work, not
an independent human or separately commissioned referee. No proof assistant
has formally verified the complete argument.

The new quotient equivalence, its field quantifiers, the symmetry-averaging
argument and the sharp isotropic field-existence theorem are the principal
load-bearing additions for a fresh review. Their proofs, finite certificates,
negative controls and explicit limits are all included.
