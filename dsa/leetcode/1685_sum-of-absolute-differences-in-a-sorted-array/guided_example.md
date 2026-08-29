# Guided Example: Sum of Absolute Differences in a Sorted Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 5]}`
- **Required output:** `[4, 3, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` sorted in **non-decreasing** order.

The objective is to compute `[4, 3, 5]` from `{"nums": [2, 3, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use sorted order to remove absolute-value branches

For current value `x = nums[i]`, every element to the left is at most `x` and every element to the right is at least `x`. Therefore:

- a left contribution is `x - nums[j]`;
- a right contribution is `nums[j] - x`.

The sorted guarantee is what lets the algorithm replace every absolute value with one known subtraction direction.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sum all left-side differences at once

There are `i` elements before index `i`. If all of them were raised to `x`, their combined value would be `x * i`. Their actual combined value is the running prefix sum `t`.

Thus the total difference from the left side is

$$
x\cdot i-t.
$$

At the start of each iteration, `t` contains only indices strictly before `i` because the source adds `x` after computing the answer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sum all right-side differences at once

`s = sum(nums)` is the total of the entire array. The actual sum strictly to the right is

$$
s-t-x.
$$

There are `n-i-1` right-side elements. If each were reduced to `x`, their combined value would be

$$
x(n-i-1).
$$

So the right contribution is

$$
(s-t-x)-x(n-i-1).
$$

The exact source writes the complete expression as

`x * i - t + s - t - x * (len(nums) - i)`.

To see the equivalence, expand its right portion:

$$
s-t-x(n-i)
=s-t-x-x(n-i-1).
$$

That is exactly right sum minus the target total for the right-side count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 3, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 3, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Full prefix-sum array:** It provides left and right sums by indexing and is easy to derive, but uses $O(n)$ auxiliary space beyond the output.
- **Brute force per index:** Summing all absolute differences independently takes $O(n^2)$ time and ignores sorted structure.
- **Unsorted input:** The signed-side formulas become invalid. Sorting first would cost $O(n\log n)$ and would also lose original output positions unless indices are tracked.
- **All values equal:** Both side formulas cancel to zero at every index, returning an all-zero result.
- **Duplicate runs:** Equal neighbors contribute zero and require no special branch.
- **First index:** The left count and prefix sum are zero, so only right contributions remain.
- **Last index:** The algebraic right contribution becomes zero, so only left contributions remain.
- **Two elements:** Each result is the same absolute difference between the pair.
- **Update prefix after calculation:** Moving `t += x` before the formula would include the current value in the left prefix and break the count relationship.
- **Large total sums:** Python integers avoid overflow. Fixed-width languages should use a sufficiently wide integer type because up to $10^5$ values contribute.
- **Output-space convention:** The manifest’s $O(1)$ space excludes the required result array; the implementation necessarily returns $O(n)$ values.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `nums`. Computing `s` scans the array once, and the main loop scans it once more. Every iteration performs constant-time arithmetic, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
