## General
**Precompute the next usable position:** Build a table for every source index and lowercase letter. Entry `next_position[i][c]` is the earliest position at or after `i` containing character `c`, or `-1` if none exists. Construct rows from right to left by copying the following row and updating the current character.

**Consume each subsequence greedily:** Start at source index zero and process target characters in order. Use the table to take the earliest possible occurrence at or after the current source index. Choosing the earliest occurrence leaves the greatest possible suffix available for later target characters and can never require more source copies than a later choice.

**Restart only when necessary:** If the current source suffix has no occurrence of the required character, begin a new subsequence and look for that character from source index zero. If it is absent there too, construction is impossible. Otherwise count the new copy and continue just after the chosen position.

Within one source copy, the chosen positions strictly increase, so they form a valid subsequence. The greedy earliest choice maximizes remaining room and therefore consumes at least as long a target prefix as any other choice from that copy. Each restart is consequently unavoidable, proving the number of subsequences is minimal.

## Complexity detail
Building $S+1$ table rows of $A$ entries costs $O(AS)$ time and space. Each of the $T$ target characters performs constant-time table lookups, for total time $O(AS+T)$. With the fixed lowercase alphabet, this is linear in the two string lengths.

## Alternatives and edge cases
- **Position lists plus binary search:** Store sorted source indices for each letter and find the next one in $O(log S)$ time, giving $O(S+Tlog S)$ time and $O(S)$ space.
- **Repeated source scans:** Scan `source` from the beginning for every subsequence. It uses constant extra space but can take $O(ST)$ time.
- **Dynamic programming over prefixes:** It can model the construction but stores unnecessary states because earliest feasible matches are greedily optimal.
- **Missing character:** If any target character is absent from `source`, return `-1`.
- **Target already a subsequence:** Exactly one source copy is needed.
- **Repeated target character:** A source copy may contribute as many ordered occurrences as it contains; further copies restart the scan.
- **Reverse order:** Characters present in `source` may still require several subsequences when target order repeatedly moves backward.
- **Single-character source:** A matching target needs one copy per target character.
