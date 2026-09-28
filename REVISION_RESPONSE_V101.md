# Response to the supplied v1 review

28 September 2026; version 1.0.1-candidate. Main theorems unchanged.

1. **Closest predecessor.** Added a theorem-to-theorem comparison in the introduction. Shiraishi–Yamaguchi already use symmetry to constrain the correction. The extension here averages affine local equations including unknown fields, not a conserved quantity under a symmetry-breaking Hamiltonian.
2. **Separate completeness claims.** Retained quotient consistency as almost-conservation only, field-existence classification for the spin-1 isotropic family, and range-bounded residual commutant as separate statements. Almost-conservation explicitly concerns support, not a small norm.
3. **Portable witnesses.** Added optional `--witness`, exporting a sparse rational dual functional or rational consistency vector. `portable_witness.py` checks reconstructed equations by multiplication without rank computation and requires a separate intended input. It shares matrix assembly and is not independently implemented. Ordinary output now says exact recomputation. Witnesses do not certify the entire proof or residual commutant.
4. **External reduction.** Preserved the explicit mapping of boundary injectivity and the pair kernel to Hokkyo v3 equations (4),(6) and Theorems 1,2; arbitrary site fields and range limits remain explicit.
5. **Citation metadata.** Publisher and arXiv HTML v4 identify Mizuki Yamaguchi in Hokkyo–Yamaguchi–Chiba; the arXiv abstract metadata displays Sanatani. The manuscript now follows publisher/full-text metadata. The discrepancy is documented, not interpreted biographically.
6. **Terminology.** Replaced parameter rays by lines and ambiguous positive lines by charge-admitting lines. Both signs are included. Added the Hermitian physical-current convention i C_N.
7. **Worked example.** Existing AKLT and the two non-isotropic blind-family examples provide explicit before/after obstruction comparisons; no additional research sweep was commissioned.
8. **Verification safety.** Assertion-based legacy suites now refuse -O/-OO. New portable checker uses explicit failure branches. Added witness corruption controls and pinned clean-extraction replay.

## Review provenance boundary

The user supplied the review text. Its claimed separate computations are reported evidence, not independently authenticated review. The mentioned sandbox reviewer-check ZIP was not among supplied files and was not found by the targeted local filename check; it is not represented as inspected or replayed. The original package's separate integer implementation was replayed as producer-side implementation diversity. The review's indicative REF grade is not an official assessment and is not used as a public quality badge.
