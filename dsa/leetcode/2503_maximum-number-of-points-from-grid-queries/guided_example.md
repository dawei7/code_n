# Guided Example: Maximum Number of Points From Grid Queries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 2, 3], [2, 5, 7], [3, 5, 1]], "queries": [5, 6, 2]}`
- **Required output:** `[5, 8, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` integer matrix `grid` and an array `queries` of size `k`.

The objective is to compute `[5, 8, 1]` from `{"grid": [[1, 2, 3], [2, 5, 7], [3, 5, 1]], "queries": [5, 6, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A query asks for a reachable threshold component

For threshold `v`, a cell can score a point only when its value is strictly less than `v`. Starting at the top-left cell, the maximum score is therefore the number of cells connected to `(0,0)` through four-directional paths whose every cell value is below `v`.

Revisiting cells cannot add points, so the task is a reachability count, not a longest walk.

Larger query thresholds can only add eligible cells; they never remove a previously reachable one. This monotonicity lets all queries share one incremental graph expansion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 2, 3], [2, 5, 7], [3, 5, 1]], "queries": [5, 6, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort queries but remember their original positions

`qs` contains pairs `(query_value,original_index)` sorted by value. The algorithm processes thresholds from smallest to largest while `ans` remains indexed in the original order.

After finishing threshold `v`, it writes the current reachable count into `ans[k]`. Equal query values naturally receive the same count because no new cell can be popped between identical thresholds after the first has exhausted all values below that threshold.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the smallest boundary cell in a heap

The min-heap `q` begins with the top-left cell represented as `(grid[0][0],0,0)`. It contains discovered cells adjacent to the already expanded region that have not yet been counted.

For a query value `v`, the loop pops while the smallest heap value is strictly less than `v`. A popped cell is eligible for this query, so `cnt` increases. Its four neighbors are then discovered and pushed if they have never been seen.

If the smallest boundary value is at least `v`, no heap cell is eligible. Because it is the minimum, every other boundary cell is also too large. Any route to an undiscovered cell must cross the current boundary, so expansion cannot legally proceed for this threshold.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 8, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 2, 3], [2, 5, 7], [3, 5, 1]], "queries": [5, 6, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 8, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fresh BFS per query:** It is correct but can cost $O(kmn)$ and repeats reachability work.
- **Union-find offline:** Sort cells by value, activate them below each sorted query, and track the component containing the start. It has comparable offline efficiency.
- **Equal cell and query values:** The cell is not eligible because the comparison is strict.
- **Blocked start:** The answer is zero and no neighbors can be reached.
- **Duplicate queries:** They receive identical counts and retain their separate original positions.
- **Unsorted input queries:** Sorting enables reuse; `original_index` restores output order.
- **Cell discovered early but too large:** Leave it in the heap for a later threshold.
- **Multiple paths to one cell:** Marking on push prevents duplicates.
- **Revisiting allowed:** It cannot earn another point, so visited-state counting remains correct.
- **Heap frontier:** If its minimum is blocked, every route to undiscovered cells is blocked for that threshold.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N+k\log k)$. Let $N=mn$ be the number of grid cells and $k$ the number of queries. Sorting queries costs $O(k\log k)$.
- **Auxiliary Space Complexity:** $O(N+k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
