# Guided Example: Largest Submatrix With Rearrangements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[0, 0, 1], [1, 1, 1], [1, 0, 1]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a binary matrix `matrix` of size `m x n`, and you are allowed to rearrange the **columns** of the `matrix` in any order.

The objective is to compute `4` from `{"matrix": [[0, 0, 1], [1, 1, 1], [1, 0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert each one into a vertical height

Column rearrangement can place chosen columns beside one another, but it cannot change the vertical order of cells within a column. For a rectangle whose bottom lies on row `i`, the important value for each column is how many consecutive ones end at that row.

The source converts `matrix[i][j]` into that height. Starting with row one, if the current cell is one, it sets

`matrix[i][j] = matrix[i - 1][j] + 1`.

If the current cell is zero, it remains zero and resets the vertical streak. Row zero already contains correct heights of zero or one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[0, 0, 1], [1, 1, 1], [1, 0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Complete all heights before rearranging any row

The height-construction loops finish for the entire matrix before the later sorting loop begins. This phase separation is essential.

When computing row `i`, `matrix[i-1][j]` still refers to the same original column `j`. If an earlier row had already been sorted, its values would no longer align with the current row's columns and height accumulation would be wrong.

Only after every vertical streak has been calculated does the source reorder rows for area evaluation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret one height row

Fix a bottom row. A column with height $h$ can support an all-one rectangle of any height at most $h$ ending on this row.

If we choose $w$ columns, the maximum common rectangle height is the smallest height among those columns. Because columns may be globally rearranged, any chosen set of columns can be moved next to one another while preserving each column's vertical streak.

Thus the best width-$w$ rectangle uses the $w$ largest heights.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[0, 0, 1], [1, 1, 1], [1, 0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Maintain sorted height-column pairs:** Extend prior heights while preserving order and append new height-one columns, achieving $O(mn)$ time and $O(n)$ space.
- **Counting sort heights:** Heights range from zero to $m$, so frequency counting per row can replace comparison sorting when dimensions make it attractive.
- **Copy each row before sorting:** It preserves height-column alignment for later accumulation only if done during a one-pass variant, at the cost of $O(n)$ storage.
- **All zeros:** Every height and area is zero.
- **Single row:** Heights are the bits; sorting groups all ones and returns their count.
- **Single column:** Rearrangement has no effect, and the answer is the longest vertical run of ones.
- **Zero cell:** It resets that column's height to zero.
- **Several equal heights:** Any order among them yields the same width-area candidates.
- **Sort after accumulation:** Sorting earlier would corrupt column correspondence for the next row.
- **Global column operation:** Selecting and grouping the winning row's columns realizes its candidate even though other rows were hypothetically sorted differently.
- **Input mutation:** Both binary values and original column ordering are destroyed.
- **Area bound:** `j*v` never exceeds $mn$, the total number of cells.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ the number of columns. Height accumulation touches every cell in $O(mn)$ time. Sorting each of $m$ rows costs $O(n\log n)$, and scanning areas costs another $O(mn)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
