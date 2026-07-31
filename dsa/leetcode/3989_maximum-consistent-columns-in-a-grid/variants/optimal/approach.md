## General

View every original column as one item in an order-preserving subsequence. For indices $a<b$, draw a directed edge from `a` to `b` exactly when

$$
\lvert \texttt{grid[r][b]}-\texttt{grid[r][a]} \rvert \le \texttt{limit}
$$

for every row `r`. Indices always increase along an edge, so this compatibility graph is a directed acyclic graph. A retained grid is consistent exactly when its consecutive columns form a path in this graph.

**Longest path in column order**

Let `dp[b]` be the maximum number of retained columns in a consistent subsequence whose last column is `b`. Keeping `b` alone always gives length one. For every earlier column `a`, test the pair across all rows. When the pair is compatible, a best subsequence ending at `a` can append `b`, giving the transition

$$
\texttt{dp[b]}=\max(\texttt{dp[b]},\texttt{dp[a]}+1).
$$

Processing columns from left to right guarantees that every `dp[a]` needed by `b` is already final. The answer is the largest state over all possible final columns.

**Why the recurrence is exact**

Take any consistent subsequence ending at `b`. If it has more than one column, let `a` be its preceding retained column. The definition of consistency makes `a` and `b` compatible, and everything before `b` is a consistent subsequence ending at `a`; therefore the recurrence considers a candidate at least as long. Conversely, every recurrence transition appends `b` only to a compatible predecessor, so it preserves every old adjacent pair and creates one valid new adjacent pair. Induction over increasing `b` proves that each state and their maximum are optimal.

Compatibility is evaluated during each transition instead of stored. This retains the hinted pairwise test while avoiding an unnecessary $n\times n$ matrix.

## Complexity detail

There are $\binom{n}{2}=O(n^2)$ ordered column pairs. Testing one pair may inspect all $m$ rows, giving $O(mn^2)$ time. The one-dimensional `dp` array uses $O(n)$ auxiliary space. The input matrix itself is not copied.

## Alternatives and edge cases

- **Precomputed compatibility matrix:** Test every column pair first and then run the same longest-path dynamic program. It has the same $O(mn^2)$ time but uses $O(n^2)$ additional space.
- **Explicit DAG adjacency lists:** Store every compatible edge and compute a longest path in topological index order. This is equivalent to the recurrence and may also require $O(n^2)$ space.
- **Length-layer dynamic programming:** Track whether each subsequence length can end at each column. It is correct but introduces an extra length dimension, taking $O(mn^2+n^3)$ time and $O(n^2)$ space.
- **Enumerating retained subsets:** Checking all $2^n-1$ nonempty column subsets is infeasible for $n=250$.
- **Only adjacent retained columns matter:** Two nonadjacent retained columns may differ by more than `limit` when another retained column connects them through valid steps.
- **Every row must agree:** A pair is incompatible as soon as one row exceeds the limit, even if every other row satisfies it.
- **Equality is valid:** A difference exactly equal to `limit` is allowed.
- **Order is by index, not value:** Retained values may increase, decrease, or repeat; only original column order is preserved.
- **At least one column remains:** Every legal input has answer at least `1`, including a one-column grid or a grid with no compatible pair.
