# Guided Example: Ways to Make a Fair Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 6, 4]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. You can choose **exactly one** index (**0-indexed**) and remove the element. Notice that the index of the elements may change after the removal.

The objective is to compute `1` from `{"nums": [2, 1, 6, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The key effect of deleting one position

Deleting index `i` does not merely remove `nums[i]`. Every element to the right shifts one position left, so its parity changes: original even indices become odd indices, and original odd indices become even indices. Elements to the left keep their indices and therefore keep their parity.

Rebuilding the array and resumming it for every possible deletion would make this parity shift easy to model but would cost quadratic time. The source instead separates each candidate array into a left part that keeps parity and a right part that swaps parity.

`s1 = sum(nums[::2])` is the total of all original even-indexed values. `s2 = sum(nums[1::2])` is the total of all original odd-indexed values. During the scan:

- `t1` is the sum of original even-indexed values strictly before `i`;
- `t2` is the sum of original odd-indexed values strictly before `i`.

Both prefix variables start at zero. Crucially, the fairness test occurs before the current value is added, so they always describe only indices to the left of the candidate deletion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 6, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Deleting an even index

Suppose `i` is even and `v = nums[i]`. On the left, the new even-index sum receives `t1` and the new odd-index sum receives `t2`.

On the right, parities swap. The original odd-indexed suffix becomes even-indexed after deletion. Its sum is `s2 - t2` because the current even value is not part of `s2`. Therefore

$$
\text{newEven} = t1 + s2 - t2.
$$

The original even-indexed suffix becomes odd-indexed. From the original even total `s1`, subtract the earlier even prefix `t1` and also subtract the deleted current value `v`. Therefore

$$
\text{newOdd} = t2 + s1 - t1 - v.
$$

The first Boolean expression in the source compares exactly these two quantities:

`t2 + s1 - t1 - v == t1 + s2 - t2`.

It is guarded by `i % 2 == 0`, so it contributes only for an even deletion.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Deleting an odd index

If `i` is odd, the left contributions are still `t1` to new even and `t2` to new odd. The right suffix again swaps parity.

The original odd suffix, excluding current `v`, moves to even positions. Its sum is `s2 - t2 - v`. The original even suffix moves to odd positions and has sum `s1 - t1`. Hence

$$
\text{newEven} = t1 + s2 - t2 - v
$$

and

$$
\text{newOdd} = t2 + s1 - t1.
$$

The second source expression checks their equality and is guarded by `i % 2 == 1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 6, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Four running sums without slices:** First accumulate even and odd totals in one loop, then use the same prefix formulas. This preserves $O(n)$ time and achieves true $O(1)$ auxiliary space.
- **Prefix arrays:** Store even and odd prefix sums for every boundary and evaluate each deletion from those arrays. The formulas can be intuitive, but storage is $O(n)$ and more than the exact rolling state needs.
- **Delete and rescan for every index:** This directly follows the definition but takes $O(n^2)$ time and repeatedly shifts or reconstructs data.
- **Single-element array:** Removing its only element leaves an empty array; both parity sums are zero, so the sole index is correctly counted.
- **Deletion at index zero:** Both prefix sums are zero, and every surviving original index shifts parity. The formulas reduce to the swapped suffix totals.
- **Deletion at the last index:** There is no right suffix to swap. The total-minus-prefix expressions correctly reduce to zero after excluding the current value.
- **Odd array length:** Nothing requires equal counts of even and odd positions; only their value sums after deletion must match.
- **All equal values:** Some or all removals may work depending on length. The parity formulas handle the shifted counts rather than assuming equality automatically.
- **Positive-value constraint:** The derivation uses only addition and subtraction, so it would remain correct for zero or negative values as well.
- **Update ordering:** Adding `v` to `t1` or `t2` before testing would incorrectly treat the deleted value as part of the preserved left prefix.
- **Slice-memory subtlety:** Slicing is not a view in Python lists. A constant-space rewrite must avoid `nums[::2]` and `nums[1::2]` rather than merely discarding them after `sum`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `nums`. The two total-sum computations together inspect all elements once, and the main loop inspects all elements once more. Every loop iteration performs constant-time arithmetic, so total running time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
