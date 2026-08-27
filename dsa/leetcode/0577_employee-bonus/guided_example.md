# Guided Example: Employee Bonus

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"empId": 1, "name": "Ada", "supervisor": null, "salary": 50000}, {"empId": 2, "name": "Grace", "supervisor": 1, "salary": 50000}, {"empId": 3, "name": "Linus", "supervisor": 1, "salary": 50000}], "Bonus": [{"empId": 1, "bonus": 500}, {"empId": 2, "bonus": 1500}]}}`
- **Required output:** `{"columns": ["name", "bonus"], "rows": [["Ada", 500], ["Linus", null]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["name", "bonus"], "rows": [["Ada", 500], ["Linus", null]]}` from `{"tables": {"Employee": [{"empId": 1, "name": "Ada", "supervisor": null, "salary": 50000}, {"empId": 2, "name": "Grace", "supervisor": 1, "salary": 50000}, {"empId": 3, "name": "Linus", "supervisor": 1, "salary": 50000}], "Bonus": [{"empId": 1, "bonus": 500}, {"empId": 2, "bonus": 1500}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What `USING (empId)` means

Both tables have a column named `empId`. `USING (empId)` is shorthand for joining on equality of those same-named columns, conceptually:



The schema says `Employee.empId` is unique, `Bonus.empId` is unique, and the latter references the former. Therefore, each employee can match at most one bonus row, and every bonus row belongs to a real employee. The left join consequently produces exactly one joined row per employee rather than multiplying an employee into several rows.

The requested output does not include `empId`, `salary`, or `supervisor`. After joining and filtering, `SELECT name, bonus` projects only the two requested columns. The problem permits any result order, so no `ORDER BY` is necessary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"empId": 1, "name": "Ada", "supervisor": null, "salary": 50000}, {"empId": 2, "name": "Grace", "supervisor": 1, "salary": 50000}, {"empId": 3, "name": "Linus", "supervisor": 1, "salary": 50000}], "Bonus": [{"empId": 1, "bonus": 500}, {"empId": 2, "bonus": 1500}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why ordinary comparison is not enough for missing bonuses

SQL uses three-valued logic: conditions can be true, false, or unknown. If `bonus` is `NULL`, the expression `bonus < 1000` is not true; it evaluates to unknown. A `WHERE` clause retains only rows for which its condition is true. Therefore, writing only `WHERE bonus < 1000` would incorrectly remove the employees whose left-joined bonus is missing.

The exact solution handles that with:



`COALESCE` returns its first non-`NULL` argument. For an employee with a bonus row, `bonus` is a number, so `COALESCE(bonus, 0)` returns that number. The condition then keeps it exactly when it is below 1000. For an employee with no bonus row, `bonus` is `NULL`, so `COALESCE` returns zero; zero is below 1000, and the employee is kept.

This single predicate therefore represents the required logical disjunction:



The explicit disjunction is often the clearest version for discussing SQL null behavior. The `COALESCE` form is compact and is equivalent under the intended bonus domain, where an actual bonus value of zero would also correctly qualify as less than 1000.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | SQL uses three-valued logic: conditions can be true, false, ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Following the sample row by row

Dan has a matching bonus row with value 500. The left join attaches 500, `COALESCE` keeps 500, and `500 < 1000` is true, so `(Dan, 500)` is returned.

Thomas has value 2000. `COALESCE` returns 2000, but `2000 < 1000` is false, so his row is removed.

Brad and John have no matching bonus rows. The left join still retains both employee rows and supplies `NULL` as each `bonus`. The predicate temporarily treats each missing value as zero for comparison, so both rows pass. Importantly, `COALESCE` appears only in the `WHERE` condition. The selected column is the original `bonus`, so their output values remain `NULL` rather than being displayed as zero. The query uses zero only to make the filter decision; it does not rewrite the result.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "bonus"], "rows": [["Ada", 500], ["Linus", null]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"empId": 1, "name": "Ada", "supervisor": null, "salary": 50000}, {"empId": 2, "name": "Grace", "supervisor": 1, "salary": 50000}, {"empId": 3, "name": "Linus", "supervisor": 1, "salary": 50000}], "Bonus": [{"empId": 1, "bonus": 500}, {"empId": 2, "bonus": 1500}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "bonus"], "rows": [["Ada", 500], ["Linus", null]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit null predicate:** `WHERE bonus < 1000:** - **Explicit null predicate:** `WHERE bonus < 1000 OR bonus IS NULL` states the two requirements word for word and does not depend on a replacement value. It is generally the clearest alternative.
- **Inner join:** This is incorrect because it removes employees without a `Bonus` row before the filter gets a chance to include them.
- **Right join from `Bonus`:** Driving from the optional table is easy to get wrong. A left join from `Employee` directly expresses that every employee must remain eligible.
- **`NOT EXISTS` plus a joined query:** Separate branches could find low bonuses and employees without bonus rows, then combine them with `UNION ALL`. That is longer and may scan data multiple times.
- **Correlated scalar subquery:** Looking up a bonus separately for every employee can produce the correct relation, but performance may depend heavily on an index and the null filtering becomes less direct.
- **Bonus exactly 1000:** The condition is strictly “less than,” so 1000 does not qualify.
- **Bonus above 1000:** The employee is excluded because the numeric comparison is false.
- **No bonus row:** The left join produces `NULL`; `COALESCE` makes the predicate true while `SELECT bonus` still returns `NULL`.
- **Actual zero bonus:** Zero is a present numeric bonus and is below 1000, so it correctly qualifies just like any other small bonus.
- **Actual `NULL` stored in `Bonus.bonus`:** If the schema allowed it, the query would treat it the same as no bonus row. The problem’s intended data model uses the joined `NULL` to represent absence; the explicit `IS NULL` alternative has the same behavior.
- **Unique join keys:** The uniqueness guarantees prevent duplicate output rows per employee. Without uniqueness in `Bonus.empId`, one employee could appear once per matching bonus record.
- **Employees table empty:** The left side has no rows, so the result is empty, which is consistent.
- **Bonus table empty:** Every employee is preserved with `NULL` bonus and therefore qualifies.
- **Any output order:** Omitting `ORDER BY` is intentional. Adding one would do unnecessary work unless a consumer imposed an ordering requirement.
- **Preserving display semantics:** Applying `COALESCE` in `SELECT` would display missing bonuses as zero, changing the requested result. Its placement only in `WHERE` is significant.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E+B)$. Let $E$ be the number of `Employee` rows and $B$ the number of `Bonus` rows. The logical query must consider the employee rows and match optional bonus rows. With a hash join, building a lookup for one input and probing it with the other takes expected $O(E+B)$ time and $O(E+B)$ worst-case working space, often reducible to the size of the hashed side. With suitable indexes, an optimizer may instead scan employees and perform indexed bonus lookups.
- **Auxiliary Space Complexity:** $O(E + B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
