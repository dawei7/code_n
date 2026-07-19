## General
**Define the prefix decision.** Let $D(i,j)$ denote the LCS length of the first $i$ characters of one string and the first $j$ characters of the other. An empty prefix has no nonempty subsequence, so row zero and column zero contain `0`.

**Handle matching and mismatching final characters.** If the two new final characters match, an optimal common subsequence can extend the best result for the two shorter prefixes, giving `previous[j - 1] + 1`. If they differ, an optimal subsequence must omit at least one of them, so take `max(previous[j], current[j - 1])`. These are exactly the two ways a common subsequence can relate to the latest prefix characters, which makes the recurrence exhaustive and correct by induction over prefix lengths.

**Retain only the preceding row.** Each state uses the current row's left neighbor and values from the immediately previous row. Keep `previous` and build a fresh `current` row for every character of the longer string. Put the shorter input on the column axis so both rows have $\min(m,n)+1$ entries. The final cell is the LCS length of the complete strings.

## Complexity detail
The algorithm evaluates all $mn$ prefix pairs once, with constant work per pair, for $O(mn)$ time. Two rows of length $\min(m,n)+1$ use $O(\min(m,n))$ auxiliary space.

## Alternatives and edge cases
- **Full two-dimensional table:** Storing every $D(i,j)$ state has the same $O(mn)$ time but uses $O(mn)$ space; it is useful when reconstructing an actual subsequence.
- **Memoized recursion with string slices:** The recurrence is correct, but allocating suffix slices for states adds avoidable copying and recursion overhead.
- **Naive recursion:** Branching on every mismatch without memoization repeats prefix states exponentially.
- **Substring confusion:** Matching characters may have gaps; requiring adjacency solves longest common substring instead.
- **No common character:** Every state remains zero and the answer is `0`.
- **Repeated characters:** Their occurrences cannot be reused or reordered; prefix indices enforce valid one-to-one order.
