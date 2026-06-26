# M-Coloring Problem

| | |
|---|---|
| **ID** | `graph_19` |
| **Category** | graphs |
| **Complexity (required)** | $O(M^V)$ Time, $O(V)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [m Coloring Problem](https://www.geeksforgeeks.org/m-coloring-problem/) |

## Problem statement

Given an undirected graph and an integer `M`. Determine if it is possible to color every vertex using at most `M` different colors, such that no two adjacent vertices share the same color.

**Input:** Number of vertices `V`, an adjacency list `adj` (or matrix), and an integer `M`.
**Output:** A boolean. `True` if a valid coloring exists, `False` otherwise.

## When to use it

- When M = 2, this is just the $O(V+E)$ Bipartite Graph Check (`graph_12`).
- When M \ge 3, the problem becomes **NP-Complete**. There is no polynomial-time algorithm. You MUST use Backtracking.
- When you need to solve scheduling or map-coloring constraints.

## Approach

**1. The Backtracking State-Space Tree:**
Since there is no clever graph algorithm to solve this, we must brute-force it smartly using Backtracking (`backtracking_01`).
Our state is simply a `colors[]` array tracking the color assignment (from 1 to M) for each vertex `0` through `V-1`.

**2. The Recursive Step:**
Start at vertex `0`.
Try assigning color `1`. Is it safe? (Check all neighbors of vertex `0`. Does any neighbor currently have color `1`? If not, it's safe!).
If it's safe, temporarily assign `colors[0] = 1`, and recursively move to vertex `1`!
If vertex `1` successfully finds a valid color, keep moving forward!
If we ever hit a vertex where NONE of the `M` colors are safe, the recursion returns `False`.
This triggers a backtrack! The previous vertex undoes its color assignment `colors[i] = 0`, and tries the next color in the loop.

**3. Termination:**
If our recursive function successfully reaches vertex `V` (meaning it successfully assigned a color to `V-1`), we found a valid global coloring! Return `True`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_19: M-Coloring Problem.

Return True iff the graph can be colored with m colors
such that no two adjacent vertices share a color.

Backtracking: assign colors to vertices one at a time.
At each step, try each color; if it doesn't conflict with
any already-colored neighbor, recurse.
"""


def solve(n, edges, m):
    if n == 0:
        return True
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    color = [-1] * n

    def safe(v, c):
        for u in adj[v]:
            if color[u] == c:
                return False
        return True

    def helper(v):
        if v == n:
            return True
        for c in range(m):
            if safe(v, c):
                color[v] = c
                if helper(v + 1):
                    return True
                color[v] = -1
        return False

    return helper(0)
```

</details>

## Walk-through

`V = 4`. `M = 3`. Graph is a complete graph K_4 (every node connected to every other node).
`adj = {0:[1,2,3], 1:[0,2,3], 2:[0,1,3], 3:[0,1,2]}`.

1. `curr = 0`:
   - Try color 1. Safe. `colors[0] = 1`. Recurse.
2. `curr = 1`:
   - Try color 1. Unsafe (neighbor 0 is 1).
   - Try color 2. Safe. `colors[1] = 2`. Recurse.
3. `curr = 2`:
   - Try color 1. Unsafe.
   - Try color 2. Unsafe.
   - Try color 3. Safe. `colors[2] = 3`. Recurse.
4. `curr = 3`:
   - Try color 1. Unsafe.
   - Try color 2. Unsafe.
   - Try color 3. Unsafe.
   - Loop ends. Returns `False`.
5. Backtracks to `curr=2`.
   - `colors[2] = 0`. No more colors to try. Returns `False`.
6. Backtracks to `curr=1`.
   - `colors[1] = 0`. Try color 3. Safe. `colors[1] = 3`. Recurse.
7. `curr = 2`:
   - Try color 1. Unsafe.
   - Try color 2. Safe! `colors[2] = 2`. Recurse.
8. `curr = 3`:
   - Try color 1, 2, 3... all unsafe! Returns `False`.
9. The entire tree eventually evaluates to `False`. A complete graph of 4 nodes requires exactly 4 colors.

Result `False`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V)$ | $O(V)$ |
| **Average** | $O(M^V)$ | $O(V)$ |
| **Worst** | $O(M^V)$ | $O(V)$ |

At each of the V vertices, we loop through M possible color choices. This creates an M-ary tree of depth V.
The total number of theoretical nodes in the state-space tree is M^V.
At each node, `is_safe` takes $O(V)$ time. Thus, worst-case time is strictly bounded by $O(V \cdot M^V)$.
Space complexity is strictly $O(V)$ for the `colors` array and the depth of the recursion stack.

## Variants & optimizations

- **Degree Ordering (Heuristic Optimization):** Instead of processing nodes in numerical order `0, 1, 2...`, sort the vertices by their degree (number of edges) in descending order! Coloring the most highly constrained (connected) nodes first drastically prunes the backtracking tree early on, drastically improving average-case runtime.
- **Four Color Theorem:** In planar graphs (graphs that can be drawn on 2D paper without edges crossing, like a physical map of countries), M=4 is mathematically ALWAYS sufficient to color the graph! This was the first major mathematical theorem proven by a computer.

## Real-world applications

- **Sudoku Solvers:** A Sudoku board is just an 81-node graph where M=9. Edges exist between any two cells in the same row, column, or 3x3 box. The exact same backtracking code solves Sudoku!
- **University Timetabling:** Nodes are Exams. Edges exist between two exams if a student is enrolled in both. M is the number of available time slots. If the graph is M-colorable, a conflict-free schedule exists!

## Related algorithms in cOde(n)

- **[graph_12 - Bipartite Check](graph_12_bipartite-check.md)** — The M=2 special case which is linearly solvable using BFS.
- **[backtracking_01 - Subset Sum Decision](../backtracking/backtrack_01_subset-sum-decision.md)** — The foundational pattern for all NP-Complete exhaustive search algorithms.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
