# Guided Example: Second Highest Salary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}]}}`
- **Required output:** `{"columns": ["SecondHighestSalary"], "rows": [[200]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["SecondHighestSalary"], "rows": [[200]]}` from `{"tables": {"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rank distinct salary values

The word **distinct** changes the problem. If the highest salary appears for
several employees, those rows still represent only one salary level. The
second output must be the next lower value, not the second employee row after
sorting.

The inner query first selects `DISTINCT salary`, collapsing all equal salary
values into one row. It then orders those values from largest to smallest.

After these two relational operations, row zero is the highest distinct salary
and row one is the second highest.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use MySQL offset-and-count syntax

`LIMIT 1, 1` is MySQL's comma form:

`LIMIT offset, row_count`.

The first one skips one row—the highest salary. The second one requests at most
one row after that skip. It is equivalent to `LIMIT 1 OFFSET 1`.

For salaries 100, 200, and 300, the ordered distinct inner rows are 300, 200,
100. Skipping one and taking one yields 200.

For salaries 300, 300, and 200, `DISTINCT` produces 300 and 200 before the
limit. The result is again 200 rather than another 300.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `LIMIT 1, 1` is MySQL's comma form:

`LIMIT offset, row_coun... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Wrap the result as a scalar subquery

The outer query selects:

`(inner query) AS SecondHighestSalary`.

A scalar subquery used as an expression has special empty-result behavior. If
it returns one row, that row's value becomes the expression. If it returns no
rows, the expression evaluates to SQL `NULL`.

This is how the source meets the “exactly one row” requirement. Writing only
the inner `SELECT DISTINCT ... LIMIT 1,1` would return an empty result table
when fewer than two distinct salaries exist. Wrapping it causes the outer
`SELECT`—which has no `FROM` clause—to emit one row whose expression is null.

The alias gives that one column the exact required name
`SecondHighestSalary`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["SecondHighestSalary"], "rows": [[200]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["SecondHighestSalary"], "rows": [[200]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Maximum below the maximum:** Select `MAX(salar:** - **Maximum below the maximum:** Select `MAX(salary)` where salary is less than the global `MAX(salary)`. This naturally returns one null aggregate row when no candidate exists.
- **`DENSE_RANK`:** Rank distinct salary levels and select rank two; portable across modern SQL engines but may require similar sorting.
- **`IFNULL` wrapper:** Can turn an empty scalar result into null explicitly, though a scalar subquery already does so.
- **Duplicate maximum:** `DISTINCT` prevents it from occupying both rank positions.
- **One distinct salary:** The inner query is empty after offset and the outer row contains null.
- **Empty table:** Produces the same one-row null result.
- **Column alias:** Must be exactly `SecondHighestSalary`.
- **Descending order:** Required before applying the offset.
- **Nullable salary:** A production query should define whether nulls are excluded.
- **Physical cost:** Indexes and optimizer strategy determine whether an explicit sort is needed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Let $n$ be the employee-row count and $u$ the number of distinct salaries.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
