# Guided Example: Analyze Subscription Conversion 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"UserActivity": [{"user_id": 1, "activity_date": "2023-01-01", "activity_type": "free_trial", "activity_duration": 45}, {"user_id": 1, "activity_date": "2023-01-02", "activity_type": "free_trial", "activity_duration": 30}, {"user_id": 1, "activity_date": "2023-01-05", "activity_type": "free_trial", "activity_duration": 60}, {"user_id": 1, "activity_date": "2023-01-10", "activity_type": "paid", "activity_duration": 75}, {"user_id": 1, "activity_date": "2023-01-12", "activity_type": "paid", "activity_duration": 90}, {"user_id": 1, "activity_date": "2023-01-15", "activity_type": "paid", "activity_duration": 65}, {"user_id": 2, "activity_date": "2023-02-01", "activity_type": "free_trial", "activity_duration": 55}, {"user_id": 2, "activity_date": "2023-02-03", "activity_type": "free_trial", "activity_duration": 25}, {"user_id": 2, "activity_date": "2023-02-07", "activity_type": "free_trial", "activity_duration": 50}, {"user_id": 2, "activity_date": "2023-02-10", "activity_type": "cancelled", "activity_duration": 0}, {"user_id": 3, "activity_date": "2023-03-05", "activity_type": "free_trial", "activity_duration": 70}, {"user_id": 3, "activity_date": "2023-03-06", "activity_type": "free_trial", "activity_duration": 60}, {"user_id": 3, "activity_date": "2023-03-08", "activity_type": "free_trial", "activity_duration": 80}, {"user_id": 3, "activity_date": "2023-03-12", "activity_type": "paid", "activity_duration": 50}, {"user_id": 3, "activity_date": "2023-03-15", "activity_type": "paid", "activity_duration": 55}, {"user_id": 3, "activity_date": "2023-03-20", "activity_type": "paid", "activity_duration": 85}, {"user_id": 4, "activity_date": "2023-04-01", "activity_type": "free_trial", "activity_duration": 40}, {"user_id": 4, "activity_date": "2023-04-03", "activity_type": "free_trial", "activity_duration": 35}, {"user_id": 4, "activity_date": "2023-04-05", "activity_type": "paid", "activity_duration": 45}, {"user_id": 4, "activity_date": "2023-04-07", "activity_type": "cancelled", "activity_duration": 0}]}}`
- **Required output:** `{"columns": ["user_id", "trial_avg_duration", "paid_avg_duration"], "rows": [[1, 45.0, 76.67], [3, 70.0, 63.33], [4, 37.5, 45.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `UserActivity`

The objective is to compute `{"columns": ["user_id", "trial_avg_duration", "paid_avg_duration"], "rows": [[1, 45.0, 76.67], [3, 70.0, 63.33], [4, 37.5, 45.0]]}` from `{"tables": {"UserActivity": [{"user_id": 1, "activity_date": "2023-01-01", "activity_type": "free_trial", "activity_duration": 45}, {"user_id": 1, "activity_date": "2023-01-02", "activity_type": "free_trial", "activity_duration": 30}, {"user_id": 1, "activity_date": "2023-01-05", "activity_type": "free_trial", "activity_duration": 60}, {"user_id": 1, "activity_date": "2023-01-10", "activity_type": "paid", "activity_duration": 75}, {"user_id": 1, "activity_date": "2023-01-12", "activity_type": "paid", "activity_duration": 90}, {"user_id": 1, "activity_date": "2023-01-15", "activity_type": "paid", "activity_duration": 65}, {"user_id": 2, "activity_date": "2023-02-01", "activity_type": "free_trial", "activity_duration": 55}, {"user_id": 2, "activity_date": "2023-02-03", "activity_type": "free_trial", "activity_duration": 25}, {"user_id": 2, "activity_date": "2023-02-07", "activity_type": "free_trial", "activity_duration": 50}, {"user_id": 2, "activity_date": "2023-02-10", "activity_type": "cancelled", "activity_duration": 0}, {"user_id": 3, "activity_date": "2023-03-05", "activity_type": "free_trial", "activity_duration": 70}, {"user_id": 3, "activity_date": "2023-03-06", "activity_type": "free_trial", "activity_duration": 60}, {"user_id": 3, "activity_date": "2023-03-08", "activity_type": "free_trial", "activity_duration": 80}, {"user_id": 3, "activity_date": "2023-03-12", "activity_type": "paid", "activity_duration": 50}, {"user_id": 3, "activity_date": "2023-03-15", "activity_type": "paid", "activity_duration": 55}, {"user_id": 3, "activity_date": "2023-03-20", "activity_type": "paid", "activity_duration": 85}, {"user_id": 4, "activity_date": "2023-04-01", "activity_type": "free_trial", "activity_duration": 40}, {"user_id": 4, "activity_date": "2023-04-03", "activity_type": "free_trial", "activity_duration": 35}, {"user_id": 4, "activity_date": "2023-04-05", "activity_type": "paid", "activity_duration": 45}, {"user_id": 4, "activity_date": "2023-04-07", "activity_type": "cancelled", "activity_duration": 0}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Aggregate the two relevant subscription stages separately per user.** The first common table expression, `T`, reads `UserActivity` rows whose type is not `cancelled`. That leaves `free_trial` and `paid` activity, the only stages contributing to requested averages.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"UserActivity": [{"user_id": 1, "activity_date": "2023-01-01", "activity_type": "free_trial", "activity_duration": 45}, {"user_id": 1, "activity_date": "2023-01-02", "activity_type": "free_trial", "activity_duration": 30}, {"user_id": 1, "activity_date": "2023-01-05", "activity_type": "free_trial", "activity_duration": 60}, {"user_id": 1, "activity_date": "2023-01-10", "activity_type": "paid", "activity_duration": 75}, {"user_id": 1, "activity_date": "2023-01-12", "activity_type": "paid", "activity_duration": 90}, {"user_id": 1, "activity_date": "2023-01-15", "activity_type": "paid", "activity_duration": 65}, {"user_id": 2, "activity_date": "2023-02-01", "activity_type": "free_trial", "activity_duration": 55}, {"user_id": 2, "activity_date": "2023-02-03", "activity_type": "free_trial", "activity_duration": 25}, {"user_id": 2, "activity_date": "2023-02-07", "activity_type": "free_trial", "activity_duration": 50}, {"user_id": 2, "activity_date": "2023-02-10", "activity_type": "cancelled", "activity_duration": 0}, {"user_id": 3, "activity_date": "2023-03-05", "activity_type": "free_trial", "activity_duration": 70}, {"user_id": 3, "activity_date": "2023-03-06", "activity_type": "free_trial", "activity_duration": 60}, {"user_id": 3, "activity_date": "2023-03-08", "activity_type": "free_trial", "activity_duration": 80}, {"user_id": 3, "activity_date": "2023-03-12", "activity_type": "paid", "activity_duration": 50}, {"user_id": 3, "activity_date": "2023-03-15", "activity_type": "paid", "activity_duration": 55}, {"user_id": 3, "activity_date": "2023-03-20", "activity_type": "paid", "activity_duration": 85}, {"user_id": 4, "activity_date": "2023-04-01", "activity_type": "free_trial", "activity_duration": 40}, {"user_id": 4, "activity_date": "2023-04-03", "activity_type": "free_trial", "activity_duration": 35}, {"user_id": 4, "activity_date": "2023-04-05", "activity_type": "paid", "activity_duration": 45}, {"user_id": 4, "activity_date": "2023-04-07", "activity_type": "cancelled", "activity_duration": 0}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

It groups by both `user_id` and `activity_type`. Therefore, one user can produce up to two aggregate rows: one trial row and one paid row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

`ROUND(SUM(activity_duration) / COUNT(1), 2)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "trial_avg_duration", "paid_avg_duration"], "rows": [[1, 45.0, 76.67], [3, 70.0, 63.33], [4, 37.5, 45.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"UserActivity": [{"user_id": 1, "activity_date": "2023-01-01", "activity_type": "free_trial", "activity_duration": 45}, {"user_id": 1, "activity_date": "2023-01-02", "activity_type": "free_trial", "activity_duration": 30}, {"user_id": 1, "activity_date": "2023-01-05", "activity_type": "free_trial", "activity_duration": 60}, {"user_id": 1, "activity_date": "2023-01-10", "activity_type": "paid", "activity_duration": 75}, {"user_id": 1, "activity_date": "2023-01-12", "activity_type": "paid", "activity_duration": 90}, {"user_id": 1, "activity_date": "2023-01-15", "activity_type": "paid", "activity_duration": 65}, {"user_id": 2, "activity_date": "2023-02-01", "activity_type": "free_trial", "activity_duration": 55}, {"user_id": 2, "activity_date": "2023-02-03", "activity_type": "free_trial", "activity_duration": 25}, {"user_id": 2, "activity_date": "2023-02-07", "activity_type": "free_trial", "activity_duration": 50}, {"user_id": 2, "activity_date": "2023-02-10", "activity_type": "cancelled", "activity_duration": 0}, {"user_id": 3, "activity_date": "2023-03-05", "activity_type": "free_trial", "activity_duration": 70}, {"user_id": 3, "activity_date": "2023-03-06", "activity_type": "free_trial", "activity_duration": 60}, {"user_id": 3, "activity_date": "2023-03-08", "activity_type": "free_trial", "activity_duration": 80}, {"user_id": 3, "activity_date": "2023-03-12", "activity_type": "paid", "activity_duration": 50}, {"user_id": 3, "activity_date": "2023-03-15", "activity_type": "paid", "activity_duration": 55}, {"user_id": 3, "activity_date": "2023-03-20", "activity_type": "paid", "activity_duration": 85}, {"user_id": 4, "activity_date": "2023-04-01", "activity_type": "free_trial", "activity_duration": 40}, {"user_id": 4, "activity_date": "2023-04-03", "activity_type": "free_trial", "activity_duration": 35}, {"user_id": 4, "activity_date": "2023-04-05", "activity_type": "paid", "activity_duration": 45}, {"user_id": 4, "activity_date": "2023-04-07", "activity_type": "cancelled", "activity_duration": 0}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "trial_avg_duration", "paid_avg_duration"], "rows": [[1, 45.0, 76.67], [3, 70.0, 63.33], [4, 37.5, 45.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional aggregation in one grouped query:** `AVG(CASE WHEN ... END)` plus a `HAVING` condition can produce the same result without separate `F` and `P` CTEs.
- **Include cancelled rows in one average:** Their duration belongs to neither requested stage and would corrupt the result.
- **Exclude anyone who ever cancelled:** A user may convert, later cancel, and still belong in the analysis, as user four demonstrates.
- **Trial-only user:** They have no paid CTE row and are removed by the inner join.
- **Paid-only user:** They have no trial CTE row and are also excluded.
- **One activity day in a stage:** Sum divided by one returns that day's duration.
- **Several dates:** Every labeled activity row contributes equally to the daily average.
- **Round inputs before averaging:** Rounding belongs after division; durations are integers, and the source rounds only the final average.
- **Chronology:** The source infers conversion from presence of both labels and does not verify that paid dates follow trial dates.
- **Seven-day wording:** No date-range filter appears; stage membership comes from `activity_type`.
- **Later cancellation:** Filtering cancellation affects neither conversion presence nor paid average.
- **`ORDER BY 1`:** It is correct while `user_id` remains the first selected expression; naming the column directly can be clearer for maintenance.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A\log A)$. Let $A$ be the number of activity rows and $U$ the number of users. Filtering scans $A$ rows. Grouping by user and activity type can be implemented with hashing in expected $O(A)$ time or sorting in $O(A\log A)$ time. The manifest uses the conservative $O(A\log A)$ bound.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
