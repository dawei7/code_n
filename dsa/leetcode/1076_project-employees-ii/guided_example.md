# Guided Example: Project Employees II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 1}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}`
- **Required output:** `{"columns": ["project_id"], "rows": [[1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Project`

The objective is to compute `{"columns": ["project_id"], "rows": [[1]]}` from `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 1}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count assignments per project

Every row in `Project` represents one employee assigned to one project. The composite primary key `(project_id, employee_id)` guarantees that the same employee cannot appear twice for the same project.

Therefore, counting rows in a project group is exactly the same as counting distinct assigned employees. No join to `Employee` is needed because employee names and experience do not affect the requested count.

The outer query starts:



`GROUP BY 1` refers to the first select expression, `project_id`. It creates one group for every represented project.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 1}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Measure the size of each outer group

The filter uses:



`COUNT(1)` counts rows in the current group. The literal one is non-null for every row, so every assignment contributes exactly one.

`HAVING` is required rather than `WHERE` because the condition depends on an aggregate computed after grouping. `WHERE` filters individual rows before grouping and cannot directly compare a project's completed count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build the collection of all project counts

The subquery is:



It independently groups the same assignment table and returns one count for each project. For projects with three, two, and three employees, this subquery produces the values three, two, and three.

The actual project identifiers are unnecessary inside this subquery. The outer query needs only the collection of counts to decide whether its current group reaches the global maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["project_id"], "rows": [[1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Project": [{"project_id": 1, "employee_id": 1}, {"project_id": 1, "employee_id": 2}, {"project_id": 1, "employee_id": 3}, {"project_id": 2, "employee_id": 1}, {"project_id": 2, "employee_id": 4}], "Employee": [{"employee_id": 1, "name": "Khaled", "experience_years": 3}, {"employee_id": 2, "name": "Ali", "experience_years": 2}, {"employee_id": 3, "name": "John", "experience_years": 1}, {"employee_id": 4, "name": "Doe", "experience_years": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["project_id"], "rows": [[1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Maximum subquery:** Group project counts in a derived table, compute `MAX(employee_count)`, and keep groups equal to it. This is explicit but more verbose.
- **ORDER BY with dense rank:** Rank projects by `COUNT(*)` descending and select rank one. `DENSE_RANK` or `RANK` preserves ties; `ROW_NUMBER` does not.
- **CTE for counts:** Compute one row per project once, then compare each count with the maximum from that CTE. This can improve readability and encourage reuse.
- **GROUP BY project_id:** Naming the column is equivalent to `GROUP BY 1` and safer if the select-list order changes.
- **COUNT employee_id:** Because the primary-key component is non-null, `COUNT(employee_id)` and `COUNT(1)` produce the same group sizes.
- **COUNT DISTINCT:** It is unnecessary because the composite primary key already prevents duplicate employees within a project.
- **Single project:** Its count is automatically at least all counts, so it is returned.
- **All projects tied:** Every group satisfies the condition and all project identifiers are returned.
- **One unique maximum:** Only that project passes.
- **Employee on multiple projects:** Each assignment belongs to its own project group and correctly counts once in each.
- **Employee table:** It is not needed for counting valid assignment rows.
- **Any output order:** Omitting `ORDER BY` is correct.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `R` be the number of rows in `Project` and `G` the number of distinct projects.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
