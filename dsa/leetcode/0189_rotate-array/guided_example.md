# Guided Example: Rotate Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3}`
- **Required output:** `[5, 6, 7, 1, 2, 3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

The objective is to compute `[5, 6, 7, 1, 2, 3, 4]` from `{"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce large rotations to one equivalent shift

Rotating an array of length $n$ right by $n$ positions returns every element to
its original index. Therefore only the remainder `k % n` matters. The statement
guarantees that `nums` is nonempty, so `k %= n` cannot divide by zero.

This normalization handles both very large values and exact multiples of the
length. If the remainder is zero, the desired result is the original array;
the later reversals still produce that result without a special branch.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Describe the desired block movement

After normalization, split the original array conceptually into two blocks:

- `A`, the first $n-k$ elements.
- `B`, the final $k$ elements.

A right rotation changes `A B` into `B A`. The challenge is to perform that
block swap in place without allocating another length-$n$ array. Three
reversals accomplish it because reversing a concatenation reverses both the
block order and the character order inside each block.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use an inclusive reversal helper

The nested `reverse(i, j)` treats both indices as included. While `i < j`, it
swaps the two endpoint values and moves the pointers inward. An odd-length
interval leaves its middle element untouched after all surrounding pairs have
been swapped. Empty or one-element intervals perform no swaps.

Only a constant number of indices and temporary references are used. Python's
parallel assignment exchanges list elements in the existing list rather than
constructing a replacement array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 6, 7, 1, 2, 3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 6, 7, 1, 2, 3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Cyclic replacement:** Follow target indices `(i + k) % n` and use one temporary value; also $O(n)$ time and $O(1)$ space, but multiple index cycles require careful counting.
- **Extra array:** Write each value directly to its target index, then copy back; straightforward $O(n)$ time but $O(n)$ extra space.
- **Repeated one-step rotation:** Constant space but $O(nk)$ time after normalization.
- **Left/right block interpretation:** Right rotation by `k` is also left rotation by `n - k`; the reversal boundaries must match the chosen direction.
- **`k = 0`:** The first and third full reversals cancel while the empty prefix reversal does nothing.
- **`k` multiple of `n`:** Normalizes to zero and leaves the array unchanged.
- **One element:** Every reversal is empty or length one, so the sole value remains.
- **Negative and duplicate values:** Movement depends only on indices, not value comparisons.
- **Nonempty guarantee:** Required for `k %= n`; a generalized API should guard an empty list.
- **Missing typing import:** Supply `List` outside a harness that already defines it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The three reversal lengths are $n$, $k$, and
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
