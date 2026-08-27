# Guided Example: Analyze Organization Hierarchy

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice", "manager_id": null, "salary": 12000, "department": "Executive"}, {"employee_id": 2, "employee_name": "Bob", "manager_id": 1, "salary": 10000, "department": "Sales"}, {"employee_id": 3, "employee_name": "Charlie", "manager_id": 1, "salary": 10000, "department": "Engineering"}, {"employee_id": 4, "employee_name": "David", "manager_id": 2, "salary": 7500, "department": "Sales"}, {"employee_id": 5, "employee_name": "Eva", "manager_id": 2, "salary": 7500, "department": "Sales"}, {"employee_id": 6, "employee_name": "Frank", "manager_id": 3, "salary": 9000, "department": "Engineering"}, {"employee_id": 7, "employee_name": "Grace", "manager_id": 3, "salary": 8500, "department": "Engineering"}, {"employee_id": 8, "employee_name": "Hank", "manager_id": 4, "salary": 6000, "department": "Sales"}, {"employee_id": 9, "employee_name": "Ivy", "manager_id": 6, "salary": 7000, "department": "Engineering"}, {"employee_id": 10, "employee_name": "Judy", "manager_id": 6, "salary": 7000, "department": "Engineering"}]}}`
- **Required output:** `{"columns": ["employee_id", "employee_name", "level", "team_size", "budget"], "rows": [[1, "Alice", 1, 9, 84500], [3, "Charlie", 2, 4, 41500], [2, "Bob", 2, 3, 31000], [6, "Frank", 3, 2, 23000], [4, "David", 3, 1, 13500], [7, "Grace", 3, 0, 8500], [5, "Eva", 3, 0, 7500], [9, "Ivy", 4, 0, 7000], [10, "Judy", 4, 0, 7000], [8, "Hank", 4, 0, 6000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["employee_id", "employee_name", "level", "team_size", "budget"], "rows": [[1, "Alice", 1, 9, 84500], [3, "Charlie", 2, 4, 41500], [2, "Bob", 2, 3, 31000], [6, "Frank", 3, 2, 23000], [4, "David", 3, 1, 13500], [7, "Grace", 3, 0, 8500], [5, "Eva", 3, 0, 7500], [9, "Ivy", 4, 0, 7000], [10, "Judy", 4, 0, 7000], [8, "Hank", 4, 0, 6000]]}` from `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice", "manager_id": null, "salary": 12000, "department": "Executive"}, {"employee_id": 2, "employee_name": "Bob", "manager_id": 1, "salary": 10000, "department": "Sales"}, {"employee_id": 3, "employee_name": "Charlie", "manager_id": 1, "salary": 10000, "department": "Engineering"}, {"employee_id": 4, "employee_name": "David", "manager_id": 2, "salary": 7500, "department": "Sales"}, {"employee_id": 5, "employee_name": "Eva", "manager_id": 2, "salary": 7500, "department": "Sales"}, {"employee_id": 6, "employee_name": "Frank", "manager_id": 3, "salary": 9000, "department": "Engineering"}, {"employee_id": 7, "employee_name": "Grace", "manager_id": 3, "salary": 8500, "department": "Engineering"}, {"employee_id": 8, "employee_name": "Hank", "manager_id": 4, "salary": 6000, "department": "Sales"}, {"employee_id": 9, "employee_name": "Ivy", "manager_id": 6, "salary": 7000, "department": "Engineering"}, {"employee_id": 10, "employee_name": "Judy", "manager_id": 6, "salary": 7000, "department": "Engineering"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Use one recursive CTE to walk upward from every employee.** The CTE named `level_cte` begins with one anchor row per employee:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice", "manager_id": null, "salary": 12000, "department": "Executive"}, {"employee_id": 2, "employee_name": "Bob", "manager_id": 1, "salary": 10000, "department": "Sales"}, {"employee_id": 3, "employee_name": "Charlie", "manager_id": 1, "salary": 10000, "department": "Engineering"}, {"employee_id": 4, "employee_name": "David", "manager_id": 2, "salary": 7500, "department": "Sales"}, {"employee_id": 5, "employee_name": "Eva", "manager_id": 2, "salary": 7500, "department": "Sales"}, {"employee_id": 6, "employee_name": "Frank", "manager_id": 3, "salary": 9000, "department": "Engineering"}, {"employee_id": 7, "employee_name": "Grace", "manager_id": 3, "salary": 8500, "department": "Engineering"}, {"employee_id": 8, "employee_name": "Hank", "manager_id": 4, "salary": 6000, "department": "Sales"}, {"employee_id": 9, "employee_name": "Ivy", "manager_id": 6, "salary": 7000, "department": "Engineering"}, {"employee_id": 10, "employee_name": "Judy", "manager_id": 6, "salary": 7000, "department": "Engineering"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`employee_id, manager_id, level = 1, salary`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `employee_id, manager_id, level = 1, salary`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Its recursive term joins the current row's `manager_id` to that manager's employee record. It keeps the original `a.employee_id` and salary, replaces `manager_id` with the manager's own manager, and increments `level`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "employee_name", "level", "team_size", "budget"], "rows": [[1, "Alice", 1, 9, 84500], [3, "Charlie", 2, 4, 41500], [2, "Bob", 2, 3, 31000], [6, "Frank", 3, 2, 23000], [4, "David", 3, 1, 13500], [7, "Grace", 3, 0, 8500], [5, "Eva", 3, 0, 7500], [9, "Ivy", 4, 0, 7000], [10, "Judy", 4, 0, 7000], [8, "Hank", 4, 0, 6000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice", "manager_id": null, "salary": 12000, "department": "Executive"}, {"employee_id": 2, "employee_name": "Bob", "manager_id": 1, "salary": 10000, "department": "Sales"}, {"employee_id": 3, "employee_name": "Charlie", "manager_id": 1, "salary": 10000, "department": "Engineering"}, {"employee_id": 4, "employee_name": "David", "manager_id": 2, "salary": 7500, "department": "Sales"}, {"employee_id": 5, "employee_name": "Eva", "manager_id": 2, "salary": 7500, "department": "Sales"}, {"employee_id": 6, "employee_name": "Frank", "manager_id": 3, "salary": 9000, "department": "Engineering"}, {"employee_id": 7, "employee_name": "Grace", "manager_id": 3, "salary": 8500, "department": "Engineering"}, {"employee_id": 8, "employee_name": "Hank", "manager_id": 4, "salary": 6000, "department": "Sales"}, {"employee_id": 9, "employee_name": "Ivy", "manager_id": 6, "salary": 7000, "department": "Engineering"}, {"employee_id": 10, "employee_name": "Judy", "manager_id": 6, "salary": 7000, "department": "Engineering"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "employee_name", "level", "team_size", "budget"], "rows": [[1, "Alice", 1, 9, 84500], [3, "Charlie", 2, 4, 41500], [2, "Bob", 2, 3, 31000], [6, "Frank", 3, 2, 23000], [4, "David", 3, 1, 13500], [7, "Grace", 3, 0, 8500], [5, "Eva", 3, 0, 7500], [9, "Ivy", 4, 0, 7000], [10, "Judy", 4, 0, 7000], [8, "Hank", 4, 0, 6000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recursive traversal once per manager:** It rep:** - **Recursive traversal once per manager:** It repeats subtree work and can be far more expensive than sharing one ancestor closure.
- **Start only from the CEO and traverse downward:** This also computes levels, but additional path information is needed to aggregate every manager's complete subtree.
- **Count only direct reports:** Grouping the base table by `manager_id` misses indirect descendants; recursive CTE rows supply all ancestor relationships.
- **Include the manager in `COUNT(*)`:** Team size excludes the manager, and the closure naturally counts descendants only.
- **Forget to add own salary:** The grouped sum contains reports' salaries, so `a.salary` is required for the full controlled budget.
- **Leaf employee:** The left join and `COALESCE` produce team size zero and budget equal to own salary.
- **CEO:** Their terminal level is one, and every other employee contributes to their descendant aggregate.
- **Several employees with equal level and budget:** `employee_name` ascending resolves the remaining order.
- **Duplicate employee names:** The requested keys may still tie completely; `employee_id` is not specified as a final ordering key.
- **Missing manager row:** The upward join would stop before a null terminal row and the employee could disappear from `employee_with_level`; the hierarchy model assumes valid manager references.
- **Management cycle:** Recursive expansion would not reach null; the organizational-tree contract implicitly excludes cycles.
- **Long chain:** The closure becomes quadratic in employee count, which is why complexity is expressed in terms of $a$ rather than only $n$.
- **Comma join syntax:** The `WHERE a.employee_id = b.employee_id` condition makes it an inner join despite the older notation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a+n\log n)$. Let $n$ be the number of employees and let $a$ be the total number of employee-to-ancestor relationships materialized by the recursive CTE, including the upward chain rows. A shallow organization has $a=O(n)$, while a chain-shaped hierarchy can have $a=O(n^2)$.
- **Auxiliary Space Complexity:** $O(a + n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
