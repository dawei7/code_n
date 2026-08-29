# Guided Example: Create a New Column

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"employees": [{"name": "Piper", "salary": 4548}, {"name": "Grace", "salary": 28150}, {"name": "Georgia", "salary": 1103}, {"name": "Willow", "salary": 6593}, {"name": "Finn", "salary": 74576}, {"name": "Thomas", "salary": 24433}]}}`
- **Required output:** `{"columns": ["name", "salary", "bonus"], "rows": [["Piper", 4548, 9096], ["Grace", 28150, 56300], ["Georgia", 1103, 2206], ["Willow", 6593, 13186], ["Finn", 74576, 149152], ["Thomas", 24433, 48866]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A company plans to provide its employees with a bonus.

The objective is to compute `{"columns": ["name", "salary", "bonus"], "rows": [["Piper", 4548, 9096], ["Grace", 28150, 56300], ["Georgia", 1103, 2206], ["Willow", 6593, 13186], ["Finn", 74576, 149152], ["Thomas", 24433, 48866]]}` from `{"tables": {"employees": [{"name": "Piper", "salary": 4548}, {"name": "Grace", "salary": 28150}, {"name": "Georgia", "salary": 1103}, {"name": "Willow", "salary": 6593}, {"name": "Finn", "salary": 74576}, {"name": "Thomas", "salary": 24433}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Operate on the entire salary column as one labeled vector.** A pandas DataFrame column is a Series: a one-dimensional array of values paired with row-index labels. The expression `employees['salary']` selects that Series. Multiplying it by scalar two applies the arithmetic to every salary:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"employees": [{"name": "Piper", "salary": 4548}, {"name": "Grace", "salary": 28150}, {"name": "Georgia", "salary": 1103}, {"name": "Willow", "salary": 6593}, {"name": "Finn", "salary": 74576}, {"name": "Thomas", "salary": 24433}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

The result is another Series with the same index labels and one doubled value per employee.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Assignment creates the new column.** The left side `employees['bonus']` names a column. Since `bonus` is not already present in the stated schema, assigning the doubled Series creates it. pandas aligns the right-hand Series to the DataFrame's index labels before storing values, so every bonus remains attached to the employee whose salary generated it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "salary", "bonus"], "rows": [["Piper", 4548, 9096], ["Grace", 28150, 56300], ["Georgia", 1103, 2206], ["Willow", 6593, 13186], ["Finn", 74576, 149152], ["Thomas", 24433, 48866]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"employees": [{"name": "Piper", "salary": 4548}, {"name": "Grace", "salary": 28150}, {"name": "Georgia", "salary": 1103}, {"name": "Willow", "salary": 6593}, {"name": "Finn", "salary": 74576}, {"name": "Thomas", "salary": 24433}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "salary", "bonus"], "rows": [["Piper", 4548, 9096], ["Grace", 28150, 56300], ["Georgia", 1103, 2206], ["Willow", 6593, 13186], ["Finn", 74576, 149152], ["Thomas", 24433, 48866]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`assign` method:** `employees.assign(bonus=employees['salary'] * 2)` returns a transformed DataFrame and is convenient in method chains, but the exact source deliberately mutates `employees`.
- **Row-wise `apply`:** Applying a lambda per value is more flexible but adds Python-level overhead for simple scalar multiplication.
- **Manual loop:** It is verbose, slower in pandas, and risks confusing positional and label indexes.
- **Empty DataFrame:** Assignment creates an empty `bonus` column with no rows, preserving the requested schema.
- **Custom row index:** Series alignment keeps doubled values attached to the correct labels.
- **Existing `bonus` column:** It would be overwritten, not duplicated.
- **Missing salary:** Standard numeric multiplication propagates missingness; this problem does not request filling it.
- **Input mutation:** Callers needing the original unchanged should copy first, because this source modifies the provided object.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of employees. The vectorized multiplication processes $n$ salary values and assignment stores $n$ bonus values, so time is $O(n)$. The result Series and new DataFrame column require $O(n)$ additional storage. The manifest's $O(n)$ time and $O(n)$ space accurately describe the exact implementation.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
