# Ruff formatting audit for LeetCode Python solutions

## Final result

- Formatter: Ruff 0.15.18
- Target line length: 120
- Indentation: four spaces; tabs rejected
- Optimal Python packages: 3,611
- Optimal paired files: 7,222
- Additional simplified files: 2
- Total checked and formatted: 7,224
- Remaining Ruff formatting failures: 0

## Changes

- Ruff reformatted 1,565 Optimal `solve.py` files and the simplified `solve.py` for problem 1502.
- Ruff reformatted 2,086 Optimal `leetcode_python*.py` files and the simplified native file for problem 1502.
- All 2,086 Optimal native candidates were staged before promotion. Every candidate parsed successfully, preserved the exact Python AST, used four-space indentation, contained no tabs, stayed within 120 characters, and changed only its source hash.
- The first 20 corpus-format candidates were remotely Accepted before promotion. The remaining formatting-only candidates were promoted under the user's explicit exception to the normal exact-byte resubmission rule.

## Post-format validation

- Candidate-to-canonical hashes: 2,086 checked, zero mismatches.
- Candidate-to-canonical ASTs: 2,086 checked, zero mismatches.
- Full alignment audit: 3,903 structurally aligned, 102 hash-reviewed unavoidable differences, zero review-required, 4,005 total.
- Ruff formatting check: all 7,224 files already formatted.
- Ruff indentation checks: passed.
