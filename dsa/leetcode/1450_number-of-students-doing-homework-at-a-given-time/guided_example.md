# Guided Example: Number of Students Doing Homework at a Given Time

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"startTime": [1, 2, 3], "endTime": [3, 2, 7], "queryTime": 4}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integer arrays `startTime` and `endTime` and given an integer `queryTime`.

The objective is to compute `1` from `{"startTime": [1, 2, 3], "endTime": [3, 2, 7], "queryTime": 4}` while avoiding redundant calculations and unnecessary overhead.

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

**Test whether one time belongs to each student's interval.** Student `i` works from `startTime[i]` through `endTime[i]`. The word “through” is important because both endpoints are included. The student is busy at `queryTime` precisely when

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"startTime": [1, 2, 3], "endTime": [3, 2, 7], "queryTime": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`startTime[i] <= queryTime <= endTime[i]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Python supports chained comparisons, so `x <= queryTime <= y` means that `x <= queryTime` and `queryTime <= y` must both hold. It evaluates the interval condition directly without repeating `queryTime`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"startTime": [1, 2, 3], "endTime": [3, 2, 7], "queryTime": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit counter loop:** Iterate over indices or zipped pairs and increment `answer` inside an `if`. It has the same bounds and can be easier to step through in a debugger.
- **List comprehension before sum:** `sum([condition for ...])` returns the same count but allocates `O(n)` temporary Booleans. The generator keeps auxiliary space constant.
- **Count starts and finishes separately:** The number active at a query equals starts at or before it minus finishes strictly before it. This can help with many queries, but sorting or preprocessing is unnecessary for one query.
- **Sweep-line events:** Event sorting is useful for a full activity timeline. It would add `O(n log n)` work for a single point that direct interval tests solve in `O(n)`.
- **Query equals start time:** The left `<=` includes the student.
- **Query equals end time:** The right `<=` includes the student.
- **Start equals end:** The interval contains exactly one time, and the student counts only when the query equals it.
- **Query before every start:** Every left inequality fails, so the answer is zero.
- **Query after every end:** Every right inequality fails, so the answer is zero.
- **All intervals overlap the query:** Every Boolean is true and the result is `n`.
- **Overlapping students:** Intervals do not interfere with one another. Each matching student contributes independently.
- **Unsorted arrays:** Sorting is not required because corresponding indices already identify students and interval containment is order-independent.
- **Equal-length guarantee:** `zip` processes every student. With unequal arrays it would silently ignore unmatched entries, but such input is outside the contract.
- **Boolean arithmetic:** Python defines `true` as one and `false` as zero for summation. In a language without that property, use an explicit conditional increment.
- **Single student:** The sum contains one Boolean and returns either zero or one.
- **Closed interval semantics:** Replacing `<=` with `<` on either side would incorrectly treat an endpoint as inactive.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the common length of `startTime` and `endTime`. `zip` yields `n` pairs, and the generator performs two constant-time integer comparisons for each pair. `sum` performs one constant-time accumulation per result. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
