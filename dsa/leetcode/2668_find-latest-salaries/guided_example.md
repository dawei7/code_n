# Guided Example: Find Latest Salaries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Salary": [{"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": "110000", "department_id": "D1006"}, {"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": "106119", "department_id": "D1006"}, {"emp_id": 2, "firstname": "Justin", "lastname": "Simon", "salary": "128922", "department_id": "D1005"}, {"emp_id": 2, "firstname": "Justin", "lastname": "Simon", "salary": "130000", "department_id": "D1005"}, {"emp_id": 3, "firstname": "Kelly", "lastname": "Rosario", "salary": "42689", "department_id": "D1002"}]}}`
- **Required output:** `{"columns": ["emp_id", "firstname", "lastname", "salary", "department_id"], "rows": [[1, "Todd", "Wilson", "110000", "D1006"], [2, "Justin", "Simon", "130000", "D1005"], [3, "Kelly", "Rosario", "42689", "D1002"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Salary`

The objective is to compute `{"columns": ["emp_id", "firstname", "lastname", "salary", "department_id"], "rows": [[1, "Todd", "Wilson", "110000", "D1006"], [2, "Justin", "Simon", "130000", "D1005"], [3, "Kelly", "Rosario", "42689", "D1002"]]}` from `{"tables": {"Salary": [{"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": "110000", "department_id": "D1006"}, {"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": "106119", "department_id": "D1006"}, {"emp_id": 2, "firstname": "Justin", "lastname": "Simon", "salary": "128922", "department_id": "D1005"}, {"emp_id": 2, "firstname": "Justin", "lastname": "Simon", "salary": "130000", "department_id": "D1005"}, {"emp_id": 3, "firstname": "Kelly", "lastname": "Rosario", "salary": "42689", "department_id": "D1002"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Group historical records by employee

An employee can have several salary rows. Under the assumption that salary increases over time, the current salary is the greatest salary recorded for that employee.

The query groups rows with:

`GROUP BY emp_id`.

Each group represents one employee identifier. Aggregate `MAX(salary)` then chooses one greatest salary value from that employee's records.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Salary": [{"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": "110000", "department_id": "D1006"}, {"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": "106119", "department_id": "D1006"}, {"emp_id": 2, "firstname": "Justin", "lastname": "Simon", "salary": "128922", "department_id": "D1005"}, {"emp_id": 2, "firstname": "Justin", "lastname": "Simon", "salary": "130000", "department_id": "D1005"}, {"emp_id": 3, "firstname": "Kelly", "lastname": "Rosario", "salary": "42689", "department_id": "D1002"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Select the requested columns

The output projects:

- `emp_id`;
- `firstname`;
- `lastname`;
- maximum salary aliased back to `salary`;
- `department_id`.

`AS salary` ensures the aggregate result uses the required output column name rather than a generated expression label.

The query assumes name and department fields are stable across all historical rows for the same employee. Under that intended data model, selecting those nonaggregated values alongside the grouped identifier yields the employee details associated with the group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The output projects:

- `emp_id`;
- `firstname`;
- `lastname... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why maximum represents latest

No year or timestamp column exists. The problem supplies a semantic assumption instead: salaries increase each year.

If historical salary sequence is strictly or non-strictly increasing over time, its greatest numeric value is the most recent value.

Thus:

$$
\text{currentSalary}(e)
=
\max\{\text{salary from rows with emp\_id }e\}.
$$

The query uses this inference rather than attempting to infer row insertion order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["emp_id", "firstname", "lastname", "salary", "department_id"], "rows": [[1, "Todd", "Wilson", "110000", "D1006"], [2, "Justin", "Simon", "130000", "D1005"], [3, "Kelly", "Rosario", "42689", "D1002"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Salary": [{"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": "110000", "department_id": "D1006"}, {"emp_id": 1, "firstname": "Todd", "lastname": "Wilson", "salary": "106119", "department_id": "D1006"}, {"emp_id": 2, "firstname": "Justin", "lastname": "Simon", "salary": "128922", "department_id": "D1005"}, {"emp_id": 2, "firstname": "Justin", "lastname": "Simon", "salary": "130000", "department_id": "D1005"}, {"emp_id": 3, "firstname": "Kelly", "lastname": "Rosario", "salary": "42689", "department_id": "D1002"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["emp_id", "firstname", "lastname", "salary", "department_id"], "rows": [[1, "Todd", "Wilson", "110000", "D1006"], [2, "Justin", "Simon", "130000", "D1005"], [3, "Kelly", "Rosario", "42689", "D1002"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Numeric cast inside `MAX`:** Safer because `sa:** - **Numeric cast inside `MAX`:** Safer because `salary` is declared `varchar` and numeric order may differ from text order.
- **Window function `ROW_NUMBER`:** Rank rows per employee by numeric salary descending and keep rank one; useful when row-specific changing attributes must come from the winning record.
- **Aggregate subquery plus join:** Portable way to retrieve the row corresponding to each maximum salary.
- **One record for an employee:** It is automatically current.
- **Equal numeric text formats:** Direct string maximum agrees with numeric maximum when positive strings have equal length.
- **Different digit lengths:** Exact query may compare lexically; a cast is needed for robust numeric semantics.
- **Stable employee details:** Required for nonaggregated selected fields to be unambiguous.
- **Strict SQL mode:** May require grouping additional columns or a join.
- **Composite primary key:** Prevents the same employee-salary pair from repeating.
- **Output order:** Bare `ORDER BY emp_id` means ascending by default.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of Salary rows and $E$ the number of employees.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
