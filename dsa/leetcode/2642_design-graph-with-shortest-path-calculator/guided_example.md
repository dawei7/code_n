# Guided Example: Design Graph With Shortest Path Calculator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["Graph", "shortestPath"], "arguments": [[2, []], [1, 1]]}`
- **Required output:** `[null, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a **directed weighted** graph that consists of `n` nodes numbered from `0` to $n - 1$. The edges of the graph are initially represented by the given array `edges` where $\text{edges}[i] = [\text{from}_{i}, \text{to}_{i}, \text{edgeCost}_{i}]$ meaning that there is an edge from $\text{from}_{i}$ to $\text{to}_{i}$ with the cost $\text{edgeCost}_{i}$.

The objective is to compute `[null, 0]` from `{"operations": ["Graph", "shortestPath"], "arguments": [[2, []], [1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store direct edge costs in a matrix

The graph has at most 100 nodes and receives both edge additions and shortest-path queries.

The constructor allocates an $n\times n$ matrix `g` filled with infinity. For every directed input edge $(f,t,c)$, it stores:

`g[f][t] = c`.

Infinity means no direct edge. Only the forward entry changes because the graph is directed; `g[t][f]` remains unrelated unless that reverse edge is explicitly supplied.

The contract guarantees no repeated edge and no self-loop, so one matrix cell represents at most one direct edge.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["Graph", "shortestPath"], "arguments": [[2, []], [1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Adding an edge is one assignment

`addEdge([f,t,c])` simply sets `g[f][t] = c`.

The matrix reserves every possible ordered node pair during construction, so no adjacency list needs resizing and no existing path table needs updating.

Future shortest-path calls read the new edge automatically. Previously returned answers are not cached, so there is no stale result to invalidate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Run array-based Dijkstra for each query

All edge costs are positive. Dijkstra's algorithm can therefore settle nodes in increasing shortest-known distance.

For one `shortestPath(node1, node2)` call:

- `dist` starts as infinity for every node;
- source distance is zero;
- `vis` marks which nodes have been finalized.

The algorithm performs $n$ rounds. In each round, it finds the unvisited node `t` with the smallest `dist[t]` by scanning all nodes.

It marks `t` visited, then tries every possible destination `j`:

`dist[j] = min(dist[j], dist[t] + g[t][j])`.

If no direct edge $t\to j$ exists, `g[t][j]` is infinity and cannot improve a finite distance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["Graph", "shortestPath"], "arguments": [[2, []], [1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Heap-based adjacency-list Dijkstra:** Gives $O((n+e)\log n)$ per query and $O(n+e)$ storage, matching the manifest and helping sparse graphs.
- **Floyd–Warshall:** Precompute all-pairs paths in $O(n^3)$, then answer queries in $O(1)$, but dynamic edge updates need additional work.
- **Incremental all-pairs update:** A new edge can update every source-destination pair in $O(n^2)$ using existing all-pairs distances.
- **Directed edge:** Adding $f\to t$ must not create $t\to f$.
- **No path:** Infinity survives and becomes `-1`.
- **Source equals destination:** The empty path has cost zero.
- **Unreachable selection:** Infinity arithmetic leaves all distances unchanged.
- **Positive weights:** They are essential to Dijkstra's finalization proof.
- **Added edge:** Every later query sees it directly in the matrix.
- **No early destination exit:** The exact loop runs all $n$ rounds even after the target could be finalized.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Construction allocates and initializes $n^2$ matrix cells, then writes $e$ input edges, costing $O(n^2+e)$ time and $O(n^2)$ space.
- **Auxiliary Space Complexity:** $O(n + e)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
