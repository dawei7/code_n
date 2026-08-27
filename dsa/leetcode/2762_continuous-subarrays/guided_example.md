# Guided Example: Continuous Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 4, 2, 4]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. A subarray of `nums` is called **continuous** if:

The objective is to compute `8` from `{"nums": [5, 4, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce an all-pairs condition to two extreme values

A subarray is continuous when the absolute difference between every pair of its elements is at most two. Checking all pairs would be unnecessarily expensive. In any collection, the largest possible difference is

$$
\max(\text{window}) - \min(\text{window}).
$$

If this extreme difference is at most two, every other pair lies between those extremes and is also within two. If it is greater than two, the minimum and maximum themselves form a violating pair. The entire validity condition is therefore equivalent to maintaining `maximum - minimum <= 2`.

The exact solution uses a sliding window and a `SortedList`. The sorted multiset contains all values in the current index interval. Its first item `sl[0]` is the minimum, its last item `sl[-1]` is the maximum, and duplicate values are stored with their full multiplicity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 4, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Grow on the right, repair on the left

Variable `i` is the left boundary. The `for x in nums` loop supplies each successive right-end value. The algorithm first adds `x` to the sorted multiset. If the new maximum and minimum differ by more than two, it repeatedly removes `nums[i]` and increments `i` until the condition becomes valid again.

The left pointer never moves backward. Once a window ending at the current position is invalid because of its extremes, keeping its old left endpoint cannot become valid merely by adding more elements. Removing the oldest values is the only available way to repair that current ending.

`SortedList.remove(nums[i])` removes one occurrence, not every equal occurrence. This matters because the window may contain duplicates. The data structure must mirror exactly how many positions remain in the interval, not merely which distinct values occur.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Variable `i` is the left boundary.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The window is the longest valid suffix ending here

After the shrinking loop stops, the multiset represents precisely `nums[i:right + 1]` and is valid. Moreover, `i` is the smallest possible left boundary for a valid subarray ending at this right endpoint.

Why? If the newly expanded window was already valid, `i` did not change and it remains the earliest boundary inherited from the previous step. If it was invalid, the loop removed elements from the left one by one and stopped at the first point where the extreme difference became at most two. The immediately earlier boundary was still invalid at the moment it was removed. Thus the surviving interval is the longest valid suffix ending at the current element.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 4, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two monotonic deques:** One decreasing deque c:** - **Two monotonic deques:** One decreasing deque can track maxima and one increasing deque can track minima in amortized constant time per element, giving `O(n)` time and `O(n)` worst-case space. This is the strategy described by the manifest, but it is not the exact solution file.
- **Frequency map over the three possible values:** Once a valid window is known, it has at most three distinct integer values, but discovering and repairing the range still requires careful minimum and maximum maintenance. A sorted map can exploit the small distinct range.
- **Recompute minimum and maximum for every window:** This avoids an ordered structure but can rescan long windows repeatedly and degrade to quadratic time.
- **All values equal:** No shrinking occurs. The contributions are `1, 2, ..., n`, correctly counting every subarray.
- **Difference exactly two:** The window remains valid because the condition is inclusive.
- **Difference greater than two after insertion:** The loop may remove several old values; it stops only when both extremes fit the bound.
- **Duplicate values:** `SortedList` preserves multiplicity, and `remove` deletes only one departing occurrence.
- **One-element input:** The single value forms one continuous subarray, so the answer becomes one.
- **Very large element values:** Only comparisons and subtraction matter; the algorithm never allocates an array indexed by value.
- **Large answer:** The count can be `n(n + 1) / 2`. Python integers grow as needed, so no fixed-width overflow occurs.
- **Input order:** Sorting the entire input would destroy contiguity. Only the active window's value multiset is sorted; original positions remain represented by the moving boundaries.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let `n` be `nums.length`. Each element is inserted into `SortedList` once. Because `i` only increases, each element is also removed at most once. Under the standard ordered-multiset cost model, both insertion and removal take `O(log n)` time, while reading the first and last values and getting the length are constant time. The total time is `O(n log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
