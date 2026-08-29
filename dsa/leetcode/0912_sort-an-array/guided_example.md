# Guided Example: Sort an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 2, 3, 1]}`
- **Required output:** `[1, 2, 3, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums`, sort the array in ascending order and return it.

The objective is to compute `[1, 2, 3, 5]` from `{"nums": [5, 2, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

The exact solution implements randomized three-way quicksort. It selects a pivot value, partitions the current interval into values smaller than, equal to, and greater than the pivot, then recursively sorts only the smaller and greater regions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 2, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Three-way partitioning is particularly important when many values are equal. An ordinary two-way quicksort may repeatedly include duplicates in recursive calls, while this method finishes the entire equal region in one partition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 2, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Merge sort:** Guarantees $O(n\log n)$ time but needs $O(n)$ merge storage.
- **Heap sort:** Guarantees $O(n\log n)$ time with $O(1)$ auxiliary array storage and avoids recursion, though it is often less cache-friendly.
- **Counting sort:** Values lie in a bounded range, so frequency counting can run in $O(n+K)$ time with $O(K)$ space.
- **Two-way quicksort:** It can perform poorly on many duplicates; three-way partitioning removes the entire equal block.
- **Already sorted input:** Random pivot selection avoids the deterministic first-pivot worst-case pattern in expectation.
- **All values equal:** One partition places the whole interval in the middle, and no nontrivial recursion follows.
- **Duplicate values:** They remain grouped in the equal region and appear with correct multiplicity.
- **Negative values:** Ordinary comparisons partition them correctly.
- **One element:** The base case returns immediately.
- **Pivot by value:** The pivot element may move during swaps, but stored scalar `x` remains the comparison value.
- **Do not advance `k` after a greater swap:** The incoming element is unclassified and must be examined.
- **Input mutation:** The returned object is the now-sorted original list.
- **Random worst case:** Randomization improves expected behavior but does not create a deterministic worst-case guarantee.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(\log n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
