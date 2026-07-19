## General
**View the string as equal-character runs**

For example, `0011100` has run lengths `2, 3, 2`. A qualifying substring must cross exactly one boundary between adjacent runs: its left half is a suffix of one run and its right half is an equally long prefix of the next.

**Count what each boundary contributes**

If consecutive runs have lengths $a$ and $b$, the common half-length can be any integer from $1$ through $\min(a,b)$. That boundary therefore contributes $\min(a,b)$ distinct substrings.

**Maintain only two run lengths**

Scan from left to right with `current_run` and `previous_run`. When the character changes, the completed pair contributes `min(previous_run, current_run)`; then shift the current length into the previous slot and begin a new run. Add the final pair after the scan.

**Why every valid substring is counted once**

Every qualifying substring has exactly one character change, so it belongs to exactly one adjacent-run boundary. Its equal half-length is among the lengths counted by that boundary. Conversely, every counted length selects equal-sized portions of two different neighboring runs and therefore forms a valid substring. The boundary partition is exhaustive and disjoint.

## Complexity detail
The scan performs constant work for each of the `n` characters, taking $O(n)$ time. It keeps only two run lengths and the answer, so it uses $O(1)$ extra space.

## Alternatives and edge cases
- **Store all run lengths:** build a list and sum `min(lengths[i - 1], lengths[i])`; it is equally linear but uses $O(n)$ space in the worst case.
- **Expand around every change:** grow equally into the two neighboring runs; it is intuitive, although the run-count formula expresses the same work more directly.
- **Enumerate every substring:** count zeros, ones, and transitions for every interval; it is correct but takes $O(n^2)$ time.
- A one-character or uniform string returns `0` because it has no boundary between different runs.
- Alternating strings count every adjacent pair, and overlapping pairs are distinct substrings.
- Equal totals are insufficient when the characters alternate more than once inside the substring.
