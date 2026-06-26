# Kosaraju's Algorithm (SCC)

| | |
|---|---|
| **ID** | `graph_16` |
| **Category** | graphs |
| **Complexity (required)** | $O(V + E)$ Time, $O(V + E)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Kosaraju's algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm) |

## Problem statement

Given a **Directed** Graph. Find all its Strongly Connected Components (SCCs).
An SCC is a maximal subset of vertices where every vertex can reach every other vertex in the subset.
*Constraint:* Solve this using the two-pass Kosaraju's Algorithm instead of Tarjan's single-pass algorithm.

**Input:** Number of vertices `V` and an adjacency list `adj`.
**Output:** A list of lists, where each inner list contains the vertices of one SCC.

## When to use it

- To find Strongly Connected Components when Tarjan's Algorithm (`graph_15`) is too difficult to remember. Kosaraju's logic is vastly simpler because it relies purely on standard DFS, at the cost of requiring two passes and a transposed graph in memory.

## Approach

**1. The Topological Sort Insight (Pass 1):**
Imagine a graph with two SCCs: SCC_1 and SCC_2. There is a directed edge connecting them: SCC_1 \rightarrow SCC_2.
If we run DFS starting from a node in SCC_1, it will explore all of SCC_1, cross the bridge, and explore all of SCC_2 before returning.
If we push nodes to a `stack` ONLY when their recursive DFS function completely finishes (just like in Topological Sort), the nodes in SCC_1 will end up at the TOP of the stack, and the nodes in SCC_2 will end up at the BOTTOM.
Why? Because DFS gets trapped in SCC_2! SCC_2 has no way to return to SCC_1, so SCC_2's DFS calls must finish first.

**2. Graph Transposition (Reversing the Edges):**
What if we take every directed edge U \rightarrow V in the graph and flip it to V \rightarrow U?
- Inside an SCC, reversing all edges changes nothing. It is still a cycle, and every node can still reach every other node.
- BUT, the bridge edge SCC_1 \rightarrow SCC_2 is reversed into SCC_2 \rightarrow SCC_1!

**3. The Second Pass:**
Let's pop nodes off the `stack` we built in Pass 1. The top of the stack is guaranteed to be a node from SCC_1.
We run a new DFS starting from this SCC_1 node on the **TRANSPOSED** graph.
Because the bridge edge was reversed, the DFS is now *trapped* inside SCC_1! It cannot reach SCC_2 anymore!
Therefore, whatever nodes this second DFS successfully visits constitutes exactly one pure SCC. We collect them, mark them visited, and pop the next unvisited node from the stack to find the next SCC!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_16: Kosaraju's SCC.

Two-pass DFS on a directed graph. Pass 1 walks the original
graph, pushing each node onto a stack when its DFS finishes.
Pass 2 walks the transpose graph in stack-pop order; each DFS
tree in pass 2 is one SCC. Outer list sorted by smallest
element.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    radj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)
    visited = [False] * num_nodes
    order = []

    def dfs1(u):
        visited[u] = True
        for v in sorted(adj[u]):
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(num_nodes):
        if not visited[u]:
            dfs1(u)
    visited = [False] * num_nodes
    sccs = []

    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in sorted(radj[u]):
            if not visited[v]:
                dfs2(v, comp)

    for u in reversed(order):
        if not visited[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(sorted(comp))
    return sorted(sccs, key=lambda c: c[0])
```

</details>

## Walk-through

`V = 4`. Directed edges: `0->1`, `1->2`, `2->0`, `1->3`.
The triangle `{0, 1, 2}` is SCC_1. `{3}` is SCC_2. The bridge is `1->3`.

**Pass 1:**
1. `dfs_pass1(0)`: Calls `dfs(1)`.
2. `dfs_pass1(1)`: Calls `dfs(2)` and `dfs(3)`.
3. `dfs_pass1(3)`: No unvisited neighbors. Finishes! `stack = [3]`.
4. `dfs_pass1(2)`: Neighbor `0` is visited. Finishes! `stack = [3, 2]`.
5. `dfs(1)` finishes. `stack = [3, 2, 1]`.
6. `dfs(0)` finishes. `stack = [3, 2, 1, 0]`.

**Transpose:**
Reversed edges: `1->0`, `2->1`, `0->2`, `3->1`.
Notice the bridge is now `3->1`. SCC_1 cannot reach SCC_2!

**Pass 2:**
1. Pop `0`. Unvisited. `dfs_pass2(0)` on reversed graph:
   - `0` reaches `2`. `2` reaches `1`. `1` tries to reach `0` (visited).
   - Trapped! Collects `[0, 2, 1]`. `sccs = [[0, 2, 1]]`.
2. Pop `1`. Visited. Skip.
3. Pop `2`. Visited. Skip.
4. Pop `3`. Unvisited. `dfs_pass2(3)` on reversed graph:
   - `3` tries to reach `1`. `1` is already visited!
   - Trapped! Collects `[3]`. `sccs = [[0, 2, 1], [3]]`.

Result: `[[0, 2, 1], [3]]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V + E)$ |
| **Average** | $O(V + E)$ | $O(V + E)$ |
| **Worst** | $O(V + E)$ | $O(V + E)$ |

We perform exactly two DFS traversals ($O(V+E)$ each) and one loop to build the transposed graph ($O(V+E)$). Total time complexity is strictly $O(V + E)$.
Space complexity is $O(V + E)$ because we MUST construct an entirely new Adjacency List to hold the reversed edges in memory. (This makes it noticeably more memory intensive than Tarjan's algorithm, which only uses $O(V)$ space for arrays).

## Variants & optimizations

- **Condensation Graph:** Once you find the SCCs using Kosaraju's, you can build a new "Condensation Graph" where every entire SCC is treated as a single massive vertex. The resulting graph is guaranteed to be a Directed Acyclic Graph (DAG), which unlocks Topological Sorting and simple DP pathfinding logic!

## Real-world applications

- **Twitter / Social Networks:** Finding isolated communities or echo chambers. If a group of 100 users all follow each other (creating an SCC), but nobody outside the group follows them, Kosaraju's identifies the cluster instantly.

## Related algorithms in cOde(n)

- **[graph_15 - Tarjan's SCC](graph_15_tarjan-s-scc.md)** — The one-pass algorithm that does not require building a transposed graph.
- **[graph_07 - Topological Sort](graph_07_topological-sort.md)** — The foundation of Pass 1 (pushing nodes to a stack based on finish time).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
