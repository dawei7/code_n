# Bridges in a Graph (Cut Edges)

| | |
|---|---|
| **ID** | `graph_14` |
| **Category** | graphs |
| **Complexity (required)** | $O(V + E)$ Time, $O(V)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 5/10 |
| **LeetCode Equivalent** | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) |

## Problem statement

Given an undirected graph. Find all the Bridges in the graph.
A Bridge (or Cut Edge) is an edge that, if removed, would increase the number of disconnected components in the graph.

**Input:** Number of vertices `V` and an adjacency list `adj`.
**Output:** A list of edges `[u, v]` that are Bridges.

## When to use it

- To identify "Critical Connections" in a network.
- When asked to find single-point-of-failure edges rather than vertices.

## Approach

This algorithm is essentially identical to **Articulation Points (`graph_13`)**. You must read and understand that algorithm first. We use Tarjan's Discovery Time (`tin`) and Lowest Time (`low`) arrays.

**The Magic Condition (Modified):**
Let's say we are at node `U`, and we traverse an edge to recursively call DFS on a neighbor `V`.
When `DFS(V)` returns, we update `U`'s lowest time: `low[U] = min(low[U], low[V])`.
Now, how do we know if the edge U - V is a Bridge?

In Articulation Points, the condition was `low[V] >= tin[U]`. This meant the subtree V could reach as high as U, but no higher. Removing U partitions the graph.
But for Bridges, we are not removing U, we are removing the edge U - V itself!
If the subtree V can reach U (meaning `low[V] == tin[U]`), it means there is an alternative Back-Edge from the subtree pointing directly to U! So, if we remove the primary edge U - V, the subtree is STILL connected to U via that back-edge! The graph is not partitioned.

Therefore, for an edge U - V to be a Bridge, the subtree V must have NO BACK-EDGES capable of reaching U or higher! The absolute lowest node it can reach must be strictly below U.
Thus, the condition is **strictly greater**: **`low[V] > tin[U]`**.

*(Bonus: Because we are dealing with edges instead of vertices, the annoying "Root Node" edge case from Articulation Points completely disappears! The logic applies universally to all nodes including the root).*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_14: Bridges.

Tarjan-style DFS on an undirected graph. An edge (u, v) is a
bridge iff, in the DFS tree, ``low[v] > disc[u]``. The result
is the sorted list of (u, v) bridge tuples with u < v.
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
    bridges = set()

    def dfs(u, parent, time):
        disc[u] = low[u] = time
        time += 1
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, u, time)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((min(u, v), max(u, v)))
            elif v != parent:
                low[u] = min(low[u], disc[v])
        return time

    dfs(0, -1, 0)
    return sorted(bridges)
```

</details>

## Walk-through

`V = 5`. Edges: `0-1`, `1-2`, `2-0`, `1-3`, `3-4`.
Graph is a triangle `{0, 1, 2}` connected to a line `1-3-4`.
Intuitively, `1-3` and `3-4` are the bridges. The triangle has redundant edges.

1. `dfs(0, -1)`. `tin[0]=1, low[0]=1`.
   - `dfs(1, 0)`. `tin[1]=2, low[1]=2`.
2. `dfs(1, 0)`:
   - `dfs(2, 1)`. `tin[2]=3, low[2]=3`.
3. `dfs(2, 1)`:
   - Neighbor `0`. Back-edge! `low[2] = min(3, 1) = 1`.
   - Returns to `dfs(1)`.
4. `dfs(1)` resumes:
   - Updates `low[1] = min(2, 1) = 1`.
   - Condition: `low[2] > tin[1]` -> `1 > 2`. FALSE. `1-2` is NOT a bridge.
   - Neighbor `3`. `dfs(3, 1)`.
5. `dfs(3, 1)`:
   - `dfs(4, 3)`. `tin[4]=5, low[4]=5`.
6. `dfs(4, 3)`:
   - No neighbors. Returns to `dfs(3)`.
7. `dfs(3)` resumes:
   - Updates `low[3] = min(4, 5) = 4`.
   - Condition: `low[4] > tin[3]` -> `5 > 4`. TRUE!
   - Append `[3, 4]` to bridges!
   - Returns to `dfs(1)`.
8. `dfs(1)` resumes:
   - Updates `low[1] = min(1, 4) = 1`.
   - Condition: `low[3] > tin[1]` -> `4 > 2`. TRUE!
   - Append `[1, 3]` to bridges!

Result: `[[3, 4], [1, 3]]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V + E)$ |
| **Average** | $O(V + E)$ | $O(V + E)$ |
| **Worst** | $O(V + E)$ | $O(V + E)$ |

Just like Articulation Points, this is exactly one complete DFS traversal evaluating every edge. Time complexity is strictly $O(V + E)$.
Space complexity is $O(V)$ for arrays and the recursion stack, plus $O(E)$ worst-case to store the output array of bridges.

## Variants & optimizations

- **2-Edge-Connected Components:** If you find all bridges and physically remove them from the graph, the remaining disjoint subgraphs are called "2-Edge-Connected Components". Within these components, there are at least 2 separate paths between any pair of nodes (meaning any single edge can fail and the component remains connected).

## Real-world applications

- **Traffic Engineering:** Identifying "chokepoint" roads. If a bridge edge is closed due to an accident, there is mathematically no alternative detour; the city is partitioned.
- **Circuit Design:** Finding critical wires whose severing breaks the circuit completely.

## Related algorithms in cOde(n)

- **[graph_13 - Articulation Points](graph_13_articulation-points.md)** — The vertex-equivalent of this algorithm.
- **[graph_15 - Tarjan's SCC](graph_15_tarjan-s-scc.md)** — The generalization of this logic to Directed graphs to find components that are mutually reachable.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
