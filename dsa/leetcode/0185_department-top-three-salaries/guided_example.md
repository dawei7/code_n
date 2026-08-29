# Guided Example: Department Top Three Salaries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1}, {"id": 2, "name": "Jim", "salary": 90000, "departmentId": 1}, {"id": 3, "name": "Henry", "salary": 80000, "departmentId": 2}, {"id": 4, "name": "Sam", "salary": 60000, "departmentId": 2}, {"id": 5, "name": "Max", "salary": 90000, "departmentId": 1}, {"id": 6, "name": "Janet", "salary": 69000, "departmentId": 1}, {"id": 7, "name": "Randy", "salary": 85000, "departmentId": 1}], "Department": [{"id": 1, "name": "IT"}, {"id": 2, "name": "Sales"}]}}`
- **Required output:** `{"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Jim", 90000], ["IT", "Max", 90000], ["IT", "Joe", 85000], ["IT", "Randy", 85000], ["IT", "Janet", 69000], ["Sales", "Henry", 80000], ["Sales", "Sam", 60000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Jim", 90000], ["IT", "Max", 90000], ["IT", "Joe", 85000], ["IT", "Randy", 85000], ["IT", "Janet", 69000], ["Sales", "Henry", 80000], ["Sales", "Sam", 60000]]}` from `{"tables": {"Employee": [{"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1}, {"id": 2, "name": "Jim", "salary": 90000, "departmentId": 1}, {"id": 3, "name": "Henry", "salary": 80000, "departmentId": 2}, {"id": 4, "name": "Sam", "salary": 60000, "departmentId": 2}, {"id": 5, "name": "Max", "salary": 90000, "departmentId": 1}, {"id": 6, "name": "Janet", "salary": 69000, "departmentId": 1}, {"id": 7, "name": "Randy", "salary": 85000, "departmentId": 1}], "Department": [{"id": 1, "name": "IT"}, {"id": 2, "name": "Sales"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Understand what “top three unique salaries” counts

An employee is a high earner when the employee's salary is one of the three
largest distinct salary values in that employee's department. The word
“unique” changes the ranking rule. If two employees both earn 85000, that value
occupies one salary level, not two positions. Both employees must receive the
same effective rank.

A convenient way to determine the rank of a salary $s$ is to ask how many
distinct salaries in the same department are strictly greater than $s$. If
that count is zero, $s$ is the highest unique salary. If it is one, $s$ is the
second-highest; if it is two, $s$ is the third-highest. Therefore, the employee
qualifies exactly when the count is less than three.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1}, {"id": 2, "name": "Jim", "salary": 90000, "departmentId": 1}, {"id": 3, "name": "Henry", "salary": 80000, "departmentId": 2}, {"id": 4, "name": "Sam", "salary": 60000, "departmentId": 2}, {"id": 5, "name": "Max", "salary": 90000, "departmentId": 1}, {"id": 6, "name": "Janet", "salary": 69000, "departmentId": 1}, {"id": 7, "name": "Randy", "salary": 85000, "departmentId": 1}], "Department": [{"id": 1, "name": "IT"}, {"id": 2, "name": "Sales"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build each employee's department context

The outer query reads `Employee` and `Department` with comma-style join syntax.
The condition `Employee.DepartmentId = Department.Id` turns that Cartesian
product into an inner equijoin. It associates every employee with the readable
department name required in the result.

Modern SQL usually writes this as an explicit `INNER JOIN ... ON ...`. The two
forms have the same relational meaning here, but explicit join syntax makes it
harder to forget the matching condition and accidentally create every possible
employee-department pair.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Correlate the count with the current employee

For each outer `Employee` row, the subquery scans another logical copy of the
employee table named `e2`. Its first predicate, `e2.Salary > Employee.Salary`,
keeps only salaries strictly greater than the current salary. Its second
predicate, `Employee.DepartmentId = e2.DepartmentId`, restricts the comparison
to the current employee's own department.

Both predicates are indispensable. Replacing `>` with `>=` would count the
current salary level and shift every rank by one. Omitting the department
condition would compare against the whole company and incorrectly suppress
leaders in departments whose salaries are lower than another department's.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Jim", 90000], ["IT", "Max", 90000], ["IT", "Joe", 85000], ["IT", "Randy", 85000], ["IT", "Janet", 69000], ["Sales", "Henry", 80000], ["Sales", "Sam", 60000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1}, {"id": 2, "name": "Jim", "salary": 90000, "departmentId": 1}, {"id": 3, "name": "Henry", "salary": 80000, "departmentId": 2}, {"id": 4, "name": "Sam", "salary": 60000, "departmentId": 2}, {"id": 5, "name": "Max", "salary": 90000, "departmentId": 1}, {"id": 6, "name": "Janet", "salary": 69000, "departmentId": 1}, {"id": 7, "name": "Randy", "salary": 85000, "departmentId": 1}], "Department": [{"id": 1, "name": "IT"}, {"id": 2, "name": "Sales"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Jim", 90000], ["IT", "Max", 90000], ["IT", "Joe", 85000], ["IT", "Randy", 85000], ["IT", "Janet", 69000], ["Sales", "Henry", 80000], ["Sales", "Sam", 60000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`DENSE_RANK()` window function:** Partition by department, order salary descending, and retain ranks at most three; this directly models unique salary levels.
- **Distinct salary table:** Deduplicate department-salary pairs, choose the top three per department, then join back to all employees so ties survive.
- **Pandas dense rank:** The local editorial uses descending dense rank within each department and filters values at most three.
- **Plain `COUNT(*)`:** Incorrect when several higher-paid employees share a salary because it ranks people instead of unique salary values.
- **Strict comparison:** Use `>`; `>=` would count the current salary level and cause an off-by-one error.
- **Ties at any qualifying level:** Return every tied employee.
- **Fewer than three unique salaries:** Return every employee in that department.
- **Same salary in different departments:** The correlation must include `DepartmentId`.
- **Nullable salary:** The stored comparison does not define a safe null ranking and may admit nulls incorrectly.
- **Any order:** No output sorting is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m)$. Let $n$ be the number of employees and $m$ the number of departments. Read
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
