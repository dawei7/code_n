# Guided Example: Maximum Product of Three Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, *find three numbers whose product is maximum and return the maximum product*.

The objective is to compute `6` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

**Negative numbers create a second winning shape.** If all numbers were nonnegative, the answer would obviously use the three largest values. With negatives, two very small values can have a large positive product because negative times negative is positive. That positive pair can then be multiplied by the largest positive value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

After sorting `nums` in ascending order, the only two products that can be optimal are:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After sorting `nums` in ascending order, the only two produc... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

1. `nums[-1] * nums[-2] * nums[-3]`, the three largest values;
2. `nums[-1] * nums[0] * nums[1]`, the largest value with the two smallest values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Single scan over five extrema:** Track the two:** - **Single scan over five extrema:** Track the two smallest and three largest values in $O(n)$ time and $O(1)$ space. This is the true optimal implementation and matches the manifest.
- **Heap selection:** Find three maxima and two minima with small heaps. It remains linear up to constant heap factors but is more complex than five scalar variables.
- **Brute-force triplets:** Checking every triple costs $O(n^3)$ and ignores the extreme-value structure.
- **All positive values:** The three-largest candidate wins.
- **Two large-magnitude negatives:** Their positive pair may make the two-smallest candidate win.
- **All negative values:** The three largest, meaning those closest to zero, produce the least negative and therefore maximum product.
- **Zeros present:** Zero correctly beats every negative product when no positive triplet exists.
- **Exactly three elements:** Both formulas use those same three positions in some order, so their product is returned.
- **Duplicate extrema:** Duplicates are separate array elements and may all be selected when present.
- **Input mutation:** `sort()` changes `nums`; use `sorted(nums)` to copy or a single scan to preserve order.
- **Manifest mismatch:** Do not claim $O(n)$/$O(1)$ for the literal Python source merely because a different algorithm can attain those bounds.
- **Integer range:** The constraint bounds the product by $10^9$ in absolute value, so fixed-width 32-bit signed arithmetic is safe.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the length of `nums`. Python's in-place sort takes $O(n\log n)$ worst-case time. Reading six indexed values, computing two products, and taking their maximum are $O(1)$. The exact implementation's total time is therefore $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
