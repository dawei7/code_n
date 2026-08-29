# Guided Example: Modify Columns

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"employees": [{"name": "Jack", "salary": 19666}, {"name": "Piper", "salary": 74754}, {"name": "Mia", "salary": 62509}, {"name": "Ulysses", "salary": 54866}]}}`
- **Required output:** `{"columns": ["name", "salary"], "rows": [["Jack", 39332], ["Piper", 149508], ["Mia", 125018], ["Ulysses", 109732]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A company intends to give its employees a pay rise.

The objective is to compute `{"columns": ["name", "salary"], "rows": [["Jack", 39332], ["Piper", 149508], ["Mia", 125018], ["Ulysses", 109732]]}` from `{"tables": {"employees": [{"name": "Jack", "salary": 19666}, {"name": "Piper", "salary": 74754}, {"name": "Mia", "salary": 62509}, {"name": "Ulysses", "salary": 54866}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Transform the existing column rather than adding a second one.** The requested schema still has only `name` and `salary`. Each salary value must be replaced by twice itself. The source uses pandas' augmented assignment:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"employees": [{"name": "Jack", "salary": 19666}, {"name": "Piper", "salary": 74754}, {"name": "Mia", "salary": 62509}, {"name": "Ulysses", "salary": 54866}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

The left side selects the salary Series, multiplication applies to every numeric entry, and augmented assignment writes the resulting values back under the same `salary` label.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**How to read the statement conceptually.** It is equivalent in result to:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "salary"], "rows": [["Jack", 39332], ["Piper", 149508], ["Mia", 125018], ["Ulysses", 109732]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"employees": [{"name": "Jack", "salary": 19666}, {"name": "Piper", "salary": 74754}, {"name": "Mia", "salary": 62509}, {"name": "Ulysses", "salary": 54866}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "salary"], "rows": [["Jack", 39332], ["Piper", 149508], ["Mia", 125018], ["Ulysses", 109732]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit reassignment:** `employees['salary'] = employees['salary'] * 2` has the same table result and makes the read-compute-write stages visible.
- **`assign` method:** `employees.assign(salary=employees['salary'] * 2)` returns a transformed DataFrame and is useful when input mutation is undesirable.
- **Row-wise `apply`:** It works but introduces unnecessary per-element Python function calls.
- **Empty DataFrame:** The salary column remains present and empty; the operation completes without inventing rows.
- **Custom index:** Labeled Series arithmetic preserves each employee association.
- **Missing salary:** It propagates rather than being replaced, because missing-data handling is outside this task.
- **Overflow:** Very narrow integer dtypes may overflow when doubled; valid challenge data is expected to support the result.
- **Input mutation:** Preserve original salaries with an explicit copy before calling this exact implementation if they are needed later.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of employees. Every salary must be read, multiplied, and stored, so time is $O(n)$. pandas may allocate a temporary or replacement Series or numeric block of length $n$, and the modified column itself contains $n$ values. A conservative auxiliary-space bound is $O(n)$, matching the manifest; some execution paths may reuse storage more aggressively.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
