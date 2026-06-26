# Depth-First Search (DFS)

| | |
|---|---|
| **ID** | `graph_03` |
| **Category** | graphs |
| **Complexity (required)** | $O(n²)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) |

## Problem statement

Given a graph `G = (V, E)` and a source vertex `s`, traverse
the graph by going **as deep as possible** before
backtracking. Output: the DFS order, the discovery and
finish times (in a directed graph), the parent of each
vertex, and the connected components reachable from `s`.

**Input:** a graph (adjacency list or matrix), a source `s`.
**Output:** DFS order, parent array, connected components.

**Example:**

```
    0 - 1 - 3
    |   |   |
    2 - 4   5
    |
    6

Adjacency:
  0: [1, 2]
  1: [0, 3, 4]
  2: [0, 4, 6]
  3: [1, 5]
  4: [1, 2]
  5: [3]
  6: [2]

DFS from 0:
  Order (discovery times):  0(0), 1(1), 3(2), 5(3),
                            [backtrack 5, 3] 4(4), [b 4] 2(5), 6(6)
  Parents: 0:None, 1:0, 3:1, 5:3, 4:1, 2:0, 6:2
```

## When to use it

- The other fundamental graph search. Asked in some form at
  every interview; often paired with BFS.
- Foundation for **topological sort**, **cycle detection**,
  **strongly connected components**, **bipartite check**,
  **articulation points & bridges**, **maze solving**, and
  **path existence** queries.

## Approach

DFS uses a **LIFO stack** (or recursion, which uses the
call stack). The invariant: when a vertex is "finished",
all its descendants have been fully explored.

Two equivalent formulations:

**Recursive** (cleaner, may stack-overflow on very deep
graphs):
```
dfs(u):
    mark u as visited
    time += 1; disc[u] = time
    for v in G[u]:
        if v not visited:
            parent[v] = u
            dfs(v)
    time += 1; finish[u] = time
```

**Iterative** (explicit stack, no recursion limit):
```
push (s, 0)  # (vertex, neighbor-index)
while stack:
    u, i = stack[-1]
    if i < len(G[u]):
        v = G[u][i]
        stack[-1] = (u, i + 1)
        if v not visited:
            mark v as visited
            parent[v] = u
            push (v, 0)
    else:
        stack.pop()
        finish u
```

**Performance:** $O(V + E)$ for adjacency list, $O(V²)$ for
matrix. Same as BFS, but DFS uses much less memory in
practice (the stack is depth-bounded, the queue can hold
the whole frontier).

**Why use DFS over BFS:** DFS is better for:
- Topological sort (we need finish times).
- Cycle detection (back edges).
- Tree-structured problems (path sum, etc.).
- Memory efficiency when the graph is "tall" (a long path
  before the next branching).

## Algorithm (pseudocode, recursive)

```
dfs(G, s):
    visited = set()
    parent = {}
    order = []
    def go(u):
        visited.add(u)
        order.append(u)
        for v in G[u]:
            if v not in visited:
                parent[v] = u
                go(v)
    go(s)
    return order, parent
```

For **all connected components**, wrap with:
```
for v in G:
    if v not in visited:
        go(v)
```

## Walk-through

Graph from the example. DFS from `s = 0`.

`go(0)`: visit 0. Neighbors: 1 (unvisited), 2 (unvisited).
Pick 1.
- `go(1)`: visit 1. Neighbors: 0 (visited), 3 (unvisited), 4 (unvisited).
  Pick 3.
  - `go(3)`: visit 3. Neighbors: 1 (visited), 5 (unvisited). Pick 5.
    - `go(5)`: visit 5. Neighbors: 3 (visited). Backtrack.
  - Back at 3, no more unvisited neighbors. Backtrack.
- Back at 1, next unvisited: 4.
  - `go(4)`: visit 4. Neighbors: 1 (visited), 2 (unvisited). Pick 2.
    - `go(2)`: visit 2. Neighbors: 0 (visited), 4 (visited), 6 (unvisited). Pick 6.
      - `go(6)`: visit 6. Neighbors: 2 (visited). Backtrack.
    - Back at 2, no more unvisited. Backtrack.
  - Back at 4, no more unvisited. Backtrack.
- Back at 1, no more unvisited. Backtrack.
- Back at 0, next unvisited: 2 (already visited). Done.

DFS order: `[0, 1, 3, 5, 4, 2, 6]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V)$ |
| **Average** | $O(V + E)$ | $O(V)$ |
| **Worst** | $O(V + E)$ | $O(V)$ |

Recursive DFS uses $O(depth)$ stack space; iterative uses
$O(depth)$ explicit-stack space too. The "$O(V)$" is for the
visited set and parent array; the actual stack can be much
less in practice (worst case: V).

The required complexity is $O(n²)$ for cOde(n)'s matrix variant.

## Variants & optimizations

- **Topological sort** — DFS on a DAG, output vertices in
  reverse finish order. $O(V + E)$.
- **Cycle detection** — in undirected: any back edge is a
  cycle. In directed: a back-edge to an ancestor (using the
  gray/black coloring) is a cycle.
- **Strongly connected components** — Tarjan's or Kosaraju's
  algorithm, both based on DFS. $O(V + E)$. See `graph_15`
  and `graph_16`.
- **Bipartite check** — 2-color the levels; if a back edge
  connects same-color vertices, not bipartite.
- **Articulation points / bridges** — DFS tree + low-link
  values. See `graph_13`, `graph_14`.
- **Iterative deepening DFS (IDDFS)** — DFS with a depth
  limit, increasing the limit on each iteration. Combines
  DFS's space efficiency with BFS's completeness.

## Real-world applications

- **Maze solving** — DFS finds any path; BFS finds shortest.
- **Topological scheduling** — task ordering with dependencies.
- **Strongly connected components** — analyzing social
  networks, web graphs.
- **Cycle detection in dependency graphs** — package
  managers (npm, pip) use it to find circular deps.
- **Garbage collection** — some GCs use DFS instead of BFS.
- **SCC-based 2-SAT solver** — boolean satisfiability for
  2-CNF formulas.
- **Tarjan's bridge-finding** — single-points-of-failure
  analysis in networks.

## Related algorithms in cOde(n)

- **[graph_02 — BFS](graph_02_bfs.md)** — the other
  fundamental search. (d=4/10, r=8/10)
- **[graph_07 — Topological Sort](graph_07_topological-sort.md)** —
  DFS on a DAG. (d=5/10, r=8/10)
- **[graph_11 — Cycle Detection](graph_11_cycle-detection.md)** —
  DFS with back-edge detection. (d=4/10, r=8/10)
- **[graph_15 — Tarjan's SCC](graph_15_tarjans-scc.md)** —
  DFS with low-link values. (d=6/10, r=8/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
