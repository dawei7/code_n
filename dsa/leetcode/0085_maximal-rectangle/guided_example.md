# Guided Example: Maximal Rectangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [["0"]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return *its area*.

The objective is to compute `0` from `{"matrix": [["0"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn each row into the bottom of a histogram

`heights[j]` stores the number of consecutive `"1"` cells in column `j` ending at the current row. When the current matrix cell is `"1"`, the vertical run from the preceding row extends by one, so the source increments the height. When the cell is `"0"`, no all-one rectangle ending at this row can pass through that column, so the height resets to zero.

After updating one complete row, `heights` is a histogram whose bars measure how far an all-one column segment reaches upward from this row. A consecutive interval of histogram bars can support a rectangle whose height is their minimum and whose width is the interval length. That histogram rectangle corresponds directly to an all-one matrix rectangle with its bottom edge at the current row.

The algorithm finds the largest histogram rectangle for every possible bottom row and retains the largest area in `ans`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [["0"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why considering every bottom row is complete

Take any all-one rectangle in the matrix. It has some bottom row `r`, spans consecutive columns, and has some height `h`. When row `r` is processed, every spanned column has at least `h` consecutive ones ending there. The row's histogram therefore contains a rectangle over the same columns with height at least `h`, so the histogram solver considers an area at least as large as that matrix rectangle.

Conversely, if a histogram interval has minimum height `h`, each of its columns contains `h` consecutive ones ending at the current row. Those cells form a genuine all-one matrix rectangle. Histogram candidates cannot invent invalid matrix cells.

Thus the maximum across row histograms is exactly the maximum matrix rectangle, not merely an approximation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: For one histogram, find the nearest strictly lower bars

For each bar `i`, the helper wants the first position to its left with height strictly smaller than `heights[i]` and the first such position to its right. Between those boundaries, every bar is at least as tall as `heights[i]`, so a rectangle of that height can cover the entire open interval.

The width is `right[i] - left[i] - 1`, and the candidate area is the width times `heights[i]`. Sentinel defaults `-1` and `n` represent no smaller bar before the beginning or after the end.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [["0"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One-pass histogram stack:** Finalize bar areas as soon as a lower-or-equal bar appears and flush at a virtual zero. It avoids `left` and `right` arrays but still uses $O(n)$ stack space.
- **Dynamic left/right/height arrays across rows:** Update rectangle boundaries directly for each row. It also achieves $O(mn)$ time and $O(n)$ space but has more coupled state.
- **Upward scan from every cell:** Maintain horizontal widths and scan previous rows, which can take $O(m^2n)$ time.
- **All zeroes:** Every height remains zero and all candidate areas are zero.
- **All ones:** Heights increase each row, and the final full-width histogram yields area `m * n`.
- **One row:** The method reduces exactly to largest rectangle in a binary histogram.
- **One column:** Heights count the longest vertical run of ones.
- **Zero within a column:** Resetting to zero prevents rectangles from crossing it vertically.
- **Equal histogram heights:** The `>=` pop rule makes boundaries strictly lower and allows spanning the plateau.
- **Non-square matrix:** State size depends on columns and the row loop handles any positive row count.
- **String cells:** Comparisons correctly use `"1"` and `"0"`, not integers.
- **Nonempty guarantee:** Direct `matrix[0]` and nonempty `max` depend on it.
- **Input preservation:** Only derived height and boundary arrays change.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ the number of columns. Updating heights costs $O(n)$ per row. Each boundary pass pushes and pops every histogram index at most once, and area evaluation is another linear pass. Therefore each row costs $O(n)$ and total time is $O(mn)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
