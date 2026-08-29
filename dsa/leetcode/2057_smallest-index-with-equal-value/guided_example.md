# Guided Example: Smallest Index With Equal Value

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 2]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** integer array `nums`, return *the **smallest** index *`i`* of *`nums`* such that *$i mod 10 = \text{nums}[i]$*, or *`-1`* if such index does not exist*.

The objective is to compute `0` from `{"nums": [0, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Test the condition exactly as written

For index `i`, the required comparison is between `i % 10` and `nums[i]`. The modulo operation keeps only the remainder after division by ten, so its result is always one of the digits zero through nine.

The input values are also guaranteed to lie between zero and nine. No conversion or normalization is needed before equality comparison.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan from left to right

`enumerate(nums)` produces pairs `(i,x)` in increasing index order, beginning with index zero.

For each pair, the source checks `i % 10 == x`. When it succeeds, the method returns `i` immediately.

Because no larger index is examined before a smaller one, the first successful index is automatically the smallest successful index. The algorithm does not need to store all matches and take their minimum afterward.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the repeating remainder pattern

The value `i % 10` repeats every ten indices:

$$
0,1,2,\ldots,9,0,1,2,\ldots
$$

Thus index zero can match only value zero, index seven can match only value seven, index ten can match only value zero, and index 23 can match only value three.

This periodicity is why array values outside zero through nine could never match. The provided value constraint already restricts the data to the only meaningful range.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Collect every matching index:** Correct but wastes $O(N)$ output storage when only the smallest is needed.
- **Use a generator with `next`:** Can express the same left-to-right early search, though the explicit loop is clearer.
- **Sort the array:** Incorrect because the condition depends on original indices.
- **Index zero:** Matches exactly when the first value is zero.
- **Indices ten, twenty, and so on:** Their remainder returns to zero.
- **Several valid indices:** Immediate return selects the smallest.
- **Only the final index valid:** The full scan returns that index.
- **No valid index:** Return `-1` after exhausting the loop.
- **Array length one hundred:** The remainder pattern completes ten cycles.
- **Values zero through nine:** Exactly match the possible modulo results.
- **Nonnegative indexing:** `enumerate` begins at zero, matching the problem's indexing.
- **Input preservation:** No sorting or mutation occurs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of `nums`. At most $N$ iterations are performed, and modulo plus equality are constant-time operations for these bounded integers. Worst-case time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
