# Recorded benchmarks and reproduction results

**Run:** 2026-09-28T16:52:59.523065+00:00. This is a single observed run, not a performance study.

Python: 3.13.5 (main, Jul 15 2026, 20:25:40) [GCC 14.2.0]

SymPy: 1.14.0

Platform: Linux-6.18.44-x86_64-with-glibc2.41

| Suite | Wall-clock seconds, including child-process startup | Result |
|---|---:|---|
| `verify_integer.py` | 0.594 | PASS |
| `verify_symbolic.py` | 1.568 | PASS |
| `test_certifier.py` | 2.933 | PASS |
| `verify_extensions.py` | 5.029 | PASS |
| `verify_isotropic_independent.py` | 0.687 | PASS |
| `verify_dense_regression.py` | 9.945 | PASS |
| `test_field_uniform.py` | 3.866 | PASS |

**Total runner time: 24.626 seconds. All seven suites passed.**

The independent isotropic check also reports its internal computation time in
`evidence/isotropic_independent_report.json`; the runner timing includes process
startup. Inputs, exact outputs and selected minors are included. No floating-point
rank calculation occurs in any release verifier or certifier.

The quotient uses 36 real unknowns for qutrits, regardless of chain length. The
transparent redundant matrix has 1458 real-coordinate rows; the intrinsic ambient
Hermitian range-three space has dimension 576. The local pair certificates have
729 by 128 matrices and 127 by 127 selected minors. The abstract Lie-algebra pair
check inherited from version 0.1 instead has a 512 by 128 matrix.

Bit lengths, symbolic expression management, interpreter startup and hardware
all affect runtime. These measurements do not imply constant bit complexity or
predict runtime for large-denominator user inputs. Before the recorded final run,
exact expansion replaced unnecessary simplification in the legacy certifier;
the checked theorem and outcomes are unchanged.

## Clean archive reproduction

After building the archive, all 52 then-listed SHA-256 entries passed in a fresh
extraction, and all seven suites passed again in 26.170725 seconds. The actual
second-run report is `evidence/clean_reproduction_report.json`. Adding that
report and these references does not change any mathematical input or program.
