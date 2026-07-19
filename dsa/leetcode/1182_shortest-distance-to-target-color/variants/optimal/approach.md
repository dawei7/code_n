## General
**Turn repeated searches into nearest-distance data.** There are only three possible colors, so store three distances for every index. After this table is built, a query `[i, c]` needs only the cell for index `i` and color `c` rather than another search through `colors`.

**Find the nearest occurrence on the left.** Sweep indices from left to right while remembering the latest index of each color. At index `i`, first record `i` as the latest occurrence of `colors[i]`; for every color already seen, `i - last[color]` is its closest distance from the left. Any earlier occurrence is farther away because `last[color]` is the greatest eligible index at most `i`.

**Combine the nearest occurrence on the right.** Sweep back from right to left and analogously remember the next index of each color. For each index and color, minimize the stored left distance with `next[color] - i`. Every occurrence lies on the left or right of `i`, and each sweep selects the closest occurrence on its side, so the smaller of those two distances is the global minimum. A sentinel distance at least $n$ survives exactly when the color never occurs; convert that sentinel to `-1` when answering a query.

## Complexity detail
Each directional sweep performs three constant-size color updates at each of the $n$ indices, and the $q$ queries take constant time apiece. The total time is therefore $O(n+q)$. The table contains three entries per array index, which is $O(n)$ space; the two three-element state arrays are $O(1)$.

## Alternatives and edge cases
- **Sorted positions plus binary search:** Store each color's occurrence indices and binary-search around every query index. This uses $O(n)$ space and $O(n+q\log n)$ time, which is effective but not constant time per query.
- **Scan the array for every query:** Taking the minimum distance over all matching indices is direct, but it costs $O(nq)$ time in the worst case.
- **Target at the query index:** The shortest distance is `0`; both sweeps preserve that value.
- **Missing target color:** Its sentinel is never replaced, so the corresponding answer must be `-1`.
- **One-sided nearest occurrence:** At an array boundary, or when all occurrences lie on one side, the valid directional distance wins over the other sentinel.
- **Equal nearest distances:** Two target occurrences may be equally close; only their shared distance is returned, not an index.
