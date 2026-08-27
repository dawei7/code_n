# Guided Example: Remove Duplicates from Sorted Array II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 1, 2, 2, 3]}`
- **Required output:** `{"return_value": 5, "prefix": [1, 1, 2, 2, 3]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**in-place**</a> such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

The objective is to compute `{"return_value": 5, "prefix": [1, 1, 2, 2, 3]}` from `{"nums": [1, 1, 1, 2, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the front of the array as the output buffer

`k` is both the number of values retained so far and the index where the next retained value should be written. At every point, `nums[:k]` is the correct compacted result for the original values already scanned. Positions at or after `k` are irrelevant to the final contract until they are used as unread input or overwritten with later retained values.

The loop variable `x` visits the input values in their original non-decreasing order. When a value is accepted, the source writes it to `nums[k]` and increments `k`. When it is rejected as an excessive duplicate, `k` stays fixed, so a later acceptable value overwrites that unused output slot.

The physical list length never changes. This matches the custom judge: only the returned length and the prefix before it matter; stale values after that prefix are unspecified.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 1, 2, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why mutating during `for x in nums` is safe here

Python's list iterator visits indices from left to right. Overwriting a list during iteration can be dangerous if writes alter unread positions. Here, after `p` original positions have been processed, at most `p` values have been retained, so `k <= p`. The next write is therefore at or behind the current scan position, never ahead of it.

If no value has been skipped, `k` equals the current index and the write is a harmless self-assignment. After skips, `k` is smaller and the write changes a position the iterator has already passed. Future original input values remain intact until they are read. The algorithm does not insert, delete, or change the list length, so iteration indices remain stable.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Python's list iterator visits indices from left to right.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep the first two retained values unconditionally

When `k < 2`, fewer than two total values have been retained. No value can yet be a forbidden third occurrence, so the condition accepts it. This also avoids reading `nums[k - 2]` with a negative logical output position.

The array is nonempty by contract, but the same logic would naturally return zero for an empty input because the loop would not run.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"return_value": 5, "prefix": [1, 1, 2, 2, 3]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 1, 2, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"return_value": 5, "prefix": [1, 1, 2, 2, 3]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit run counter:** Track the current valu:** - **Explicit run counter:** Track the current value's occurrence count and copy only counts one and two. It is equally linear and constant-space but uses more state.
- **Two-pointer plus previous comparisons:** Scan from index two and compare against the output at `write - 2`; this is the indexed form of the selected method.
- **Delete excessive values:** Removing list elements while scanning can shift a linear suffix for every deletion, producing quadratic time in Python.
- **Frequency dictionary:** It works without sorted input but uses extra space and ignores the key simplifying guarantee.
- **One element:** `k < 2` accepts it and returns one.
- **Exactly two equal elements:** Both are accepted.
- **Three or more equal elements:** Only the first two reach the output prefix.
- **All values distinct:** Every comparison differs and `k` becomes the original length.
- **All values equal:** The returned length is two when the input has at least two entries.
- **Negative values:** Only equality and sorted position matter, so sign is irrelevant.
- **Unspecified suffix:** The algorithm intentionally does not erase values after `k`.
- **No resizing:** Stable list length makes mutation during iteration safe together with the never-write-ahead invariant.
- **Sorted-order dependency:** Without grouping equal values, comparison with `k - 2` would not reliably count occurrences.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the original array length. Every original element is read once, and each iteration performs a constant number of comparisons and at most one assignment. Time is $O(n)$, matching the manifest. No costly element deletion or shifting occurs.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
