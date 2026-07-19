## General
**Encode one row as a bitmask.** Bit $c$ is one when column $c$ contains a student. For each classroom row, form a broken-seat mask and enumerate all $2^n$ candidate masks. A candidate is legal within that row exactly when it selects no broken seat and `mask & (mask << 1)` is zero, which excludes horizontally adjacent students.

**Remember only the previous row.** Let the dynamic-programming map associate each legal mask of the previous row with the maximum students seated through that row. To place a current mask, compare it with every reachable previous mask. The diagonal rules are satisfied exactly when both `mask & (previous << 1)` and `mask & (previous >> 1)` are zero. Among compatible histories, keep the largest previous total plus the number of set bits in the current mask.

Every valid seating has one legal mask per row and therefore follows one sequence considered by these transitions. Conversely, the row and diagonal checks make every sequence accepted by the DP a legal seating. Histories that end with the same current mask impose identical restrictions on future rows, so retaining only their maximum total cannot discard an optimal completion.

## Complexity detail
There are at most $2^n$ legal masks for any row. Comparing every current mask with every previous mask costs $O(4^n)$ per row, hence $O(m4^n)$ worst-case time. The two rolling maps hold at most $2^n$ states, giving $O(2^n)$ auxiliary space; the temporary row-mask list has the same bound.

## Alternatives and edge cases
- **Recursive placement without memoization:** Enumerating compatible row masks recursively is correct but repeatedly solves the same suffix for identical previous masks and grows exponentially across rows.
- **Maximum independent set formulation:** The usable seats and cheating relations form a graph, but a generic exponential graph search ignores the grid's small row width.
- **All seats broken:** The zero mask remains legal on every row, producing an answer of zero.
- **One row:** Only horizontal conflicts matter, reducing the task to choosing nonadjacent usable seats.
- **Students in the same column:** Vertically aligned students do not conflict; only the two diagonals connect adjacent rows.
