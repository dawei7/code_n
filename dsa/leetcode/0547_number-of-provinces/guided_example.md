# Guided Example: Number of Provinces

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"isConnected": [[1, 1, 0], [1, 1, 0], [0, 0, 1]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

The objective is to compute `2` from `{"isConnected": [[1, 1, 0], [1, 1, 0], [0, 0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

The matrix describes an undirected graph:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"isConnected": [[1, 1, 0], [1, 1, 0], [0, 0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- each city is a vertex;
- `isConnected[i][j] == 1` means an edge directly connects cities `i` and `j`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - each city is a vertex;
- `isConnected[i][j] == 1` means an... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

A province is exactly a connected component of this graph. The solution counts how many depth-first searches are needed to visit every city.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"isConnected": [[1, 1, 0], [1, 1, 0], [0, 0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Breadth-first search:** A queue can mark one c:** - **Breadth-first search:** A queue can mark one component at a time with the same $O(n^2)$ time and $O(n)$ space.
- **Union-find:** Union every connected pair and count roots. It is useful for edge streams but still scans this full matrix.
- **Count direct neighbor groups only:** Direct adjacency is not enough; indirect paths must merge cities into one province.
- **Single city:** One unvisited start launches DFS and returns one province.
- **Identity matrix:** Every city is isolated, so the result is `n`.
- **Fully connected matrix:** The first DFS marks all cities and the result is one.
- **Self-connections:** Diagonal ones are harmless because the current city is marked first.
- **Symmetric duplicate edges:** Visited checks prevent repeated recursive work.
- **Long chain of cities:** Indirect connectivity makes the entire chain one province.
- **Recursion depth:** With up to 200 cities, the call depth is bounded and modest; an explicit stack is an easy substitute.
- **Input immutability:** Connectivity entries remain unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of cities. Every city is marked once, but processing a city scans its complete matrix row of length $n$. Across all cities, time is $O(n^2)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
