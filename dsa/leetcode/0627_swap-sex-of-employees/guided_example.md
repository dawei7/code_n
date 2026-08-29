# Guided Example: Swap Sex of Employees

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Salary": [{"id": 1, "name": "A", "sex": "m", "salary": 2500}, {"id": 2, "name": "B", "sex": "f", "salary": 1500}, {"id": 3, "name": "C", "sex": "m", "salary": 5500}, {"id": 4, "name": "D", "sex": "f", "salary": 500}]}}`
- **Required output:** `{"columns": ["id", "name", "sex", "salary"], "rows": [[1, "A", "f", 2500], [2, "B", "m", 1500], [3, "C", "f", 5500], [4, "D", "m", 500]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Salary`

The objective is to compute `{"columns": ["id", "name", "sex", "salary"], "rows": [[1, "A", "f", 2500], [2, "B", "m", 1500], [3, "C", "f", 5500], [4, "D", "m", 500]]}` from `{"tables": {"Salary": [{"id": 1, "name": "A", "sex": "m", "salary": 2500}, {"id": 2, "name": "B", "sex": "f", "salary": 1500}, {"id": 3, "name": "C", "sex": "m", "salary": 5500}, {"id": 4, "name": "D", "sex": "f", "salary": 500}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**This task changes stored rows rather than returning a derived table.** The required statement must update every employee's `sex` value in place. The exact source uses one `UPDATE Salary` statement and assigns a new expression to the `sex` column. It contains no `SELECT`, temporary table, or separate intermediate update.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Salary": [{"id": 1, "name": "A", "sex": "m", "salary": 2500}, {"id": 2, "name": "B", "sex": "f", "salary": 1500}, {"id": 3, "name": "C", "sex": "m", "salary": 5500}, {"id": 4, "name": "D", "sex": "f", "salary": 500}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The table guarantees that `sex` belongs to the two-value domain `('m', 'f')`. That closed domain makes the swap a simple two-way choice.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Read the `IF` expression as a complete mapping.** MySQL's `IF(condition, value_if_true, value_if_false)` evaluates

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "name", "sex", "salary"], "rows": [[1, "A", "f", 2500], [2, "B", "m", 1500], [3, "C", "f", 5500], [4, "D", "m", 500]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Salary": [{"id": 1, "name": "A", "sex": "m", "salary": 2500}, {"id": 2, "name": "B", "sex": "f", "salary": 1500}, {"id": 3, "name": "C", "sex": "m", "salary": 5500}, {"id": 4, "name": "D", "sex": "f", "salary": 500}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "name", "sex", "salary"], "rows": [[1, "A", "f", 2500], [2, "B", "m", 1500], [3, "C", "f", 5500], [4, "D", "m", 500]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`CASE` expression:** `CASE sex WHEN 'm' THEN 'f' ELSE 'm' END` is the editorial form. It is equally set-based and may read more clearly when branches multiply.
- **Explicit two-value `CASE`:** Handle `'f'` and `'m'` separately and use `ELSE sex`. This safely preserves unexpected or null values in a broader schema.
- **Two update statements:** Updating female and male rows separately violates the contract and can undo the first change if the second statement sees newly written values.
- **Temporary mapping table:** Joining a two-row mapping table is unnecessary and explicitly outside the requested form.
- **Empty table:** The statement affects zero rows and still completes correctly.
- **All rows have the same sex:** Every row independently changes to the opposite value.
- **Valid ENUM domain:** The compact false branch is correct because every non-`'f'` value must be `'m'`.
- **Null value:** Outside the intended domain, it would become `'f'` rather than remain null; use explicit handling if nullability is possible.
- **Other columns:** They are untouched because only `sex` appears on the left side of `SET`.
- **Repeated execution:** Two executions restore the original values, confirming the mapping is a true swap.
- **Missing `WHERE`:** Here it is required behavior, not an accidental full-table update, because every employee must be changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of rows in `Salary`. Every row must be examined and its `sex` value rewritten, so time complexity is $O(R)$. No algorithm can asymptotically avoid touching rows whose stored value must change.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
