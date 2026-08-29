# Guided Example: Sum of Subsequence Widths

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 3]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **width** of a sequence is the difference between the maximum and minimum elements in the sequence.

The objective is to compute `6` from `{"nums": [2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

Enumerating all nonempty subsequences would require exponential time. The useful transformation is to stop thinking about one subsequence at a time and instead ask how many times each array value contributes as a maximum and how many times it contributes as a minimum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Sorting `nums` places values in nondecreasing order. Subsequences are defined by original indices, but width depends only on selected values, not their original order. Sorting is safe for counting because each chosen index still represents one occurrence. Duplicate values remain separate sorted positions and therefore retain the correct multiplicity of index-based subsequences.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Consider sorted position $i$ with value `nums[i]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all subsequences:** This takes $O(2^n)$ subsets and is impossible for $n=10^5$.
- **Precompute all powers of two:** It simplifies indexing but uses $O(n)$ extra storage. The running `p` avoids that array.
- **Use the direct coefficient formula:** Add `nums[i] * (pow2[i] - pow2[n-1-i])`. It is equivalent to the mirrored-pair loop.
- **Do not sort:** The number of smaller and larger eligible values cannot be inferred from position without sorted order.
- **One value:** Positive and negative contributions cancel, yielding width zero.
- **All values equal:** Every subsequence has width zero, and the global maximum/minimum contributions cancel.
- **Duplicate values:** Sorted occurrences are still distinct indices. The representative tie convention counts every subsequence once.
- **Singletons:** They are included among nonempty subsequences but add zero width automatically.
- **Negative intermediate residue:** Python modulo normalizes it; no manual correction is needed.
- **Large power counts:** Reducing `p` after every doubling prevents enormous intermediate powers while preserving the result.
- **Input mutation:** `nums.sort()` changes the caller's array. Sorting a copy would preserve it at linear additional storage.
- **Subsequence order:** Sorting is used only for combinatorial counting. Width ignores the selected order, so original-order constraints do not change a selected set's width.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length. Sorting costs $O(n\log n)$. The contribution loop is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
