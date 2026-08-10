## General

**Ask how many valid paths remain from one cell**

`dfs(i,j)` returns the number of obstacle-free paths from grid cell `(i,j)` to the bottom-right destination. From an open non-destination cell, the robot's only possible next moves are down to `(i+1,j)` and right to `(i,j+1)`. These two path sets have different first moves, so their counts can be added.

The public answer is `dfs(0,0)`, the number of paths from the specified starting corner.

**Reject invalid states before anything else**

The first condition returns zero if the row is beyond `m`, the column is beyond `n`, or the current grid entry is an obstacle. Returning zero is the correct contribution because no valid path can start from an invalid or blocked cell.

The bounds checks appear before `obstacleGrid[i][j]` in an `or` chain. Python short-circuits from left to right, so an out-of-range state never attempts an invalid grid access.

Obstacle testing also occurs before the destination base case. If the bottom-right cell itself is blocked, the call returns zero rather than incorrectly counting arrival there as a path.

**Count one completed path at the destination**

If `(i,j)` is the open bottom-right cell, the function returns 1. No more moves are required, and the current recursion route represents one complete valid path.

This is analogous to counting one empty suffix of moves after arrival. Returning zero would erase every successfully completed route from its parents' sums.

**The recursive recurrence**

For any other open cell,

$$
F(i,j)=F(i+1,j)+F(i,j+1).
$$

Every valid path begins with exactly one of those two moves. Removing that first move gives a path counted by the corresponding child. Conversely, prefixing a down or right move to a child path creates a valid path from the current cell. The two sets are disjoint, so addition is exact.

If both directions are blocked or outside, both children return zero and the current state correctly returns zero. No special dead-end branch is needed.

**Why memoization changes exponential recursion into grid-sized work**

Many different move sequences reach the same coordinate. Without caching, each arrival would recursively recount all paths from that cell. `@cache` stores the return value keyed by `(i,j)`, so the first call solves the subproblem and later calls reuse it.

The state needs no visited set because moves strictly increase `i` or `j`; recursion cannot cycle. Obstacles remain immutable throughout the method, so the answer for a coordinate never changes and is safe to cache.

**A trace around the central obstacle**

For `[[0,0,0],[0,1,0],[0,0,0]]`, a call at `(0,0)` splits down and right. Any call reaching `(1,1)` returns zero. The routes along the top/right edge and left/bottom edge each reach the destination and contribute one. Shared suffix states, such as cells near the destination, are evaluated once and reused.


Order cells by their Manhattan distance to the destination. Invalid and blocked cells correctly have zero paths, and the open destination correctly has one. Assume cells closer to the destination return exact counts. An open current cell's valid paths partition by first move into its down and right children, whose exact counts are known by the induction hypothesis. Their sum is therefore exact.

This establishes `dfs(0,0)` as the required total.

**A required runtime name**

The decorator `cache` normally comes from `functools`. The selected file does not show that import, so a standalone environment must provide `from functools import cache` or inject the name. The algorithm depends on memoization; an unavailable name would be a namespace failure before execution rather than a recurrence error.

**Source-versus-manifest space**

The cache can hold a result for every open or blocked in-bounds coordinate reached, plus boundary states, for $O(mn)$ entries overall. Recursion can also be $O(m+n)$ calls deep. This is not the manifest's $O(n)$ rolling-row storage. The exact source uses $O(mn)$ auxiliary space.

## Complexity detail

There are $mn$ in-bounds coordinate states and only $O(m+n)$ distinct one-step-outside boundary states. Each cached state performs constant work after its children are known, so time is $O(mn)$.

Memoized entries dominate at $O(mn)$ space, while the recursion stack is $O(m+n)$. Thus exact auxiliary space is $O(mn)$, not the manifest's $O(n)$ claim. The input grid is read without mutation.

## Alternatives and edge cases

- **Rolling one-dimensional DP:** Store one row of counts, zero obstacle cells, and combine above with left. It achieves $O(mn)$ time and $O(n)$ space.
- **Full bottom-up table:** It avoids recursion and has the same $O(mn)$ time and space as memoization.
- **Combinatorial formula:** Obstacles destroy the simple choose-move-positions formula because forbidden coordinates remove selected sequences irregularly.
- **Blocked start:** The first call sees an obstacle and returns zero.
- **Blocked destination:** Obstacle checking precedes the destination base case, so zero is returned.
- **One open cell:** Start equals destination and contributes one path.
- **One row or column:** The recursion follows the only direction until an obstacle returns zero or the destination returns one.
- **Repeated subproblem:** Caching ensures a coordinate reached from above and left is solved once.
- **No cycles:** Both allowed moves increase an index, so recursion always approaches a boundary or destination.
- **Input preservation:** Obstacles are never overwritten or used as memo markers.
