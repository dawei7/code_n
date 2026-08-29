# Guided Example: CEO Subordinate Hierarchy

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice", "manager_id": null, "salary": 150000}, {"employee_id": 2, "employee_name": "Bob", "manager_id": 1, "salary": 120000}, {"employee_id": 3, "employee_name": "Charlie", "manager_id": 1, "salary": 110000}, {"employee_id": 4, "employee_name": "David", "manager_id": 2, "salary": 105000}, {"employee_id": 5, "employee_name": "Eve", "manager_id": 2, "salary": 100000}, {"employee_id": 6, "employee_name": "Frank", "manager_id": 3, "salary": 95000}, {"employee_id": 7, "employee_name": "Grace", "manager_id": 3, "salary": 98000}, {"employee_id": 8, "employee_name": "Helen", "manager_id": 5, "salary": 90000}]}}`
- **Required output:** `{"columns": ["subordinate_id", "subordinate_name", "hierarchy_level", "salary_difference"], "rows": [[2, "Bob", 1, -30000], [3, "Charlie", 1, -40000], [4, "David", 2, -45000], [5, "Eve", 2, -50000], [6, "Frank", 2, -55000], [7, "Grace", 2, -52000], [8, "Helen", 3, -60000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["subordinate_id", "subordinate_name", "hierarchy_level", "salary_difference"], "rows": [[2, "Bob", 1, -30000], [3, "Charlie", 1, -40000], [4, "David", 2, -45000], [5, "Eve", 2, -50000], [6, "Frank", 2, -55000], [7, "Grace", 2, -52000], [8, "Helen", 3, -60000]]}` from `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice", "manager_id": null, "salary": 150000}, {"employee_id": 2, "employee_name": "Bob", "manager_id": 1, "salary": 120000}, {"employee_id": 3, "employee_name": "Charlie", "manager_id": 1, "salary": 110000}, {"employee_id": 4, "employee_name": "David", "manager_id": 2, "salary": 105000}, {"employee_id": 5, "employee_name": "Eve", "manager_id": 2, "salary": 100000}, {"employee_id": 6, "employee_name": "Frank", "manager_id": 3, "salary": 95000}, {"employee_id": 7, "employee_name": "Grace", "manager_id": 3, "salary": 98000}, {"employee_id": 8, "employee_name": "Helen", "manager_id": 5, "salary": 90000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

The reporting structure is a hierarchy rooted at the CEO. Direct reports are one edge below the CEO, their reports are two edges below, and so on. An ordinary self-join can find one fixed depth, but the maximum depth is not known in advance. A recursive common table expression is designed for exactly this kind of parent-to-child traversal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice", "manager_id": null, "salary": 150000}, {"employee_id": 2, "employee_name": "Bob", "manager_id": 1, "salary": 120000}, {"employee_id": 3, "employee_name": "Charlie", "manager_id": 1, "salary": 110000}, {"employee_id": 4, "employee_name": "David", "manager_id": 2, "salary": 105000}, {"employee_id": 5, "employee_name": "Eve", "manager_id": 2, "salary": 100000}, {"employee_id": 6, "employee_name": "Frank", "manager_id": 3, "salary": 95000}, {"employee_id": 7, "employee_name": "Grace", "manager_id": 3, "salary": 98000}, {"employee_id": 8, "employee_name": "Helen", "manager_id": 5, "salary": 90000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The first CTE, `T`, represents all employees reached from the root together with their depth. Its non-recursive anchor selects the row whose `manager_id IS NULL`. That row is the CEO according to the table contract. The anchor copies the CEO's identifier, name, manager, and salary, and assigns `hierarchy_level = 0`. Level zero is useful internally even though the CEO must not appear in the final output.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The recursive member joins the rows already in `T`, aliased as `t`, to `Employees`, aliased as `e`, using

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["subordinate_id", "subordinate_name", "hierarchy_level", "salary_difference"], "rows": [[2, "Bob", 1, -30000], [3, "Charlie", 1, -40000], [4, "David", 2, -45000], [5, "Eve", 2, -50000], [6, "Frank", 2, -55000], [7, "Grace", 2, -52000], [8, "Helen", 3, -60000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"employees": [{"employee_id": 1, "employee_name": "Alice", "manager_id": null, "salary": 150000}, {"employee_id": 2, "employee_name": "Bob", "manager_id": 1, "salary": 120000}, {"employee_id": 3, "employee_name": "Charlie", "manager_id": 1, "salary": 110000}, {"employee_id": 4, "employee_name": "David", "manager_id": 2, "salary": 105000}, {"employee_id": 5, "employee_name": "Eve", "manager_id": 2, "salary": 100000}, {"employee_id": 6, "employee_name": "Frank", "manager_id": 3, "salary": 95000}, {"employee_id": 7, "employee_name": "Grace", "manager_id": 3, "salary": 98000}, {"employee_id": 8, "employee_name": "Helen", "manager_id": 5, "salary": 90000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["subordinate_id", "subordinate_name", "hierarchy_level", "salary_difference"], "rows": [[2, "Bob", 1, -30000], [3, "Charlie", 1, -40000], [4, "David", 2, -45000], [5, "Eve", 2, -50000], [6, "Frank", 2, -55000], [7, "Grace", 2, -52000], [8, "Helen", 3, -60000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed self-joins:** Joining `Employees` to itself once finds direct reports, twice finds second-level reports, and so forth. This cannot handle an unknown hierarchy depth without hard-coding a maximum.
- **Application-side traversal:** Fetching rows and running BFS or DFS in application code can compute levels in $O(e)$ after building child lists, but the task asks for a SQL result and the recursive CTE keeps traversal close to the data.
- **Carry CEO salary inside `T`:** The anchor could add a `ceo_salary` column and propagate it unchanged through recursion. That would remove CTE `P` and its cross join while producing the same calculation.
- **Explicit `CROSS JOIN`:** Writing `CROSS JOIN P p` would communicate the intended one-row Cartesian product more clearly than `JOIN P p` without an `ON` clause. The exact MySQL query relies on their equivalent behavior here.
- **Only the CEO exists:** `T` contains the level-zero anchor, the final filter removes it, and the correct result is empty.
- **A deep chain:** Each employee is reached one recursive iteration after their manager, and the level equals their position in the chain. Very deep chains may encounter the database's configured recursive-CTE depth limit.
- **Multiple employees at one level:** `ORDER BY 3, 1` deterministically sorts them by identifier, regardless of the order in which recursive evaluation discovered them.
- **Higher-paid subordinate:** `t.salary - p.salary` becomes positive. A lower salary becomes negative and an equal salary becomes zero; all three signs are meaningful.
- **Multiple null managers:** The query would cross every traversed row with every root salary and duplicate output. Correctness depends on the single-CEO hierarchy promised by the problem.
- **Cycles or multiple-parent data:** A valid `manager_id` hierarchy gives each employee one parent and has no cycle reachable from the CEO. `UNION ALL` performs no cycle elimination, so malformed cyclic input is not protected against.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(e log e)$. Let $e$ be the number of employees reachable in the CEO's hierarchy. The recursive CTE materializes $O(e)$ rows. With an index on `manager_id`, finding each manager's children is efficient; the final ordering of the $e-1$ subordinate rows costs $O(e\log e)$ in the general case. This sorting cost supports the stated overall $O(e\log e)$ bound.
- **Auxiliary Space Complexity:** $O(e)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
