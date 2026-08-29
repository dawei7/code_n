# Guided Example: Employees With Deductions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"employee_id": 1, "needed_hours": 20}, {"employee_id": 2, "needed_hours": 12}, {"employee_id": 3, "needed_hours": 2}], "Logs": [{"employee_id": 1, "in_time": "2022-10-01 09:00:00", "out_time": "2022-10-01 17:00:00"}, {"employee_id": 1, "in_time": "2022-10-06 09:05:04", "out_time": "2022-10-06 17:09:03"}, {"employee_id": 1, "in_time": "2022-10-12 23:00:00", "out_time": "2022-10-13 03:00:01"}, {"employee_id": 2, "in_time": "2022-10-29 12:00:00", "out_time": "2022-10-29 23:58:58"}]}}`
- **Required output:** `{"columns": ["employee_id"], "rows": [[2], [3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["employee_id"], "rows": [[2], [3]]}` from `{"tables": {"Employees": [{"employee_id": 1, "needed_hours": 20}, {"employee_id": 2, "needed_hours": 12}, {"employee_id": 3, "needed_hours": 2}], "Logs": [{"employee_id": 1, "in_time": "2022-10-01 09:00:00", "out_time": "2022-10-01 17:00:00"}, {"employee_id": 1, "in_time": "2022-10-06 09:05:04", "out_time": "2022-10-06 17:09:03"}, {"employee_id": 1, "in_time": "2022-10-12 23:00:00", "out_time": "2022-10-13 03:00:01"}, {"employee_id": 2, "in_time": "2022-10-29 12:00:00", "out_time": "2022-10-29 23:58:58"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Round each work session before summing

The company counts session duration in whole minutes, rounding each individual session upward. This order matters:

$$
\sum \left\lceil\frac{\text{session seconds}}{60}\right\rceil
$$

is not always equal to rounding the total seconds once. Two sessions of one minute and one second each count as two minutes each, for four total, whereas their combined two minutes and two seconds would round to three.

The CTE `T` performs the required per-session ceiling inside `SUM`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"employee_id": 1, "needed_hours": 20}, {"employee_id": 2, "needed_hours": 12}, {"employee_id": 3, "needed_hours": 2}], "Logs": [{"employee_id": 1, "in_time": "2022-10-01 09:00:00", "out_time": "2022-10-01 17:00:00"}, {"employee_id": 1, "in_time": "2022-10-06 09:05:04", "out_time": "2022-10-06 17:09:03"}, {"employee_id": 1, "in_time": "2022-10-12 23:00:00", "out_time": "2022-10-13 03:00:01"}, {"employee_id": 2, "in_time": "2022-10-29 12:00:00", "out_time": "2022-10-29 23:58:58"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute one session's rounded minutes

`TIMESTAMPDIFF(second, in_time, out_time)` returns the elapsed whole seconds between the two datetimes. It naturally handles a session crossing midnight because both values contain dates, not only clock times.

Dividing by `60` converts seconds to minutes, possibly fractional. `CEILING(...)` raises any partial minute to the next integer. A duration exactly divisible by sixty remains unchanged.

The expression inside the CTE is:



Grouping by `employee_id` adds all independently rounded session minutes for that employee.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Convert total minutes to hours

The CTE divides the summed minutes by `60` and names the result `tot`. This yields total worked hours, possibly fractional, so it can be compared directly with integer `needed_hours`.

Equivalently, the query could keep total minutes and compare against `needed_hours * 60`. The current units are consistent because both sides of:



are hours.

The comparison is strict. An employee who works exactly the required number of hours should not be deducted; only a smaller total qualifies.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id"], "rows": [[2], [3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"employee_id": 1, "needed_hours": 20}, {"employee_id": 2, "needed_hours": 12}, {"employee_id": 3, "needed_hours": 2}], "Logs": [{"employee_id": 1, "in_time": "2022-10-01 09:00:00", "out_time": "2022-10-01 17:00:00"}, {"employee_id": 1, "in_time": "2022-10-06 09:05:04", "out_time": "2022-10-06 17:09:03"}, {"employee_id": 1, "in_time": "2022-10-12 23:00:00", "out_time": "2022-10-13 03:00:01"}, {"employee_id": 2, "in_time": "2022-10-29 12:00:00", "out_time": "2022-10-29 23:58:58"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id"], "rows": [[2], [3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Round after summing seconds:** This is incorrect because the specification rounds every session independently.
- **Compare in minutes:** Keep the summed rounded minutes and test against `needed_hours * 60`. It is equivalent and avoids fractional-hour representation.
- **Inner join:** It loses employees with no sessions, who must be treated as working zero hours.
- **Exact-minute session:** `CEILING` leaves its integer minute count unchanged.
- **Any positive leftover seconds:** The session receives one additional credited minute.
- **Session crossing midnight:** Full datetime difference handles it correctly.
- **Exactly enough total time:** The strict `<` comparison does not report that employee.
- **No logs:** `COALESCE` supplies zero and the employee is deducted because required hours are positive.
- **Multiple sessions:** Each ceiling occurs before `SUM`, preserving the rule.
- **Any output order:** No sorting is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E+L)$. Let $E$ be the number of employees and $L$ the number of log rows. The manifest gives $O((E+L)\log(E+L))$ time and $O(E+L)$ space for a general sort/group/join execution.
- **Auxiliary Space Complexity:** $O(E + L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
