# Guided Example: Two Sum Less Than K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [34, 23, 1, 24, 75, 33, 54, 8], "k": 60}`
- **Required output:** `58`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` of integers and integer `k`, return the maximum `sum` such that there exists `i < j` with $\text{nums}[i] + \text{nums}[j] = sum$ and `sum < k`. If no `i`, `j` exist satisfying this equation, return `-1`.

The objective is to compute `58` from `{"nums": [34, 23, 1, 24, 75, 33, 54, 8], "k": 60}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort so the best partner can be found by boundary search

For a fixed value `x`, a partner `y` is valid when `x + y < k`, which is equivalent to `y < k - x`. After sorting `nums`, the greatest valid partner to the right of `x` is immediately before the first value that is at least `k - x`.

The method sorts the input list in place. This changes the caller’s element order, but the result depends only on values and distinct positions, not original ordering. Sorting preserves multiplicity, so two equal values at different indices remain two selectable elements.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [34, 23, 1, 24, 75, 33, 54, 8], "k": 60}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Restrict the search to a distinct later position

The loop visits sorted index `i` with value `x`. `bisect_left(nums, k - x, lo=i + 1)` searches only the suffix beginning after `i`. It returns the first index whose value is greater than or equal to the exclusive complement limit.

Subtracting one yields `j`, the greatest index in that suffix whose value is strictly less than `k - x`. Therefore, if such a suffix element exists, `x + nums[j]` is strictly less than `k`.

The check `i < j` confirms that the binary search actually found an element in the allowed suffix. If the insertion position was `i + 1`, subtraction produces `i` and there is no valid later partner. This also enforces two distinct array positions even when the desired numeric values are equal.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only that partner matters for one left index

Within the sorted suffix, every earlier candidate is no greater than `nums[j]`. Pairing `x` with any of them produces a sum no larger than `x + nums[j]`. Every later element is at least the threshold and therefore makes the sum greater than or equal to `k`.

Thus `j` gives the maximum legal sum among all pairs whose first sorted index is `i`. Taking `max` across every `i` then gives the maximum over all legal pairs.

Sorting changes indices, but any two positions in the sorted array correspond to two original occurrences. The condition `i < j` is only a canonical way to consider each unordered pair once; it still covers every possible pair of distinct input elements.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `58` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [34, 23, 1, 24, 75, 33, 54, 8], "k": 60}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `58` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two pointers after sorting:** Put one pointer at each end. If the sum is below `k`, record it and move the left pointer right; otherwise move the right pointer left. This reduces the post-sort scan to $O(n)$ and keeps the same $O(n\log n)$ total.
- **Brute force:** Check every pair in $O(n^2)$ time and $O(1)$ auxiliary space. It is simplest for small constraints but scales worse.
- **Counting array:** Values are bounded by one thousand, so frequency counts can search value pairs without comparison sorting. Duplicate handling and distinct-occurrence checks require care.
- **Array length one:** Every suffix is empty, `i < j` never holds, and the answer remains `-1`.
- **Sum exactly `k`:** It is invalid. The left-boundary search and one-step retreat enforce the strict inequality.
- **Repeated values:** They may form a pair only when at least two occurrences exist. Searching from `i + 1` guarantees a separate occurrence.
- **No valid pair:** Every computed candidate fails the index check, so the sentinel `-1` is returned.
- **Several pairs with the same best sum:** The algorithm stores only the numeric maximum, which is all the contract requests.
- **Very large complement:** `bisect_left` can return the list length; subtracting one correctly chooses the last suffix value.
- **Very small complement:** It can return `i + 1`; subtracting one gives `i` and the distinct-position check rejects the nonexistent partner.
- **Input mutation:** `nums.sort()` permanently reorders the supplied list. If caller-visible order had to be preserved, use `sorted(nums)` and accept an explicit $O(n)$ copy.
- **Positive-value guarantee:** It makes `-1` an unambiguous failure sentinel below every real pair sum.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Let $n$ be the number of values. Sorting costs $O(n\log n)$ time. The loop executes $n$ times, and each `bisect_left` over a suffix costs $O(\log n)$ time. The combined search work is $O(n\log n)$, so total time remains $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
