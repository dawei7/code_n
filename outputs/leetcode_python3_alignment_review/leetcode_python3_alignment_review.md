# Reassessment of the 20 recovered `leetcode_python3.py` sources

## Outcome

- Reassessed all 20 recovered sources for readability and algorithm quality rather than merely for structural mismatch.
- Retained 2 readable recovered sources (2086 and 3551) and aligned their app-local `solve.py` bodies to the existing Accepted implementations.
- Staged, tested, remotely submitted, and promoted 18 readable replacements. Every promoted native file is byte-for-byte identical to the candidate that LeetCode accepted.
- Problem 3549 now uses separate forward transforms and one inverse transform instead of the packed-complex shortcut.
- Problems 3553, 3559, and 3562 no longer contain compressed dynamic `exec` payloads.
- All 40 paired files pass Ruff with the 120-character configuration.

## Per-problem decision

| ID | Decision | Accepted submission | Reason and final implementation |
|---:|---|---:|---|
| 2086 | Retained recovered source | 2073066821 | Recovered source is readable: the street is copied and placed buckets are marked explicitly. `solve.py` was aligned to that already-Accepted implementation. |
| 3548 | Replaced | 2089300244 | Recovered source was heavily minified. Promoted the readable four-orientation prefix-sum implementation from the app source. |
| 3549 | Replaced and redesigned | 2089300333 | Recovered source was minified and used a packed-complex FFT identity. Promoted a standard, readable two-forward-plus-one-inverse FFT with the same required complexity. |
| 3551 | Retained recovered source | 2082959802 | Recovered swap-cycle implementation was already compact and readable. `solve.py` was aligned to its Accepted body. |
| 3552 | Replaced | 2089300447 | Recovered 0-1 BFS was heavily minified. Promoted the readable portal-indexing and deque implementation. |
| 3553 | Replaced | 2089300578 | Recovered source hid the entire algorithm in a compressed `exec` payload. Promoted the visible binary-lifting, LCA, and tree-distance implementation. |
| 3555 | Replaced | 2089300687 | Recovered sliding-window boundary expansion was heavily minified. Promoted the readable implementation with explicit window and core-extrema concepts. |
| 3556 | Replaced | 2089300796 | Recovered substring/primality implementation was heavily minified. Promoted the readable equivalent. |
| 3557 | Replaced | 2089300894 | Recovered greedy implementation was heavily minified. Promoted the readable first-position/reset implementation. |
| 3558 | Replaced | 2089300987 | Recovered depth traversal was heavily minified. Promoted the readable adjacency/stack implementation. |
| 3559 | Replaced | 2089301097 | Recovered source hid the algorithm in a compressed `exec` payload. Promoted the visible binary-lifting and distance implementation. |
| 3562 | Replaced | 2089301203 | Recovered source hid the algorithm in a compressed `exec` payload. Promoted the visible tree-knapsack implementation. |
| 3563 | Replaced | 2089301329 | Recovered interval DP was heavily minified. Promoted the readable removable-interval implementation. |
| 3565 | Replaced | 2089301490 | Recovered backtracking search was heavily minified. Promoted the readable checkpoint/path implementation. |
| 3566 | Replaced | 2089301574 | Recovered subset-product search was heavily minified. Promoted the readable product precheck and DFS. |
| 3567 | Replaced | 2089301675 | Recovered sliding-submatrix enumeration was heavily minified. Promoted the readable set/sort/gap implementation. |
| 3568 | Replaced | 2089301754 | Recovered BFS used a compact padded and flattened representation. Promoted the clearer coordinate, mask, energy, and deque representation. |
| 3569 | Replaced | 2089301861 | Recovered sieve, heap, and segment-tree implementation was highly compressed. Promoted the implementation with named algorithmic concepts and explicit input-copy semantics. |
| 3571 | Replaced | 2089302000 | Recovered KMP overlap implementation was heavily minified. Promoted the named containment-and-overlap helper. |
| 3572 | Replaced | 2089302078 | Recovered implementation was minified. Promoted the readable best-per-x scan using conventional `xi` and `yi` notation. |

## Verification

- Exact candidate-to-canonical SHA-256 comparison: 18/18 matched after promotion.
- Candidate checks before submission: 160 authored cases, 54 benchmark cases, structural alignment, Ruff, and indentation checks.
- Additional 3549 checks: 300 randomized differential cases and a legal 50,000-by-50,000 coefficient stress case.
- Additional 3572 checks: 500 randomized differential cases.
- Canonical post-promotion checks: both app and native forms passed 176 authored cases and 60 benchmark cases each.
- Focused regression tests: 22 passed; alignment-audit tests: 9 passed.
- Full corpus audit: 3,903 structurally aligned, 102 hash-reviewed unavoidable differences, zero review-required, 4,005 total.

## Corpus-wide Ruff snapshot

- Optimal Python pairs: 3,611 (7,222 files), plus the 2-file simplified branch for problem 1502.
- App-local files reformatted in the authorized bulk pass: 1,565 Optimal files plus 1 simplified file.
- Native files reformatted in the authorized bulk pass: 2,086 Optimal files plus 1 simplified file.
- All 7,224 LeetCode Python solution files pass Ruff with the 120-character configuration.
- The first 20 corpus-format candidates were submitted, Accepted, and promoted with new submission evidence. The remaining formatting-only changes were promoted under the user's explicit exception to the usual exact-byte resubmission rule after every candidate passed AST-identity, syntax, indentation, line-length, and hash checks.
