# TSP via Reduced Matrix (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_06` |
| **Category** | branch_and_bound |
| **Complexity (required)** | $O(N!)$ Worst Case |
| **Difficulty** | 9/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) |

## Problem statement

Given an N x N matrix representing the distances between cities, find the absolute shortest optimal Travelling Salesman Tour.
Unlike approximations (`approx_03`, `approx_04`), you must find the **exact** optimal solution.
Unlike Dynamic Programming (Held-Karp `graph_20` which takes $O(N^2 2^N)$ space and crashes at N=30), you must use **Branch and Bound** with Matrix Reduction, which uses very little space and heavily prunes the search tree to solve much larger datasets on average.

**Input:** An N x N integer adjacency matrix.
**Output:** The minimum total distance of the exact optimal tour.

## When to use it

- To find the exact mathematical minimum route for a Travelling Salesman Problem when N is roughly between 20 and 60.

## Approach

We explore the state-space tree where Level 0 is the starting city, Level 1 is picking the next city, etc.
To use Best-First Search Branch and Bound, we need an incredibly tight **Lower Bound** mathematical formula. If we are currently at City 2, what is the absolute minimum distance required to finish the tour?
We calculate this using the **Reduced Matrix** technique!

1. **Matrix Reduction:** A matrix is "reduced" if every row and every column contains at least one `0`.
   - To reduce a row, find its minimum element, and subtract that minimum from every cell in the row.
   - To reduce a column, find its minimum element, and subtract it from every cell in the column.
   - **The Magic Insight:** The total amount we subtracted from all rows and columns is the absolute mathematical lower bound cost of *any* tour utilizing this matrix! (Because every city must be entered and exited, you *must* pay at least the row minimum and the column minimum).

2. **Branching:** If we are at City i and decide to travel to City j:
   - The cost of this specific branch is: `cost_matrix[i][j]`.
   - We create a new matrix for this child node. Since we left i and arrived at j, we cannot leave i again or arrive at j again! We set row i and column j to infinity (`inf`).
   - We also cannot travel directly back from j to the start of our path, so we set `cost_matrix[j][start_city] = inf`.
   - Now, we **reduce this new child matrix**.
   - The Lower Bound for this child node is: `Parent_Bound + cost_matrix[i][j] + Total_Reduction_Cost_Of_Child_Matrix`.

3. **Best-First Search:** Insert all child nodes into a Priority Queue ordered by this Lower Bound. Always expand the node with the lowest bound until we reach a leaf node (a complete tour). Since it's a Min-Heap, the first complete tour popped is guaranteed to be optimal!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bb_06: TSP via Reduced Matrix (B&B).

Solve the traveling salesman problem using the
"""


def solve(cost, n):
    """TSP via reduced-matrix LC branch and bound.

    Each live node has: (lb, path, matrix, cost_so_far).
    Lower bound = path cost + row/column reduction cost.
    Branching: include or exclude the next edge from the
    current node to an unvisited city.
    """
    INF = float("inf")
    N_MAX = 12
    if n <= 1:
        return 0
    if n == 2:
        return cost[0][1] + cost[1][0]

    def reduce(mat):
        """Return (reduced_matrix, reduction_cost)."""
        red = [row[:] for row in mat]
        reduction = 0
        # Row reduction.
        for i in range(n):
            finite = [v for v in red[i] if v < INF]
            if not finite:
                continue
            min_val = min(finite)
            if min_val == 0:
                continue
            reduction += min_val
            for j in range(n):
                if red[i][j] < INF:
                    red[i][j] -= min_val
        # Column reduction.
        for j in range(n):
            col_vals = [red[i][j] for i in range(n) if red[i][j] < INF]
            if not col_vals:
                continue
            min_val = min(col_vals)
            if min_val == 0:
                continue
            reduction += min_val
            for i in range(n):
                if red[i][j] < INF:
                    red[i][j] -= min_val
        return red, reduction

    # Each priority queue entry:
    # (lb, path_tuple, matrix, cost_so_far, parent_reduction)
    # lb = cost_so_far + (current reduction). The reduction at
    # this node has been accounted for in `lb`; for the child,
    # we use: new_lb = lb + edge_cost + (new_reduction - old_reduction).
    import heapq
    root_red, root_red_cost = reduce(cost)
    pq = [(root_red_cost, (0,), tuple(tuple(row) for row in root_red), 0, root_red_cost)]
    best = INF
    while pq:
        lb, path, mat_t, cost_so_far, parent_red = heapq.heappop(pq)
        if lb >= best:
            continue
        if len(path) == n:
            # Complete tour: return to start.
            total = cost_so_far + cost[path[-1]][0]
            if total < best:
                best = total
            continue
        # Branch: try each unvisited city from path[-1].
        cur = path[-1]
        for nxt in range(n):
            if nxt in path:
                continue
            edge_cost = cost[cur][nxt]
            if edge_cost >= INF:
                continue
            new_mat = [list(row) for row in mat_t]
            for j in range(n):
                new_mat[cur][j] = INF
            for i in range(n):
                new_mat[i][nxt] = INF
            new_mat[nxt][0] = INF
            new_red, new_red_cost = reduce(new_mat)
            new_lb = lb + edge_cost + (new_red_cost - parent_red)
            if new_lb < best:
                new_path = path + (nxt,)
                heapq.heappush(pq, (new_lb, new_path,
                                    tuple(tuple(row) for row in new_red),
                                    cost_so_far + edge_cost,
                                    new_red_cost))
    return best if best < INF else -1
```

</details>

## Walk-through

*(Conceptual)*
If reducing the root matrix subtracts 10 from the rows and 5 from the columns, the absolute minimum cost of *any* tour is 15. Root node pushed to Heap with `cost=15`.

Pop Root. Try travelling `0 -> 1`.
- The distance `matrix[0][1]` was 3 (after root reduction).
- Create child matrix. Set Row 0 and Col 1 to `inf`. Set `1 -> 0` to `inf`.
- Reduce child matrix. Suppose it costs 2 to reduce it.
- Bound for `0 -> 1` branch = `Parent_Cost (15) + Edge (3) + Child_Reduction (2) = 20`.
- Push to Heap.

If `0 -> 2` results in a Bound of 18, the Priority Queue will expand `0 -> 2` first!

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^3)$ | $O(N^2)$ |
| **Average** | Much faster than DP! | $O(Nodes * N^2)$ |
| **Worst** | $O(N!)$ | $O(N! * N^2)$ |

In the absolute mathematical worst-case where no pruning occurs, the tree expands N! leaves, and at each node, we do an $O(N^2)$ matrix copy and reduction!
However, the Matrix Reduction lower bound is so astonishingly tight and accurate that for practical datasets (e.g. 40 cities), Best-First Search dives directly to the solution, exploring a tiny fraction of the tree.
Space complexity is heavy, as every node in the Priority Queue holds a unique N x N matrix.

## Variants & optimizations

- **Held-Karp DP:** The exact opposite paradigm. Held-Karp takes exactly $O(N^2 2^N)$ time and space for *any* graph. B&B takes unpredictable time, but often scales to larger N because it avoids exploring the full state space.

## Real-world applications

- **Supply Chain Logistics:** Calculating exact minimal routing distances for fleet trucking distribution where fuel costs strictly require the absolute mathematical minimum.

## Related algorithms in cOde(n)

- **[graph_20 - TSP Held Karp DP](../graphs/graph_20_travelling-salesman-held-karp-dp.md)** — The Dynamic Programming exact solution to this same problem.
- **[bb_02 - Job Assignment (Hungarian)](bb_02_job-assignment-hungarian.md)** — Matrix reduction is the exact same fundamental mechanism that drives the Hungarian assignment algorithm!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
