## General

**Define a backward dynamic-programming state**

The memoized function `dfs(i,j,k)` returns the maximum score of a right/down path from the top-left cell to `(i,j)` when `k` units of cost are still available for the cells being processed backward.

Looking backward is equivalent to looking forward: the predecessor of `(i,j)` must be either `(i-1,j)` or `(i,j-1)`. No other move can reach the cell under the right/down rule.

The state includes remaining cost because two paths reaching the same cell with different budgets are not interchangeable. A lower-scoring path that preserved more budget might become better later.

**Reject invalid coordinates and exhausted budgets**

If `i<0` or `j<0`, the path stepped outside the grid. If `k<0`, it exceeded the budget. The source returns `-inf` for all these impossible states.

Negative infinity is useful because `max(a,b)` automatically ignores an impossible predecessor when the other is valid. If both are impossible, adding the current nonnegative score still leaves the result at negative infinity.

The top-left base case returns zero. The contract guarantees `grid[0][0]=0`, so the start contributes neither score nor cost. Checking this base after invalid-state rejection also ensures a negative budget never becomes valid merely by reaching the start.

**Pay for the current cell and choose the better predecessor**

For a non-start cell, `res` begins as `grid[i][j]`, its score contribution.

Cell zero costs zero. Cells one and two both cost one, so the code decrements `k` exactly when `grid[i][j]` is truthy/nonzero.

It then evaluates the two possible predecessors with the adjusted remaining budget:

`dfs(i-1,j,k)` and `dfs(i,j-1,k)`.

Adding the larger predecessor score to `res` gives the best valid path ending at this cell under the original state budget.

This transition treats score and cost separately: value two adds two score but consumes only one budget, while value one adds one score for the same cost. The DP can therefore prefer paths containing more twos without exceeding `k`.

**Memoization removes repeated subproblems**

Many right/down paths merge at the same cell and remaining budget. The `@cache` decorator stores each distinct `(i,j,k)` result, so the recursive transition is evaluated once per state. Later calls reuse it.

The final call asks for the destination with the full budget. If its result is negative, it must be negative infinity because all real path scores are nonnegative; the source returns `-1`. Otherwise it returns the maximum score.

Calling `dfs.cache_clear()` after computing the answer releases state retained by the function-level cache. It does not affect the already stored `ans`.

**Why the recurrence is exact**

Every valid path to `(i,j)` ends at exactly one of the two predecessor cells. Removing the current cell from that path leaves a valid predecessor path with the current cell's cost removed from the budget. The recurrence examines both possibilities and adds the exact current score.

Conversely, appending `(i,j)` to any valid predecessor state creates a legal right/down path and accounts for its score and cost once. Induction over `i+j` proves each cached state is optimal.

For `[[0,1],[2,0]]` with budget one, the route through value two spends one and scores two; the route through one scores one. The destination zero adds nothing, and the maximum is two.

**Useful cost-state limit**

A path visits exactly `m+n-1` cells. The guaranteed-zero start costs nothing, and every other cell costs at most one. Thus no path can spend more than `m+n-2`.

Define

$$
L=\min(k,m+n-2).
$$

Only $O(L)$ relevant budget variations can arise per cell. This gives the useful state bound even when input `k` is much larger than every possible path cost.

## Complexity detail

There are `m*n` cells and up to $O(L)$ reachable remaining-budget states per cell. Each cached state does constant work besides two cached recursive calls, so time complexity is $O(mnL)$.

The exact source stores all memoized `(cell,budget)` states, requiring $O(mnL)$ space, plus $O(m+n)$ recursion depth. This contradicts the manifest's $O(nL)$ space claim, which would require a rolling-row iterative DP. The source does not roll rows; its cache retains states across the full grid.

The recursion depth is at most `m+n-1<=399` under the constraints, below Python's usual recursion limit.

## Alternatives and edge cases

- **Three-dimensional iterative DP:** It implements the same state explicitly and avoids recursion, but full storage remains $O(mnL)$.
- **Rolling rows:** Keeping only current and previous rows can reduce space to $O(nL)$, matching the manifest, but it is not the exact source.
- **Greedily prefer value two:** A high immediate score can consume budget and block all routes to the destination. DP must retain cost states.
- **Track only maximum score per cell:** Paths with different spent costs cannot be safely merged into one scalar.
- **Budget zero:** Only all-zero paths are valid; the negative-budget base rejects nonzero cells.
- **Single-cell grid:** The guaranteed-zero start returns score zero.
- **Nonzero destination:** Its cost is deducted and its value added like every non-start cell.
- **No valid path:** Every predecessor chain reaches negative budget, yielding `-inf` and final `-1`.
- **Budget exceeds path length:** Extra budget does not create additional score; `L` caps meaningful state variation.
- **Value two:** It costs one, not two. The truthiness check implements the stated cost rule exactly.
- **Start-cell guarantee:** Returning zero without charging the start relies on `grid[0][0]=0` from the contract.
- **Cache lifetime:** Clearing after evaluation prevents retained memoized data from outliving the method result.
- **Manifest mismatch:** Space documentation must reflect the full memoization cache actually allocated.
