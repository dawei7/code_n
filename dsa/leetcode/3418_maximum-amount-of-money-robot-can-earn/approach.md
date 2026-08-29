## General

**The path alone is not enough to describe a state.** From a cell $(i,j)$, the best future profit depends not only on the position but also on how many robber neutralizations remain. The protected source defines

`dfs(i, j, k)`

as the maximum profit obtainable from cell $(i,j)$ through the bottom-right cell when `k` neutralizations remain. Since the ability can be used at most twice, `k` is $0$, $1$, or $2$.

The method starts with `dfs(0, 0, 2)`. Every path moves only down or right, so recursion always advances toward the destination and cannot form a cycle.

**Reject paths that leave the grid.** If `i >= m` or `j >= n`, the state lies outside the grid and returns `-inf`. This sentinel is important. A boundary move must never appear better than a real path merely because the real path has a negative profit. Adding a finite cell value to negative infinity remains negative infinity, so invalid directions disappear naturally inside `max`.

The problem explicitly allows a negative final profit. Returning zero for an invalid move would incorrectly let the robot stop before reaching the destination whenever the remaining route loses money.

**Handle the destination as a complete final decision.** At $(m-1,n-1)$ there is no next move. If the cell value is nonnegative, collecting it is optimal. If it is negative and at least one neutralization remains, the robot may neutralize the robber and receive zero from the cell. The source combines these possibilities as

`max(coins[i][j], 0) if k else coins[i][j]`.

When `k == 0`, the negative value cannot be avoided. If the value is positive, `max(value, 0)` still returns the value, so no ability is wasted.

**Transition without neutralizing.** At an ordinary cell, the robot can always accept the cell value and choose the better of moving down or right:

$$
\texttt{coins}[i][j]
+\max(\texttt{dfs}(i+1,j,k),\texttt{dfs}(i,j+1,k)).
$$

This becomes the initial `ans`. The same number of neutralizations is passed forward.

**Transition by neutralizing a robber.** If the current value is negative and `k` is positive, the robot may make this cell contribute zero. The two resulting choices are

`dfs(i + 1, j, k - 1)`

and

`dfs(i, j + 1, k - 1)`.

There is no addition of `coins[i][j]` in these branches because the robber was neutralized. The source takes the maximum of both neutralized directions and the earlier non-neutralized result. It does not consider neutralizing a nonnegative cell, because replacing a gain by zero can never improve a route.

For the first example, the state at the `-2` cell can either subtract two and keep both abilities or contribute zero and continue with one fewer ability. The latter branch joins the positive cells $3$ and $4$ and participates in the route of total $8$.

**Memoization turns overlapping recursion into dynamic programming.** Many paths reach the same triple $(i,j,k)$. The `@cache` decorator stores the result of the first computation and reuses it for every later request. There are only three possible `k` values per cell, so exponential path enumeration collapses to a constant amount of work per state.

The variables `m` and `n` are assigned after the nested function is defined but before it is called. Python closures resolve them when `dfs` runs, so the bounds are available.

After obtaining the answer, the source calls `dfs.cache_clear()`. This releases references held by this function's cache rather than retaining a potentially large grid-state table after the method returns. It does not reduce peak memory during computation, but it is a deliberate cleanup step.

**Why the recurrence is correct.** At any non-destination cell, every legal route makes exactly one first choice: move down or right, and either accept the current robber loss or neutralize it if allowed. The recurrence enumerates all legal combinations of those decisions and no illegal one. After that first decision, the remaining problem is exactly the smaller cached state named by the transition. The destination base case makes the correct final-cell choice, and outside-grid states are excluded. Backward induction on distance to the destination therefore proves that each cached value is optimal, including `dfs(0,0,2)`.

The manifest summary describes a row-compressed bottom-up array and claims $O(n)$ space. Although the local editorial contains such an alternative, the protected Optimal source shown here uses recursive memoization. A faithful explanation must account for its full cache and recursion stack.

## Complexity detail

Let the grid have $m$ rows and $n$ columns. There are at most $3mn$ in-grid states. Each cached state performs a constant number of arithmetic operations and makes at most four cached calls, so total time is $O(mn)$. A small number of out-of-grid states are also cached, without changing the bound.

The memoization cache can hold $O(mn)$ results. The longest recursion chain follows a monotone path and has $O(m+n)$ frames. Peak auxiliary space is therefore $O(mn)$, dominated by the cache, not the manifest's $O(n)$. Clearing the cache at the end frees it after the answer is computed but does not change that peak bound.

## Alternatives and edge cases

- **Row-compressed bottom-up DP:** Three values per column can produce the same $O(mn)$ time with $O(n)$ space and no recursion. This is the approach described by the manifest, but it is not the protected source.
- **Uncached recursion:** Exploring both directions and ability choices independently repeats states exponentially and is infeasible for a large grid.
- **Standard maximum path DP without \(k\):** Omitting the neutralization dimension cannot distinguish paths that reach the same cell with different remaining abilities.
- **All positive cells:** No neutralization branch is considered, and the recurrence reduces to the ordinary maximum-sum right/down path.
- **Negative destination:** With an ability remaining, the destination contributes zero; without one, its negative value is unavoidable.
- **Negative start:** The same choice applies at $(0,0)$, so a neutralization may be spent immediately.
- **Profit below zero:** Negative infinity, rather than zero, protects the requirement to reach the destination and allows a genuinely negative optimum.
- **Single-cell grid:** The destination base case immediately returns the cell value or zero if a robber can be neutralized.
- **At most two uses:** The robot is never forced to consume abilities. Non-neutralizing transitions preserve `k`, and unused abilities may remain at the destination.
- **Recursion depth:** A path contains $m+n-1$ cells. With the stated maximum dimensions this approaches Python's usual recursion-depth boundary, so an iterative implementation can be operationally safer even though the source's mathematical state graph is acyclic.
