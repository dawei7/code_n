# Guided Example: Find Cumulative Salary of an Employee

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"Id": 1, "Month": 1, "Salary": 20}, {"Id": 2, "Month": 1, "Salary": 20}, {"Id": 1, "Month": 2, "Salary": 30}, {"Id": 2, "Month": 2, "Salary": 30}, {"Id": 3, "Month": 2, "Salary": 40}, {"Id": 1, "Month": 3, "Salary": 40}, {"Id": 3, "Month": 3, "Salary": 60}, {"Id": 1, "Month": 4, "Salary": 60}, {"Id": 3, "Month": 4, "Salary": 70}, {"Id": 1, "Month": 7, "Salary": 90}, {"Id": 1, "Month": 8, "Salary": 90}]}}`
- **Required output:** `{"columns": ["Id", "Month", "Salary"], "rows": [[1, 7, 90], [1, 4, 130], [1, 3, 90], [1, 2, 50], [1, 1, 20], [2, 1, 20], [3, 3, 100], [3, 2, 40]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["Id", "Month", "Salary"], "rows": [[1, 7, 90], [1, 4, 130], [1, 3, 90], [1, 2, 50], [1, 1, 20], [2, 1, 20], [3, 3, 100], [3, 2, 40]]}` from `{"tables": {"Employee": [{"Id": 1, "Month": 1, "Salary": 20}, {"Id": 2, "Month": 1, "Salary": 20}, {"Id": 1, "Month": 2, "Salary": 30}, {"Id": 2, "Month": 2, "Salary": 30}, {"Id": 3, "Month": 2, "Salary": 40}, {"Id": 1, "Month": 3, "Salary": 40}, {"Id": 3, "Month": 3, "Salary": 60}, {"Id": 1, "Month": 4, "Salary": 60}, {"Id": 3, "Month": 4, "Salary": 70}, {"Id": 1, "Month": 7, "Salary": 90}, {"Id": 1, "Month": 8, "Salary": 90}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Removing each employee’s latest month

The subquery



creates one pair per employee: the employee ID and that employee’s greatest recorded month. The outer `WHERE` excludes rows whose `(id, month)` pair appears in this set:



Using a pair is essential. Month 8 might be the latest month for employee 1 but an ordinary earlier month for a different employee. Comparing only `month` would incorrectly remove rows across employees. The composite comparison ties each maximum to its own ID.

The primary key is `(id, month)`, so these columns are non-`NULL` and unique together. That makes the composite `NOT IN` safe from the confusing unknown result that nullable values can introduce.

An employee with only one salary record has that sole row selected as the maximum and therefore has no output rows. This exactly follows “do not include the most recent month”; there is no other worked month to report.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"Id": 1, "Month": 1, "Salary": 20}, {"Id": 2, "Month": 1, "Salary": 20}, {"Id": 1, "Month": 2, "Salary": 30}, {"Id": 2, "Month": 2, "Salary": 30}, {"Id": 3, "Month": 2, "Salary": 40}, {"Id": 1, "Month": 3, "Salary": 40}, {"Id": 3, "Month": 3, "Salary": 60}, {"Id": 1, "Month": 4, "Salary": 60}, {"Id": 3, "Month": 4, "Salary": 70}, {"Id": 1, "Month": 7, "Salary": 90}, {"Id": 1, "Month": 8, "Salary": 90}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why filtering before the window does not damage earlier sums

SQL logically applies `WHERE` before window functions. Thus, the most recent row is removed before `SUM(...) OVER (...)` is evaluated. That might initially seem dangerous, but the frame for an earlier month looks only at the current month and prior months. A removed most-recent month is later than every retained month for that employee, so it could never belong to any retained row’s backward-looking frame. Removing it changes only the row that should not be output, not any earlier result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | SQL logically applies `WHERE` before window functions.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Partitioning keeps employees independent

`PARTITION BY id` starts a separate window calculation for every employee. Salary records belonging to one ID can never enter another employee’s sum. Within each partition, `ORDER BY month` establishes calendar-month order.

The frame is:



With the default endpoint of the current row, this means all rows whose ordering value lies from `current month - 2` through `current month`. If the current month is 7, only recorded months 5, 6, and 7 are eligible. Missing rows for 5 or 6 simply contribute nothing, which is equivalent to salaries of zero.

This is why `RANGE` is the right concept. `ROWS 2 PRECEDING` would mean the previous two *records*, regardless of their month numbers. For employee 1 in the sample, the previous recorded months before 7 are 4 and 3, but they are not the previous two calendar months. A row-based frame would incorrectly include those old salaries. The range-based frame sees the gap and returns only month 7’s salary, 90.

Because `(id, month)` is unique, there is at most one salary row for a particular employee-month. The frame does not need to combine duplicate monthly records.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["Id", "Month", "Salary"], "rows": [[1, 7, 90], [1, 4, 130], [1, 3, 90], [1, 2, 50], [1, 1, 20], [2, 1, 20], [3, 3, 100], [3, 2, 40]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"Id": 1, "Month": 1, "Salary": 20}, {"Id": 2, "Month": 1, "Salary": 20}, {"Id": 1, "Month": 2, "Salary": 30}, {"Id": 2, "Month": 2, "Salary": 30}, {"Id": 3, "Month": 2, "Salary": 40}, {"Id": 1, "Month": 3, "Salary": 40}, {"Id": 3, "Month": 3, "Salary": 60}, {"Id": 1, "Month": 4, "Salary": 60}, {"Id": 3, "Month": 4, "Salary": 70}, {"Id": 1, "Month": 7, "Salary": 90}, {"Id": 1, "Month": 8, "Salary": 90}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["Id", "Month", "Salary"], "rows": [[1, 7, 90], [1, 4, 130], [1, 3, 90], [1, 2, 50], [1, 1, 20], [2, 1, 20], [3, 3, 100], [3, 2, 40]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Three self-joins:** Join each current row to t:** - **Three self-joins:** Join each current row to the same employee at `month - 1` and `month - 2`, replacing missing salaries with zero. This directly models the three months but is longer and less adaptable than a window.
- **`ROWS 2 PRECEDING`:** This is incorrect when recorded months have gaps because it chooses prior rows rather than prior calendar values.
- **Correlated range subquery:** For every row, sum salaries with matching ID and month between `month - 2` and `month`. It is clear but may repeat range lookups for many rows.
- **`ROW_NUMBER` for latest exclusion:** Rank each employee’s rows by month descending, discard rank one, and then compute sums from an unfiltered base relation. This needs careful query layering so the latest row remains available during any calculation that needs it.
- **Single recorded month:** It is the employee’s most recent month and is entirely excluded.
- **Gaps in employment:** Missing months do not create rows and contribute zero. `RANGE` preserves this calendar meaning.
- **January or February:** Months below 1 have no records, so the range naturally adds only existing months.
- **Different employees with the same latest month:** The composite `(id, month)` comparison excludes each employee’s own maximum without cross-contamination.
- **Window order versus output order:** Ascending month inside `OVER` defines a backward numeric frame; descending month in the final `ORDER BY` only formats results.
- **Null behavior:** Primary-key columns `id` and `month` are non-`NULL`, avoiding the usual `NOT IN` null trap.
- **Only worked months reported:** Since every output originates from an `Employee` row, the query never invents a row for a missing calendar month.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of salary records. Grouping by employee to find maxima takes expected $O(R)$ time with hash aggregation, while a sort-based plan can take $O(R\log R)$. Evaluating the window requires rows to be organized by `id` and `month`. Without a covering order already available, sorting dominates at $O(R\log R)$. The final requested ordering can often reuse or partially reuse ordered data, but the conservative declared time remains $O(R\log R)$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
