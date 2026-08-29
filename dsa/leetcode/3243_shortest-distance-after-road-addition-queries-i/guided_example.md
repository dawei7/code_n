# Guided Example: Shortest Distance After Road Addition Queries I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "queries": [[2, 4], [0, 2], [0, 4]]}`
- **Required output:** `[3, 2, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` and a 2D integer array `queries`.

The objective is to compute `[3, 2, 1]` from `{"n": 5, "queries": [[2, 4], [0, 2], [0, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

Cities are vertices and directed roads are edges. Every road has the same cost of one, so the shortest-path length is the minimum number of edges from city zero to city `n - 1`. Breadth-first search finds exactly that distance in an unweighted graph.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "queries": [[2, 4], [0, 2], [0, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The graph persists across queries because every query adds a road and no road is removed. The adjacency list `g` begins with the original chain: for each index from zero through `n - 2`, `g[i]` contains `i + 1`. The list has only `n - 1` rows rather than $n$ because destination city `n - 1` has no outgoing road under the forward-edge constraints. The BFS returns as soon as that destination is dequeued, so it never indexes `g[n - 1]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For each query `[u,v]`, the code appends `v` to `g[u]`. The road is available not only for the current result but for every later result. It then runs `bfs(0)` against the complete graph built so far and appends the returned distance to `ans`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 2, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "queries": [[2, 4], [0, 2], [0, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 2, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bottom-up DAG dynamic programming:** Because all edges point to larger identifiers, compute distances to `n - 1` from right to left after every query. It has the same $O(q(n+q))$ total worst-case time and avoids a queue.
- **Top-down memoized recursion:** The DAG permits a shortest-distance recurrence over outgoing neighbors. Reinitializing memoization after each query is necessary, and a long chain risks Python recursion depth.
- **Incremental distance relaxation:** When a new edge improves `dist[v]`, propagate improvements forward through outgoing edges. This may do less work in practice but needs more careful cumulative analysis.
- **Direct BFS after each query:** This is the exact source approach. Its simplicity is well matched to the version-I limit of five hundred nodes and queries.
- **A shortcut directly to the destination:** Once `0 -> n - 1` exists, the answer is one and can never decrease further. The source still runs BFS for later queries, but it returns from the first next layer.
- **A query that does not improve the shortest path:** The road remains in `g`, BFS finds the same distance, and that unchanged value is appended.
- **Persistent roads:** Clearing or rebuilding `g` with only the latest query would be wrong because every answer includes all earlier additions.
- **Fresh visited state:** Reusing `vis` across queries would skip cities and miss paths created by the new road. The helper correctly allocates it per run.
- **No repeated query roads:** The constraint avoids duplicate adjacency entries, although BFS correctness would survive duplicates because `vis` prevents duplicate enqueues.
- **Guaranteed reachability:** The original chain means `while 1` always reaches `n - 1`. Without that guarantee, the helper would need an empty-queue condition and a value representing no path.
- **Forward-only roads:** They make the graph acyclic and ensure `u <= n - 3` under the required gap, so the compact `g` with no destination row is safe.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q(n+q))$. Let $q$ be the number of queries. After processing query $k$, using one-based counting, the graph contains $n-1+k$ edges. That BFS takes $O(n+n-1+k)=O(n+k)$ time. Summing over all queries gives
- **Auxiliary Space Complexity:** $O(n+q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
