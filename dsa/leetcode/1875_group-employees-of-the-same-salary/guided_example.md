# Guided Example: Group Employees of the Same Salary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"employee_id": 2, "name": "Meir", "salary": 3000}, {"employee_id": 3, "name": "Michael", "salary": 3000}, {"employee_id": 7, "name": "Addilyn", "salary": 7400}, {"employee_id": 8, "name": "Juan", "salary": 6100}, {"employee_id": 9, "name": "Kannon", "salary": 7400}]}}`
- **Required output:** `{"columns": ["employee_id", "name", "salary", "team_id"], "rows": [[2, "Meir", 3000, 1], [3, "Michael", 3000, 1], [7, "Addilyn", 7400, 2], [9, "Kannon", 7400, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["employee_id", "name", "salary", "team_id"], "rows": [[2, "Meir", 3000, 1], [3, "Michael", 3000, 1], [7, "Addilyn", 7400, 2], [9, "Kannon", 7400, 2]]}` from `{"tables": {"Employees": [{"employee_id": 2, "name": "Meir", "salary": 3000}, {"employee_id": 3, "name": "Michael", "salary": 3000}, {"employee_id": 7, "name": "Addilyn", "salary": 7400}, {"employee_id": 8, "name": "Juan", "salary": 6100}, {"employee_id": 9, "name": "Kannon", "salary": 7400}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Separate qualification from ranking.** A salary creates a team only if at least two employees have that salary. Team identifiers then rank only those qualifying salaries; a unique salary must not consume a rank. This ordering of operations is the central challenge. The query first discovers qualifying salaries in common table expression `S`, then assigns their ranks in common table expression `T`, and only afterward joins those team definitions back to employee rows. If ranking happened before unique salaries were removed, gaps or incorrect larger identifiers could appear.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"employee_id": 2, "name": "Meir", "salary": 3000}, {"employee_id": 3, "name": "Michael", "salary": 3000}, {"employee_id": 7, "name": "Addilyn", "salary": 7400}, {"employee_id": 8, "name": "Juan", "salary": 6100}, {"employee_id": 9, "name": "Kannon", "salary": 7400}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Build one row per qualifying salary.** The first CTE is

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Build one row per qualifying salary.** The first CTE is... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`SELECT salary FROM Employees GROUP BY salary HAVING COUNT(1) > 1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "name", "salary", "team_id"], "rows": [[2, "Meir", 3000, 1], [3, "Michael", 3000, 1], [7, "Addilyn", 7400, 2], [9, "Kannon", 7400, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"employee_id": 2, "name": "Meir", "salary": 3000}, {"employee_id": 3, "name": "Michael", "salary": 3000}, {"employee_id": 7, "name": "Addilyn", "salary": 7400}, {"employee_id": 8, "name": "Juan", "salary": 6100}, {"employee_id": 9, "name": "Kannon", "salary": 7400}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "name", "salary", "team_id"], "rows": [[2, "Meir", 3000, 1], [3, "Michael", 3000, 1], [7, "Addilyn", 7400, 2], [9, "Kannon", 7400, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window count followed by dense rank:** A subqu:** - **Window count followed by dense rank:** A subquery can compute `COUNT(*) OVER (PARTITION BY salary)`, filter counts greater than one, and then rank salaries. Care is needed to rank distinct qualifying salaries rather than every employee row; applying `DENSE_RANK` at the wrong level or before filtering unique salaries can assign incorrect IDs.
- **Self-join to detect coworkers:** Joining employees to another employee with the same salary and a different ID can identify team members, but it creates duplicate pairs when a salary has many employees and still requires deduplication and salary ranking. Grouping is cleaner and scales better.
- **Correlated count subquery:** Counting matching salaries separately for every employee expresses eligibility but may repeat work unless the optimizer decorrelates it. The CTE computes each salary count once.
- **Exactly two employees at one salary:** `COUNT(1) > 1` includes the group, both rows join to the same team, and that salary receives one identifier. The strict comparison is equivalent to “at least two.”
- **All salaries unique:** `S` and `T` are empty, the inner join returns no rows, and the result is correctly empty. There is no team ID to assign.
- **Every employee has the same salary:** `S` contains one salary, `ROW_NUMBER` assigns team `1`, and all employees join to it. The final secondary order arranges all members by `employee_id`.
- **A unique salary between two team salaries:** It is excluded before `ROW_NUMBER`, so it creates no gap. For example, qualifying salaries `3000` and `7400` remain teams `1` and `2` even if unique salary `6100` lies between them.
- **Multiple employees and duplicate join output:** `T` has one row per eligible salary because it is built from a grouped relation. Therefore each employee matches at most one team row; the join does not multiply an employee even when their salary group is large.
- **Positional ordering and schema changes:** `ORDER BY 4, 1` depends on `e.*` expanding to exactly the declared three employee columns. Explicit `ORDER BY t.team_id, e.employee_id` would be more maintainable, but the source is exact for the fixed contract.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of employee rows and let $G$ be the number of distinct salaries that qualify as teams, with $G\le R$. Reading and grouping all employees requires $O(R)$ expected time with hash aggregation or $O(R\log R)$ time with sort-based aggregation. Ordering the $G$ qualifying salaries for `ROW_NUMBER` costs up to $O(G\log G)$. Joining `Employees` to `T` can take $O(R+G)$ expected time with a hash join, while the required final ordering of at most $R$ returned employees costs $O(R\log R)$ in the general case. The overall conservative bound is therefore $O(R\log R)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
