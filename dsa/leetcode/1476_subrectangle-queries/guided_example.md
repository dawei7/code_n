# Guided Example: Subrectangle Queries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rectangle": [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]], "operations": [["getValue", [0, 2]], ["updateSubrectangle", [0, 0, 3, 2, 5]], ["getValue", [0, 2]], ["getValue", [3, 1]], ["updateSubrectangle", [3, 0, 3, 2, 10]], ["getValue", [3, 1]], ["getValue", [0, 2]]]}`
- **Required output:** `[1, null, 5, 5, null, 10, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Implement the class `SubrectangleQueries` which receives a `rows x cols` rectangle as a matrix of integers in the constructor and supports two methods:

The objective is to compute `[1, null, 5, 5, null, 10, 5]` from `{"rectangle": [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]], "operations": [["getValue", [0, 2]], ["updateSubrectangle", [0, 0, 3, 2, 5]], ["getValue", [0, 2]], ["getValue", [3, 1]], ["updateSubrectangle", [3, 0, 3, 2, 10]], ["getValue", [3, 1]], ["getValue", [0, 2]]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Record updates lazily instead of rewriting cells.** The constructor stores the supplied matrix as `g` and creates an empty operation log `ops`. An update does not visit any cell. It appends the rectangle boundaries and new value as one tuple.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rectangle": [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]], "operations": [["getValue", [0, 2]], ["updateSubrectangle", [0, 0, 3, 2, 5]], ["getValue", [0, 2]], ["getValue", [3, 1]], ["updateSubrectangle", [3, 0, 3, 2, 10]], ["getValue", [3, 1]], ["getValue", [0, 2]]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This makes even a very large subrectangle update constant-time: its effect is represented symbolically. The original matrix remains unchanged and serves as the baseline before any recorded update covers a queried coordinate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | This makes even a very large subrectangle update constant-ti... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**A later update overrides an earlier one.** To answer `getValue(row, col)`, the code examines operations from newest to oldest through `ops[::-1]`. The first rectangle containing the coordinate is the most recent assignment affecting that cell, so its stored value is immediately returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, null, 5, 5, null, 10, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rectangle": [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]], "operations": [["getValue", [0, 2]], ["updateSubrectangle", [0, 0, 3, 2, 5]], ["getValue", [0, 2]], ["getValue", [3, 1]], ["updateSubrectangle", [3, 0, 3, 2, 10]], ["getValue", [3, 1]], ["getValue", [0, 2]]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, null, 5, 5, null, 10, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use reversed directly:** `reversed(ops)` avoid:** - **Use reversed directly:** `reversed(ops)` avoids the copied reverse slice and reduces each query's temporary space to `O(1)`, while keeping `O(U)` worst-case time.
- **Eagerly update every cell:** Queries become `O(1)`, but one update costs the rectangle's area.
- **Two-dimensional lazy structures:** Segment trees or other range-update structures can improve larger workloads but are much more complex.
- **No updates:** The query falls through to the original matrix value.
- **Newest update covers the cell:** It is logically found first, though the reverse slice still copies the entire log.
- **Overlapping updates:** The most recent covering rectangle wins.
- **Disjoint updates:** Each affects only its own coordinates.
- **Boundary coordinate:** Inclusive comparisons correctly include rectangle edges and corners.
- **Whole-matrix update:** One tuple represents it; no cell loop occurs.
- **Repeated same value:** It is still a valid later write and may be returned.
- **Original matrix ownership:** External baseline mutation can be observed for never-updated cells because no copy is made.
- **Operation-log growth:** Updates are never compacted, so retained space grows linearly with update calls.
- **Complexity reporting:** Use `O(1)` update, `O(U)` query, and `O(U)` retained space for this source.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Construction stores references and initializes a list in `O(1)` auxiliary work, excluding the already supplied matrix. Each append is amortized `O(1)`.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
