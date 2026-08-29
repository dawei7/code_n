# Guided Example: Unique Middle Element

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of odd length `n`.

The objective is to compute `true` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Counting the selected value

Python's list method `count(value)` scans the list and returns how many entries compare equal to `value`. The source passes the middle value to that method:



The count always includes the middle position itself, so it is at least one. It equals one precisely when no other index contains the same value.

The final comparison:



directly returns the required boolean:

- `true` when the middle value has total frequency one;
- `false` when it appears at least twice.

The problem asks about the middle **element's value**, not whether the middle index is unique. Every index is naturally unique; the count checks whether the value stored there is duplicated.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the entire array must be considered

A duplicate can occur anywhere, not just adjacent to the middle. For example, in `[7,2,3,4,7]` the middle value three is unique even though another value repeats. In `[3,2,3,4,5]` the middle value three is not unique because an equal occurrence appears at the far left.

Looking only at the middle element's neighbors would miss distant duplicates. `list.count` inspects every position and handles all locations uniformly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A direct invariant view

Conceptually, the scan performed by `count` maintains an occurrence total. After processing the first `i` positions, that total equals the number of those positions whose value matches the selected middle value. Once all `n` positions are processed, it is the value's complete array frequency.

Comparing the complete frequency with one is both necessary and sufficient:

- necessity: if the middle value is unique, only its own position contributes, so the frequency is one;
- sufficiency: if the frequency is one, the known middle occurrence is the only occurrence.

No information about other values is relevant.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build a frequency dictionary:** Counting every distinct value also finds the middle value's frequency in `O(n)` time, but it uses `O(n)` space even though only one value matters.
- **Sort the array:** Sorting destroys the original positional meaning of the middle element unless that value is saved first, and it costs `O(n\log n)` time. It is unnecessary for a frequency question.
- **Check only neighboring positions:** Equal values need not be adjacent, so local comparison cannot establish global uniqueness.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. Computing `len(nums)`, integer-dividing the length, and indexing the list are constant-time operations. `nums.count(...)` scans all `n` elements, so total time complexity is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
