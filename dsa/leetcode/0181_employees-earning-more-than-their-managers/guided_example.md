# Guided Example: Employees Earning More Than Their Managers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"id": 1, "name": "Owner", "salary": 100, "managerId": null}]}}`
- **Required output:** `{"columns": ["Employee"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["Employee"], "rows": []}` from `{"tables": {"Employee": [{"id": 1, "name": "Owner", "salary": 100, "managerId": null}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Give the employee table two roles

Each row contains both an employee's data and the ID of another row representing
that employee's manager. To compare their salaries, the query joins `Employee`
to itself.

Alias `e1` is the employee being evaluated. Alias `e2` is that employee's
manager. The aliases are necessary because otherwise references such as
`salary` and `id` would be ambiguous between the two uses of the same table.

The join condition:

`e1.managerId = e2.id`

connects each employee row to the unique manager row named by its foreign-key
value. `e2.id` is a primary key, so at most one manager row matches.

No assumption is made that a manager's row appears before or after a
subordinate's row. Relational matching uses identifier equality, so physical
table order is irrelevant.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"id": 1, "name": "Owner", "salary": 100, "managerId": null}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an inner join is appropriate

Employees with no manager have `managerId = NULL`. SQL equality with null is
not true, so those rows do not match `e2`.

That exclusion is correct. A top-level employee without a manager cannot
satisfy “earns more than their manager,” because there is no manager salary to
compare.

If a non-null `managerId` referred to no existing row, an inner join would
exclude it for the same reason. The expected relational data normally maintains
the reference, but the query remains semantically sensible.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Employees with no manager have `managerId = NULL`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply the salary comparison after matching

The `WHERE` clause keeps a joined employee-manager pair only when:

`e1.salary > e2.salary`.

The operator is strictly greater. Equal salaries do not qualify, and a lower
employee salary does not qualify.

Matching first is important conceptually. Comparing an employee with every
other employee would create unrelated salary pairs; the ID join restricts the
comparison to the one designated manager.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["Employee"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"id": 1, "name": "Owner", "salary": 100, "managerId": null}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["Employee"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated scalar subquery:** Fetch the manage:** - **Correlated scalar subquery:** Fetch the manager salary for each employee and compare it; clear but may repeat lookup work.
- **Left join:** A later manager-salary predicate removes null matches, making it effectively inner; direct inner join better states intent.
- **Cartesian product plus `WHERE`:** Logically equivalent when both join and salary predicates are present, but explicit join syntax is clearer.
- **No manager:** The employee is excluded.
- **Equal salary:** Strict `>` correctly excludes it.
- **Several employees with one manager:** Each qualifying employee produces its own row.
- **Duplicate employee names:** They can legitimately appear multiple times because IDs identify employees.
- **Broken manager reference:** Inner join produces no output for that row.
- **Null salary:** The comparison is unknown and does not qualify.
- **Any order:** No sorting clause is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of employees. With the primary-key index on `e2.id`, an
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
