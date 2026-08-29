# Guided Example: Sum of Subarray Minimums

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [3, 1, 2, 4]}`
- **Required output:** `17`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers arr, find the sum of `min(b)`, where `b` ranges over every (contiguous) subarray of `arr`. Since the answer may be large, return the answer **modulo** $10^{9} + 7$.

The objective is to compute `17` from `{"arr": [3, 1, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

Enumerating every subarray and finding its minimum would be quadratic or worse. The contribution method instead asks:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [3, 1, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

> For how many subarrays is `arr[i]` the chosen minimum?

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

If that count is known, index `i` contributes its value multiplied by the count. Summing over indices accounts for every subarray.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `17` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [3, 1, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `17` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all subarrays:** Maintaining a running minimum for every start costs $O(n^2)$ time.
- **Dynamic programming with a monotonic stack:** Compute the sum of minima for subarrays ending at each index. It also reaches $O(n)$ time.
- **Use strict comparisons on both sides:** Equal minima double-count shared subarrays.
- **Use non-strict comparisons on both sides:** Equal minima can leave shared subarrays unassigned.
- **All values increasing:** Left boundaries are immediate predecessors, while right boundaries are the sentinel.
- **All values decreasing:** Left boundaries are the sentinel, while right boundaries are immediate successors.
- **All values equal:** The asymmetric rule assigns each subarray to its rightmost element exactly once.
- **One element:** Its start and end choice counts are both one, so it contributes itself.
- **Boundary sentinels:** `-1` and `n` make formulas work without special cases at array ends.
- **Positive values:** The contract ensures every minimum is positive, though the contribution proof also works with other integers.
- **Modulo timing:** Reducing only after the sum is mathematically valid in Python; fixed-width languages may reduce during accumulation.
- **Store indices, not values:** Boundaries need distances, so stack entries must retain positions.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Each index is pushed once and popped at most once in each monotonic-stack pass. Boundary construction is therefore linear, and the final contribution generator is linear.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
