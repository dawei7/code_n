# Guided Example: Find the Closest Marked Node

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[0, 1, 1], [1, 2, 3], [2, 3, 2], [0, 3, 4]], "s": 0, "marked": [2, 3]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n` which is the number of nodes of a **0-indexed directed weighted** graph and a **0-indexed** **2D array** `edges` where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ indicates that there is an edge from node $u_{i}$ to node $v_{i}$ with weight $w_{i}$.

The objective is to compute `4` from `{"n": 4, "edges": [[0, 1, 1], [1, 2, 3], [2, 3, 2], [0, 3, 4]], "s": 0, "marked": [2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use Dijkstra because every edge weight is positive

The graph is directed, so only the listed direction `u -> v` is usable. Every weight is at least one, which makes Dijkstra's greedy shortest-path rule valid.

The exact implementation uses the dense, array-based form of Dijkstra rather than a heap. It computes shortest distances from source `s` to every node and only afterward takes the minimum over marked nodes.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[0, 1, 1], [1, 2, 3], [2, 3, 2], [0, 3, 4]], "s": 0, "marked": [2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build a dense adjacency matrix

`g` is an `n by n` matrix initially filled with infinity. Entry `g[u][v]` represents the cheapest direct edge from `u` to `v`.

Repeated edges are allowed. The assignment:

`g[u][v] = min(g[u][v], w)`

keeps only the lightest parallel edge. A heavier direct edge can never improve a shortest path between the same endpoints, so discarding it is safe.

Missing directed edges remain infinity. The code does not mirror entries, correctly preserving direction.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `g` is an `n by n` matrix initially filled with infinity.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Distance and finalized arrays

`dist[v]` is the best source-to-`v` distance discovered so far. It starts at infinity for every node except `dist[s] = 0`.

`vis[v]` records whether Dijkstra has finalized node `v`. Once finalized, its distance will never improve because all edge weights are nonnegative and it was the smallest unvisited tentative distance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[0, 1, 1], [1, 2, 3], [2, 3, 2], [0, 3, 4]], "s": 0, "marked": [2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Adjacency-list heap Dijkstra:** Achieves $O((n:** - **Adjacency-list heap Dijkstra:** Achieves $O((n+e)\log n)$ time and $O(n+e)$ space and can return when the first marked node is popped without stale distance.
- **Bellman-Ford:** Handles negative weights but costs $O(ne)$ and is unnecessary because weights are positive.
- **Reverse multi-source search:** Reversing edges and starting from all marked nodes is another valid formulation for the distance to `s`.
- **Repeated directed edges:** Only the minimum weight is retained.
- **Unreachable nodes:** They remain at infinity; dense rounds over them do not alter distances.
- **All marked nodes unreachable:** The final answer is `-1`.
- **Several closest marked nodes:** Only their common minimum distance matters.
- **Directedness:** An edge `u -> v` does not permit travel from `v` to `u`.
- **No self-loops:** Guaranteed, though positive self-loops would not improve a shortest path anyway.
- **Manifest mismatch:** The exact code is dense $O(n^2)$ Dijkstra and does not stop early.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2+e)$. Let $n$ be the node count and $e$ the input edge count. Initializing the matrix costs $O(n^2)$ time and space. Reading edges costs $O(e)$. The algorithm performs $n$ rounds, each with an $O(n)$ selection and $O(n)$ relaxation scan, for $O(n^2)$ shortest-path time.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
