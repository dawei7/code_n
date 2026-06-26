# Strongly Connected Components (Tarjan's)

| | |
|---|---|
| **ID** | `graph_15` |
| **Category** | graphs |
| **Complexity (required)** | $O(V + E)$ Time, $O(V)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Tarjan's strongly connected components algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm) |

## Problem statement

Given a **Directed** Graph. Find all its Strongly Connected Components (SCCs).
An SCC is a maximal subset of vertices where every vertex can reach every other vertex in the subset. (In a directed graph, just because A \rightarrow B exists does not mean B can reach A).

**Input:** Number of vertices `V` and an adjacency list `adj`.
**Output:** A list of lists, where each inner list contains the vertices of one SCC.

## When to use it

- When you need to condense a Directed Graph with cycles into a Directed Acyclic Graph (DAG) by crushing every cycle into a single "super-node".
- To find mutually reachable clusters of nodes.

## Approach

Tarjan's Algorithm uses the exact same `tin` (Discovery Time) and `low` (Lowest Time) arrays from Articulation Points/Bridges (`graph_13`), but introduces a **Stack**.

**1. The SCC Root:**
In a DFS traversal, the first node of an SCC we visit is considered the "Root" of that SCC. Every other node in the SCC will be part of the DFS subtree under this root.
Because every node in an SCC can reach every other node, they all have back-edges connecting to each other!
Therefore, the `low` value for EVERY node in the SCC will eventually bubble down to match the `tin` value of the SCC Root!
Conclusion: A node `U` is the root of an SCC if and only if **`low[U] == tin[U]`** after exploring its entire subtree.

**2. The Stack:**
When we visit a node, we push it onto a `stack` and mark it as `on_stack = True`.
When we evaluate a neighbor V:
- If it's unvisited, we DFS into it, and `low[U] = min(low[U], low[V])`.
- If it IS visited, we check if it is `on_stack`. If it is, it's a back-edge! `low[U] = min(low[U], tin[V])`. (Notice we use `tin[V]`, not `low[V]`, to prevent cross-component leakage).
- If it's visited but NOT `on_stack`, it means it belongs to an entirely different SCC that was already completely processed and closed. We ignore it completely! (Cross-edge).

**3. Extracting the SCC:**
When `DFS(U)` finishes evaluating all neighbors, we check if `low[U] == tin[U]`.
If so, `U` is an SCC Root! That means every node currently sitting above `U` on the `stack` belongs to `U`'s SCC!
We pop nodes off the stack one by one, adding them to our current SCC component array, until we pop `U` itself.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_15: Tarjan's SCC.

Single-pass DFS on a directed graph that maintains each node's
discovery time and low-link value. When low[u] == disc[u], u
is the root of an SCC; pop the stack until u is removed.
Returns a list of SCCs, each sorted; outer list sorted by
smallest element.
"""


def solve(num_nodes, edges):
    if num_nodes <= 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    on_stack = [False] * num_nodes
    stack = []
    sccs = []

    def dfs(u, time):
        disc[u] = low[u] = time
        time += 1
        stack.append(u)
        on_stack[u] = True
        for v in sorted(adj[u]):
            if disc[v] == -1:
                time = dfs(v, time)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])
        if low[u] == disc[u]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == u:
                    break
            sccs.append(sorted(component))
        return time

    for start in range(num_nodes):
        if disc[start] == -1:
            dfs(start, 0)
    return sorted(sccs, key=lambda c: c[0])
```

</details>

## Walk-through

`V = 4`. Directed edges: `0->1`, `1->2`, `2->0`, `1->3`.
The triangle `{0, 1, 2}` is an SCC. `{3}` is its own SCC.

1. `dfs(0)`. `tin[0]=1, low[0]=1`. `stack=[0]`.
2. `dfs(1)`. `tin[1]=2, low[1]=2`. `stack=[0, 1]`.
3. `dfs(2)`. `tin[2]=3, low[2]=3`. `stack=[0, 1, 2]`.
   - Neighbor `0`. It's visited AND `on_stack`!
   - `low[2] = min(3, tin[0]) = 1`.
   - Returns to `dfs(1)`.
4. `dfs(1)` resumes:
   - Updates `low[1] = min(2, low[2]) = 1`.
   - Evaluates next neighbor `3`.
   - `dfs(3)`. `tin[3]=4, low[3]=4`. `stack=[0, 1, 2, 3]`.
5. `dfs(3)`:
   - No neighbors.
   - Check SCC: `low[3] == tin[3]` (4 == 4). TRUE!
   - Pop from stack until we hit `3`. We pop `3`.
   - `sccs.append([3])`. `stack = [0, 1, 2]`.
   - Returns to `dfs(1)`.
6. `dfs(1)` resumes:
   - Neighbors exhausted. Check SCC: `low[1] == tin[1]` (1 == 2). FALSE.
   - Returns to `dfs(0)`.
7. `dfs(0)` resumes:
   - Updates `low[0] = min(1, low[1]) = 1`.
   - Neighbors exhausted. Check SCC: `low[0] == tin[0]` (1 == 1). TRUE!
   - Pop from stack until we hit `0`. We pop `2`, `1`, `0`.
   - `sccs.append([2, 1, 0])`. `stack = []`.

Result: `[[3], [2, 1, 0]]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V)$ |
| **Average** | $O(V + E)$ | $O(V)$ |
| **Worst** | $O(V + E)$ | $O(V)$ |

This is a single-pass DFS. Each vertex is visited once, pushed to the stack once, and popped from the stack once. Each directed edge is traversed exactly once. Time complexity is highly optimized $O(V + E)$.
Space complexity is $O(V)$ to hold the `tin`, `low`, `on_stack`, and `stack` structures.

## Variants & optimizations

- **Kosaraju's Algorithm (`graph_16`):** The alternative to Tarjan's. It runs standard DFS once, physically REVERSES every edge in the entire graph, and then runs DFS again based on the exit order of the first pass! It is conceptually much easier to understand but requires two full passes and building a secondary reversed adjacency list.

## Real-world applications

- **2-SAT Problem:** In boolean logic, determining if an equation like `(A OR B) AND (!A OR C)` is satisfiable is solved by constructing an Implication Graph (`!A -> B, !B -> A...`). The equation is solvable if and only if NO variable and its negation exist within the exact same Strongly Connected Component!

## Related algorithms in cOde(n)

- **[graph_13 - Articulation Points](graph_13_articulation-points.md)** — The foundation of the `tin/low` concept for undirected graphs.
- **[graph_16 - Kosaraju's SCC](graph_16_kosaraju-s-scc.md)** — The alternative double-pass algorithm to find SCCs.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
