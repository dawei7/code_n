## General
**Turn deletions into a longest retained subsequence.** Any valid result is determined by an increasing sequence of column indices. Two consecutive retained columns $i<j$ are compatible exactly when `strs[row][i] <= strs[row][j]` for every row. If this condition holds for every consecutive pair in the retained sequence, transitivity makes every resulting row non-decreasing.

**Dynamic-programming state.** Let `best[j]` be the greatest number of compatible columns in a retained sequence whose final column is `j`. A sequence containing only `j` is always valid, so initialize every state to `1`. For every earlier column `i`, test all rows. When no row decreases from `i` to `j`, append `j` to the best sequence ending at `i` and update `best[j] = max(best[j], best[i] + 1)`.

**Recover the minimum deletion count.** Every valid retained sequence appears in these transitions, because its consecutive indices satisfy the same all-rows compatibility test. Conversely, each transition preserves the required order in every row, so every sequence represented by the dynamic program is valid. Therefore `max(best)` is the maximum number of columns that can remain, and the required answer is `C - max(best)`.

## Complexity detail
There are $O(C^2)$ ordered pairs of columns, and checking one pair examines at most $R$ rows. The running time is therefore $O(RC^2)$. The one-dimensional dynamic-programming array uses $O(C)$ auxiliary space.

## Alternatives and edge cases
- **Longest path in a compatibility DAG:** Treat each column as a vertex and add an edge from $i$ to $j$ when $i<j$ and all rows are compatible. A longest path gives the same result, but explicitly storing all edges uses $O(C^2)$ space.
- **Enumerate retained subsets:** Testing every subsequence is correct but takes exponential time in $C$.
- **Repeated compatibility scans:** Rechecking the same column pair once for every possible intermediate index preserves correctness but raises the worst-case time to $O(RC^3)$.
- **One column:** It is already ordered, so no deletion is needed.
- **Equal characters:** Equality is allowed; rows must be non-decreasing rather than strictly increasing.
- **Rows versus the array:** Only characters within each row must be ordered. The strings themselves need not be lexicographically ordered relative to neighboring strings.
