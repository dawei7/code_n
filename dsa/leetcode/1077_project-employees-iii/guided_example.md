# Guided Example: Project Employees III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 3}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}`
- **Required output:** `{"columns": ["project_id", "employee_id"], "rows": [[1, 1], [1, 3], [2, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Project`

The objective is to compute `{"columns": ["project_id", "employee_id"], "rows": [[1, 1], [1, 3], [2, 1]]}` from `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 3}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Combine project membership with experience

`Project` identifies which employees belong to each project. `Employee` supplies `experience_years`. The ranking decision needs both facts, so the CTE joins them:



`Project.employee_id` is a foreign key and `Employee.employee_id` is a primary key. Every assignment therefore matches exactly one employee record. The join neither drops valid assignments nor duplicates them.

`USING (employee_id)` is an equality join on the same-named column and exposes one merged employee identifier.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 3}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create a ranked intermediate relation

The CTE is named `T`:



The wildcard carries the joined columns, including `project_id`, `employee_id`, and `experience_years`. The query also adds a computed rank `rk`.

Although the final answer needs only two identifiers, experience must remain available long enough to establish which employees are maximal.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The CTE is named `T`:



The wildcard carries the joined col... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Restart ranking independently for every project

The window definition contains:



Partitioning divides joined rows into independent project groups for the window calculation. Rank values restart at one for every project.

This matters when one employee works on several projects. That employee is evaluated against different colleagues in each partition and may be a winner in one project but not another.

Without `PARTITION BY`, the query would rank employees globally and fail to return the most experienced employee of projects whose members are below the global maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["project_id", "employee_id"], "rows": [[1, 1], [1, 3], [2, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 3}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["project_id", "employee_id"], "rows": [[1, 1], [1, 3], [2, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Group maximum plus join:** Compute maximum exp:** - **Group maximum plus join:** Compute maximum experience per project and join it back on both `project_id` and `experience_years`. This also preserves every tie.
- **Correlated maximum:** Keep an assignment when its employee experience equals a project-local scalar maximum. It is correct but may be harder for readers and optimizers.
- **DENSE_RANK:** Filtering dense rank one is equivalent because ties receive the same first rank.
- **ROW_NUMBER:** It is incorrect for this contract because it discards tied maximum employees.
- **FIRST_VALUE alone:** It identifies the maximum value but still needs a comparison to retain all rows sharing it.
- **One employee on a project:** That row receives rank one and is returned.
- **Several maximum ties:** Every tied row receives rank one and survives.
- **Employee on several projects:** Partitioning ranks that employee independently in each project.
- **Equal names:** Names are irrelevant and never break experience ties.
- **Composite assignment key:** It prevents duplicate project-employee output pairs.
- **Window filter level:** The CTE is necessary so `rk` exists before the outer `WHERE`.
- **Any output order:** No `ORDER BY` is required in the final result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E + R)$. Let `R` be the number of project-assignment rows and `E` the number of employee rows.
- **Auxiliary Space Complexity:** $O(E+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
