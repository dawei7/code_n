# Guided Example: Department Highest Salary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1}, {"id": 2, "name": "Max", "salary": 90000, "departmentId": 1}, {"id": 3, "name": "Sam", "salary": 60000, "departmentId": 2}, {"id": 4, "name": "Randy", "salary": 85000, "departmentId": 2}], "Department": [{"id": 1, "name": "IT"}, {"id": 2, "name": "Sales"}]}}`
- **Required output:** `{"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Max", 90000], ["Sales", "Randy", 85000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Max", 90000], ["Sales", "Randy", 85000]]}` from `{"tables": {"Employee": [{"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1}, {"id": 2, "name": "Max", "salary": 90000, "departmentId": 1}, {"id": 3, "name": "Sam", "salary": 60000, "departmentId": 2}, {"id": 4, "name": "Randy", "salary": 85000, "departmentId": 2}], "Department": [{"id": 1, "name": "IT"}, {"id": 2, "name": "Sales"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate the problem into a threshold and the rows meeting it

For each department, the query must first determine one value: the greatest
salary among that department's employees. It must then return every employee
whose salary equals that value. These are distinct operations because an
aggregate such as `MAX(salary)` produces the maximum value but does not by
itself preserve all employee rows tied at that maximum.

The stored query expresses the two operations with a grouped subquery followed
by a tuple-membership filter. This is especially important for ties. Selecting
an arbitrary employee beside `MAX(salary)` could lose another employee who has
the same top salary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1}, {"id": 2, "name": "Max", "salary": 90000, "departmentId": 1}, {"id": 3, "name": "Sam", "salary": 60000, "departmentId": 2}, {"id": 4, "name": "Randy", "salary": 85000, "departmentId": 2}], "Department": [{"id": 1, "name": "IT"}, {"id": 2, "name": "Sales"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute one maximum per department

The inner query reads `Employee`, groups rows by `departmentId`, and selects
the group key together with `MAX(salary)`. Its conceptual result contains
pairs of the form:

`(department ID, that department's maximum salary)`

`GROUP BY 1` means “group by the first expression in this select list,” which
is `departmentId`. The positional syntax is valid MySQL, though spelling out
`GROUP BY departmentId` would be easier to maintain if the select-list order
later changed.

For the example, department 1 produces `(1, 90000)` and department 2 produces
`(2, 80000)`. There is one pair per department represented in `Employee`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Join employees to their department names

The outer query joins `Employee AS e` to `Department AS d` using
`e.departmentId = d.id`. This converts the numeric foreign key into the human
readable department name required by the output.

An inner join is appropriate. The Reference says `departmentId` refers to the
department table, so every valid employee has a matching department. A
department with no employees contributes no employee row and therefore should
not appear in a result about highest-paid employees.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Max", 90000], ["Sales", "Randy", 85000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1}, {"id": 2, "name": "Max", "salary": 90000, "departmentId": 1}, {"id": 3, "name": "Sam", "salary": 60000, "departmentId": 2}, {"id": 4, "name": "Randy", "salary": 85000, "departmentId": 2}], "Department": [{"id": 1, "name": "IT"}, {"id": 2, "name": "Sales"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Max", 90000], ["Sales", "Randy", 85000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Join to a derived maximum table:** Group `(departmentId, MAX(salary))`, then join employees on both fields; equivalent and often more explicit than tuple `IN`.
- **Correlated maximum subquery:** Compare each salary with its department's maximum; concise, but a naive plan can repeat scans.
- **Window function:** Use `DENSE_RANK()` or `MAX() OVER (PARTITION BY departmentId)` and keep top rows; clear tie handling on engines supporting windows.
- **Pandas transform:** The local editorial joins names, broadcasts each group's maximum with `transform('max')`, and filters equal salaries.
- **Tied maximum:** Return every tied employee, never an arbitrary single row.
- **One employee in a department:** That employee is automatically highest.
- **Department with no employees:** Produce no row because there is no employee to report.
- **Duplicate names:** Keys, not names, determine membership, so identical display names remain distinct employee rows.
- **Positional grouping:** `GROUP BY 1` depends on select order; explicit grouping is safer during maintenance.
- **Any order:** The absence of `ORDER BY` is intentional.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of employee rows and $m$ the number of departments. A
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
