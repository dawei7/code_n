# Guided Example: Find Pivot Index

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 7, 3, 6, 5, 6]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums`, calculate the **pivot index** of this array.

The objective is to compute `3` from `{"nums": [1, 7, 3, 6, 5, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace repeated range sums with a running balance

An index `i` is a pivot when the sum of elements strictly to its left equals the sum of elements strictly to its right. Computing both sides from scratch for every index would repeat most additions and lead to quadratic time.

The exact solution instead keeps two running sums:

- `left` is the sum of elements strictly before the current index.
- `right` is adjusted to become the sum of elements strictly after the current index.

The total array sum gives an efficient starting point. Initially `left = 0` because no element lies before index `0`, while `right = sum(nums)` still includes every element. During the iteration at value `x = nums[i]`, the code first executes `right -= x`. Only then does `right` represent the strictly-right side required by the pivot definition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 7, 3, 6, 5, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The order of updates is the algorithm

For each index, the operations occur in this exact order:

1. Remove the current value from `right`.
2. Compare `left` and `right`.
3. If they differ, add the current value to `left` before advancing.

Moving either update can create an off-by-one-side error. If the comparison happened before subtracting `x`, the right sum would incorrectly include the pivot candidate. If `x` were added to `left` before the comparison, the left sum would also incorrectly include it.

The current element belongs to neither side. The update order makes that fact explicit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The loop invariant

Immediately after `right -= x` and before the equality test:

- `left` equals `nums[0] + ... + nums[i - 1]`.
- `right` equals `nums[i + 1] + ... + nums[n - 1]`.

At the first index, `left` is correctly zero, and removing `nums[0]` from the total leaves exactly the suffix after index zero.

If index `i` is not a pivot, `left += x` prepares the invariant for the next iteration: the next index’s left side includes the current element. At the start of the next iteration, subtracting its current value from `right` similarly removes that candidate from the remaining suffix.

Thus the comparison at every index uses precisely the two sums named in the problem, not approximations or inclusive variants.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 7, 3, 6, 5, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prefix-sum array:** Build cumulative sums, then compute each left and right side in constant time. This also takes `O(n)` time but uses `O(n)` additional storage. The two-running-sum method retains only the information needed at the current index.
- **Recompute both sides for each index:** Summing slices or loops around every candidate is easy to describe but costs `O(n^2)` time and may allocate temporary slices. Most additions are needlessly repeated.
- **Use the equation `2 * left + nums[i] == total`:** This algebraic form is equivalent because `right = total - left - nums[i]`. It can reduce the maintained state to a total and a left sum. The exact solution’s explicit right sum closely mirrors the problem definition.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of elements.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
