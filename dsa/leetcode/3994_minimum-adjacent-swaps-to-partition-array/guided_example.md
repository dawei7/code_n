# Guided Example: Minimum Adjacent Swaps to Partition Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2, 4, 5, 6], "a": 3, "b": 4}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and two integers `a` and `b` such that `a < b`.

The objective is to compute `1` from `{"nums": [1, 3, 2, 4, 5, 6], "a": 3, "b": 4}` while avoiding redundant calculations and unnecessary overhead.

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

**The actual values matter only through three categories.**  A good array must contain, in order:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2, 4, 5, 6], "a": 3, "b": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

1. every value smaller than `a`;
2. every value in the inclusive range `[a, b]`;
3. every value larger than `b`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Call these categories low, middle, and high. The order of two values inside the same category is irrelevant. For example, two middle values may appear in either order because both belong to the same contiguous middle part.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2, 4, 5, 6], "a": 3, "b": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Actually performing adjacent swaps:** Bubble sorting the three categories reaches a good array, but explicitly moving elements can take `O(n^2)` time. Counting the swaps through inversions obtains the same minimum in one pass.
- **Merge-sort inversion counting:** A general inversion counter works in `O(n \log n)` time and `O(n)` extra space. It is unnecessary here because there are only three ordered categories, so two counters capture every possible inversion.
- **Fenwick tree over category ranks:** A frequency tree could count earlier larger ranks, but a structure for three ranks is needless overhead. `middle` and `high` are the only frequencies each branch needs.
- **Already-good input:** No low ever appears after a middle or high, and no middle appears after a high. Every addition is zero, so the algorithm returns `0`.
- **All values in one category:** Equal-category pairs never need to cross. The relevant counters may grow, but `swaps` remains zero.
- **An empty low, middle, or high part:** The statement explicitly permits empty parts. A missing category simply contributes a count of zero; no separate branch is required.
- **Values equal to `a` or `b`:** Both endpoints belong to the inclusive middle range. The ordered `if value < a` and `elif value <= b` checks implement that boundary exactly.
- **Duplicate values:** Duplicates do not cause extra swaps. Only category order matters, and equal values necessarily have the same category.
- **Stability inside a part:** The algorithm computes the minimum needed to group categories. It does not require or pay for sorting values within any part.
- **Modulo arithmetic:** The minimum is determined using the full inversion count. Returning `swaps % MOD` satisfies the output contract; the modulo must not be used as a comparison criterion for alternative arrangements.
- **Large inversion totals:** A reverse category arrangement can have billions of inversions at the maximum input size. Use 64-bit accumulation outside Python.
- **Input preservation:** The source only reads `nums`. This is useful when callers expect the original ordering to remain available after the method returns.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `nums`. The loop visits each element exactly once. Every iteration performs only comparisons, counter updates, and integer additions.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
