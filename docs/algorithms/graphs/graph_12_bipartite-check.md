# Bipartite Graph Check

| | |
|---|---|
| **ID** | `graph_12` |
| **Category** | graphs |
| **Complexity (required)** | $O(V + E)$ Time, $O(V)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) |

## Problem statement

Given an undirected graph represented as an adjacency list. Determine if the graph is Bipartite.
A graph is bipartite if its vertices can be divided into two independent sets, U and V, such that every edge connects a vertex in U to a vertex in V.
Equivalently: Can you color every node in the graph using exactly 2 colors such that no two adjacent nodes share the same color?

**Input:** Number of vertices `V` and an adjacency list `adj`.
**Output:** A boolean. `True` if the graph is bipartite, `False` otherwise.

## When to use it

- When checking if elements can be separated into two mutually exclusive groups (e.g., matching applicants to jobs, checking if a group of people can be split into two rival teams where no friends are on the same team).
- *Mathematical property:* A graph is bipartite if and only if it contains NO cycles of ODD length.

## Approach

**The 2-Coloring Method (BFS or DFS):**
We can solve this easily using Breadth-First Search (BFS).
We maintain an array `colors[]` initialized to -1 (uncolored). We will use `0` for Red and `1` for Blue.

1. Pick an uncolored node. Color it `0` (Red), and push it to a Queue.
2. While the Queue is not empty, pop a node `curr`.
3. Look at all its `neighbors`.
   - If a `neighbor` is uncolored (`-1`), color it with the OPPOSITE color of `curr` (`1 - colors[curr]`), and push it to the Queue!
   - If a `neighbor` IS already colored, check its color! If `colors[neighbor] == colors[curr]`, we have two adjacent nodes with the exact same color! The graph is NOT bipartite! Return `False`.
4. If the queue empties and no conflicts occurred, the connected component is bipartite.
5. Because the graph might be disconnected, wrap this logic in a `for` loop across all V vertices.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_12: Bipartite Check.

BFS-based 2-coloring. A graph is bipartite iff no node is forced
to have the same color as an already-colored neighbor.
"""


def solve(num_nodes, edges):
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    color = [-1] * num_nodes
    for start in range(num_nodes):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
```

</details>

## Walk-through

`V = 4`. Graph: `0-1`, `0-3`, `1-2`, `2-3`. (A square cycle).
`adj = {0:[1,3], 1:[0,2], 2:[1,3], 3:[0,2]}`.
`colors = [-1, -1, -1, -1]`.

1. Loop `i=0`. Uncolored.
   - `colors[0] = 0`. `queue = [0]`.
2. `curr = 0`.
   - Neighbors: `1`, `3`.
   - `1` uncolored. `colors[1] = 1 - 0 = 1`. `queue = [1]`.
   - `3` uncolored. `colors[3] = 1 - 0 = 1`. `queue = [1, 3]`.
3. `curr = 1`.
   - Neighbors: `0`, `2`.
   - `0` colored `0`. `colors[curr]` is `1`. Fine.
   - `2` uncolored. `colors[2] = 1 - 1 = 0`. `queue = [3, 2]`.
4. `curr = 3`.
   - Neighbors: `0`, `2`.
   - `0` colored `0`. `colors[curr]` is `1`. Fine.
   - `2` colored `0`. `colors[curr]` is `1`. Fine.
5. `curr = 2`.
   - Neighbors: `1`, `3`.
   - `1` colored `1`. `colors[curr]` is `0`. Fine.
   - `3` colored `1`. `colors[curr]` is `0`. Fine.

Result is `True`. (The sets are `{0, 2}` and `{1, 3}`).

*What if we added edge `0-2`? (Creating a triangle / odd cycle).*
At step 4, `curr=2` (color 0). Neighbor `0` is color 0.
Conflict! `0 == 0`. Returns `False`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V)$ |
| **Average** | $O(V + E)$ | $O(V)$ |
| **Worst** | $O(V + E)$ | $O(V)$ |

This is literally just a standard Breadth-First Search with one extra $O(1)$ array lookup per neighbor.
Every vertex is queued exactly once, and every edge is traversed twice. Time complexity is strictly $O(V + E)$.
Space complexity is $O(V)$ for the `colors` array and the BFS `queue`.

## Variants & optimizations

- **DFS Approach:** You can easily implement the exact same logic using a recursive DFS. Instead of pushing to a queue, you just call `if not dfs(neighbor, 1 - color): return False`. Time and space complexities are identical.
- **Graph Coloring (NP-Hard):** Determining if a graph is Bipartite is asking "Is this graph 2-colorable?". This is easy! However, asking "Is this graph 3-colorable?" or k-colorable is the famous Graph Coloring Problem, which is NP-Complete and requires Backtracking (`graph_19`)!

## Real-world applications

- **Recommendation Engines / Matching Algorithms:** Formulating dating apps (matching group A to group B) or ride-sharing networks (matching drivers to riders) mathematically requires modeling the system as a Bipartite Graph to run the Hopcroft-Karp algorithm for Maximum Bipartite Matching.

## Related algorithms in cOde(n)

- **[graph_02 - Breadth-First Search](graph_02_bfs.md)** — The core traversal algorithm.
- **[graph_19 - M-Coloring Problem](graph_19_m-coloring-problem.md)** — The generalization of this problem to M colors, which instantly elevates the difficulty from $O(V+E)$ linear to $O(M^V)$ exponential!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
