# Guided Example: Rename Columns

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"students": [{"id": 1, "first": "Mason", "last": "King", "age": 6}, {"id": 2, "first": "Ava", "last": "Wright", "age": 7}, {"id": 3, "first": "Taylor", "last": "Hall", "age": 16}, {"id": 4, "first": "Georgia", "last": "Thompson", "age": 18}, {"id": 5, "first": "Thomas", "last": "Moore", "age": 10}]}}`
- **Required output:** `{"columns": ["student_id", "first_name", "last_name", "age_in_years"], "rows": [[1, "Mason", "King", 6], [2, "Ava", "Wright", 7], [3, "Taylor", "Hall", 16], [4, "Georgia", "Thompson", 18], [5, "Thomas", "Moore", 10]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to rename the columns as follows:

The objective is to compute `{"columns": ["student_id", "first_name", "last_name", "age_in_years"], "rows": [[1, "Mason", "King", 6], [2, "Ava", "Wright", 7], [3, "Taylor", "Hall", 16], [4, "Georgia", "Thompson", 18], [5, "Thomas", "Moore", 10]]}` from `{"tables": {"students": [{"id": 1, "first": "Mason", "last": "King", "age": 6}, {"id": 2, "first": "Ava", "last": "Wright", "age": 7}, {"id": 3, "first": "Taylor", "last": "Hall", "age": 16}, {"id": 4, "first": "Georgia", "last": "Thompson", "age": 18}, {"id": 5, "first": "Thomas", "last": "Moore", "age": 10}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Column labels are metadata, not cell values.** The task leaves every student record unchanged. Only four names at the top of the table must change. pandas' `rename` method accepts a mapping from each old label to its replacement, which is exactly the structure this task provides.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"students": [{"id": 1, "first": "Mason", "last": "King", "age": 6}, {"id": 2, "first": "Ava", "last": "Wright", "age": 7}, {"id": 3, "first": "Taylor", "last": "Hall", "age": 16}, {"id": 4, "first": "Georgia", "last": "Thompson", "age": 18}, {"id": 5, "first": "Thomas", "last": "Moore", "age": 10}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

`{'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'}`

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `{'id': 'student_id', 'first': 'first_name', 'last': 'last_n... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

to the `columns` parameter. Keys are labels pandas should look for on the column axis; values are the labels that should replace them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "first_name", "last_name", "age_in_years"], "rows": [[1, "Mason", "King", 6], [2, "Ava", "Wright", 7], [3, "Taylor", "Hall", 16], [4, "Georgia", "Thompson", 18], [5, "Thomas", "Moore", 10]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"students": [{"id": 1, "first": "Mason", "last": "King", "age": 6}, {"id": 2, "first": "Ava", "last": "Wright", "age": 7}, {"id": 3, "first": "Taylor", "last": "Hall", "age": 16}, {"id": 4, "first": "Georgia", "last": "Thompson", "age": 18}, {"id": 5, "first": "Thomas", "last": "Moore", "age": 10}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "first_name", "last_name", "age_in_years"], "rows": [[1, "Mason", "King", 6], [2, "Ava", "Wright", 7], [3, "Taylor", "Hall", 16], [4, "Georgia", "Thompson", 18], [5, "Thomas", "Moore", 10]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Non-in-place `rename`:** Return `students.rena:** - **Non-in-place `rename`:** Return `students.rename(columns=mapping)` to avoid changing the caller's DataFrame.
- **Assign `students.columns` directly:** Supplying all four new labels can work, but it depends entirely on positional order and is less explicit about old-to-new correspondence.
- **Rename cell contents:** `replace` on a Series would alter data, not headers, and would solve a different problem.
- **Extra columns:** Any label not present in the mapping remains unchanged.
- **Missing mapping key:** Default pandas behavior ignores it; `errors='raise'` is preferable when validating an uncertain schema.
- **Column order:** `rename` changes names without sorting or rearranging columns.
- **Empty DataFrame:** Even with zero rows, its four column labels are renamed correctly.
- **Input mutation:** Other references to `students` see the new labels because `inplace=true` is used.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(c)$. Let $c$ be the number of columns and $n$ the number of rows. Renaming column labels requires examining or rebuilding column-axis metadata, so the natural bound is $O(c)$ time and $O(c)$ metadata space in the worst case. It does not need $O(n)$ work because row values are untouched.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
