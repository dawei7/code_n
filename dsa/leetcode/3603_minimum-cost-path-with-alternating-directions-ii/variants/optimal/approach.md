## General

Every move advances either one row or one column, so the reachable-state graph is a directed acyclic grid. The action after entering any non-destination cell is forced to be a wait before the next move. Therefore a reached cell can be assigned one combined local charge: its entrance cost plus its waiting cost. The destination is the sole exception because the path stops immediately after entering it.

Let the dynamic-programming value at `(i, j)` include the start entrance cost and every combined charge through `(i, j)`. The only predecessors are `(i - 1, j)` and `(i, j - 1)`, giving the recurrence

$$
\operatorname{dp}[i][j]
=
\min(\operatorname{dp}[i-1][j],\operatorname{dp}[i][j-1])
+(i+1)(j+1)+\texttt{waitCost}[i][j].
$$

Initialize the origin to `1`, because its entrance cost is paid but it is not waited on. After evaluating the destination, subtract `waitCost[m - 1][n - 1]`, which the uniform recurrence included although the trip ends before that wait. Each candidate path to a cell must end through exactly one of its two predecessors, and the added local charge is independent of the earlier route. Choosing the cheaper predecessor therefore preserves the minimum inductively for every cell.

Only the previous outer slice and the current slice are needed. A single array retains the value from above before an update and the value from the left after an update. If columns outnumber rows, conceptually transpose the grid: right/down paths correspond bijectively after transposition, the entrance product is symmetric, and waiting costs are read with swapped indices. This makes the frontier length $\min(m,n)$.

## Complexity detail

Every one of the $mn$ cells is processed once with constant arithmetic and comparison work, so time is $O(mn)$. The compressed frontier has $\min(m,n)$ entries, giving $O(\min(m,n))$ auxiliary space.

The benchmark defines $S=mn$ on square grids. The reference performs one topological pass. A calibrated correct alternative scans cells in reverse topological order repeatedly until no distance changes, requiring $\Theta(S^{3/2})$ work on these grids while preserving every output.

## Alternatives and edge cases

- **Full two-dimensional DP:** It uses the same recurrence and time but stores all $mn$ states instead of one frontier.
- **Dijkstra's algorithm:** Nonnegative costs make it valid, but the monotone grid is already a DAG, so a heap adds unnecessary logarithmic overhead.
- **Repeated relaxation:** Bellman-Ford-style passes eventually find the same costs, but a deliberately adverse scan order advances only one diagonal per pass.
- **Wait at the start:** The first post-entry action occurs on an odd second and must move, so `waitCost[0][0]` is never charged.
- **Wait at the destination:** Stop on arrival; subtract or otherwise omit the destination waiting cost.
- **Single row or column:** The path is forced, but every internal cell still incurs one wait before the next move.
- **Zero waiting costs:** Entrance costs still depend on cell coordinates, so different monotone routes can have different totals.
- **Transposed frontier:** Swap only the logical traversal indices; continue reading the original matrix at the corresponding original coordinates.
- **Large costs:** The total may exceed 32-bit integer range even though each individual waiting cost does not.
