# Guided Example: Nth Highest Salary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}], "Request": [{"N": 2}]}}`
- **Required output:** `{"columns": ["getNthHighestSalary"], "rows": [[200]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["getNthHighestSalary"], "rows": [[200]]}` from `{"tables": {"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}], "Request": [{"N": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn a one-based rank into a row offset

The requested rank `N` begins at one: the highest distinct salary has rank one,
the next distinct level has rank two, and so on. MySQL offset positions begin
at zero.

The function therefore executes `SET N = N - 1`. After that assignment, `N`
is the number of distinct salary rows to skip in descending order.

For an original request of two, the stored offset becomes one. Skipping the
single highest distinct salary exposes the second highest.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}], "Request": [{"N": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remove employee-level duplicates before ranking

The inner query selects `DISTINCT salary`. This collapses employees with the
same salary into one rank level.

Without `DISTINCT`, two employees earning the maximum could occupy the first
two ordered rows and cause rank two to return the maximum again. The task ranks
salary values, not employee records.

`ORDER BY salary DESC` then places the largest distinct value first, followed
by the second largest and so forth.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The inner query selects `DISTINCT salary`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Select exactly the requested row

`LIMIT 1 OFFSET N` asks for one row after skipping `N` rows. Since `N` has
already been decremented, this row corresponds to the original one-based rank.

Inside a stored MySQL routine, a local parameter or variable can be used as the
limit offset. The positive-rank contract ensures the decremented value is
nonnegative.

The ordering must occur before the offset is meaningful. Without `ORDER BY`,
row position is unspecified and would not represent salary rank.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["getNthHighestSalary"], "rows": [[200]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"id": 1, "salary": 100}, {"id": 2, "salary": 200}, {"id": 3, "salary": 300}], "Request": [{"N": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["getNthHighestSalary"], "rows": [[200]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`DENSE_RANK`:** Assign descending dense ranks :** - **`DENSE_RANK`:** Assign descending dense ranks and select rank `N`; it directly states the ranking intent.
- **Correlated greater-count:** A salary has rank `N` when exactly `N - 1` distinct salaries are greater, but naive execution is quadratic.
- **Repeated maximum:** `DISTINCT` gives it only rank one.
- **`N = 1`:** Zero offset returns the maximum salary.
- **Too-large `N`:** The scalar subquery returns null.
- **Empty table:** Also returns null.
- **One-based conversion:** Decrement exactly once before applying the offset.
- **Ordering:** Descending order is essential to rank highest first.
- **Nullable salaries:** Define or filter their policy if the schema permits them.
- **MySQL routine syntax:** Porting requires adapting the function declaration and limit-variable form.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the employee count and $u$ the number of distinct salaries. A
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
