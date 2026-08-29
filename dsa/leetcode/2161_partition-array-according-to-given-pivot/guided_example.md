# Guided Example: Partition Array According to Given Pivot

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [9, 12, 5, 10, 14, 3, 10], "pivot": 10}`
- **Required output:** `[9, 5, 3, 10, 10, 12, 14]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:

The objective is to compute `[9, 5, 3, 10, 10, 12, 14]` from `{"nums": [9, 12, 5, 10, 14, 3, 10], "pivot": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Classify every value exactly once

Three lists begin empty:

- `a` stores values less than the pivot;
- `b` stores values equal to the pivot;
- `c` stores values greater than the pivot.

For each `x` in `nums`, the `if`, `elif`, and `else` chain places it into exactly one list. Integer comparison is exhaustive: every value is less than, equal to, or greater than the pivot, and no value belongs to two categories.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [9, 12, 5, 10, 14, 3, 10], "pivot": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why appending preserves relative order

The loop visits `nums` from left to right. Suppose two less-than values occur at original indexes $i<j$. The first is appended to `a` before the second, and list append never changes earlier positions. They retain their relative order.

The same argument applies to greater-than values in `c`. Equal values are indistinguishable numerically, but `b` also preserves their encounter order.

This stability is the reason an in-place quicksort-style partition is unsuitable: swapping values toward opposite ends can reverse or scramble elements within a category.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Concatenate groups in the required order

The return expression `a + b + c` creates a list containing all of `a`, followed by all of `b`, followed by all of `c`.

Every less-than value therefore precedes every equal and greater value. Every pivot value lies between the outer groups. Every greater value appears last. Since each group is stable, all contract conditions hold simultaneously.

For `[9,12,5,10,14,3,10]` with pivot ten:

- `a` becomes `[9,5,3]`;
- `b` becomes `[10,10]`;
- `c` becomes `[12,14]`.

Concatenation yields `[9,5,3,10,10,12,14]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[9, 5, 3, 10, 10, 12, 14]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [9, 12, 5, 10, 14, 3, 10], "pivot": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[9, 5, 3, 10, 10, 12, 14]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed output with counted boundaries:** First count category sizes, then make a second stable pass writing into three known output regions. This is also $O(n)$ time and output space.
- **Two-direction stable fill:** Scan less-than values forward and greater-than values backward while filling opposite ends carefully. It can reduce temporary lists but is less direct.
- **Quicksort partition:** Standard swaps achieve category separation but do not preserve relative order.
- **Sort the array:** Sorting is $O(n\log n)$ and imposes value order within categories rather than merely preserving original order.
- **All values equal pivot:** `a` and `c` are empty, and the output equals the input.
- **No values less than pivot:** Concatenation begins with `b` and then `c`.
- **No values greater than pivot:** `c` is empty, so pivot values finish the result.
- **One element:** It must equal the pivot under the guarantee and is returned alone.
- **Duplicate non-pivot values:** Every occurrence is appended, and their original sequence is retained.
- **Negative values:** Comparisons work without sign-specific branches.
- **Pivot at the input’s beginning or end:** Original pivot position is irrelevant; all equal values move into the middle block.
- **Stable requirement applies separately:** A less-than value need not preserve order relative to a greater-than value because categories must be separated.
- **Input preservation:** Fresh lists satisfy the instruction without mutating `nums`.
- **Unique stable result:** Although equal pivot copies are indistinguishable, the less-than and greater-than subsequences have only one order that satisfies stability.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. Classification visits each element once, costing $O(n)$ time. Concatenating three lists copies $n$ references into the returned list, adding another $O(n)$ pass. Total time remains $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
