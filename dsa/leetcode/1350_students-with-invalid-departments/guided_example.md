# Guided Example: Students With Invalid Departments

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Departments": [{"id": 1, "name": "Electrical Engineering"}, {"id": 7, "name": "Computer Engineering"}, {"id": 13, "name": "Bussiness Administration"}], "Students": [{"id": 23, "name": "Alice", "department_id": 1}, {"id": 1, "name": "Bob", "department_id": 7}, {"id": 5, "name": "Jennifer", "department_id": 13}, {"id": 2, "name": "John", "department_id": 14}, {"id": 4, "name": "Jasmine", "department_id": 77}, {"id": 3, "name": "Steve", "department_id": 74}, {"id": 6, "name": "Luis", "department_id": 1}, {"id": 8, "name": "Jonathan", "department_id": 7}, {"id": 7, "name": "Daiana", "department_id": 33}, {"id": 11, "name": "Madelynn", "department_id": 1}]}}`
- **Required output:** `{"columns": ["id", "name"], "rows": [[2, "John"], [7, "Daiana"], [4, "Jasmine"], [3, "Steve"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Departments`

The objective is to compute `{"columns": ["id", "name"], "rows": [[2, "John"], [7, "Daiana"], [4, "Jasmine"], [3, "Steve"]]}` from `{"tables": {"Departments": [{"id": 1, "name": "Electrical Engineering"}, {"id": 7, "name": "Computer Engineering"}, {"id": 13, "name": "Bussiness Administration"}], "Students": [{"id": 23, "name": "Alice", "department_id": 1}, {"id": 1, "name": "Bob", "department_id": 7}, {"id": 5, "name": "Jennifer", "department_id": 13}, {"id": 2, "name": "John", "department_id": 14}, {"id": 4, "name": "Jasmine", "department_id": 77}, {"id": 3, "name": "Steve", "department_id": 74}, {"id": 6, "name": "Luis", "department_id": 1}, {"id": 8, "name": "Jonathan", "department_id": 7}, {"id": 7, "name": "Daiana", "department_id": 33}, {"id": 11, "name": "Madelynn", "department_id": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build the set of current identifiers

The subquery `SELECT id FROM Departments` produces every department identifier that currently exists. Because `id` is a primary key, these values are unique and non-null under ordinary SQL primary-key semantics. Duplicate removal is unnecessary.

For each row of `Students`, `NOT IN` asks whether its recorded `department_id` differs from every value returned by that subquery. A true result means no matching current department exists, so the student is enrolled under an obsolete identifier.

The outer `SELECT id, name` returns the student’s own primary-key identifier and name, not the missing department identifier. These are exactly the two requested output columns.

The result order is unrestricted, so there is no `ORDER BY`. Omitting an unnecessary sort avoids work and still satisfies the contract.

In the example, department identifiers one, seven, and thirteen appear in `Departments`. Students whose values are fourteen, seventy-seven, seventy-four, or thirty-three pass `NOT IN` and are returned. Students referring to one, seven, or thirteen are filtered out.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Departments": [{"id": 1, "name": "Electrical Engineering"}, {"id": 7, "name": "Computer Engineering"}, {"id": 13, "name": "Bussiness Administration"}], "Students": [{"id": 23, "name": "Alice", "department_id": 1}, {"id": 1, "name": "Bob", "department_id": 7}, {"id": 5, "name": "Jennifer", "department_id": 13}, {"id": 2, "name": "John", "department_id": 14}, {"id": 4, "name": "Jasmine", "department_id": 77}, {"id": 3, "name": "Steve", "department_id": 74}, {"id": 6, "name": "Luis", "department_id": 1}, {"id": 8, "name": "Jonathan", "department_id": 7}, {"id": 7, "name": "Daiana", "department_id": 33}, {"id": 11, "name": "Madelynn", "department_id": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every selected row is correct

If a student passes the predicate, its `department_id` is unequal to every current department `id`, so its department no longer exists and the row belongs in the answer. If a student’s department exists, the subquery contains an equal identifier, making `NOT IN` false and excluding that row. Thus the predicate is both necessary and sufficient for non-null department identifiers.

The use of primary keys also means a matching department appears at most once. Multiplicity would not change membership truth, but uniqueness helps the database build or use an efficient lookup structure.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If a student passes the predicate, its `department_id` is un... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: SQL null semantics

`NOT IN` needs care in generalized schemas because SQL uses three-valued logic. If the subquery contained `NULL`, comparisons against that value could make the predicate unknown for otherwise absent identifiers. Here, `Departments.id` is a primary key and therefore cannot be null, so that classic trap does not arise on the right side.

If `Students.department_id` itself is null, `NULL NOT IN (...)` is unknown and the row is not returned. The task describes students as enrolled in a recorded department identifier, so the intended rows use actual identifiers. If a generalized requirement considered a null department invalid, `NOT EXISTS` or an explicit null condition would be safer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "name"], "rows": [[2, "John"], [7, "Daiana"], [4, "Jasmine"], [3, "Steve"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Departments": [{"id": 1, "name": "Electrical Engineering"}, {"id": 7, "name": "Computer Engineering"}, {"id": 13, "name": "Bussiness Administration"}], "Students": [{"id": 23, "name": "Alice", "department_id": 1}, {"id": 1, "name": "Bob", "department_id": 7}, {"id": 5, "name": "Jennifer", "department_id": 13}, {"id": 2, "name": "John", "department_id": 14}, {"id": 4, "name": "Jasmine", "department_id": 77}, {"id": 3, "name": "Steve", "department_id": 74}, {"id": 6, "name": "Luis", "department_id": 1}, {"id": 8, "name": "Jonathan", "department_id": 7}, {"id": 7, "name": "Daiana", "department_id": 33}, {"id": 11, "name": "Madelynn", "department_id": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "name"], "rows": [[2, "John"], [7, "Daiana"], [4, "Jasmine"], [3, "Steve"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`NOT EXISTS`:** A correlated anti-membership t:** - **`NOT EXISTS`:** A correlated anti-membership test using matching IDs is robust to nulls and often optimized into an anti-join.
- **Left anti-join:** Left-join departments on the identifier and keep rows where the joined department ID is null. It makes the missing-match interpretation visually explicit.
- **Application-side filtering:** Loading both tables and comparing identifiers outside SQL duplicates database work and moves unnecessary data.
- **Empty department table:** Every student with a non-null `department_id` passes because the right-hand set is empty.
- **No invalid students:** The predicate rejects every row and the result is an empty table.
- **Repeated student names:** Selection is based on department membership and returns student IDs, so equal names would not merge rows.
- **Non-null primary key:** The right-side `id` cannot contain null, preventing the most dangerous `NOT IN` behavior.
- **Null student department:** The exact query omits it because the predicate becomes unknown. Add explicit handling if null should mean invalid.
- **Any output order:** No sort is required, and consumers must not infer a stable order from the execution plan.
- **Return columns:** The query returns the student’s `id` and `name` only; the obsolete department value is used solely for filtering.
- **No `DISTINCT` needed:** `Students.id` is a primary key, and the subquery is used as a membership set rather than joined multiplicatively. Each qualifying student row can appear only once in the output.
- **Missing foreign-key enforcement:** The very existence of invalid department identifiers means this dataset is not relying on an active foreign-key constraint that rejects them. The query intentionally detects those orphan references.
- **Department renamed but ID retained:** Validity depends only on the identifier. Changing a department’s name does not make its students invalid as long as the same `Departments.id` remains present.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $D$ be the number of department rows and $S$ the number of student rows.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
