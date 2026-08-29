# Guided Example: Maximum Distance Between a Pair of Values

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"args": [[55, 30, 5, 4, 2], [100, 20, 10, 10, 5]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **non-increasing 0-indexed **integer arrays `nums1` and `nums2`.

The objective is to compute `2` from `{"args": [[55, 30, 5, 4, 2], [100, 20, 10, 10, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

**For each `i`, find the farthest possible `j`.** A valid pair requires `nums2[j] >= nums1[i]` and `j >= i`. For a fixed `i`, the best distance comes from the largest index `j` whose value still satisfies the inequality. Because `nums2` is non-increasing, all values large enough for `nums1[i]` form a prefix of `nums2`. Binary search can locate the end of that prefix.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"args": [[55, 30, 5, 4, 2], [100, 20, 10, 10, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Reverse `nums2` to use ordinary ascending binary search.** The exact code assigns `nums2 = nums2[::-1]`. This creates a new reversed list in nondecreasing order and leaves the caller’s original array unchanged.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

In the reversed list, `bisect_left(nums2, v)` returns the first position `p` whose value is at least `v`. All reversed positions from `p` onward meet the condition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"args": [[55, 30, 5, 4, 2], [100, 20, 10, 10, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two pointers:** Move monotonically through both non-increasing arrays to achieve `O(n + m)` time and `O(1)` auxiliary space.
- **Manual binary search on descending data:** It avoids the reversed copy and retains `O(n log m)` time with constant auxiliary space.
- **No qualifying value for an `i`:** Lower bound returns `m`, conversion gives minus one, and the negative distance is ignored.
- **Qualifying values only before `i`:** The farthest `j` still gives a negative distance, proving no valid partner exists for that `i`.
- **Pair with `i = j`:** Distance zero is valid and needs no special handling.
- **No valid pair anywhere:** `ans` remains zero as required.
- **Equal values:** `bisect_left` locates the first equal value in reversed order, which maps to the last equal value in original order and maximizes `j`.
- **One-element arrays:** The only possible pair is handled by the same conversion.
- **Different array lengths:** Each index is bounded by its own array, and negative candidates safely handle `i` beyond every qualifying `nums2` position.
- **Reversed-copy behavior:** The caller’s `nums2` remains unchanged, but `O(m)` memory is allocated.
- **Sortedness requirement:** Binary search correctness depends completely on both stated non-increasing orders.
- **Manifest mismatch:** The exact source is not the linear constant-space approach and should not be described as one.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m + n log m)$. Let `n = nums1.length` and `m = nums2.length`. Creating `nums2[::-1]` takes `O(m)` time. The loop performs `n` binary searches, each `O(log m)`. Total time is `O(m + n log m)`.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
