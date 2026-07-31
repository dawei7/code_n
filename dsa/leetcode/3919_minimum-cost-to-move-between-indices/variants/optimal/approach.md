## General

Write the gap between adjacent indices $i$ and $i+1$ as

$$
g_i=\texttt{nums[i+1]}-\texttt{nums[i]}.
$$

Because `nums` is strictly increasing, every $g_i$ is positive. Moving right from $i$ to $i+1$ costs `1` exactly when the right neighbor is `closest(i)`; otherwise it costs $g_i$. For an interior index, the right neighbor wins only when $g_i<g_{i-1}$, since a tie must choose the smaller, left-hand index. Index `0` always chooses index `1`.

The reverse edge can have a different cost. Moving left from $i+1$ to $i$ costs `1` exactly when the left neighbor is `closest(i+1)`. At an interior index this occurs when $g_i\le g_{i+1}$, including a tie, and the final index always chooses its only neighbor.

**Why only adjacent moves are needed**

A normal move from index $x$ to a farther index $y$ costs the absolute value difference. Along the strictly increasing array, that difference is exactly the sum of the intervening adjacent gaps. Replacing the jump with adjacent moves in the same direction cannot cost more: each adjacent move costs either its gap or the discounted value `1`. Therefore some optimal route uses adjacent moves only.

Once restricted to adjacent moves, the indices form a line with positive directed edge costs. The simple path from a query's start to its target is the monotone segment between them. Any route that backtracks traverses additional positive-cost edges, so it cannot improve that simple path.

Build `right`, where `right[k]` is the total cost of moving right from index `0` to index `k`. Independently build `left`, where `left[k]` is the total cost of moving left across edges `k-1, k-2, ..., 0`. Then:

- if `l < r`, the answer is `right[r] - right[l]`;
- if `l > r`, the answer is `left[l] - left[r]`;
- if `l == r`, either difference is `0`.

These differences select exactly the directed adjacent edges on the unique monotone path, so they equal the minimum travel costs.

## Complexity detail

Let $n$ be the length of `nums` and $q$ the number of queries. Computing both directional prefix arrays takes $O(n)$ time, and every query takes $O(1)$ time, for $O(n+q)$ total time. The two prefix arrays use $O(n)$ auxiliary space; the returned list uses $O(q)$ output space.

## Alternatives and edge cases

- **Walk every query separately:** The same directed edge costs can be summed from `l` to `r` for each query, but this takes $O(nq)$ time in the worst case instead of reusing prefix sums.
- **Dijkstra on the complete move graph:** General shortest-path machinery models the moves, but explicitly considering all direct destinations creates quadratic work and ignores the line metric that makes distant jumps unnecessary.
- **One prefix sum for both directions:** The discounted relation is directed. An edge may cost `1` one way and its full gap the other way, so rightward and leftward totals must be stored separately.
- **Equal adjacent gaps:** At an interior index, a tie chooses the smaller index. Consequently the left edge is discounted on equality, while the right edge is not.
- **Array endpoints:** Index `0` chooses index `1`, and index `n - 1` chooses index `n - 2`, because each has only one adjacent index.
- **Equal query endpoints:** No move is needed, and subtracting the same prefix value returns `0`.
- **Large coordinate gaps:** Costs can exceed 32-bit integer range after accumulation even though indices do not; use the language's sufficiently wide integer type.
