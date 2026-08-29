# Guided Example: Find Overbooked Employees

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice Johnson", "department": "Engineering"}, {"employee_id": 2, "employee_name": "Bob Smith", "department": "Marketing"}, {"employee_id": 3, "employee_name": "Carol Davis", "department": "Sales"}, {"employee_id": 4, "employee_name": "David Wilson", "department": "Engineering"}, {"employee_id": 5, "employee_name": "Emma Brown", "department": "HR"}], "meetings": [{"meeting_id": 1, "employee_id": 1, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 8.0}, {"meeting_id": 2, "employee_id": 1, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 6.0}, {"meeting_id": 3, "employee_id": 1, "meeting_date": "2023-06-07", "meeting_type": "Training", "duration_hours": 7.0}, {"meeting_id": 4, "employee_id": 1, "meeting_date": "2023-06-12", "meeting_type": "Team", "duration_hours": 12.0}, {"meeting_id": 5, "employee_id": 1, "meeting_date": "2023-06-13", "meeting_type": "Client", "duration_hours": 9.0}, {"meeting_id": 6, "employee_id": 2, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 15.0}, {"meeting_id": 7, "employee_id": 2, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 8.0}, {"meeting_id": 8, "employee_id": 2, "meeting_date": "2023-06-12", "meeting_type": "Training", "duration_hours": 10.0}, {"meeting_id": 9, "employee_id": 3, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 4.0}, {"meeting_id": 10, "employee_id": 3, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 3.0}, {"meeting_id": 11, "employee_id": 4, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 25.0}, {"meeting_id": 12, "employee_id": 4, "meeting_date": "2023-06-19", "meeting_type": "Client", "duration_hours": 22.0}, {"meeting_id": 13, "employee_id": 5, "meeting_date": "2023-06-05", "meeting_type": "Training", "duration_hours": 2.0}]}}`
- **Required output:** `{"columns": ["employee_id", "employee_name", "department", "meeting_heavy_weeks"], "rows": [[1, "Alice Johnson", "Engineering", 2], [4, "David Wilson", "Engineering", 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `employees`

The objective is to compute `{"columns": ["employee_id", "employee_name", "department", "meeting_heavy_weeks"], "rows": [[1, "Alice Johnson", "Engineering", 2], [4, "David Wilson", "Engineering", 2]]}` from `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice Johnson", "department": "Engineering"}, {"employee_id": 2, "employee_name": "Bob Smith", "department": "Marketing"}, {"employee_id": 3, "employee_name": "Carol Davis", "department": "Sales"}, {"employee_id": 4, "employee_name": "David Wilson", "department": "Engineering"}, {"employee_id": 5, "employee_name": "Emma Brown", "department": "HR"}], "meetings": [{"meeting_id": 1, "employee_id": 1, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 8.0}, {"meeting_id": 2, "employee_id": 1, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 6.0}, {"meeting_id": 3, "employee_id": 1, "meeting_date": "2023-06-07", "meeting_type": "Training", "duration_hours": 7.0}, {"meeting_id": 4, "employee_id": 1, "meeting_date": "2023-06-12", "meeting_type": "Team", "duration_hours": 12.0}, {"meeting_id": 5, "employee_id": 1, "meeting_date": "2023-06-13", "meeting_type": "Client", "duration_hours": 9.0}, {"meeting_id": 6, "employee_id": 2, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 15.0}, {"meeting_id": 7, "employee_id": 2, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 8.0}, {"meeting_id": 8, "employee_id": 2, "meeting_date": "2023-06-12", "meeting_type": "Training", "duration_hours": 10.0}, {"meeting_id": 9, "employee_id": 3, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 4.0}, {"meeting_id": 10, "employee_id": 3, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 3.0}, {"meeting_id": 11, "employee_id": 4, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 25.0}, {"meeting_id": 12, "employee_id": 4, "meeting_date": "2023-06-19", "meeting_type": "Client", "duration_hours": 22.0}, {"meeting_id": 13, "employee_id": 5, "meeting_date": "2023-06-05", "meeting_type": "Training", "duration_hours": 2.0}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First CTE: weekly totals

`week_meeting_hours` reads `meetings` and groups by three selected expressions:

- `employee_id`;
- `YEAR(meeting_date)`, aliased as `year`;
- `WEEK(meeting_date, 1)`, aliased as `week`.

`GROUP BY 1, 2, 3` uses ordinal positions, so it refers to those first three selected columns. For every resulting group:

`SUM(duration_hours) hours`

adds the durations of all meeting types. Team, Client, and Training meetings are treated equally because the task asks for total meeting time and the query applies no type filter.

MySQL's `WEEK(date, 1)` uses Monday as the first day of the week, which matches the Monday-to-Sunday requirement for ordinary within-year dates. The mode can produce week numbers from 0 through 53.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice Johnson", "department": "Engineering"}, {"employee_id": 2, "employee_name": "Bob Smith", "department": "Marketing"}, {"employee_id": 3, "employee_name": "Carol Davis", "department": "Sales"}, {"employee_id": 4, "employee_name": "David Wilson", "department": "Engineering"}, {"employee_id": 5, "employee_name": "Emma Brown", "department": "HR"}], "meetings": [{"meeting_id": 1, "employee_id": 1, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 8.0}, {"meeting_id": 2, "employee_id": 1, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 6.0}, {"meeting_id": 3, "employee_id": 1, "meeting_date": "2023-06-07", "meeting_type": "Training", "duration_hours": 7.0}, {"meeting_id": 4, "employee_id": 1, "meeting_date": "2023-06-12", "meeting_type": "Team", "duration_hours": 12.0}, {"meeting_id": 5, "employee_id": 1, "meeting_date": "2023-06-13", "meeting_type": "Client", "duration_hours": 9.0}, {"meeting_id": 6, "employee_id": 2, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 15.0}, {"meeting_id": 7, "employee_id": 2, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 8.0}, {"meeting_id": 8, "employee_id": 2, "meeting_date": "2023-06-12", "meeting_type": "Training", "duration_hours": 10.0}, {"meeting_id": 9, "employee_id": 3, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 4.0}, {"meeting_id": 10, "employee_id": 3, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 3.0}, {"meeting_id": 11, "employee_id": 4, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 25.0}, {"meeting_id": 12, "employee_id": 4, "meeting_date": "2023-06-19", "meeting_type": "Client", "duration_hours": 22.0}, {"meeting_id": 13, "employee_id": 5, "meeting_date": "2023-06-05", "meeting_type": "Training", "duration_hours": 2.0}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A year-boundary limitation

The CTE pairs `WEEK(meeting_date, 1)` with the calendar value `YEAR(meeting_date)`. A Monday-to-Sunday week that crosses December 31 may contain dates from two calendar years. Those dates can receive different `year` grouping values even though they belong to the same physical Monday-to-Sunday week.

A more robust key would use a Monday week-start date or a compatible `YEARWEEK` mode as one combined week identity. The exact query does not do that. Under data that does not exercise a cross-year week, its grouping behaves as intended; at a year boundary, it may split one week into two groups.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Filtering weekly totals

The second CTE, `intensive_weeks`, joins weekly totals to `employees` with `USING (employee_id)`. This supplies `employee_name` and `department` for each aggregated employee week.

The `WHERE` clause is applied before the employee-level grouping, so only rows considered heavy remain. The query writes:

`WHERE hours >= 20`.

The problem's 40-hour-week rule says more than 50 percent, equivalently:

`hours > 20`.

Exactly 20 hours is 50 percent, not more than 50 percent. Therefore, the non-strict operator is a real semantic mismatch. Any later count and filtering can be inflated by weeks totaling exactly 20.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "employee_name", "department", "meeting_heavy_weeks"], "rows": [[1, "Alice Johnson", "Engineering", 2], [4, "David Wilson", "Engineering", 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice Johnson", "department": "Engineering"}, {"employee_id": 2, "employee_name": "Bob Smith", "department": "Marketing"}, {"employee_id": 3, "employee_name": "Carol Davis", "department": "Sales"}, {"employee_id": 4, "employee_name": "David Wilson", "department": "Engineering"}, {"employee_id": 5, "employee_name": "Emma Brown", "department": "HR"}], "meetings": [{"meeting_id": 1, "employee_id": 1, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 8.0}, {"meeting_id": 2, "employee_id": 1, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 6.0}, {"meeting_id": 3, "employee_id": 1, "meeting_date": "2023-06-07", "meeting_type": "Training", "duration_hours": 7.0}, {"meeting_id": 4, "employee_id": 1, "meeting_date": "2023-06-12", "meeting_type": "Team", "duration_hours": 12.0}, {"meeting_id": 5, "employee_id": 1, "meeting_date": "2023-06-13", "meeting_type": "Client", "duration_hours": 9.0}, {"meeting_id": 6, "employee_id": 2, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 15.0}, {"meeting_id": 7, "employee_id": 2, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 8.0}, {"meeting_id": 8, "employee_id": 2, "meeting_date": "2023-06-12", "meeting_type": "Training", "duration_hours": 10.0}, {"meeting_id": 9, "employee_id": 3, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 4.0}, {"meeting_id": 10, "employee_id": 3, "meeting_date": "2023-06-06", "meeting_type": "Client", "duration_hours": 3.0}, {"meeting_id": 11, "employee_id": 4, "meeting_date": "2023-06-05", "meeting_type": "Team", "duration_hours": 25.0}, {"meeting_id": 12, "employee_id": 4, "meeting_date": "2023-06-19", "meeting_type": "Client", "duration_hours": 22.0}, {"meeting_id": 13, "employee_id": 5, "meeting_date": "2023-06-05", "meeting_type": "Training", "duration_hours": 2.0}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "employee_name", "department", "meeting_heavy_weeks"], "rows": [[1, "Alice Johnson", "Engineering", 2], [4, "David Wilson", "Engineering", 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correct the heavy predicate:** The required comparison is `hours > 20`. The source's `>= 20` incorrectly includes exactly-half weeks.
- **Group by Monday start date:** Compute the date of each week's Monday and group by that single value, avoiding calendar-year boundary splits.
- **Use compatible `YEARWEEK`:** A properly chosen MySQL mode can provide one combined Monday-based week key; mixing `YEAR` with `WEEK` is less robust.
- **Conditional employee aggregation:** Weekly totals still require a first grouping, but a second grouped query with `HAVING COUNT(*) >= 2` can replace the outer CTE filter.
- **Join employee details after counting:** Count by `employee_id` first, then join `employees`, avoiding reliance on functional-dependency handling in grouped selection.
- **Exactly 20 hours:** It must not count under the statement, but the exact source counts it.
- **More than 20 hours:** Decimal totals such as 20.01 qualify.
- **One heavy week:** The employee is excluded by the at-least-two rule.
- **Two heavy weeks:** The employee qualifies regardless of whether those weeks are consecutive.
- **Several meetings in one week:** Their durations are summed before the week is counted, so they contribute one heavy-week row at most.
- **Different meeting types:** All types contribute because no type filter appears.
- **Week crossing New Year:** `YEAR` may split dates that share one Monday-to-Sunday interval.
- **Employee with no meetings:** No first-CTE row exists, so the employee cannot appear.
- **Meeting without employee metadata:** The inner join removes it; valid relational data should prevent that situation.
- **NULL duration:** MySQL `SUM` ignores NULL values; explicit data-quality behavior would be needed if NULLs are allowed.
- **Tied heavy-week counts:** Employee name breaks the tie in ascending order.
- **Duplicate employee names:** Their remaining relative order is unspecified unless `employee_id` is added as a final key.
- **Read-only behavior:** The CTEs aggregate and select data; they do not modify either table.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let `M` be the number of meeting rows and `E` the number of employee rows. The physical cost depends on MySQL's execution plan, indexes, and available memory.
- **Auxiliary Space Complexity:** $O(M + E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
