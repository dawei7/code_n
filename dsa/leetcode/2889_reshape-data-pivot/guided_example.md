# Guided Example: Reshape Data: Pivot

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"weather": [{"city": "Jacksonville", "month": "January", "temperature": 13}, {"city": "Jacksonville", "month": "February", "temperature": 23}, {"city": "Jacksonville", "month": "March", "temperature": 38}, {"city": "Jacksonville", "month": "April", "temperature": 5}, {"city": "Jacksonville", "month": "May", "temperature": 34}, {"city": "ElPaso", "month": "January", "temperature": 20}, {"city": "ElPaso", "month": "February", "temperature": 6}, {"city": "ElPaso", "month": "March", "temperature": 26}, {"city": "ElPaso", "month": "April", "temperature": 2}, {"city": "ElPaso", "month": "May", "temperature": 43}]}}`
- **Required output:** `{"columns": ["month", "ElPaso", "Jacksonville"], "rows": [["April", 2, 5], ["February", 6, 23], ["January", 20, 13], ["March", 26, 38], ["May", 43, 34]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to **pivot** the data so that each row represents temperatures for a specific month, and each city is a separate column.

The objective is to compute `{"columns": ["month", "ElPaso", "Jacksonville"], "rows": [["April", 2, 5], ["February", 6, 23], ["January", 20, 13], ["March", 26, 38], ["May", 43, 34]]}` from `{"tables": {"weather": [{"city": "Jacksonville", "month": "January", "temperature": 13}, {"city": "Jacksonville", "month": "February", "temperature": 23}, {"city": "Jacksonville", "month": "March", "temperature": 38}, {"city": "Jacksonville", "month": "April", "temperature": 5}, {"city": "Jacksonville", "month": "May", "temperature": 34}, {"city": "ElPaso", "month": "January", "temperature": 20}, {"city": "ElPaso", "month": "February", "temperature": 6}, {"city": "ElPaso", "month": "March", "temperature": 26}, {"city": "ElPaso", "month": "April", "temperature": 2}, {"city": "ElPaso", "month": "May", "temperature": 43}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Convert three long-format columns into a two-dimensional lookup.** Each input row describes one observation:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"weather": [{"city": "Jacksonville", "month": "January", "temperature": 13}, {"city": "Jacksonville", "month": "February", "temperature": 23}, {"city": "Jacksonville", "month": "March", "temperature": 38}, {"city": "Jacksonville", "month": "April", "temperature": 5}, {"city": "Jacksonville", "month": "May", "temperature": 34}, {"city": "ElPaso", "month": "January", "temperature": 20}, {"city": "ElPaso", "month": "February", "temperature": 6}, {"city": "ElPaso", "month": "March", "temperature": 26}, {"city": "ElPaso", "month": "April", "temperature": 2}, {"city": "ElPaso", "month": "May", "temperature": 43}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

In long format, city and month repeat across rows. The requested wide format uses each distinct month as a row key, each distinct city as a column key, and places the corresponding temperature at their intersection.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | In long format, city and month repeat across rows.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

The exact solution states those three roles directly:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["month", "ElPaso", "Jacksonville"], "rows": [["April", 2, 5], ["February", 6, 23], ["January", 20, 13], ["March", 26, 38], ["May", 43, 34]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"weather": [{"city": "Jacksonville", "month": "January", "temperature": 13}, {"city": "Jacksonville", "month": "February", "temperature": 23}, {"city": "Jacksonville", "month": "March", "temperature": 38}, {"city": "Jacksonville", "month": "April", "temperature": 5}, {"city": "Jacksonville", "month": "May", "temperature": 34}, {"city": "ElPaso", "month": "January", "temperature": 20}, {"city": "ElPaso", "month": "February", "temperature": 6}, {"city": "ElPaso", "month": "March", "temperature": 26}, {"city": "ElPaso", "month": "April", "temperature": 2}, {"city": "ElPaso", "month": "May", "temperature": 43}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["month", "ElPaso", "Jacksonville"], "rows": [["April", 2, 5], ["February", 6, 23], ["January", 20, 13], ["March", 26, 38], ["May", 43, 34]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`pivot_table`:** Use it only when duplicate mo:** - **`pivot_table`:** Use it only when duplicate month-city pairs require an explicit aggregation; plain `pivot` correctly rejects ambiguity.
- **Group then unstack:** `groupby` or `set_index(...).unstack()` can reproduce the reshape but is more verbose for unique keys.
- **Duplicate key pair:** The exact source raises instead of choosing one temperature.
- **Missing month-city combination:** The wide cell becomes missing.
- **One city:** The result has one city column and one row per distinct month.
- **One month:** The result has one row and one column per distinct city.
- **Month order:** The source does not enforce chronological order; add categorical ordering only if explicitly required.
- **Index versus ordinary column:** `month` becomes the named row index, which renders like the leftmost table field but is not a regular data column.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r + cm)$. Let $r$ be the number of input observations, $m$ the number of distinct months, and $c$ the number of distinct cities. pandas must process the $r$ keys and organize them for reshaping; the manifest models this as $O(r\log r)$ key ordering plus $O(cm)$ output construction, for total $O(r\log r+cm)$ time.
- **Auxiliary Space Complexity:** $O(cm)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
