# Guided Example: Find if Path Exists in Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1], [1, 2], [2, 0]], "source": 0, "destination": 2}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to $n - 1$ (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each $\text{edges}[i] = [u_{i}, v_{i}]$ denotes a bi-directional edge between vertex $u_{i}$ and vertex $v_{i}$. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself.

The objective is to compute `true` from `{"n": 3, "edges": [[0, 1], [1, 2], [2, 0]], "source": 0, "destination": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent the undirected graph with both directions

The code creates one adjacency list per vertex. For every edge `[u, v]`, it appends `v` to `g[u]` and `u` to `g[v]`. A path can therefore traverse an edge in either direction.

The intended search is depth-first: starting from `source`, recursively search neighbors until `destination` is reached. `any(...)` short-circuits when a recursive call returns true.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1], [1, 2], [2, 0]], "source": 0, "destination": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The required visited invariant

In an undirected graph, every traversed edge immediately offers a route back to the parent. A correct DFS must mark a vertex visited before recursively exploring its neighbors. Revisiting a marked vertex should return false for that branch.

With that invariant, each reachable vertex is processed once. Reaching `destination` proves a path; exhausting all source-component vertices proves none exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | In an undirected graph, every traversed edge immediately off... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The exact source omits the marking operation

The function creates `vis = set()` and checks:

`if i in vis: return false`.

However, it never executes `vis.add(i)`. The set remains empty forever. The visited check therefore cannot stop a back edge.

For a simple edge `0 -- 1` with source zero and an unreachable destination elsewhere, `dfs(0)` calls `dfs(1)`, which calls `dfs(0)` again, and recursion repeats until Python raises `RecursionError`. A longer cycle has the same problem.

Even an acyclic undirected graph has two-way adjacency, so parent-child backtracking is already a length-two recursion cycle unless the destination is found before that edge is followed.

The exact implementation may return true in favorable cases—for example, when source equals destination or a neighbor path reaches destination before any failing backtrack—and it returns false for an isolated nondestination source. But it is not a correct general solution.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1], [1, 2], [2, 0]], "source": 0, "destination": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative DFS:** Use an explicit stack and mar:** - **Iterative DFS:** Use an explicit stack and mark vertices when pushed or popped. It avoids both the missing-mark bug and Python recursion limits.
- **Breadth-first search:** A deque explores the same connected component in $O(V+E)$ time and can stop when destination is reached.
- **Disjoint Set Union:** Union every edge, then compare representatives of source and destination. This is useful for repeated connectivity queries.
- **Source equals destination:** The exact code returns true before needing visited state, which is correct.
- **Isolated source:** If it is not the destination, `any` over an empty neighbor list returns false.
- **Single undirected edge away from destination:** The missing visited insertion causes immediate parent-child recursion.
- **Cycle:** The exact source can loop recursively around it until `RecursionError`.
- **Favorable neighbor ordering:** Reaching destination early may hide the bug on some true cases, but correctness must hold for all inputs.
- **No duplicate edges:** Adjacency still contains one entry in each direction, so visited marking remains essential.
- **Minimal fix:** Add `vis.add(i)` before the recursive neighbor search.
- **Recursion depth after fixing:** A chain can still exceed Python's call-stack limit; an explicit stack is production-safe.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Building adjacency lists takes $O(V+E)$ time and space.
- **Auxiliary Space Complexity:** $O(V+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
