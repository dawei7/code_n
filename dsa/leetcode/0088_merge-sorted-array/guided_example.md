# Guided Example: Merge Sorted Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3}`
- **Required output:** `[1, 2, 2, 3, 5, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

The objective is to compute `[1, 2, 2, 3, 5, 6]` from `{"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the empty capacity from right to left

The first `m` positions of `nums1` contain meaningful sorted values, while its final `n` positions are capacity for the result. Writing the merged sequence from left to right would risk overwriting a meaningful `nums1` value before it had been compared. Writing from the right solves that problem because the destination begins in unused capacity.

`i = m - 1` points to the largest unread meaningful value in `nums1`. `j = n - 1` points to the largest unread value in `nums2`. `k = m + n - 1` points to the final unfilled result position in `nums1`.

At each step, the larger of the two readable values must be the largest value not yet placed, so it belongs at `nums1[k]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compare only when `nums1` still has a candidate

The condition `i >= 0 and nums1[i] > nums2[j]` first checks that an unread first-array value exists. Short-circuit evaluation prevents `nums1[-1]` from being treated as a legitimate candidate after the meaningful prefix is exhausted.

If that condition is true, `nums1[i]` is strictly larger and is copied to `nums1[k]`; `i` then moves left. Otherwise, `nums2[j]` is selected and `j` moves left. The otherwise case covers both a smaller-or-equal second-array value and exhaustion of the first array.

On equal values, the source chooses from `nums2`. The contract requires sorted values but does not attach identities that require stable ordering between the two input arrays, so either equal copy could be placed first from the right.

After either choice, `k` decreases because exactly one final position has been filled.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why overwriting `nums1[k]` is safe

Initially `k - i = n`, so the write pointer is separated from the unread first-array pointer by the entire extra capacity. Every iteration decrements `k` and decrements either `i` or `j`.

When `i` decreases, the gap between `k` and `i` stays unchanged. When `j` decreases, the gap shrinks, but this can happen only `n` times because `nums2` has `n` values. The write pointer cannot move ahead of an unread `nums1` value while any second-array value still needs placement.

Another way to see it is by counting: before writing a position, there are exactly `k + 1` total unread values across both arrays. There is enough space through index `k` for all of them, and the largest belongs at the boundary. A meaningful first-array cell is overwritten only after its original value has already been moved or when the same position is its final position.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 2, 3, 5, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 2, 3, 5, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Forward merge with a copy:** Copy the first `m` values, then merge from the beginning. It is linear time but uses $O(m)$ extra space.
- **Append and sort:** Copy `nums2` into the placeholders and sort all values. It ignores existing order and costs $O((m+n)\log(m+n))$ time.
- **Repeated insertion:** Insert second-array values into the meaningful prefix. Array shifting can make this quadratic.
- **`n == 0`:** `j` starts negative, the loop is skipped, and `nums1` remains unchanged.
- **`m == 0`:** `i` starts negative, so every iteration copies from `nums2` into `nums1`.
- **All first-array values larger:** They move to the far-right positions before second-array values fill the front.
- **All second-array values larger:** They fill the trailing capacity, and the first prefix remains in place.
- **Equal values:** The source chooses `nums2` on ties, which preserves sortedness.
- **Placeholder zeroes:** They are capacity only and may not be treated as meaningful values when `m` is smaller than the physical length.
- **Negative input values:** Backward maximum comparison works regardless of sign.
- **No return value:** Correctness is observed through the mutated `nums1` list.
- **Input preservation:** `nums2` is read only; `nums1` is intentionally overwritten.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m+n)$. Each iteration places one value from `nums2` or moves one meaningful value from `nums1`. No value is processed more than once, so time is $O(m+n)$ in the worst case, matching the manifest. It may stop earlier when `nums2` is exhausted, but the upper bound remains linear in both inputs.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
