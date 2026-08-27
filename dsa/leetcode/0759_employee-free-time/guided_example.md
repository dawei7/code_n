# Guided Example: Employee Free Time

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"schedule": [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]}`
- **Required output:** `[[3, 4]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We are given a list `schedule` of employees, which represents the working time for each employee.

The objective is to compute `[[3, 4]]` from `{"schedule": [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Common free time is the gap between merged busy intervals

At a time when any employee is working, the group is not commonly free. Therefore first compute the union of every employee’s busy intervals. The finite positive gaps between consecutive components of that union are exactly the times when everyone is free.

The exact solution flattens all employee schedules into one list, sorts it, merges it, and extracts gaps.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"schedule": [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Flattening is valid

Individual employee identity no longer matters after asking whether at least one person is busy. Every interval contributes to the global busy union in the same way.

The input guarantee that each employee’s own schedule is sorted and nonoverlapping is useful source structure, but the solution does not depend on preserving it. Flattening and globally sorting handles overlaps between different employees.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Individual employee identity no longer matters after asking ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort by start and then end

Intervals are ordered by `(start, end)`. When scanning in this order, any interval that can overlap the current merged component appears before intervals that begin farther right.

`merged` starts with the earliest interval. For each next interval `x`:

- If `merged[-1].end < x.start`, a positive gap exists, so `x` starts a new merged component.
- Otherwise the intervals overlap or touch, so the current component’s end becomes the larger end.

Touching intervals are merged. If one ends at time five and another begins at five, the gap `[5, 5]` has zero length and must not be returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[3, 4]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"schedule": [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[3, 4]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **K-way merge employee schedules:** Because each:** - **K-way merge employee schedules:** Because each individual schedule is sorted, a heap can merge them before union processing. This avoids one global sort but adds heap logic.
- **- **Sweep-line endpoints:** Track active employee :** - **Sweep-line endpoints:** Track active employee intervals through start and end events. It works but is more machinery than merging their union.
- **- **Keep touching intervals separate:** That would:** - **Keep touching intervals separate:** That would emit a zero-length free interval, which is forbidden.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let `N` be the total number of busy intervals across employees. Flattening costs `O(N)`, sorting costs `O(N log N)`, and merging plus gap extraction costs `O(N)`. Total time is `O(N log N)`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
