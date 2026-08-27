# Guided Example: Network Delay Time

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"times": [[2, 1, 1], [2, 3, 1], [3, 4, 1]], "n": 4, "k": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges $\text{times}[i] = (u_{i}, v_{i}, w_{i})$, where $u_{i}$ is the source node, $v_{i}$ is the target node, and $w_{i}$ is the time it takes for a signal to travel from source to target.

The objective is to compute `2` from `{"times": [[2, 1, 1], [2, 3, 1], [3, 4, 1]], "n": 4, "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The answer depends on shortest travel time to every node

The signal can follow directed edges, and all edge weights are nonnegative. For each node, the earliest arrival time is the shortest-path distance from source `k`. All nodes have received the signal only when the farthest reachable node receives it, so the final answer is the maximum of these shortest distances.

The exact solution applies Dijkstra’s algorithm using an adjacency matrix and a linear scan to select the next node.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"times": [[2, 1, 1], [2, 3, 1], [3, 4, 1]], "n": 4, "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build a one-based-to-zero-based adjacency matrix

The matrix `g` has `n` rows and `n` columns and starts filled with infinity. For each directed edge `(u, v, w)`, the solution writes

`g[u - 1][v - 1] = w`.

Subtracting one converts labels `1..n` to Python indices `0..n-1`. The reverse cell is not written because edges are directed.

Infinity means there is no direct edge. Pair uniqueness guarantees no competing duplicate edge needs to be minimized.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The matrix `g` has `n` rows and `n` columns and starts fille... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize tentative distances

Every distance begins at infinity except the source:

`dist[k - 1] = 0`.

The Boolean array `vis` records nodes whose shortest distance has been finalized.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"times": [[2, 1, 1], [2, 3, 1], [3, 4, 1]], "n": 4, "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Adjacency list plus min-heap:** Store only rea:** - **Adjacency list plus min-heap:** Store only real edges and repeatedly pop the smallest tentative distance. This gives `O((n + e) log n)` time and `O(n + e)` space and is preferable for sparse large graphs.
- **- **Bellman-Ford:** Repeatedly relax every edge an:** - **Bellman-Ford:** Repeatedly relax every edge and handle negative weights. It is unnecessary here because all weights are nonnegative and costs `O(ne)` time.
- **- **Breadth-first search:** It finds shortest path:** - **Breadth-first search:** It finds shortest paths only when all edges have equal weight. Varying travel times require weighted shortest-path logic.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(e)$. Constructing the `n x n` matrix costs `O(n^2)` time for initialization plus `O(e)` edge writes. Dijkstra performs `n` iterations; both selecting `t` and relaxing its full matrix row scan `n` entries. The total time is `O(n^2 + e)`, simplified to `O(n^2)` because matrix initialization already dominates within the simple directed graph.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
