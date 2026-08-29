# Guided Example: Employees Whose Manager Left the Company

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"employee_id": 3, "name": "Mila", "manager_id": 9, "salary": 60301}, {"employee_id": 12, "name": "Antonella", "manager_id": null, "salary": 31000}, {"employee_id": 13, "name": "Emery", "manager_id": null, "salary": 67084}, {"employee_id": 1, "name": "Kalel", "manager_id": 11, "salary": 21241}, {"employee_id": 9, "name": "Mikaela", "manager_id": null, "salary": 50937}, {"employee_id": 11, "name": "Joziah", "manager_id": 6, "salary": 28485}]}}`
- **Required output:** `{"columns": ["employee_id"], "rows": [[11]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["employee_id"], "rows": [[11]]}` from `{"tables": {"Employees": [{"employee_id": 3, "name": "Mila", "manager_id": 9, "salary": 60301}, {"employee_id": 12, "name": "Antonella", "manager_id": null, "salary": 31000}, {"employee_id": 13, "name": "Emery", "manager_id": null, "salary": 67084}, {"employee_id": 1, "name": "Kalel", "manager_id": 11, "salary": 21241}, {"employee_id": 9, "name": "Mikaela", "manager_id": null, "salary": 50937}, {"employee_id": 11, "name": "Joziah", "manager_id": 6, "salary": 28485}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the table as both employees and possible managers

Every manager who is still employed also has a row in `Employees` whose `employee_id` equals a report's `manager_id`. A manager who left has no such row, although the report retains the old ID. The problem is therefore an existence test against the same table.

The query aliases `Employees` as `e1` for the employee being considered and as `e2` for that employee's possible manager. The join condition

`e1.manager_id = e2.employee_id`

asks the database to find the manager row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"employee_id": 3, "name": "Mila", "manager_id": 9, "salary": 60301}, {"employee_id": 12, "name": "Antonella", "manager_id": null, "salary": 31000}, {"employee_id": 13, "name": "Emery", "manager_id": null, "salary": 67084}, {"employee_id": 1, "name": "Kalel", "manager_id": 11, "salary": 21241}, {"employee_id": 9, "name": "Mikaela", "manager_id": null, "salary": 50937}, {"employee_id": 11, "name": "Joziah", "manager_id": 6, "salary": 28485}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a left join is necessary

An inner join would retain only employees whose manager row exists. Those are precisely the employees that must be excluded, so an inner join would discard the desired evidence.

A `LEFT JOIN` retains every `e1` row. If a matching manager exists, columns from `e2` contain that manager's values. If none exists, all `e2` columns are SQL `NULL`. Because `employee_id` is a primary key and cannot itself be null in a real row, `e2.employee_id IS NULL` is a reliable unmatched-row test.

This pattern is called an anti-join: keep left-side rows for which no right-side match exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply all three required filters

`e1.salary < 30000` enforces the strict salary limit. A salary equal to 30000 does not qualify.

`e1.manager_id IS NOT NULL` distinguishes "had a manager whose row is gone" from "does not have a manager." Without this condition, a top-level employee's null manager ID would fail to match any `e2` row and would incorrectly look like a departed manager.

`e2.employee_id IS NULL` then proves that the nonnull recorded manager ID is absent from the current table.

The three predicates together express the contract exactly: low salary, an actual recorded manager ID, and no current employee row for that manager.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id"], "rows": [[11]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"employee_id": 3, "name": "Mila", "manager_id": 9, "salary": 60301}, {"employee_id": 12, "name": "Antonella", "manager_id": null, "salary": 31000}, {"employee_id": 13, "name": "Emery", "manager_id": null, "salary": 67084}, {"employee_id": 1, "name": "Kalel", "manager_id": 11, "salary": 21241}, {"employee_id": 9, "name": "Mikaela", "manager_id": null, "salary": 50937}, {"employee_id": 11, "name": "Joziah", "manager_id": 6, "salary": 28485}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id"], "rows": [[11]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`NOT EXISTS` correlated subquery:** Expresses the anti-join directly and is often optimized to a similar execution plan.
- **`NOT IN` subquery:** It is concise but can have surprising three-valued-logic behavior when nulls are possible; `NOT EXISTS` or left anti-join is clearer.
- **Inner join:** Incorrectly preserves managers who still exist and discards employees whose manager left.
- **Missing `manager_id IS NOT NULL` check:** Would misclassify employees who never had a manager as having a departed manager.
- **Salary exactly 30000:** Excluded because the comparison is strict.
- **Manager still employed:** A matching `e2` primary key makes the null test false.
- **Departed manager:** The retained nonnull ID has no match, so the left-joined key is null.
- **Several employees share one departed manager:** Each qualifying low-salary report is returned independently.
- **Primary-key uniqueness:** Prevents one employee from acquiring duplicate joined manager rows.
- **Null comparison:** Use `IS NOT NULL` and `IS NULL`; equality comparisons with SQL `NULL` do not evaluate to true.
- **Required ordering:** `ORDER BY 1` sorts the sole result column in ascending order by default.
- **No table mutation:** The query only reads `Employees`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of employee rows. The database scans candidate employee rows and performs manager-existence lookups. With a hash anti-join, expected time and working space are $O(R)$, matching the manifest. With the primary-key B-tree used for repeated lookups, a possible plan is $O(R\log R)$ time and smaller extra memory. SQL complexity depends on the optimizer and indexes rather than being fixed solely by query text.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
