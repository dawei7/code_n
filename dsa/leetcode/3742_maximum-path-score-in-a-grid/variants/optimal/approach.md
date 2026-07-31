## General

A cell can be reached only from the cell above it or the cell to its left, but the best predecessor depends on how much cost has already been used. For each cell and each exact cost from `0` through $L$, retain the maximum score of any path that reaches that state. An unreachable state has no score.

When processing a cell of value `0`, carry each predecessor state forward without changing cost or score. For a value `1` or `2`, increase the cost by one and the score by the cell value. Merge states from above and left by keeping the larger score whenever both routes produce the same new cost. States beyond `k` are discarded immediately, so only budget-valid partial paths can reach the destination state set.

Every legal right/down path has exactly $m+n-1$ cells, and the starting cell is guaranteed to be zero. Its cost can therefore never exceed $m+n-2$, so costs above $L=\min(k,m+n-2)$ need not be represented. At the destination, the maximum score across all retained costs is the requested answer; an empty state set means no valid path exists.

When `k` is at least $m+n-2$, the budget cannot exclude any path. The native implementation then uses an ordinary maximum-score grid dynamic program without a cost dimension.

## Complexity detail

There are $mn$ cells and at most $L+1$ relevant cost states per cell. The worst-case running time is $O(mnL)$, and rolling the grid rows while retaining one state collection per column uses $O(nL)$ auxiliary space. In the inactive-budget shortcut, these bounds improve to $O(mn)$ time and $O(n)$ space.

## Alternatives and edge cases

- **Enumerate complete paths:** Depth-first search follows the movement rules directly, but the number of right/down paths can grow exponentially in $m+n$.
- **Ignore cost and maximize score:** A highest-score path may exceed `k`, so a score-only state is valid only when the budget is known to be inactive.
- **Treat score as cost:** Values `1` and `2` both cost one despite contributing different scores; those quantities cannot be merged into one total.
- **Zero budget:** A valid result exists only if some complete path contains no nonzero cell.
- **Single-cell grid:** The guaranteed starting value is `0`, so the answer is `0` for every legal budget.
- **Destination over budget:** Such a path is invalid even though it reaches the required cell, exactly as the source Note specifies.
