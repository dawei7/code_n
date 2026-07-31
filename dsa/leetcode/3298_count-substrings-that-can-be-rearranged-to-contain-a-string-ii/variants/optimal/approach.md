## General

The order of a substring's characters is irrelevant after rearrangement. It can begin with `word2` exactly when it contains every letter with at least the multiplicity required by `word2`. Store those requirements in a fixed 26-entry `deficit` array and initialize `missing` to the total number of required occurrences.

Scan `word1` with a right boundary. When an incoming character still has a positive deficit, it supplies one missing occurrence; then decrement its deficit in every case so surplus copies are represented by negative values. Once `missing` reaches zero, move the left boundary forward until the removed character creates a positive deficit and makes the window invalid again.

After this shrinking step, starts `0` through `left - 1` all give valid substrings ending at the current right boundary: adding characters on the left cannot destroy a satisfied frequency requirement. The start at `left` is invalid by construction. Therefore adding `left` counts every valid ending exactly once. The deficit relation is restored on every removal, and neither pointer ever retreats, which supplies the required linear scan without per-prefix storage.

## Complexity detail

Let $n=\lvert word1\rvert$ and $m=\lvert word2\rvert$. Building the requirements costs $O(m)$ time. Every source character is added once and removed at most once, so the window costs $O(n)$ time and the total is $O(n+m)$. Only 26 integer deficits and a few counters are stored, giving $O(1)$ auxiliary space under the fixed lowercase alphabet.

## Alternatives and edge cases

- **Prefix tables with binary search:** Keeping 26 counts for every prefix and searching an endpoint consumes $O(26n)$ memory and $O(26n\log n)$ time, violating this version's tighter limits.
- **Hash map window:** It can implement the same logic, but a 26-entry array has fixed storage and avoids hashing overhead at the million-character boundary.
- **Repeated required letters:** `missing` tracks individual occurrences, so surplus copies of one letter cannot compensate for a deficit of another or for another copy of the same letter.
- **Large answer:** Up to $n(n+1)/2$ substrings may qualify, so fixed-width implementations must use a 64-bit result type.
- **No valid window:** If any required frequency exceeds its frequency in all of `word1`, the left boundary remains zero and the result is zero.
