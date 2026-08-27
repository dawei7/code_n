# Guided Example: Primary Department for Each Employee

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"employee_id": 1, "department_id": 1, "primary_flag": "N"}, {"employee_id": 2, "department_id": 1, "primary_flag": "Y"}, {"employee_id": 2, "department_id": 2, "primary_flag": "N"}, {"employee_id": 3, "department_id": 3, "primary_flag": "N"}, {"employee_id": 4, "department_id": 2, "primary_flag": "N"}, {"employee_id": 4, "department_id": 3, "primary_flag": "Y"}, {"employee_id": 4, "department_id": 4, "primary_flag": "N"}]}}`
- **Required output:** `{"columns": ["employee_id", "department_id"], "rows": [[1, 1], [2, 1], [3, 3], [4, 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["employee_id", "department_id"], "rows": [[1, 1], [2, 1], [3, 3], [4, 3]]}` from `{"tables": {"Employee": [{"employee_id": 1, "department_id": 1, "primary_flag": "N"}, {"employee_id": 2, "department_id": 1, "primary_flag": "Y"}, {"employee_id": 2, "department_id": 2, "primary_flag": "N"}, {"employee_id": 3, "department_id": 3, "primary_flag": "N"}, {"employee_id": 4, "department_id": 2, "primary_flag": "N"}, {"employee_id": 4, "department_id": 3, "primary_flag": "Y"}, {"employee_id": 4, "department_id": 4, "primary_flag": "N"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: There are two kinds of employees

The table stores one row for each employee-department membership, with `(employee_id, department_id)` as the composite primary key. The requested output needs one department for each employee, but the rule depends on how many memberships that employee has:

- if the employee belongs to multiple departments, select the row explicitly marked `primary_flag = 'Y'`;
- if the employee belongs to exactly one department, select that only row even though its flag is `'N'`.

The protected SQL solution handles these as two separate queries and combines their results.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"employee_id": 1, "department_id": 1, "primary_flag": "N"}, {"employee_id": 2, "department_id": 1, "primary_flag": "Y"}, {"employee_id": 2, "department_id": 2, "primary_flag": "N"}, {"employee_id": 3, "department_id": 3, "primary_flag": "N"}, {"employee_id": 4, "department_id": 2, "primary_flag": "N"}, {"employee_id": 4, "department_id": 3, "primary_flag": "Y"}, {"employee_id": 4, "department_id": 4, "primary_flag": "N"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First query: take explicit primary rows

The first `SELECT` reads `employee_id` and `department_id` from `Employee` with the filter `primary_flag = 'Y'`. This directly handles employees with several membership rows. Their chosen department is encoded in the row itself, so no aggregation is necessary in this branch.

Single-department employees do not appear here because the description states that their sole row has flag `'N'`. They are deliberately supplied by the second branch.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first `SELECT` reads `employee_id` and `department_id` f... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Second query: identify one-row employee groups

The second `SELECT` groups the table by its first selected expression. `GROUP BY 1` is ordinal syntax: the number 1 refers to `employee_id`, the first expression in the select list. It does not group by the literal integer one.

`COUNT(1)` counts the rows in each employee group. The `HAVING COUNT(1) = 1` condition is applied after grouping and keeps only employees who have exactly one membership row. For such a group, that one row's `department_id` is necessarily the department to report.

`HAVING` is required rather than `WHERE` because the condition depends on an aggregate count computed for a whole group. A row-level `WHERE` clause cannot know how many sibling rows share its employee ID.

The composite primary key guarantees that two rows for the same employee cannot repeat the same department. Consequently, counting rows is equivalent to counting that employee's department memberships; `COUNT(DISTINCT department_id)` is unnecessary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "department_id"], "rows": [[1, 1], [2, 1], [3, 3], [4, 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"employee_id": 1, "department_id": 1, "primary_flag": "N"}, {"employee_id": 2, "department_id": 1, "primary_flag": "Y"}, {"employee_id": 2, "department_id": 2, "primary_flag": "N"}, {"employee_id": 3, "department_id": 3, "primary_flag": "N"}, {"employee_id": 4, "department_id": 2, "primary_flag": "N"}, {"employee_id": 4, "department_id": 3, "primary_flag": "Y"}, {"employee_id": 4, "department_id": 4, "primary_flag": "N"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "department_id"], "rows": [[1, 1], [2, 1], [3, 3], [4, 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`UNION ALL`:** Under the stated rules the two :** - **`UNION ALL`:** Under the stated rules the two branches are disjoint, so it can avoid duplicate elimination. Plain `UNION` is safer against overlapping rows and is what the protected source uses.
- **Window count:** Compute `COUNT(*) OVER (PARTITION BY employee_id)` for every row, then retain rows whose count is one or whose flag is `'Y'`. This expresses both cases in one filter and is portable on engines with window functions.
- **Grouped subquery plus join:** Find employee IDs having one row, join them back for their department, and union with `'Y'` rows. This avoids selecting a non-grouped column under strict SQL modes.
- **Conditional aggregation:** Group per employee and choose the flagged department, falling back to the only department. It can work but needs careful handling of the single-row `'N'` case.
- **Filter only `'Y'`:** This omits every employee who belongs to one department because those rows deliberately use `'N'`.
- **Return every `'N'` row:** This wrongly includes non-primary memberships of multi-department employees.
- **`WHERE COUNT(1) = 1`:** Aggregate values are unavailable to `WHERE`; the group-count predicate belongs in `HAVING`.
- **`GROUP BY 1` meaning:** The ordinal refers to the first select expression, `employee_id`, not to a constant.
- **Composite primary key:** It prevents duplicate employee-department memberships and makes row count a membership count.
- **One-department employee:** The only row is returned regardless of its `'N'` flag.
- **Multi-department employee:** The designated `'Y'` row is returned; its other `'N'` rows are excluded.
- **Any output order:** No ordering clause is necessary, and consumers must not rely on branch order.
- **Strict MySQL mode:** `ONLY_FULL_GROUP_BY` may reject the exact second branch; a join or window formulation is more portable.
- **Declarative execution:** Complexity can vary with indexes, statistics, memory limits, and the optimizer even though the logical result is fixed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let $R$ be the number of rows in `Employee` and $M$ the number of distinct employees. SQL describes a result rather than prescribing one physical execution plan, so exact costs depend on indexes and the database optimizer.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
