# Guided Example: Find Subsequence of Length K With the Largest Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 3, 3], "k": 2}`
- **Required output:** `[3, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`. You want to find a **subsequence **of `nums` of length `k` that has the **largest** sum.

The objective is to compute `[3, 3]` from `{"nums": [2, 1, 3, 3], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Select positions, not just values

The maximum sum comes from choosing the $k$ largest array values. However, a subsequence must preserve original order. Sorting values alone would lose the positions needed to restore that order.

The source sorts the index range `0..n-1` with key `nums[i]`:

`sorted(range(len(nums)), key=lambda i: nums[i])`.

The final `[-k:]` takes indices belonging to the $k$ largest values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 3, 3], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Restore original order after choosing the elements

The selected indices are sorted numerically. Increasing indices are exactly the order required for a subsequence.

The final comprehension returns `nums[i]` for those ordered positions. It does not sort the selected values, which could produce a sequence not obtainable from the original array.

For `nums = [-1, -2, 3, 4]` and `k = 3`, the chosen values are -1, 3, and 4 at indices 0, 2, and 3. Sorting those indices returns `[-1, 3, 4]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why ties are safe

When several equal values compete at the selection boundary, choosing any required number of their indices gives the same sum. Python's sort is stable, but correctness does not rely on a unique tie choice because the problem accepts any maximum-sum subsequence.

After selection, sorting indices always creates a valid order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 3, 3], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort values directly:** This finds the maximum multiset but loses original indices and cannot reliably reconstruct a subsequence.
- **Heap of size `k`:** Tracking the top $k$ value-index pairs can reduce selection time to $O(n\log k)$, followed by index sorting.
- **Quickselect:** It can find a threshold in expected linear time, but ties at the boundary require careful index selection.
- **`k == 1`:** Any index containing a maximum value is valid.
- **`k == n`:** Every index is selected, and sorting indices returns the original array unchanged.
- **All values equal:** Any $k$ indices give the same sum; the chosen stable-sort suffix is valid.
- **Negative values:** The $k$ numerically largest values still maximize the sum, even if all are negative.
- **Duplicate boundary values:** Any subset of tied occurrences is acceptable as long as exactly $k$ total indices are selected.
- **Original order:** The second index sort is essential; value order is not subsequence order.
- **Input preservation:** Sorting indices leaves `nums` unchanged.
- **Required output length:** The final comprehension iterates over exactly the selected $k$ indices, so its result always has length $k$.
- **Stable sorting:** Python stability determines a consistent choice among equal values, but any tied choice has the same sum and is accepted.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let $n$ be the length of `nums`.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
