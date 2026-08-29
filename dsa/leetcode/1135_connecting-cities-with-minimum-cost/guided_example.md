# Guided Example: Connecting Cities With Minimum Cost

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "connections": [[1, 2, 5], [1, 3, 6], [2, 3, 1]]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` cities labeled from `1` to `n`. You are given the integer `n` and an array `connections` where $\text{connections}[i] = [x_{i}, y_{i}, \text{cost}_{i}]$ indicates that the cost of connecting city $x_{i}$ and city $y_{i}$ (bidirectional connection) is $\text{cost}_{i}$.

The objective is to compute `6` from `{"n": 3, "connections": [[1, 2, 5], [1, 3, 6], [2, 3, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The problem asks for a minimum spanning tree

Cities are graph vertices and available bidirectional connections are weighted edges. Connecting every city with minimum total selected cost is exactly the minimum spanning tree problem when the graph is connected.

Kruskal’s algorithm considers edges from cheapest to most expensive and accepts an edge only when it connects two currently separate components.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "connections": [[1, 2, 5], [1, 3, 6], [2, 3, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort by connection cost

`connections.sort(key=lambda x: x[2])` orders edges by their third field. It sorts the caller’s list in place.

Parallel edges remain independent. The cheaper one is considered first; a later parallel edge will be skipped if its endpoints are already connected.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Track components with disjoint-set union

Parent array `p` uses zero-based city indices. Input labels are converted with `x - 1` and `y - 1`.

`find` follows parents to a representative root and applies path compression, making later searches shorter.

If two endpoints already have equal roots, adding their edge would create a cycle. A cycle is unnecessary for connectivity and adds nonnegative cost, so the edge is skipped.

If roots differ, `p[find(x)] = find(y)` merges the components and `cost` is added to `ans`.

The parent assignment uses representatives rather than raw endpoint indices. Attaching a non-root endpoint directly could fail to merge the complete components or leave an inconsistent forest.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "connections": [[1, 2, 5], [1, 3, 6], [2, 3, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prim’s algorithm:** Grow one tree with a priority queue in $O(m\log n)$ time; convenient with adjacency lists.
- **Union by rank:** Add component sizes or ranks to strengthen the DSU bound and tree shape.
- **Cycle acceptance:** Incorrect because it adds cost without connecting new components.
- **Disconnected graph:** Component count remains above one and the result is `-1`.
- **Parallel connections:** Kruskal naturally prefers the cheapest useful one.
- **Zero-cost edge:** It is considered first and safely accepted if it joins components.
- **Already connected endpoints:** The edge is skipped regardless of cost.
- **Exactly `n-1` successful unions:** Any connected spanning tree on `n` cities has this many edges.
- **One city:** Mathematically costs zero; the exact code needs an early return to support that boundary.
- **Input mutation:** Sorting permanently reorders `connections`.
- **One-based labels:** Subtracting one aligns them with the parent array.
- **Equal-cost edges:** Any order among them can lead to a minimum spanning tree.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m\log m)$. Let $m$ be connection count. Parent initialization costs $O(n)$ and sorting costs $O(m\log m)$.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
