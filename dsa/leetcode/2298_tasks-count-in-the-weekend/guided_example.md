# Guided Example: Tasks Count in the Weekend

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Tasks": [{"task_id": 1, "assignee_id": 1, "submit_date": "2022-06-13"}, {"task_id": 2, "assignee_id": 6, "submit_date": "2022-06-14"}, {"task_id": 3, "assignee_id": 6, "submit_date": "2022-06-15"}, {"task_id": 4, "assignee_id": 3, "submit_date": "2022-06-18"}, {"task_id": 5, "assignee_id": 5, "submit_date": "2022-06-19"}, {"task_id": 6, "assignee_id": 7, "submit_date": "2022-06-19"}]}}`
- **Required output:** `{"columns": ["weekend_cnt", "working_cnt"], "rows": [[3, 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Tasks`

The objective is to compute `{"columns": ["weekend_cnt", "working_cnt"], "rows": [[3, 3]]}` from `{"tables": {"Tasks": [{"task_id": 1, "assignee_id": 1, "submit_date": "2022-06-13"}, {"task_id": 2, "assignee_id": 6, "submit_date": "2022-06-14"}, {"task_id": 3, "assignee_id": 6, "submit_date": "2022-06-15"}, {"task_id": 4, "assignee_id": 3, "submit_date": "2022-06-18"}, {"task_id": 5, "assignee_id": 5, "submit_date": "2022-06-19"}, {"task_id": 6, "assignee_id": 7, "submit_date": "2022-06-19"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert each date to MySQL's weekday number

MySQL's `WEEKDAY(date)` returns zero for Monday, one for Tuesday, through five for Saturday and six for Sunday.

The weekend is therefore represented exactly by the set `(5,6)`. No textual day names, locale settings, or manual date arithmetic are needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Tasks": [{"task_id": 1, "assignee_id": 1, "submit_date": "2022-06-13"}, {"task_id": 2, "assignee_id": 6, "submit_date": "2022-06-14"}, {"task_id": 3, "assignee_id": 6, "submit_date": "2022-06-15"}, {"task_id": 4, "assignee_id": 3, "submit_date": "2022-06-18"}, {"task_id": 5, "assignee_id": 5, "submit_date": "2022-06-19"}, {"task_id": 6, "assignee_id": 7, "submit_date": "2022-06-19"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turn each classification into a zero-or-one value

For one task row,

`WEEKDAY(submit_date) IN (5, 6)`

evaluates to one when the date is Saturday or Sunday and zero otherwise in MySQL's numeric Boolean context.

The complementary expression with `NOT IN` produces one for Monday through Friday and zero for weekend dates.

Because the two conditions are complements for every non-null valid date, each task contributes exactly one to one output count and zero to the other.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For one task row,

`WEEKDAY(submit_date) IN (5, 6)`

evaluat... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Aggregate the weekend count

`SUM(WEEKDAY(submit_date) IN (5, 6)) AS weekend_cnt` adds the weekend indicator across all rows.

Each Saturday or Sunday task contributes one regardless of its assignee or task ID. The result is the number of task rows submitted during the weekend, not the number of distinct dates or assignees.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["weekend_cnt", "working_cnt"], "rows": [[3, 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Tasks": [{"task_id": 1, "assignee_id": 1, "submit_date": "2022-06-13"}, {"task_id": 2, "assignee_id": 6, "submit_date": "2022-06-14"}, {"task_id": 3, "assignee_id": 6, "submit_date": "2022-06-15"}, {"task_id": 4, "assignee_id": 3, "submit_date": "2022-06-18"}, {"task_id": 5, "assignee_id": 5, "submit_date": "2022-06-19"}, {"task_id": 6, "assignee_id": 7, "submit_date": "2022-06-19"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["weekend_cnt", "working_cnt"], "rows": [[3, 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **CASE expressions:** `SUM(CASE WHEN ... THEN 1 :** - **CASE expressions:** `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` is more portable and has the same meaning as MySQL Boolean summation.
- **DAYOFWEEK:** It uses a different numbering convention, so weekend constants must be adjusted carefully.
- **Count total minus weekend:** Working count can be `COUNT(*)-weekend_cnt`, but the exact query states both classifications independently.
- **Group by weekday:** It would produce up to seven rows and require another pivot or aggregation to reach the requested two columns.
- **Saturday:** `WEEKDAY` returns five and the row counts as weekend.
- **Sunday:** It returns six and also counts as weekend.
- **Monday through Friday:** Their values zero through four count as working days.
- **Several tasks on one date:** Every task row contributes separately.
- **Assignee repetition:** It has no effect because the requested count is not distinct by assignee.
- **Empty table extension:** Exact `SUM` returns null; `COALESCE` would be required for zero.
- **Null date extension:** `IN` and `NOT IN` on null produce null, so such a row contributes to neither sum; the stated schema semantics avoid this case.
- **Single output row:** No ordering clause is useful.
- **Primary key:** `task_id` uniqueness ensures each stored task is one row, although the aggregation does not need to reference the key explicitly.
- **Boundary between Friday and Saturday:** `WEEKDAY` changes from four to five, exactly where the weekend predicate becomes true.
- **Boolean arithmetic:** This compact syntax is MySQL-specific behavior; databases without numeric Booleans should use `CASE`.
- **No double counting:** `IN` and `NOT IN` are complementary for non-null weekday values, so the two totals sum to the task-row count.
- **Date rather than timestamp:** The schema's date type avoids timezone-dependent day changes during classification.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let `r` be the number of task rows. The database scans each row, evaluates `WEEKDAY` and two membership predicates, and updates constant-size aggregate state. Conceptual time is `O(r)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
