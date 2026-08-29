# Guided Example: Maximum Path Quality of a Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"values": [0, 32, 10, 43], "edges": [[0, 1, 10], [1, 2, 15], [0, 3, 10]], "maxTime": 49}`
- **Required output:** `75`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an **undirected** graph with `n` nodes numbered from `0` to $n - 1$ (**inclusive**). You are given a **0-indexed** integer array `values` where $\text{values}[i]$ is the **value **of the $i^{\text{th}}$ node. You are also given a **0-indexed** 2D integer array `edges`, where each $\text{edges}[j] = [u_{j}, v_{j}, \text{time}_{j}]$ indicates that there is an undirected edge between the nodes $u_{j}$ and $v_{j}$,_ and it takes $\text{time}_{j}$ seconds to travel between the two nodes. Finally, you are given an integer `maxTime`.

The objective is to compute `75` from `{"values": [0, 32, 10, 43], "edges": [[0, 1, 10], [1, 2, 15], [0, 3, 10]], "maxTime": 49}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate time-feasible walks, not only simple paths

The route may revisit nodes and edges. A simple-path algorithm would miss valid solutions such as returning through an already visited node to reach zero.

The source performs depth-first search over every walk whose accumulated travel time does not exceed `maxTime`. The degree bound of four and minimum edge time of ten keep the search depth small.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"values": [0, 32, 10, 43], "edges": [[0, 1, 10], [1, 2, 15], [0, 3, 10]], "maxTime": 49}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build an undirected weighted graph

For edge `[u,v,t]`, the source appends `(v,t)` to `g[u]` and `(u,t)` to `g[v]`.

This permits travel in both directions with the same cost, matching the graph contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Track time and current quality separately

`dfs(u,cost,value)` means the walk is currently at node `u`, has spent `cost` seconds, and has collected unique-node quality `value`.

For each adjacent edge with time `t`, recursion is allowed only when `cost+t <= maxTime`. This ensures no explored state violates the time budget.

The method does not require using all available time. Any return to zero within the budget is a valid candidate.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `75` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"values": [0, 32, 10, 43], "edges": [[0, 1, 10], [1, 2, 15], [0, 3, 10]], "maxTime": 49}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `75` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Shortest-return pruning:** Precompute shortest time from each node to zero and stop branches that cannot return; improves actual search but is absent from the source.
- **Simple-path DFS:** Incorrect because revisiting nodes and edges is allowed and often required.
- **Disconnected nodes:** Never reached from zero and correctly contribute nothing.
- **Zero-value node:** Visiting it changes no quality but may enable routes.
- **Repeated node:** Its value is not added again while its visit flag is active.
- **Return to zero early:** Produces a candidate and may still be extended for a better later return.
- **Use less than `maxTime`:** Fully valid; exact budget exhaustion is not required.
- **Edge exactly fills budget:** Traversal is allowed by `<=`.
- **No edges:** The zero-length walk returns quality `values[0]`.
- **Backtracking:** New-node flags must be reset between sibling walks.
- **Bounded degree and edge count:** Make exhaustive walk enumeration practical.
- **Input preservation:** The method builds a separate adjacency list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+E+4^L)$. Let $N$ be nodes, $E$ edges, $D\le4$ maximum degree, and $L$ the maximum number of edges fitting in the time budget. Graph construction costs $O(N+E)$.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
