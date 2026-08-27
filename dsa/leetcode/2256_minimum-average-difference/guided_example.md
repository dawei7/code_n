# Guided Example: Minimum Average Difference

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 5, 3, 9, 5, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of length `n`.

The objective is to compute `3` from `{"nums": [2, 5, 3, 9, 5, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain both side sums while moving the split

At index `i`, the left part contains positions zero through `i` and the right part contains `i + 1` through `n - 1`. Recomputing both sums from scratch at every index would repeat work.

The solution begins with `pre = 0` and `suf = sum(nums)`. Before processing an element, `pre` holds the sum strictly to its left and `suf` includes it and all later elements.

For current value `x`, the code executes:

- `pre += x`, making `pre` the sum through index `i`;
- `suf -= x`, making `suf` the sum strictly after index `i`.

These are exactly the two sums required for that split.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 5, 3, 9, 5, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute rounded-down averages

The left part contains `i + 1` elements, so its average is

`a = pre // (i + 1)`.

The right part contains `n - i - 1` elements. If that count is positive, its average is

`suf // (n - i - 1)`.

At the final index, the right part is empty and its average is defined as zero. The conditional assignment to `b` avoids division by zero and implements that rule directly.

All input values and sums are nonnegative, so Python floor division `//` is exactly the stated rounding down.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The left part contains `i + 1` elements, so its average is

... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Evaluate the average difference

`t := abs(a - b)` calculates the absolute difference and stores it in `t` through the assignment expression. The method compares `t` with the smallest value `mi` seen so far.

If `t < mi`, both `ans` and `mi` are updated. A strict comparison is essential for tie-breaking: when a later index has the same minimum difference, it does not replace the earlier `ans`. Since indices are scanned from zero upward, the retained index is the smallest minimum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 5, 3, 9, 5, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recompute both sums per index:** It is direct :** - **Recompute both sums per index:** It is direct but takes `O(n^2)` time.
- **Prefix and suffix arrays:** They give constant-time split sums after preprocessing but use `O(n)` extra space.
- **Floating-point averages:** They are unnecessary and can disagree with required integer rounding. Floor division must happen before subtraction.
- **Round the final difference:** That changes the operation order; each average is rounded down separately.
- **Single element:** The right average is zero and index zero is returned.
- **Final index:** Explicit empty-side handling avoids division by zero.
- **Difference tie:** Strict improvement preserves the earlier index.
- **Zero values:** Running sums and averages handle them naturally.
- **Minimum difference zero:** It is unbeatable, though the scan continues and retains its first occurrence.
- **Large total sum:** Wide integer arithmetic is required in fixed-width languages.
- **Nonnegative guarantee:** It makes `//` match ordinary truncating integer division for these sums.
- **Input preservation:** No array element is changed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. `sum(nums)` scans `n` elements once. The main loop scans them once more and performs constant arithmetic per index. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
