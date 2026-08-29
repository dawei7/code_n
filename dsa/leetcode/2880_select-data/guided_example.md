# Guided Example: Select Data

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"students": [{"student_id": 101, "name": "Ulysses", "age": 13}, {"student_id": 53, "name": "William", "age": 10}, {"student_id": 128, "name": "Henry", "age": 6}, {"student_id": 3, "name": "Henry", "age": 11}]}}`
- **Required output:** `{"columns": ["name", "age"], "rows": [["Ulysses", 13]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to select the name and age of the student with $\text{student}_{id} = 101$.

The objective is to compute `{"columns": ["name", "age"], "rows": [["Ulysses", 13]]}` from `{"tables": {"students": [{"student_id": 101, "name": "Ulysses", "age": 13}, {"student_id": 53, "name": "William", "age": 10}, {"student_id": 128, "name": "Henry", "age": 6}, {"student_id": 3, "name": "Henry", "age": 11}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**The task has two independent dimensions: rows and columns.** First keep only records whose `student_id` equals `101`. Then keep only `name` and `age` from those records. The exact source expresses those operations as chained DataFrame indexing:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"students": [{"student_id": 101, "name": "Ulysses", "age": 13}, {"student_id": 53, "name": "William", "age": 10}, {"student_id": 128, "name": "Henry", "age": 6}, {"student_id": 3, "name": "Henry", "age": 11}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`students[students['student_id'] == 101][['name', 'age']]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Reading the expression from the inside outward makes it much easier to understand.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "age"], "rows": [["Ulysses", 13]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"students": [{"student_id": 101, "name": "Ulysses", "age": 13}, {"student_id": 53, "name": "William", "age": 10}, {"student_id": 128, "name": "Henry", "age": 6}, {"student_id": 3, "name": "Henry", "age": 11}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "age"], "rows": [["Ulysses", 13]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Single `loc` selection:** Combine mask and columns in `students.loc[mask, ['name', 'age']]`. It is clearer and avoids read-time chained indexing.
- **Query syntax:** `students.query('student_id == 101')[['name', 'age']]` is readable but invokes expression parsing unnecessarily.
- **No matching student:** The result is an empty DataFrame that still has `name` and `age` columns.
- **Multiple matches:** The exact code returns every matching row in original order.
- **Original index:** Filtering preserves source index labels; the task does not request an index reset.
- **Strict equality:** Identifiers other than numeric 101 are excluded; no range or string search is intended.
- **Column order:** The list places `name` before `age`, matching the requested output.
- **Chained assignment warning:** This expression only selects data. Do not generalize it to mutation; use `loc` for assignments.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of rows and $h$ the number of matching rows. Building the Boolean mask takes $O(n)$ time and $O(n)$ space. Filtering reads the mask and creates an intermediate result containing $h$ rows, then projection creates the two-column output. Overall time is $O(n+h)=O(n)$ and auxiliary or result-related space is $O(n+h)=O(n)$ because the mask alone is length $n$.
- **Auxiliary Space Complexity:** $O(n+h)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
