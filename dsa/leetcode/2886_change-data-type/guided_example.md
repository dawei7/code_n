# Guided Example: Change Data Type

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"students": [{"student_id": 1, "name": "Ava", "age": 6, "grade": 73.0}, {"student_id": 2, "name": "Kate", "age": 15, "grade": 87.0}]}}`
- **Required output:** `{"columns": ["student_id", "name", "age", "grade"], "rows": [[1, "Ava", 6, 73], [2, "Kate", 15, 87]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to correct the errors:

The objective is to compute `{"columns": ["student_id", "name", "age", "grade"], "rows": [[1, "Ava", 6, 73], [2, "Kate", 15, 87]]}` from `{"tables": {"students": [{"student_id": 1, "name": "Ava", "age": 6, "grade": 73.0}, {"student_id": 2, "name": "Kate", "age": 15, "grade": 87.0}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Values and dtypes are separate parts of a table.** The `grade` column contains values such as `73.0` and `87.0`. Numerically these represent whole-number grades, but pandas stores the Series with a floating-point dtype. The task asks to correct that storage type to integer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"students": [{"student_id": 1, "name": "Ava", "age": 6, "grade": 73.0}, {"student_id": 2, "name": "Kate", "age": 15, "grade": 87.0}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The source selects only that Series and calls:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

`astype` constructs a Series whose values are converted to the requested integer type while retaining the same index labels. The source then assigns that converted Series back to `students['grade']` and returns `students`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "name", "age", "grade"], "rows": [[1, "Ava", 6, 73], [2, "Kate", 15, 87]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"students": [{"student_id": 1, "name": "Ava", "age": 6, "grade": 73.0}, {"student_id": 2, "name": "Kate", "age": 15, "grade": 87.0}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "name", "age", "grade"], "rows": [[1, "Ava", 6, 73], [2, "Kate", 15, 87]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **DataFrame-wide mapping:** `students.astype({'grade': int})` names the same one-column conversion but returns a converted DataFrame that must be captured.
- **Nullable integer dtype:** `astype('Int64')` can represent missing grades, unlike the ordinary `int` requested by this source.
- **`apply(int)` or `map(int)`:** Both can convert element by element but add Python-call overhead for a standard dtype cast.
- **Non-integral floats:** Casting truncates; round explicitly if a different rule is required.
- **Missing grade:** Ordinary `astype(int)` may raise because standard integer arrays cannot hold `NaN`.
- **Empty DataFrame:** The empty grade Series can still be assigned an integer dtype without creating rows.
- **Custom index:** Series alignment preserves which student owns each grade.
- **Input mutation:** Copy `students` first if the floating-point original must remain available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of student rows. Every grade must be read and converted, so time is $O(n)$. The converted Series or replacement numeric array contains $n$ integers and requires $O(n)$ space during conversion and as column storage. These bounds match the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
