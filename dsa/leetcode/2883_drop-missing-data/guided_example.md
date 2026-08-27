# Guided Example: Drop Missing Data

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"students": [{"student_id": 32, "name": "Piper", "age": 5}, {"student_id": 217, "name": null, "age": 19}, {"student_id": 779, "name": "Georgia", "age": 20}, {"student_id": 849, "name": "Willow", "age": 14}]}}`
- **Required output:** `{"columns": ["student_id", "name", "age"], "rows": [[32, "Piper", 5], [779, "Georgia", 20], [849, "Willow", 14]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are some rows having missing values in the `name` column.

The objective is to compute `{"columns": ["student_id", "name", "age"], "rows": [[32, "Piper", 5], [779, "Georgia", 20], [849, "Willow", 14]]}` from `{"tables": {"students": [{"student_id": 32, "name": "Piper", "age": 5}, {"student_id": 217, "name": null, "age": 19}, {"student_id": 779, "name": "Georgia", "age": 20}, {"student_id": 849, "name": "Willow", "age": 14}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Only missing names determine row removal.** A student row should be removed when its `name` entry is missing. Missing data in another column is irrelevant to this task. The exact solution creates a Boolean mask from that one Series:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"students": [{"student_id": 32, "name": "Piper", "age": 5}, {"student_id": 217, "name": null, "age": 19}, {"student_id": 779, "name": "Georgia", "age": 20}, {"student_id": 849, "name": "Willow", "age": 14}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

It then uses the mask to filter the entire DataFrame:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | It then uses the mask to filter the entire DataFrame:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "name", "age"], "rows": [[32, "Piper", 5], [779, "Georgia", 20], [849, "Willow", 14]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"students": [{"student_id": 32, "name": "Piper", "age": 5}, {"student_id": 217, "name": null, "age": 19}, {"student_id": 779, "name": "Georgia", "age": 20}, {"student_id": 849, "name": "Willow", "age": 14}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "name", "age"], "rows": [[32, "Piper", 5], [779, "Georgia", 20], [849, "Willow", 14]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`dropna(subset=['name'])`:** This directly exp:** - **`dropna(subset=['name'])`:** This directly expresses row removal based on one column and returns a new DataFrame when `inplace` is omitted.
- **Editorial in-place version:** It changes the supplied object, unlike the protected Boolean-filter source.
- **Missing values in `age`:** They do not cause removal because the predicate examines only `name`.
- **Empty string:** It is not normally considered null and remains in the result.
- **Every name present:** All rows survive, although pandas still builds the mask and result.
- **Every name missing:** The result is an empty DataFrame with the same three columns.
- **Custom index:** Filtering preserves surviving labels and does not reset them.
- **Multiple null representations:** `notnull` handles pandas-recognized `null`, `NaN`, and nullable missing markers consistently.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of students and $h$ the number of retained rows. `notnull` scans the name column and builds a Boolean Series in $O(n)$ time and $O(n)$ space. Applying the mask also examines $n$ decisions and creates an output containing $h$ rows. With a fixed three-column schema, total time is $O(n)$ and worst-case additional or result storage is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
