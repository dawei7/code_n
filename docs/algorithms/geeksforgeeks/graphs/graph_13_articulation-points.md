# Articulation Points (Cut Vertices)

| | |
|---|---|
| **ID** | `graph_13` |
| **Category** | graphs |
| **Complexity (required)** | $O(V + E)$ Time, $O(V)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Articulation Points (or Cut Vertices) in a Graph](https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/) |

## Problem statement

Given an undirected graph. Find all the Articulation Points in the graph.
An Articulation Point (or Cut Vertex) is a vertex that, if removed (along with all edges attached to it), would increase the number of disconnected components in the graph. In other words, its removal would split a connected graph into two or more separate pieces.

**Input:** Number of vertices `V` and an adjacency list `adj`.
**Output:** A list of vertices that are Articulation Points.

## When to use it

- To identify single points of failure in a network (e.g., a central router whose destruction would partition the internet).
- Uses Tarjan's Discovery/Lowest Time logic (a foundational advanced graph concept).

## Approach

**1. The DFS Spanning Tree:**
Imagine running a standard DFS and drawing solid lines for the edges we traverse. This forms a "DFS Spanning Tree".
Any edge in the original graph that we DIDN'T traverse (because it led to an already-visited node) is called a **Back-Edge**. Back-edges point UP the tree to an ancestor.

**2. Discovery Time (`tin`) and Lowest Time (`low`):**
We assign a "Discovery Time" (`tin`) to every node. It's just a counter that increments every time we visit a new node.
We also assign a "Lowest Time" (`low`). This represents the absolute lowest `tin` reachable from this node, *including taking exactly ONE back-edge*.
Initially, for any node, `low[node] = tin[node]`.

**3. The Magic Condition:**
Let's say we are at node `U`, and we recursively call DFS on a neighbor `V`.
When `DFS(V)` returns, we update `U`'s lowest time: `low[U] = min(low[U], low[V])`.
Now, how do we know if `U` is an Articulation Point?
If `low[V] >= tin[U]`, it means the subtree rooted at `V` has NO back-edges pointing higher than `U`! The absolute highest it can reach is `U` itself. Therefore, if we completely remove `U`, the subtree `V` will be completely severed from the rest of the graph!
Thus, **`U` is an Articulation Point!**

**4. The Root Node Edge Case:**
The root node of our DFS has no ancestors, so `tin[U]` is 1. All its children will logically have `low[V] >= 1`. Does that make the root an Articulation Point? Not necessarily!
The root is ONLY an Articulation Point if it has **more than one independent DFS child**. (If it only has 1 child, removing the root just removes the top of a chain, it doesn't partition anything).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_13: Articulation Points.

Tarjan-style DFS on an undirected graph. A node u is an
articulation point iff one of its DFS-tree children v has
``low[v] >= disc[u]`` (and u is not the root, OR u is the
root with more than one DFS child). The result is the sorted
list of articulation point indices.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [set() for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    parent = [-1] * num_nodes
    ap = set()

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        children = 0
        for v in sorted(adj[u]):
            if disc[v] == -1:
                parent[v] = u
                children += 1
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    ap.add(u)
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, 0)
    return sorted(ap)
```

</details>

## Walk-through

`V = 5`. Edges: `0-1`, `1-2`, `2-0`, `1-3`, `3-4`.
Graph is a triangle `{0, 1, 2}` connected to a line `1-3-4`.
Intuitively, `1` and `3` are the articulation points.

1. `dfs(0, -1)`. `tin[0]=1, low[0]=1`.
   - Neighbor `1`. `dfs(1, 0)`.
2. `dfs(1, 0)`. `tin[1]=2, low[1]=2`.
   - Neighbor `2`. `dfs(2, 1)`.
3. `dfs(2, 1)`. `tin[2]=3, low[2]=3`.
   - Neighbor `0`. Visited! Back-edge!
   - `low[2] = min(low[2], tin[0]) = min(3, 1) = 1`.
   - Return to `dfs(1)`.
4. `dfs(1)` resumes:
   - Updates `low[1] = min(low[1], low[2]) = min(2, 1) = 1`.
   - Condition: `low[2] >= tin[1]` -> `1 >= 2`. FALSE.
   - Neighbor `3`. `dfs(3, 1)`.
5. `dfs(3, 1)`. `tin[3]=4, low[3]=4`.
   - Neighbor `4`. `dfs(4, 3)`.
6. `dfs(4, 3)`. `tin[4]=5, low[4]=5`.
   - No neighbors. Return to `dfs(3)`.
7. `dfs(3)` resumes:
   - Updates `low[3] = min(low[3], low[4]) = min(4, 5) = 4`.
   - Condition: `low[4] >= tin[3]` -> `5 >= 4`. TRUE!
   - `3` is an Articulation Point! (Parent is not -1).
   - Return to `dfs(1)`.
8. `dfs(1)` resumes:
   - Updates `low[1] = min(low[1], low[3]) = min(1, 4) = 1`.
   - Condition: `low[3] >= tin[1]` -> `4 >= 2`. TRUE!
   - `1` is an Articulation Point!
9. `dfs(0)` resumes. `children = 1`. Root condition fails.

Result: `{1, 3}`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V)$ |
| **Average** | $O(V + E)$ | $O(V)$ |
| **Worst** | $O(V + E)$ | $O(V)$ |

This is exactly one complete DFS traversal. We do constant $O(1)$ math at each step to maintain the `tin` and `low` arrays. Therefore, the time complexity is strictly $O(V + E)$.
Space complexity is $O(V)$ for the `tin` array, `low` array, `visited` set, and the recursion stack.

## Variants & optimizations

- **Bridges (`graph_14`):** If you want to find Cut *Edges* instead of Cut *Vertices*, the algorithm is 99% identical! The only difference is the math condition becomes strictly greater: `low[neighbor] > tin[curr]`.

## Real-world applications

- **Network Vulnerability Analysis:** Finding the exact servers or physical cables whose destruction would partition a local LAN or a global power grid, allowing engineers to build targeted redundancies.

## Related algorithms in cOde(n)

- **[graph_14 - Bridges in a Graph](graph_14_bridges.md)** — The edge-equivalent of this exact algorithm.
- **[graph_15 - Tarjan's SCC](graph_15_tarjan-s-scc.md)** — Tarjan's master algorithm for Directed Graphs, which uses the exact same `tin` and `low` mechanism to find Strongly Connected Components.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
