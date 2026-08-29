# Guided Example: Maximum Unique Subarray Sum After Deletion

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5]}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `15` from `{"nums": [1, 2, 3, 4, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

**Arbitrary deletions turn the choice into a distinct-value subsequence.** After deleting any number of elements, the elements kept between the chosen subarray's endpoints become contiguous in the remaining array. Therefore, any nonempty subsequence of the original order can be realized as the selected subarray: delete everything else, then select the entire remaining sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The original-order condition does not restrict the sum because addition is order-independent. The task becomes choosing a nonempty set of occurrences whose values are distinct and whose sum is maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**When a positive value exists, keep one copy of every positive value.** Every positive distinct value strictly increases the sum, so excluding one cannot be optimal. Multiple copies of the same positive value cannot both appear because the selected subarray must have unique elements, but keeping any one occurrence gives the same contribution.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Maximum-unique sliding window:** Sliding windows solve the no-deletion version, but arbitrary deletions let nonadjacent positive values be joined, making a window unnecessary.
- **Dynamic programming over subsequences:** Positivity and uniqueness reduce the choice to one copy per positive value, so DP adds no value.
- **Keep duplicate positives:** That violates the unique-elements rule even though duplicates would increase the numeric sum.
- **Keep negative values between positives:** They can be deleted, after which the positive occurrences become adjacent in the remaining array.
- **Include zero:** One zero is harmless in the positive case and optimal by itself when no positive exists but zero is present.
- **All negative:** Returning zero would violate the nonempty requirement; the largest single element is correct.
- **Repeated maximum negative:** Only one occurrence is needed to form the optimal one-element subarray.
- **All positive and distinct:** Every element is kept and the answer is their total sum.
- **All positive and equal:** Exactly one copy contributes because values must be unique.
- **Original-order preservation:** Chosen occurrences remain in order after deletion, but their sum and distinctness do not depend on that order.
- **Bounded value range:** It justifies the manifest's constant-space claim for the set.
- **Input preservation:** The array is scanned without mutation; deletions are a conceptual feasibility argument rather than operations performed by the code.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Computing `max(nums)` scans $n$ elements. In the positive case, the loop scans them once more. Set membership and insertion take expected $O(1)$ time, so total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
