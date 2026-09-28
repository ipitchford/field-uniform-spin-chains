# AI index — field-uniform spin chains

## Identity and status

Anonymous; version 1.0.1-candidate, 28 September 2026. Unrefereed candidate. See [citation](CITATION.cff), [status](RELEASE_METADATA.json), [provenance](PROVENANCE.md) and [assurance](ASSURANCE.md). This index is navigation, not proof certification.

## Exact claims and safe scope

1. **Quotient equivalence:** [paper.tex](paper.tex), Theorem labelled `thm:quotient`. A fixed Hermitian swap-symmetric nearest-neighbour interaction with zero one-site partial traces must be leading-rigid. Vanishing of U(h) is equivalent to existence of a three-site candidate with commutator range at most two, for a suitable uniform field. U(h) != 0 excludes exact contiguous charge ranges 3 <= k <= floor(N/2) for every periodic N >= 6 and every site-dependent Hermitian field. No field-norm bound. This is not a complete general integrability criterion.
2. **Multiplicity-free reduction:** `sec:symmetry`. Irreducible compact-group symmetry and multiplicity-free tensor square give U(h)=Delta(h). Actual on-site fields need not preserve symmetry.
3. **Sharp BLBQ field-existence criterion:** `thm:blbq`. For spin 1, h=uB+v(B²−4I/3), Delta=u(u−v)(u+v)W with ||W||²=40. Nonzero factor excludes all specified charges uniformly in fields; on the three nonzero parameter lines u=0,u=v,u=−v, zero fields admit a conserved three-site current. No classification of all individual fields on those lines.
4. **Residual commutant:** `thm:isocommutant`; off those lines, span{I,H} plus uniform spin generators commuting with each field, only within the range bound.
5. **Generic and blind-locus results:** `thm:generic`, `thm:blind`; d>=3 open dense full-measure interaction family, plus relatively generic subsets of two specified eight-parameter diagonal hypersurfaces. Not the entire rank-deficient or quotient-zero class.

The detailed [claim ledger](evidence/claim_ledger.json) retains assumptions and exclusions. No claim implies thermalisation or absence of quasilocal conservation.

## Dependencies and semantic bridge

Hokkyo arXiv:2501.18400v3 Theorems 1,2 supply the all-range reduction. The paper maps endpoint injectivity and local pair rigidity to its hypotheses. The quasicentroid argument supplies full-rank rigidity; exact 127-minors plus a known kernel cover the two necessary deficient BLBQ lines. See [source audit](CITATION_AUDIT.md) and [historical sources](evidence/source_audit.md). Shiraishi–Yamaguchi's symmetry argument is antecedent, not a new discovery here.

## Evidence and reproduction

Install [requirements.txt](requirements.txt) in Python 3.13. Check [SHA256SUMS.txt](SHA256SUMS.txt) before replay, then run `python -B verify.py`. The eight suites take roughly half a minute in the recorded local environment; no cross-machine guarantee. A replay regenerates reports, so check hashes before running.

- [verify.py](verify.py): all finite suites.
- [verify_isotropic_independent.py](verify_isotropic_independent.py): standard-library-only independent-in-code isotropic construction; producer-coordinated, not externally independent.
- [verify_extensions.py](verify_extensions.py): symbolic identity, rank-deficient and blind-family minors.
- [certify_field_uniform.py](certify_field_uniform.py): exact rational input; outputs computation report. `python certify_field_uniform.py evidence/AKLT_input.json --witness result.json` exports a portable quotient identity.
- [portable_witness.py](portable_witness.py): `python portable_witness.py result.json evidence/AKLT_input.json`; exact multiplication, no rank computation. Shared matrix construction is a trust dependency.
- [test_portable_witness.py](test_portable_witness.py): four valid examples and sixteen corruptions.
- [publication_controls.py](publication_controls.py): sixteen optimization refusals plus retained-witness and binding checks; works under -OO.
- [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md): fresh replay and frozen archive boundaries.

A valid dual identity proves Delta is outside im T; it does not independently certify leading rigidity, the semantic bridge, or the residual-commutant claim. A valid consistency vector establishes only almost-conservation. Float/nonfinite/asymmetric input is rejected; an inconclusive output is not evidence of integrability.

## Reuse, correction and licensing

Original prose/data CC0-1.0, original code MIT, third-party exceptions in [LICENSES.md](LICENSES.md). The [revision response](REVISION_RESPONSE_V101.md) lists review actions. Reuse the immutable tag and DOI from CITATION.cff; report objections against exact versions. Universal proofs remain unformalised, review independence unestablished, and novelty search bounded. Future work: independent audit, formalisation, multiplicity-bearing symmetry and further deficient families—not an implied result of this release.
