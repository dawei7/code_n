# Topological Sort

| | |
|---|---|
| **ID** | `graph_07` |
| **Category** | graphs |
| **Complexity (required)** | $O(n²)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting) |

## Problem statement

Given a **directed acyclic graph (DAG)** `G = (V, E)`, find a
linear ordering of `V` such that for every edge `(u, v)`,
`u` comes before `v` in the ordering. This is a
**topological order** (or "topo sort").

**Input:** a directed acyclic graph.
**Output:** an ordering of vertices such that all edges go
"forward" in the order.

**Example:**

```
Build dependencies (directed):
  compiler → linker → binary
  compiler → ast → ir
  ast    → linker (after type check)

Edges: compiler→linker, compiler→ast, ast→ir, ast→linker, linker→binary

Topo sorts: [compiler, ast, linker, ir, binary]
            or [compiler, ast, ir, linker, binary]
            (many valid orderings)
```

## When to use it

- Asked whenever the problem is "do task A before B" with
  dependencies. The classic scheduling problem.
- Foundation for **build systems** (Make, Bazel, npm),
  **task schedulers**, **deadlock detection**, and
  **spreadsheet recalculation order**.

## Approach

Two equivalent approaches.

### Approach A: Kahn's algorithm (BFS-based)

Repeatedly remove vertices with **in-degree 0**. As we
remove them, decrement the in-degree of their neighbors;
any that hit 0 join the next batch.

```
topo_sort_kahn(G):
    in_deg = [0] * n
    for (u, v) in G.edges: in_deg[v] += 1
    queue = [v for v in V if in_deg[v] == 0]
    order = []
    while queue:
        u = queue.pop()
        order.append(u)
        for v in G[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
    if len(order) != n: raise "cycle detected"
    return order
```

**Pros:** naturally detects cycles. **Cons:** need a fresh
in-degree array.

### Approach B: DFS-based

Run DFS; emit each vertex in **reverse finish order**.

```
topo_sort_dfs(G):
    visited = set()
    order = []
    def go(u):
        visited.add(u)
        for v in G[u]:
            if v not in visited:
                go(v)
        order.append(u)            # post-order
    for v in V:
        if v not in visited: go(v)
    return reversed(order)
```

**Pros:** minimal state. **Cons:** also detects cycles (a
back edge means no valid topo order exists).

## Algorithm (pseudocode, Kahn)

```
topo_sort(G):
    n = len(G)
    in_deg = [0] * n
    for u in range(n):
        for v in G[u]:
            in_deg[v] += 1
    queue = deque()
    for v in range(n):
        if in_deg[v] == 0:
            queue.append(v)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in G[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
    if len(order) != n:
        raise ValueError("graph has a cycle")
    return order
```

## Walk-through

Graph (4 nodes, edges: 0→1, 0→2, 1→3, 2→3).

Adjacency: `0: [1, 2], 1: [3], 2: [3], 3: []`.

Initial: `in_deg = [0, 1, 1, 2]`. Queue: `[0]`.

| Iter | dequeue | update | queue after | order |
|---:|---|---|---|---|
| 1 | 0 | in_deg[1]=0, in_deg[2]=0, enqueue both | [1, 2] | [0] |
| 2 | 1 | in_deg[3]=1 | [2] | [0, 1] |
| 3 | 2 | in_deg[3]=0, enqueue | [3] | [0, 1, 2] |
| 4 | 3 | (no neighbors) | [] | [0, 1, 2, 3] |

Topo order: `[0, 1, 2, 3]`. ✓ (All edges go forward: 0→1 ✓,
0→2 ✓, 1→3 ✓, 2→3 ✓.)

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V)$ |
| **Average** | $O(V + E)$ | $O(V)$ |
| **Worst** | $O(V + E)$ | $O(V)$ |

For adjacency-matrix representations, the required
complexity is $O(V²)$.

## Variants & optimizations

- **Lexicographically smallest topo sort** — when multiple
  in-degree-0 vertices are available, pick the smallest
  first. Use a min-heap instead of a FIFO queue.
- **All topo sorts** — backtracking: pick an in-degree-0
  vertex, recurse, un-pick. Exponential in the worst case
  (rare in practice).
- **Parallel topological sort** — many independent
  in-degree-0 vertices can be processed in parallel.
- **Topo sort with prerequisites** — given as constraints
  (a, b) meaning "a before b", build the adjacency and run.
- **Topo sort on a cycle** — detect the cycle (e.g. the
  remaining vertices with non-zero in-degree), report.

## Real-world applications

- **Build systems** — Make, CMake, Bazel, npm, cargo all
  use topo sort to determine build order.
- **Task scheduling** — "do A before B" with constraints.
- **Course prerequisite planning** — "take intro_01 before
  dp_01".
- **Spreadsheet recalc** — which cells depend on which
  others.
- **Linker** — object file symbol resolution.
- **Deadlock detection** — find a cycle in the resource
  wait-for graph.
- **Instruction scheduling** — compiler reorders
  instructions respecting data dependencies.

## Related algorithms in cOde(n)

- **[graph_03 — DFS](graph_03_dfs.md)** — the DFS-based
  topo sort uses this. (d=4/10, r=8/10)
- **[graph_02 — BFS](graph_02_bfs.md)** — Kahn's algo uses
  BFS-style layer processing. (d=4/10, r=8/10)
- **[graph_11 — Cycle Detection](graph_11_cycle-detection.md)** —
  topo sort fails on cyclic graphs; cycle detection
  precedes topo sort. (d=4/10, r=8/10)
- **[graph_15 — Tarjan's SCC](graph_15_tarjans-scc.md)** —
  on a general directed graph, first find SCCs, then
  topo-sort the condensation (DAG of SCCs). (d=6/10, r=8/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
