# Guided Example: Employees With Missing Information

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"employee_id": 2, "name": "Crew"}, {"employee_id": 4, "name": "Haven"}, {"employee_id": 5, "name": "Kristian"}], "Salaries": [{"employee_id": 5, "salary": 76071}, {"employee_id": 1, "salary": 22517}, {"employee_id": 4, "salary": 63539}]}}`
- **Required output:** `{"columns": ["employee_id"], "rows": [[1], [2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["employee_id"], "rows": [[1], [2]]}` from `{"tables": {"Employees": [{"employee_id": 2, "name": "Crew"}, {"employee_id": 4, "name": "Haven"}, {"employee_id": 5, "name": "Kristian"}], "Salaries": [{"employee_id": 5, "salary": 76071}, {"employee_id": 1, "salary": 22517}, {"employee_id": 4, "salary": 63539}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Missing information is a symmetric difference of IDs

An employee has complete information only when their ID appears in both `Employees` and `Salaries`. Missing information means the ID appears in exactly one table:

- present in `Employees` but absent from `Salaries` means salary is missing;
- present in `Salaries` but absent from `Employees` means name is missing.

The query computes these two directions separately and unions them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"employee_id": 2, "name": "Crew"}, {"employee_id": 4, "name": "Haven"}, {"employee_id": 5, "name": "Kristian"}], "Salaries": [{"employee_id": 5, "salary": 76071}, {"employee_id": 1, "salary": 22517}, {"employee_id": 4, "salary": 63539}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find employees without salaries

The first SELECT starts from `Employees` and keeps rows whose ID is not among IDs returned by `Salaries`:

`employee_id NOT IN (SELECT employee_id FROM Salaries)`.

Every surviving ID has a name row but no salary row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first SELECT starts from `Employees` and keeps rows whos... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find salaries without employees

The second SELECT reverses the tables. It starts from `Salaries` and retains IDs absent from `Employees`. Every survivor has a salary but no name.

`UNION` combines the two result sets and performs duplicate elimination. Logically the sets are disjoint—an ID cannot simultaneously be “only in Employees” and “only in Salaries”—so `UNION ALL` would yield the same values under the schema. `UNION` is still safe and directly expresses a set symmetric difference.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id"], "rows": [[1], [2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"employee_id": 2, "name": "Crew"}, {"employee_id": 4, "name": "Haven"}, {"employee_id": 5, "name": "Kristian"}], "Salaries": [{"employee_id": 5, "salary": 76071}, {"employee_id": 1, "salary": 22517}, {"employee_id": 4, "salary": 63539}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id"], "rows": [[1], [2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two `NOT EXISTS` branches:** They express anti:** - **Two `NOT EXISTS` branches:** They express anti-joins and avoid `NULL` pitfalls associated with `NOT IN`.
- **Full outer join:** Join on employee ID and keep rows where either side is null. MySQL lacks direct full outer join syntax, so it must be simulated.
- **Left join plus right join:** Union two outer-join directions and filter missing sides. It is more verbose but equivalent.
- **ID in both tables:** It fails both anti-membership tests and is correctly omitted.
- **ID only in Employees:** It appears once as missing salary.
- **ID only in Salaries:** It appears once as missing name.
- **Both tables empty:** Both branches are empty and the ordered result is empty.
- **Empty Salaries table:** Every Employees ID is returned by the first branch.
- **Empty Employees table:** Every Salaries ID is returned by the second branch.
- **Duplicate elimination:** Unique IDs and disjoint branch meanings make duplicates impossible, but `UNION` safely enforces set output.
- **Inner join:** It would return complete employees rather than incomplete ones and is therefore unsuitable.
- **One anti-join direction:** It catches only one missing-information category; both are required.
- **Ascending order:** `ORDER BY 1` uses the sole selected column and defaults to ascending.
- **Nullable IDs:** A different schema allowing null identifiers should prefer `NOT EXISTS`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E+S)$. Let $E$ and $S$ be the row counts of `Employees` and `Salaries`.
- **Auxiliary Space Complexity:** $O(E+S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
