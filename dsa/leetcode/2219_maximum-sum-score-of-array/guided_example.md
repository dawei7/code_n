# Guided Example: Maximum Sum Score of Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 3, -2, 5]}`
- **Required output:** `10`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of length `n`.

The objective is to compute `10` from `{"nums": [4, 3, -2, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each index needs one inclusive prefix and one inclusive suffix

At index `i`, the sum score is the larger of two quantities:

$$
L_i = \sum_{t=0}^{i} \texttt{nums}[t]
$$

and

$$
R_i = \sum_{t=i}^{n-1} \texttt{nums}[t].
$$

Both sums include `nums[i]`. The task then asks for the maximum of `max(L_i, R_i)` over every valid index.

A straightforward method could build arrays containing all prefix sums and suffix sums. That would work in linear time but would store two additional length-`n` arrays. The exact solution observes that indices are processed from left to right, so only the current prefix and suffix totals are needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 3, -2, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize the two running sums

The variable `l` begins at zero because no element has yet joined the inclusive prefix. The variable `r` begins as `sum(nums)` because, before processing index zero, the suffix starting at zero is the entire array.

The answer begins as `-inf` rather than zero. Array values may be negative, and every valid score may also be negative. Initializing to zero would incorrectly return zero even though zero need not be obtainable. Negative infinity is below every finite integer score, so the first processed candidate always replaces it.

The input is nonempty by constraint, guaranteeing the loop executes and `ans` becomes a finite integer before return.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain exact meanings at the moment of comparison

At the start of the iteration for value `x = nums[i]`, before `l += x`, `l` equals the sum of elements strictly before index `i`. At that same moment, `r` equals the sum from index `i` through the end.

The first statement in the loop, `l += x`, turns `l` into the inclusive prefix `L_i`. The suffix `r` has not yet been changed, so it is already the inclusive suffix `R_i`. Therefore, exactly when the code executes

`ans = max(ans, l, r)`,

both running values match the two sums named in the problem for the current index.

After comparison, `r -= x` removes the current element. The result is the sum from index `i + 1` through the end, which is precisely the suffix needed at the start of the next iteration.

The order of these three operations is essential. If `r` were reduced before the comparison, it would exclude `nums[i]` and represent the wrong suffix. If `l` were updated after comparison, it would exclude `nums[i]` from the prefix. The exact sequence makes both sides inclusive at the same instant.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `10` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 3, -2, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `10` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Store prefix and suffix arrays:** Precompute every `L_i` and `R_i`, then scan their pairwise maxima. This is correct and still `O(n)` time, but it uses `O(n)` space that the running-sum sweep avoids.
- **Recompute both sums at every index:** Calling a sum operation on each prefix and suffix leads to `O(n^2)` total time because most elements are repeatedly added.
- **Use only the total and prefix:** Since `R_i = total - L_i + nums[i]` when both sums include index `i`, one could derive the suffix during the loop. This is also constant-space, but maintaining `r` explicitly makes the inclusive timing clear.
- **Initialize the answer to zero:** This fails when all valid prefix and suffix sums are negative. `-inf` or the first actual candidate is required.
- **All values negative:** The optimal score is still negative and often comes from a short prefix or suffix. The algorithm compares genuine inclusive sums without treating an empty selection as available.
- **All values positive:** Prefix sums grow and suffix sums shrink; the full-array sum appears as the suffix at index zero and the prefix at the last index, so it is the answer.
- **Single element:** After adding that element, both `l` and `r` equal it. The method returns the element itself, including when it is negative.
- **Zeros:** Zero values may leave one or both running sums unchanged. They need no special handling.
- **Subtracting a negative value:** The update `r -= x` increases `r` when `x` is negative, correctly removing a negative contribution from the next suffix.
- **Inclusive boundary at index `i`:** The current element belongs to both candidate sums. Updating `l` before and `r` after the comparison is mandatory.
- **Large-magnitude sums:** The result may exceed 32-bit range. Python is safe automatically; fixed-width implementations should use a 64-bit signed integer.
- **Input preservation:** The scan reads `nums` without changing its values or order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(nums)`. The initial `sum(nums)` scans all `n` elements once. The subsequent loop scans the same `n` elements once more, performing a constant number of arithmetic operations and comparisons per element. Two linear passes remain `O(n)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
