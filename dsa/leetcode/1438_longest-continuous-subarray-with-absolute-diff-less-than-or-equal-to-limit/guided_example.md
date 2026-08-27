# Guided Example: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [8, 2, 4, 7], "limit": 4}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums` and an integer `limit`, return the size of the longest **non-empty** subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`*.*

The objective is to compute `2` from `{"nums": [8, 2, 4, 7], "limit": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the window minimum and maximum determine validity

For any set of numbers, the largest absolute difference between a pair is:

$$
\max-\min.
$$

If that extreme difference is at most `limit`, every other pair is also within the limit. If it exceeds the limit, the minimum and maximum themselves form a violating pair.

The algorithm therefore maintains a sliding window and a sorted multiset `sl` containing exactly its elements. The first sorted value is its minimum and the last is its maximum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [8, 2, 4, 7], "limit": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the two boundaries mean

`j` is the left endpoint of the current window. The outer loop's index `i` is its right endpoint. After adding `nums[i]` and shrinking as needed, the window is `nums[j:i+1]`.

`ans` stores the longest valid window length observed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `j` is the left endpoint of the current window.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A sorted multiset is required, not a plain set

`SortedList` keeps values in nondecreasing order and allows duplicates. Duplicate support matters: if the current window contains three copies of 2, removing one leftmost 2 must leave the other two present.

For each new value:



inserts it into sorted position. Then `sl[0]` is the current minimum and `sl[-1]` is the current maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [8, 2, 4, 7], "limit": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two monotonic deques:** Maintain decreasing ma:** - **Two monotonic deques:** Maintain decreasing maximum candidates and increasing minimum candidates. Each index enters and leaves each deque once, realizing $O(n)$ time.
- **Two heaps with lazy deletion:** Track minimum and maximum with indices. It is correct but uses logarithmic operations and more stale-entry handling.
- **Balanced frequency map:** A sorted dictionary from values to counts implements the same multiset idea as SortedList.
- **Brute-force subarrays:** Recomputing extremes for every range can take quadratic or cubic time.
- **`limit = 0`:** A valid window can contain only equal values; duplicate-aware removal is essential.
- **All equal values:** The window never shrinks and the answer is $n$.
- **One element:** Difference is zero, so the result is one.
- **Duplicate minimum or maximum:** Removing one occurrence must not erase the others; SortedList handles multiplicity.
- **Large new outlier:** The while loop may remove many left elements, but each array position is removed only once overall.
- **Contiguity:** Shrinking always removes `nums[j]`, not an arbitrary extreme value.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length. Each element is inserted into `SortedList` once and removed at most once. Balanced sorted-container insertion and removal cost $O(\log n)$, while reading either endpoint is $O(1)$. Total time for the exact stored implementation is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
