# Guided Example: Shortest Cycle in a Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 7, "edges": [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a **bi-directional **graph with `n` vertices, where each vertex is labeled from `0` to $n - 1$. The edges in the graph are represented by a given 2D integer array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}]$ denotes an edge between vertex $u_{i}$ and vertex $v_{i}$. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

The objective is to compute `3` from `{"n": 7, "edges": [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Turn a cycle into an edge plus an alternate path

Take any undirected edge $(u,v)$. If a cycle contains this edge, removing just that edge leaves a path from $u$ to $v$ through the rest of the cycle. Conversely, if $u$ and $v$ remain connected after their direct edge is removed, that alternate path together with edge $(u,v)$ forms a cycle.

This gives a precise way to measure the shortest cycle containing a chosen edge:

$$
1+\text{the shortest distance from }u\text{ to }v
\text{ when edge }(u,v)\text{ is unavailable}.
$$

The added one counts the removed edge itself. The exact solution evaluates this quantity for every input edge and keeps the minimum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 7, "edges": [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build an undirected adjacency structure

The dictionary `g` maps each vertex to a set of its neighbors. For every input pair `u, v`, the code adds `v` to `g[u]` and `u` to `g[v]`. Both insertions are necessary because the graph is bi-directional.

Sets make the adjacency representation insensitive to repeated insertion, although the contract already guarantees that no edge is repeated. Vertices with no incident edge simply have no stored neighbors, which is harmless because no cycle can use such a vertex.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: One breadth-first search per edge

The helper `bfs(u, v)` temporarily treats edge $(u,v)$ as deleted without modifying `g`. It creates a distance array filled with infinity, sets `dist[u] = 0`, and explores outward from $u$ using a FIFO queue.

When examining adjacency step $(i,j)$, the condition

`(i, j) != (u, v) and (j, i) != (u, v)`

rejects both orientations of the selected undirected edge. This two-sided check is essential: the adjacency structure stores the edge in both directions, so skipping only $u\to v$ would still leave $v\to u$ available.

An undiscovered neighbor receives distance `dist[i] + 1` and enters the queue. Because breadth-first search visits an unweighted graph layer by layer, the first assigned distance to every vertex is its shortest number of allowed edges from $u$.

After exploration, the helper returns `dist[v] + 1`. A finite result is the length of the shortest cycle that uses the removed edge. If $v$ is unreachable, `dist[v]` remains infinity, and adding one leaves it infinite.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 7, "edges": [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **BFS from every vertex:** Track distances and parents, and use an already-visited neighbor that is not the parent to form a cycle. This can achieve $O(n(n+m))$ time and matches the manifest summary, but its cycle-length formula and parent handling require care.
- **Floyd–Warshall:** All-pairs dynamic programming can be adapted to cycle detection in $O(n^3)$ time and $O(n^2)$ space, which is unnecessary for this sparse constraint range.
- **Depth-first search alone:** DFS detects whether a cycle exists, but ordinary DFS depth does not guarantee the shortest cycle length.
- **Disconnected graph:** Each search naturally remains within its component; the minimum can come from any component.
- **Tree or forest:** Removing every edge disconnects its endpoints, so all candidates remain infinite and the result is `-1`.
- **Bridge next to a cycle:** Searches for bridge edges fail, while edges on the cyclic part still produce finite candidates.
- **Triangle:** Three is the smallest possible cycle because self-loops and repeated parallel edges are forbidden.
- **Multiple shortest cycles:** The outer minimum needs only their common length and does not need to reconstruct a particular cycle.
- **Undirected deletion:** Both ordered forms of the selected edge must be skipped during BFS.
- **Infinity arithmetic:** In Python, `inf + 1` is still `inf`, so unreachable endpoints flow safely into the final minimum and conditional.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be the number of vertices and $m$ the number of edges. Building the adjacency sets takes expected $O(m)$ time and $O(n+m)$ space when the distance array is included.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
