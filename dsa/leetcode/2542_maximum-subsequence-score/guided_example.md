# Guided Example: Maximum Subsequence Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 3, 3, 2], "nums2": [2, 1, 3, 4], "k": 3}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **0-indexed** integer arrays `nums1` and `nums2` of equal length `n` and a positive integer `k`. You must choose a **subsequence** of indices from `nums1` of length `k`.

The objective is to compute `12` from `{"nums1": [1, 3, 3, 2], "nums2": [2, 1, 3, 4], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat each selected `nums2` value as a candidate minimum

The score is:

$$
\left(\sum \text{selected }\texttt{nums1}\right)
\cdot
\min(\text{selected }\texttt{nums2}).
$$

If a particular chosen index supplies the minimum multiplier `a`, every other chosen index must have `nums2>=a`. Among those eligible indices, maximize the `nums1` sum.

Sorting paired values by `nums2` descending lets the scan consider candidate minima from large to small while all eligible larger multipliers are already available.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 3, 3, 2], "nums2": [2, 1, 3, 4], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Preserve index pairing while sorting

`zip(nums2,nums1)` creates pairs `(a,b)` from the same original index. Sorting these pairs in reverse order arranges larger `nums2` first.

The arrays need not be mutated, and their index relationship is preserved inside each tuple.

For equal `nums2`, reverse tuple ordering places larger `nums1` first. Tie order does not change correctness because the same multiplier applies across that tied group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret the current scan item

At pair `(a,b)`, all previously scanned pairs have first component at least `a`. If the current index is designated as one occurrence attaining the selected minimum, the other `k-1` indices may come from earlier eligible pairs.

To maximize the sum for this candidate, use current `b` plus the largest `k-1` `nums1` values seen earlier.

The heap maintains exactly the information needed for that choice.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 3, 3, 2], "nums2": [2, 1, 3, 4], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate subsequences:** $\binom nk$ choices are infeasible.
- **Sort ascending:** Possible with a different scan invariant, but descending order exposes eligible multipliers naturally.
- **`k=1`:** Each current item alone yields `nums1[i]*nums2[i]`.
- **Equal multipliers:** Tuple tie order does not lose any selection.
- **Zero `nums1` or `nums2`:** They are valid and heap arithmetic handles them.
- **Push before scoring:** Current index must belong to its canonical candidate.
- **Pop after scoring:** Retain only the largest `k-1` values for future minima.
- **Minimum multiplier:** It is supplied by the last selected item in sorted order.
- **Large product:** Use 64-bit arithmetic in fixed-width languages.
- **Input pairing:** Never sort arrays independently.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Creating and sorting `n` pairs costs $O(n\log n)$ time and $O(n)$ storage.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
