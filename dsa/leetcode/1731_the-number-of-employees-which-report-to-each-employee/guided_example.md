# Guided Example: The Number of Employees Which Report to Each Employee

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"employee_id": 9, "name": "Hercy", "reports_to": null, "age": 43}, {"employee_id": 6, "name": "Alice", "reports_to": 9, "age": 41}, {"employee_id": 4, "name": "Bob", "reports_to": 9, "age": 36}, {"employee_id": 2, "name": "Winston", "reports_to": null, "age": 37}]}}`
- **Required output:** `{"columns": ["employee_id", "name", "reports_count", "average_age"], "rows": [[9, "Hercy", 2, 39]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["employee_id", "name", "reports_count", "average_age"], "rows": [[9, "Hercy", 2, 39]]}` from `{"tables": {"Employees": [{"employee_id": 9, "name": "Hercy", "reports_to": null, "age": 43}, {"employee_id": 6, "name": "Alice", "reports_to": 9, "age": 41}, {"employee_id": 4, "name": "Bob", "reports_to": 9, "age": 36}, {"employee_id": 2, "name": "Winston", "reports_to": null, "age": 37}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use two roles of the same employee table

Every direct-report relationship is stored in one employee row: `reports_to` contains that employee's manager ID. Manager identity and name are stored in another row of the same table.

The query therefore uses a self-join:

- `e1` represents reporting employees.
- `e2` represents their managers.

The condition `e1.reports_to = e2.employee_id` pairs each report with the employee row for that report's manager.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"employee_id": 9, "name": "Hercy", "reports_to": null, "age": 43}, {"employee_id": 6, "name": "Alice", "reports_to": 9, "age": 41}, {"employee_id": 4, "name": "Bob", "reports_to": 9, "age": 36}, {"employee_id": 2, "name": "Winston", "reports_to": null, "age": 37}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an inner join returns only managers

An employee is a manager for this problem only if at least one other employee reports directly to them. Such an employee appears as `e2` in at least one joined pair.

Employees with no reports produce no joined rows and are absent automatically. Employees whose `reports_to` is null also do not match a manager row as `e1`, which is correct because they are not direct reports of anyone.

No separate `HAVING COUNT > 0` is needed because every output group is created from at least one successful join.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An employee is a manager for this problem only if at least o... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Group report rows by manager

`GROUP BY 1` groups by the first select expression, `e2.employee_id`. Since `employee_id` is unique, each group corresponds to one manager.

`e2.name` is functionally determined by that unique employee ID. MySQL can project the manager's name alongside the grouped key without creating separate groups for duplicate names. Two managers may share a name but remain separate because their IDs differ.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "name", "reports_count", "average_age"], "rows": [[9, "Hercy", 2, 39]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"employee_id": 9, "name": "Hercy", "reports_to": null, "age": 43}, {"employee_id": 6, "name": "Alice", "reports_to": 9, "age": 41}, {"employee_id": 4, "name": "Bob", "reports_to": 9, "age": 36}, {"employee_id": 2, "name": "Winston", "reports_to": null, "age": 37}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "name", "reports_count", "average_age"], "rows": [[9, "Hercy", 2, 39]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Group by `reports_to` then join:** Aggregate r:** - **Group by `reports_to` then join:** Aggregate report counts and ages first, then join the smaller manager summary to Employees for names. It is logically equivalent.
- **Correlated subqueries:** Count and average reports separately for every employee. Without good indexing, this repeats work.
- **Left self-join:** It would include nonmanagers unless filtered with `HAVING COUNT(e1.employee_id)>0`; the inner join naturally excludes them.
- **One direct report:** Count is one and average age equals that report's age.
- **Several hierarchy levels:** Only rows naming the manager directly enter the group.
- **Top-level employee:** A null `reports_to` does not make someone a report, but they can still appear as a manager through other rows.
- **Same manager names:** Unique IDs keep their groups separate.
- **Manager's own age:** It is excluded because averaging uses `e1.age`.
- **Half-value average:** MySQL `ROUND` produces the required nearest integer for positive ages.
- **No reports:** The employee has no joined group and is not returned.
- **Invalid manager reference outside the stated relational model:** An inner join would omit that reporting row because no manager identity exists.
- **Ordinal clauses:** `GROUP BY 1` and `ORDER BY 1` rely on manager ID remaining the first select expression.
- **Functional dependency:** Manager name is fixed by unique employee ID, allowing it to be selected with that group key.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let $E$ be the number of employee rows and $M$ the number of managers with reports. With a hash lookup or index on the unique manager ID, the self-join and aggregation can process rows in expected $O(E)$ time while storing $O(M)$ group states, matching the manifest.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
