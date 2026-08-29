# Guided Example: Maximum Sum Circular Subarray

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, -2, 3, -2]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **circular integer array** `nums` of length `n`, return *the maximum possible sum of a non-empty **subarray** of *`nums`.

The objective is to compute `3` from `{"nums": [1, -2, 3, -2]}` while avoiding redundant calculations and unnecessary overhead.

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

A maximum circular subarray has one of two forms:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, -2, 3, -2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

1. It does not wrap, so it is an ordinary contiguous subarray.
2. It wraps from the end to the beginning. Equivalently, it contains the whole array except for one contiguous middle segment.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The solution computes the best ordinary subarray and the best valid complement form in one prefix-sum pass.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, -2, 3, -2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Kadane maximum plus Kadane minimum:** Compute ordinary maximum, total minus global minimum, and explicitly guard the all-negative case. This is the common equivalent formulation.
- **Duplicate the array:** Searching all length-at-most-$n$ subarrays in a doubled array needs more complex window logic and extra storage if materialized.
- **Try every circular start:** Extending up to $n$ positions from every start costs $O(n^2)$.
- **Return total minus minimum only:** It fails when the optimal subarray is nonwrapping or when removing everything would create an illegal empty result.
- **One element:** `smi` remains infinity, so only ordinary `ans` can win and the element is returned.
- **All positive:** The ordinary full array is optimal; removing a positive segment cannot improve it.
- **All negative:** The largest single value is returned, never zero.
- **Wrapping optimum:** A negative middle segment can be excluded to join a positive suffix and prefix.
- **Zero values:** Nonempty zero-sum subarrays are handled normally.
- **Prefix update order:** Candidate sums must be computed before current prefix extrema update to prevent empty segments.
- **`pmx = -inf`:** This is intentional, not symmetric with `pmi = 0`; it keeps the complement candidate nonempty and avoids redundant prefix removal.
- **No element reuse:** Complementing one contiguous middle segment produces a suffix-plus-prefix path that uses each index at most once.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The loop performs constant work per element.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
