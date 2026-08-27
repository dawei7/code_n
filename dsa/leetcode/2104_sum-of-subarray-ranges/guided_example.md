# Guided Example: Sum of Subarray Ranges

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. The **range** of a subarray of `nums` is the difference between the largest and smallest element in the subarray.

The objective is to compute `4` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Fix a left endpoint and extend the subarray

The range of a subarray is its maximum minus its minimum. The exact source enumerates every subarray of length at least two, but avoids rescanning a subarray to rediscover those extremes.

For each starting index `i`, it initializes

`mi = mx = nums[i]`.

Then `j` moves from `i + 1` through the end. When `nums[j]` is added to the current subarray `nums[i...j]`, the new extremes are

`mi = min(mi, nums[j])`

and

`mx = max(mx, nums[j])`.

The range `mx - mi` is then added to `ans`.

This reuses the extremes from `nums[i...j - 1]`, so extending the right endpoint costs constant time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why length-one subarrays are omitted safely

The outer loop stops at `n - 2`, and the inner loop begins at `i + 1`. Therefore, the method never explicitly processes a one-element subarray.

Every one-element subarray has equal maximum and minimum, so its range is zero. Omitting these zero contributions does not change the required sum.

When the array itself has one element, the outer range is empty and the method returns the initialized zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer loop stops at `n - 2`, and the inner loop begins a... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace a starting index

For `nums = [1, 2, 3]` and `i = 0`, both extremes begin at 1.

- At `j = 1`, the maximum becomes 2 and minimum stays 1. The range of `[1, 2]` is 1.
- At `j = 2`, the maximum becomes 3 and minimum stays 1. The range of `[1, 2, 3]` is 2.

For `i = 1`, extending to `j = 2` gives range 1. The total is $1+2+1=4$. The three omitted singleton ranges are all zero.

Duplicates require no special treatment. In `[1, 3, 3]`, extending over the second 3 leaves the maximum unchanged, exactly as it should.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Monotonic contribution stacks:** Count each va:** - **Monotonic contribution stacks:** Count each value's subarrays as maximum and minimum to achieve $O(n)$ time and $O(n)$ space. This is the follow-up solution described by the manifest, not the exact source.
- **Recompute min and max for every subarray:** This adds another scan inside the endpoint loops and can cost $O(n^3)$. Carrying `mi` and `mx` avoids it.
- **Prefix sums:** They answer subarray sums, not subarray minima and maxima, so they do not directly solve range queries.
- **One element:** The only range is zero, and empty loops return zero.
- **All equal values:** Every maintained minimum equals maximum, so the result remains zero.
- **Negative values:** Min/max comparisons and their difference work without modification.
- **Duplicate extremes:** The direct enumeration does not need stack tie-breaking; it simply maintains the numeric extremes.
- **Length-one omission:** Safe only because every singleton range is exactly zero.
- **Large result:** Use a sufficiently wide accumulator outside Python.
- **Input preservation:** `nums` is read but never sorted or changed.
- **Manifest mismatch:** Complexity must follow the nested loops actually executed: $O(n^2)$ time and $O(1)$ auxiliary space.
- **Follow-up scope:** The source solves the required output correctly while not implementing the optional linear-time challenge.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the length of `nums`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
