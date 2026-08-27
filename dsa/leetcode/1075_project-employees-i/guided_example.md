# Guided Example: Project Employees I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 1}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}`
- **Required output:** `{"columns": ["project_id", "average_years"], "rows": [[1, 2.0], [2, 2.5]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Project`

The objective is to compute `{"columns": ["project_id", "average_years"], "rows": [[1, 2.0], [2, 2.5]]}` from `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 1}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Join assignments with employee experience

`Project` tells us which employees work on each project, but it does not store their experience. `Employee` stores `experience_years`, but it does not identify project membership.

The shared `employee_id` connects these facts. The query joins:



Bare `JOIN` is an inner join. `USING (employee_id)` matches rows whose employee identifiers are equal.

`Project.employee_id` is a foreign key, so each assignment references an existing employee. `Employee.employee_id` is a primary key, so each assignment matches exactly one employee row. The join therefore enriches every project assignment with one experience value without losing or multiplying assignments.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 1}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group the enriched rows by project

The query selects:



and ends with:



In MySQL, `GROUP BY 1` refers to the first select-list expression, `project_id`. It is equivalent to `GROUP BY project_id`.

Every joined assignment for the same project enters one group. Assignments for different projects remain separate.

The composite primary key `(project_id, employee_id)` guarantees that one employee is not listed twice within the same project. Thus each employee contributes once to that project's average. The same employee may legitimately work on several projects and contributes once to each corresponding group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query selects:



and ends with:



In MySQL, `GROUP BY ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Calculate the arithmetic mean

Inside each project group:



computes the sum of all member employees' experience years divided by the number of those employees.

The schema guarantees `experience_years` is not null. Therefore every joined project member contributes to both the numerator and denominator. There is no difference between employee count and non-null experience count.

For experience values three, two, and one, `AVG` computes:



The result is per employee, not weighted by any other property. The `Project` table has one assignment row per employee-project pair, so ordinary `AVG` has exactly the desired weighting.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["project_id", "average_years"], "rows": [[1, 2.0], [2, 2.5]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 1}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["project_id", "average_years"], "rows": [[1, 2.0], [2, 2.5]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit ON syntax:** `JOIN Employee ON Projec:** - **Explicit ON syntax:** `JOIN Employee ON Project.employee_id = Employee.employee_id` is equivalent and useful when table aliases make ownership clearer.
- **GROUP BY project_id:** Naming the grouping column is equivalent to `GROUP BY 1` and is more robust if select-list order changes.
- **Correlated subquery:** Computing an average separately for every project can repeat work and is less direct than one join and grouping.
- **Pre-aggregate assignments:** There is nothing useful to aggregate before joining because experience values live in `Employee`.
- **One employee on a project:** The average equals that employee's experience, rounded to two digits.
- **Employee on multiple projects:** The join creates one assignment row in each project group, which is correct.
- **Duplicate assignment prevention:** The composite primary key prevents one employee from being counted twice within the same project.
- **Equal experience values:** Every employee still contributes individually; the mean remains that common value.
- **Non-null guarantee:** `AVG` ignores nulls in SQL, but the schema guarantee ensures no project member is silently excluded.
- **Project with no assignment row:** It is absent because `Project` is the assignment relation and drives the query.
- **Rounding:** `ROUND(..., 2)` applies after averaging and gives the requested precision.
- **Any output order:** Omitting `ORDER BY` matches the contract.
- **Positional grouping:** In this MySQL query, one refers to the first selected expression rather than a constant grouping key.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `R` be the number of rows in `Project` and `E` the number of rows in `Employee`.
- **Auxiliary Space Complexity:** $O(E+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
