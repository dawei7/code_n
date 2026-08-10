## General

**Track reachability by column**

Every legal move advances exactly one column to the right. This gives the problem a natural layered structure: after $j$ moves, a path is in column $j$.

The solution does not need the entire path. It only needs to know which row positions in the current column are reachable from some permitted start.

Set `q` stores those reachable row indices. Initially it is `set(range(m))` because the path may start at any row in column zero.

**Generate the next frontier**

For each current row `i`, the next row can be `i - 1`, `i`, or `i + 1`. The loop `range(i - 1, i + 2)` enumerates exactly these three candidates.

A candidate row `k` is added to next set `t` only when:

- `0 <= k < m`, so it remains inside the grid;
- `grid[i][j] < grid[k][j + 1]`, so the destination value is strictly larger.

Every accepted destination lies in the next column because the column index is explicitly `j + 1`.

**Why a set is the right state**

Many different paths can arrive at the same cell. Once a cell at row `k` and column `j + 1` is known reachable, the history used to reach it does not affect future legal moves.

A set deduplicates those arrivals. The next iteration processes that cell once rather than once per path.

This compression prevents the algorithm from expanding an exponential number of possible path sequences.

**The frontier invariant**

At the beginning of the iteration for column `j`, `q` contains exactly the rows whose cells in column `j` are reachable by a legal path starting somewhere in column zero.

This is true initially because every first-column cell is an allowed start.

The nested loops add a row `k` to `t` exactly when at least one reachable current cell has a legal move to it. Therefore `t` is exactly the reachable-row set for column `j + 1`.

Assigning `q = t` establishes the invariant for the next column.

**Why the first empty frontier determines the answer**

If `t` is empty while attempting to move from column `j` to `j + 1`, no reachable current cell has any legal next move.

Every path that reached column `j` has made exactly $j$ moves from column zero. No path can reach a later column because moving right one column is the only transition and the next layer is empty.

The maximum number of moves is therefore `j`, which the code returns immediately.

**Why reaching the last column returns `n - 1`**

The loop considers transitions for `j` from zero through `n - 2`.

If every next frontier is nonempty, at least one legal path reaches column `n - 1`. Moving from column zero to that column requires exactly `n - 1` moves.

No move can go beyond the last column, so this is also the maximum possible value.

**Trace an immediate failure**

Suppose no cell in column one is strictly larger than any adjacent-row cell in column zero.

The first iteration has `j = 0`. Every candidate fails the comparison, so `t` remains empty and the method returns zero.

This correctly means a starting cell may be chosen, but no move can be performed.

**Trace merging paths**

Imagine two reachable rows in one column can both move to the same row in the next column.

Both attempts execute `t.add(k)`, but the set stores that row only once. This is safe because all future options from the destination depend on its location and value, not on which predecessor was used.

The method is computing reachability, not counting paths.

**Strict comparison is essential**

The move rule requires a destination value strictly bigger than the current value.

The code uses `<`. Equal values do not form a legal edge. Using `<=` would incorrectly create paths across flat values and might overstate the number of moves.

**Why dynamic programming values are unnecessary**

A traditional grid DP could store the maximum moves reaching every cell. Here all moves advance one column, so every cell in column `j` is reached after exactly $j$ moves.

Only the Boolean question of reachability matters. The current set is a space-compressed DP layer.


By induction on columns, `q` is exactly the reachable set for the current layer. The transition tests all and only the three geometrically permitted destinations and applies the exact strict-value condition, so no legal destination is missed and no illegal one is added.

If a layer becomes empty, no longer path exists, and returning its source column index gives the maximum moves already achieved. If no layer is empty, a path reaches the last column and makes the absolute maximum $n-1$ moves.

## Complexity detail

For each of the $n-1$ transitions, at most $m$ reachable rows are processed, with three constant-time candidate checks per row. Worst-case time is $O(mn)$.

The current and next frontier sets each contain at most $m$ row indices, so auxiliary space is $O(m)$. The grid is not modified.

## Alternatives and edge cases

- **Full Boolean DP table:** Correct in $O(mn)$ time but uses $O(mn)$ space instead of retaining two layers.
- **Depth-first search with memoization:** Also works on this acyclic right-moving graph, but recursion and a full memo table add overhead.
- **Enumerate complete paths:** Can be exponential because paths branch and merge.
- **One reachable row reached by many paths:** The set intentionally processes it once.
- **No first move:** Returns zero when the first next frontier is empty.
- **Reach the last column:** Returns `n - 1`, the largest geometrically possible move count.
- **Top row:** Candidate `i - 1` is rejected by the boundary check.
- **Bottom row:** Candidate `i + 1` is rejected by the boundary check.
- **Equal adjacent value:** Not reachable because growth must be strict.
- **Any starting row:** Initializing with every row correctly represents the contract.
- **Positive values:** No sentinel is needed; comparisons use actual cells only.
- **Input preservation:** Only frontier sets change.
