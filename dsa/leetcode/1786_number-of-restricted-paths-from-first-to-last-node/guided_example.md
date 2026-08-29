# Guided Example: Number of Restricted Paths From First to Last Node

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1, "edges": []}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an undirected weighted connected graph. You are given a positive integer `n` which denotes that the graph has `n` nodes labeled from `1` to `n`, and an array `edges` where each $\text{edges}[i] = [u_{i}, v_{i}, \text{weight}_{i}]$ denotes that there is an edge between nodes $u_{i}$ and $v_{i}$ with weight equal to $\text{weight}_{i}$.

The objective is to compute `1` from `{"n": 1, "edges": []}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The restriction is defined by distances to node `n`

A path is restricted when every step moves from a node with a larger shortest distance to node `n` to a node with a smaller shortest distance to node `n`. The first task is therefore not to count paths. It is to know the exact value of `distanceToLastNode(x)` for every node `x`.

The graph is undirected and all edge weights are positive. Shortest distances to node `n` can be found by running Dijkstra's algorithm with node `n` as the source. In an undirected graph, the shortest distance from `x` to `n` is the same as the shortest distance from `n` to `x`, so this reversed viewpoint computes exactly the quantities in the definition.

The solution builds an adjacency list `g`. Every input edge `[u, v, w]` is inserted once as `(v, w)` in `g[u]` and once as `(u, w)` in `g[v]`. It then creates a distance array initialized to infinity, sets `dist[n] = 0`, and starts a min-heap with `(0, n)`.

Whenever node `u` is removed from the heap, each neighbor `v` is tested. If traveling from `v` through `u` gives a shorter route to the destination, meaning `dist[u] + w < dist[v]`, the solution records that new distance and pushes a new heap entry for `v`. Positive weights and the min-heap ordering ensure that the smallest possible distances propagate outward from node `n`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1, "edges": []}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turn the undirected graph into an implicit directed acyclic graph

After the distance phase, consider an undirected edge between `i` and `j`. The counting phase may traverse it from `i` to `j` only when `dist[i] > dist[j]`. Conceptually, this orients every usable edge from a greater distance to a smaller distance.

That orientation cannot contain a directed cycle. Following a directed edge strictly decreases `dist`, so returning to a previously visited node would require its distance to be both strictly smaller and equal to its earlier value. This contradiction means the usable edges form a directed acyclic graph, even though the original graph can have many cycles.

This is the central simplification. Counting unrestricted simple paths in a general graph can be extremely expensive, but counting paths in a DAG is a dynamic-programming problem.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Memoized depth-first counting

Define `dfs(i)` as the number of restricted paths that begin at node `i` and finish at node `n`.

If `i == n`, there is one completed path: the path has already reached its destination. Thus `dfs(n)` returns 1.

For every other node, the function examines its neighbors. It follows only neighbors `j` satisfying `dist[i] > dist[j]`, because exactly those steps preserve the restricted-path condition. Every restricted path from `i` must choose one such first neighbor, and after making that choice it can use any restricted path counted by `dfs(j)`. Therefore,

$$
\operatorname{dfs}(i)
=
\sum_{\substack{j\text{ adjacent to }i\\\texttt{dist}[i]>\texttt{dist}[j]}}
\operatorname{dfs}(j).
$$

The `@cache` decorator stores each completed result, so if several incoming paths reach the same node, its suffix count is computed once and reused. Each addition is reduced modulo $10^9+7$, as required.

Although `dfs` is declared before `g`, `dist`, and `mod` are assigned, Python closures look up those names when the function is called. The only call, `dfs(1)`, occurs after the graph and distances are complete, so the references are ready.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1, "edges": []}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dijkstra with a stale-entry guard:** Keep the popped distance and skip the adjacency scan when it is not equal to `dist[u]`. This preserves the same results and attains the manifest's $O((n+E)\log n)$ time bound.
- **Iterative DAG dynamic programming:** Sort nodes by increasing distance and accumulate path counts without recursion. It avoids recursion-depth risk while using the same distance orientation.
- **Enumerate complete paths:** Backtracking through all decreasing choices repeats common suffixes and can take exponential time; memoization is essential.
- **Run Dijkstra from node 1:** That computes distances to the wrong endpoint. The restriction compares shortest distances to node `n`, so the distance source must be `n`.
- **Breadth-first search:** BFS is insufficient because edge weights vary; the fewest-edge route need not have minimum total weight.
- **Equal distances:** An edge whose endpoints have equal `dist` values is forbidden because the inequality is strict, not non-increasing.
- **Positive weights:** They support Dijkstra and ensure shortest-distance reasoning is well behaved. Negative weights would invalidate this method.
- **Original graph cycles:** They cause no counting cycle because every accepted DFS step strictly decreases distance.
- **Multiple incoming restricted paths:** Cached suffix counts are intentionally reused; the distinct prefixes still make the complete paths distinct.
- **Modulo arithmetic:** Reducing after every addition prevents the count from growing needlessly while preserving the final residue.
- **Single node:** When `n = 1`, `dfs(1)` immediately returns one for the already-complete path.
- **Connected graph guarantee:** Every `dist` becomes finite. No special unreachable-node behavior is needed.
- **Deep decreasing chain:** The recursive DFS can reach depth $O(n)$; in Python, a sufficiently long chain may exceed the runtime's recursion limit. An iterative distance-ordered DP avoids that implementation hazard.
- **Input preservation:** The method builds its own adjacency representation and never mutates `edges`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E^2+E\log E+n)$. Let $E$ be the number of undirected edges. Building the adjacency list takes $O(n+E)$ space and $O(E)$ time. The memoized DFS computes at most one result per node and examines every adjacency-list entry at most once during those first computations, so its counting work is $O(n+E)$. The distance array, cache, and recursion stack use $O(n)$ additional space.
- **Auxiliary Space Complexity:** $O(E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
