# Guided Example: Remove Duplicates from Sorted Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 2]}`
- **Required output:** `{"return_value": 2, "prefix": [1, 2]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**in-place**</a> such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

The objective is to compute `{"return_value": 2, "prefix": [1, 2]}` from `{"nums": [1, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use sorted order to recognize a new distinct value immediately

Because `nums` is sorted in non-decreasing order, all copies of the same value form one contiguous run. While scanning from left to right, a value is new exactly when it differs from the most recently retained distinct value. No set is needed: the compacted prefix itself remembers that last value.

The task does not require shrinking the Python list. It requires returning a length `k` and placing the distinct values in `nums[:k]`. Everything at index `k` or later is outside the judged answer and may contain stale data.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Give `k` two related meanings

The source initializes `k = 0`. Throughout the loop:

- `k` is the number of unique values already written; and
- `k` is the index where the next new value must be written.

Those meanings agree because a prefix with `k` elements occupies indices `0` through `k - 1`, making index `k` the next free position.

The central invariant is:

> Before processing the next scanned value `x`, `nums[:k]` contains every distinct value from the already scanned input prefix exactly once, in original sorted order.

The invariant holds initially because both the scanned prefix and `nums[:0]` are empty.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source initializes `k = 0`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle the first value without an invalid index

The acceptance condition is



When no value has been retained, `k - 1` would be `-1`, which in Python refers to the array's last element rather than representing “no previous value.” The explicit `k == 0` condition ensures that the first scanned value is always kept for the correct reason.

Python short-circuits `or`. When `k == 0` is true, it does not evaluate `x != nums[k - 1]`, so the algorithm never consults a supposed last retained value before one exists. This also lets the exact source return zero safely for an empty list, even though the stated constraints make the list non-empty.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"return_value": 2, "prefix": [1, 2]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"return_value": 2, "prefix": [1, 2]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Read index plus write index:** Iterate explici:** - **Read index plus write index:** Iterate explicit indices from one onward and compare `nums[i]` with `nums[i - 1]`. It has the same bounds and is the form used in many editorials.
- **Set followed by sorting:** It uses $O(k)$ extra space, may require sorting, and ignores the stronger in-place opportunity provided by already sorted input.
- **Delete duplicates from the list:** Repeated physical deletion shifts later elements and can make the method $O(n^2)$ in an array-backed list.
- **Empty list outside the stated constraints:** The exact source returns `0` because the loop never runs.
- **One value:** It is written to index zero and the method returns one.
- **All values equal:** Only the first is kept; `k` remains one.
- **All values distinct:** Every value is written, often back to its current position, and `k = n`.
- **Negative values:** No sentinel is used, so the full permitted numeric range works normally.
- **Tail contents:** Values at and after index `k` are unspecified and must not be interpreted as part of the answer.
- **Sortedness is essential:** On an unsorted sequence such as `[1,2,1]`, the last `1` would be retained again; the algorithm removes duplicate runs, relying on the contract to make each value one run.
- **Relative order:** Values are scanned and written left to right, so the retained sequence keeps its original order automatically.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)` and $k$ the final number of distinct values.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
