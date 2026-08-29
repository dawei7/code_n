# Guided Example: Maximum Subarray Min-Product

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"args": [[1, 2, 3, 2]]}`
- **Required output:** `14`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **min-product** of an array is equal to the **minimum value** in the array **multiplied by** the array's **sum**.

The objective is to compute `14` from `{"args": [[1, 2, 3, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Choose a minimum value, then make its subarray as wide as possible.** Suppose `nums[i] = x` is treated as the minimum of a candidate subarray. That subarray can extend left and right while every included value is at least `x`. Because all input values are positive, adding another allowed element increases the sum and leaves the minimum at `x`. Therefore the best subarray represented by index `i` is its widest valid interval.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"args": [[1, 2, 3, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution finds that interval for every index with monotonic stacks, calculates its sum with prefix sums, and takes the maximum product before applying the modulus.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Find the nearest strictly smaller value on the left.** `left` starts filled with minus one, representing an absent boundary before index zero. Scanning left to right, the stack stores indices with strictly increasing values after the loop’s removals.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `14` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"args": [[1, 2, 3, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `14` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Expand from every index:** Walking left and right separately for each possible minimum can take `O(n^2)` time.
- **Divide and conquer:** Splitting around minimum values can solve related problems, but efficient minimum selection and sum handling are more complex than the stack method.
- **All values equal:** The asymmetric equality rule lets one occurrence represent the full array, which has the greatest positive sum.
- **Single element:** Both boundaries are sentinels, and its product is the value squared.
- **Strictly increasing array:** Left boundaries are immediate predecessors, while right boundaries are mostly `n`.
- **Strictly decreasing array:** Left boundaries are mostly minus one, while right boundaries are immediate successors.
- **Positive-values dependency:** Widest valid range maximizes the sum because every extension adds a positive amount; this argument would fail with negative values.
- **Equal-boundary comparisons:** `>=` on the left and `>` on the right are deliberate, not interchangeable formatting.
- **Modulo timing:** Maximize raw products first and reduce only the final result.
- **64-bit statement guarantee:** Other languages still need a 64-bit type for products; Python integers avoid overflow.
- **Prefix indexing:** `right[i]` is exclusive, and `left[i] + 1` is inclusive, matching the subtraction formula.
- **Non-empty requirement:** Every index represents at least its own one-element interval.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each index is pushed onto and popped from each monotonic stack at most once. The two boundary passes therefore take `O(n)` total time, not quadratic time despite their inner while loops. Prefix-sum construction and the final product scan are also `O(n)`. Overall time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
