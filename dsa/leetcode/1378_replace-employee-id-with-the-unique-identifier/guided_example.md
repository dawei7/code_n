# Guided Example: Replace Employee ID With The Unique Identifier

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"id": 1, "name": "Alice"}, {"id": 7, "name": "Bob"}, {"id": 11, "name": "Meir"}, {"id": 90, "name": "Winston"}, {"id": 3, "name": "Jonathan"}], "EmployeeUNI": [{"id": 3, "unique_id": 1}, {"id": 11, "unique_id": 2}, {"id": 90, "unique_id": 3}]}}`
- **Required output:** `{"columns": ["unique_id", "name"], "rows": [[null, "Alice"], [1, "Jonathan"], [null, "Bob"], [2, "Meir"], [3, "Winston"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["unique_id", "name"], "rows": [[null, "Alice"], [1, "Jonathan"], [null, "Bob"], [2, "Meir"], [3, "Winston"]]}` from `{"tables": {"Employees": [{"id": 1, "name": "Alice"}, {"id": 7, "name": "Bob"}, {"id": 11, "name": "Meir"}, {"id": 90, "name": "Winston"}, {"id": 3, "name": "Jonathan"}], "EmployeeUNI": [{"id": 3, "unique_id": 1}, {"id": 11, "unique_id": 2}, {"id": 90, "unique_id": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose the table that defines which rows must appear

The required output asks for every employee's name, along with that employee's unique identifier when one exists. Therefore `Employees` is the table whose rows must all survive. `EmployeeUNI` is optional lookup information: it can add `unique_id`, but the absence of a matching lookup row must not remove an employee.

That requirement determines the join direction:

`Employees LEFT JOIN EmployeeUNI USING (id)`.

A left join keeps every row from the table on its left. For each employee ID, it searches the right table for matching rows. If a match exists, the joined row contains the matching `unique_id`. If none exists, SQL still emits the employee row and fills columns contributed by `EmployeeUNI` with `NULL`.

An inner join would be wrong because it would keep only employees that already have unique identifiers. Alice and Bob in the example would disappear instead of appearing with null values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"id": 1, "name": "Alice"}, {"id": 7, "name": "Bob"}, {"id": 11, "name": "Meir"}, {"id": 90, "name": "Winston"}, {"id": 3, "name": "Jonathan"}], "EmployeeUNI": [{"id": 3, "unique_id": 1}, {"id": 11, "unique_id": 2}, {"id": 90, "unique_id": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What `USING (id)` means

Both tables contain a column named `id`. The `USING (id)` syntax is a concise equality join: it matches rows for which `Employees.id = EmployeeUNI.id`. It also presents the shared join column as one combined column in a full joined projection, avoiding two separately named `id` columns.

The exact query does not need to return `id`, so its final projection is only:

`SELECT unique_id, name`.

`name` comes from the preserved `Employees` row. `unique_id` comes from the optional matching `EmployeeUNI` row and is automatically null when the match is absent. No `CASE`, `COALESCE`, or literal replacement is necessary: the null-extension behavior of the left join already implements the requirement.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Following the sample row by row

Employee ID 11 finds a matching lookup row `(11, 2)`, so the projection yields unique identifier 2 and name Meir. ID 90 similarly yields 3 and Winston, while ID 3 yields 1 and Jonathan.

Employee IDs 1 and 7 have no right-side match. The left join nevertheless produces one joined row for each, with `EmployeeUNI.unique_id` equal to `NULL`. Projecting the requested columns yields null with Alice and null with Bob.

Rows in `EmployeeUNI` whose ID does not occur in `Employees` would not appear. The query is not being asked to list identifier assignments independently; it is being asked to annotate the employee list.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["unique_id", "name"], "rows": [[null, "Alice"], [1, "Jonathan"], [null, "Bob"], [2, "Meir"], [3, "Winston"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"id": 1, "name": "Alice"}, {"id": 7, "name": "Bob"}, {"id": 11, "name": "Meir"}, {"id": 90, "name": "Winston"}, {"id": 3, "name": "Jonathan"}], "EmployeeUNI": [{"id": 3, "unique_id": 1}, {"id": 11, "unique_id": 2}, {"id": 90, "unique_id": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["unique_id", "name"], "rows": [[null, "Alice"], [1, "Jonathan"], [null, "Bob"], [2, "Meir"], [3, "Winston"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit `ON` clause:** Write `ON Employees.id = EmployeeUNI.id`. It is equivalent and can be clearer when join columns have different names or when qualified names are desired.
- **Inner join:** This incorrectly removes employees without a unique identifier and therefore fails the central null requirement.
- **Correlated scalar subquery:** Select the matching unique ID separately for every employee. It can work with a unique indexed lookup but is often less direct than one left join.
- **Right join with reversed tables:** It can preserve `Employees` if table order is reversed, but left join expresses the output ownership more naturally.
- **Employee without a mapping:** The row remains and `unique_id` is `NULL` automatically.
- **Employee with a mapping:** Equality on `id` attaches the identifier while keeping the employee name.
- **Unused mapping row:** A right-side ID absent from `Employees` is omitted, which is correct because the output is employee-driven.
- **Several mappings for one ID:** The exact join duplicates the employee. Correct one-row behavior requires an actual uniqueness guarantee or an explicit selection rule.
- **Duplicate employee IDs:** `Employees.id` is a primary key, so this case is excluded and each employee source row is unique.
- **Null display:** SQL returns a database `NULL`, not the text string `"null"`.
- **Result order:** No `ORDER BY` is necessary because any order is accepted.
- **Column projection:** Selecting only `unique_id` and `name` prevents the shared internal `id` from leaking into the requested output.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E)$. Let $E$ be the number of `Employees` rows and $U$ the number of `EmployeeUNI` rows. Under a standard hash-join plan, the database builds a lookup structure for the right table in $O(U)$ time, scans the $E$ employee rows in $O(E)$ time, and performs expected constant-time lookups. Total time is $O(E+U)$ and working space is $O(U)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
