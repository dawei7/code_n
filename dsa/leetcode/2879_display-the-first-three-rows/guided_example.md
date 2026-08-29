# Guided Example: Display the First Three Rows

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"employees": [{"employee_id": 3, "name": "Bob", "department": "Operations", "salary": 48675}, {"employee_id": 90, "name": "Alice", "department": "Sales", "salary": 11096}, {"employee_id": 9, "name": "Tatiana", "department": "Engineering", "salary": 33805}, {"employee_id": 60, "name": "Annabelle", "department": "InformationTechnology", "salary": 37678}, {"employee_id": 49, "name": "Jonathan", "department": "HumanResources", "salary": 23793}, {"employee_id": 43, "name": "Khaled", "department": "Administration", "salary": 40454}]}}`
- **Required output:** `{"columns": ["employee_id", "name", "department", "salary"], "rows": [[3, "Bob", "Operations", 48675], [90, "Alice", "Sales", 11096], [9, "Tatiana", "Engineering", 33805]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to display the **first `3` **rows** **of this DataFrame.

The objective is to compute `{"columns": ["employee_id", "name", "department", "salary"], "rows": [[3, "Bob", "Operations", 48675], [90, "Alice", "Sales", 11096], [9, "Tatiana", "Engineering", 33805]]}` from `{"tables": {"employees": [{"employee_id": 3, "name": "Bob", "department": "Operations", "salary": 48675}, {"employee_id": 90, "name": "Alice", "department": "Sales", "salary": 11096}, {"employee_id": 9, "name": "Tatiana", "department": "Engineering", "salary": 33805}, {"employee_id": 60, "name": "Annabelle", "department": "InformationTechnology", "salary": 37678}, {"employee_id": 49, "name": "Jonathan", "department": "HumanResources", "salary": 23793}, {"employee_id": 43, "name": "Khaled", "department": "Administration", "salary": 40454}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**“First” means current row order.** The task does not ask for the three smallest employee identifiers or any other sorted subset. It asks for the first three rows as the DataFrame is presently ordered. pandas provides `DataFrame.head(n)` specifically for this prefix-selection operation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"employees": [{"employee_id": 3, "name": "Bob", "department": "Operations", "salary": 48675}, {"employee_id": 90, "name": "Alice", "department": "Sales", "salary": 11096}, {"employee_id": 9, "name": "Tatiana", "department": "Engineering", "salary": 33805}, {"employee_id": 60, "name": "Annabelle", "department": "InformationTechnology", "salary": 37678}, {"employee_id": 49, "name": "Jonathan", "department": "HumanResources", "salary": 23793}, {"employee_id": 43, "name": "Khaled", "department": "Administration", "salary": 40454}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution is `employees.head(3)`. Argument three says that at most row positions zero, one, and two in the current ordering should be returned. No explicit sorting, filtering condition, or loop is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**What `head` preserves.** The returned object remains a DataFrame. It keeps every input column in the same order, including `employee_id`, `name`, `department`, and `salary`. It also preserves the selected rows' original index labels. If the input index happened to be `[10, 20, 30, ...]`, the result's index would remain `[10, 20, 30]` rather than being automatically reset to zero through two.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "name", "department", "salary"], "rows": [[3, "Bob", "Operations", 48675], [90, "Alice", "Sales", 11096], [9, "Tatiana", "Engineering", 33805]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"employees": [{"employee_id": 3, "name": "Bob", "department": "Operations", "salary": 48675}, {"employee_id": 90, "name": "Alice", "department": "Sales", "salary": 11096}, {"employee_id": 9, "name": "Tatiana", "department": "Engineering", "salary": 33805}, {"employee_id": 60, "name": "Annabelle", "department": "InformationTechnology", "salary": 37678}, {"employee_id": 49, "name": "Jonathan", "department": "HumanResources", "salary": 23793}, {"employee_id": 43, "name": "Khaled", "department": "Administration", "salary": 40454}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "name", "department", "salary"], "rows": [[3, "Bob", "Operations", 48675], [90, "Alice", "Sales", 11096], [9, "Tatiana", "Engineering", 33805]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`iloc[:3]`:** This is also positional and correct, but `head(3)` communicates “first rows” more directly.
- **`employees[:3]`:** It often works as row slicing, yet explicit `head` avoids indexing-semantics ambiguity.
- **Sorting by identifier first:** That would change the meaning of “first” and produce the wrong output when input order differs from identifier order.
- **Fewer than three rows:** `head(3)` returns every available row without error.
- **Empty DataFrame:** It returns an empty DataFrame with the original column schema.
- **Custom index labels:** Labels are preserved; the method selects by position and does not reset the index.
- **Duplicate index labels:** They do not affect positional prefix selection.
- **All columns retained:** The task asks to display rows, not project a subset of columns, so no column selection should be added.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Relative to the number $r$ of input rows, selecting a fixed three-row prefix is $O(1)$. The result contains at most three rows. With the contract's fixed four columns, its size is also constant, so additional result space is $O(1)$ with respect to $r$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
