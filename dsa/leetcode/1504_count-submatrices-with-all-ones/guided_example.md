# Guided Example: Count Submatrices With All Ones

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[1, 0, 1], [1, 1, 0], [1, 1, 0]]}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` binary matrix `mat`, *return the number of **submatrices** that have all ones*.

The objective is to compute `13` from `{"mat": [[1, 0, 1], [1, 1, 0], [1, 1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Assigning every rectangle a unique bottom-right corner

An all-ones submatrix is a rectangle. It has one bottom row and one rightmost column, so it can be counted exactly once by its bottom-right cell. The stored solution iterates over every cell and asks how many valid rectangles end there.

To answer that question, it first builds `g`. The value `g[i][j]` is the number of consecutive ones in row `i` ending at column `j` and extending left.

If `mat[i][j]` is zero, the prefilled `g[i][j]` remains zero because no all-ones horizontal segment can end there. If it is one at column zero, the width is one. Otherwise, the width is one plus `g[i][j - 1]`, extending the run ending at the previous column.

For example, a row ending with `1, 1, 1` has successive widths one, two, and three. A zero resets the next possible run.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[1, 0, 1], [1, 1, 0], [1, 1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Counting rectangles for one bottom-right cell

Fix cell `(i, j)` as the bottom-right corner. A rectangle can choose any top row `k` from `i` upward. For every row between `k` and `i`, the rectangle must fit inside that row's consecutive-one width ending at column `j`.

Therefore, the maximum valid width for top row `k` is

$$
\min_{r=k}^{i} g[r][j].
$$

If that minimum is `w`, there are exactly `w` valid rectangles with top row `k` and right boundary `j`: their widths can be one through `w`. Each width chooses a different left boundary.

The source computes this minimum incrementally. It starts `col = inf` and scans `k` from `i` down to zero. At each row, `col = min(col, g[k][j])`. It then adds `col` to `ans`.

Starting with infinity makes the first minimum equal to `g[i][j]`. As more rows are included, `col` can only stay the same or decrease, which exactly reflects the constraint that a taller rectangle must fit through every included row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A concrete small trace

Suppose the widths ending at one column, read from top to bottom, are two, three, and one. For the bottom cell, the top-row choices produce:

- Bottom row alone: minimum width one, contributing one rectangle.
- Bottom two rows: minimum of three and one is one, contributing one.
- All three rows: minimum of two, three, and one is one, contributing one.

At a different bottom row where the upward widths are three and two, contributions are three for height one and two for height two. These counts represent every possible width, not merely the widest rectangle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[1, 0, 1], [1, 1, 0], [1, 1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Monotonic stack per row:** Build upward histogram heights and count rectangles ending at each column with an increasing stack. It achieves the manifest's $O(mn)$ time and $O(n)$ space.
- **Early break at zero width:** Stop the upward scan when `col` becomes zero. It improves zero-heavy inputs but retains $O(m^2n)$ worst-case time on all ones.
- **Brute-force four boundaries:** Enumerating every rectangle and checking all its cells is much slower because it repeats cell validation.
- **Single cell:** A one contributes one submatrix, while a zero contributes none.
- **All zeros:** Every width is zero and the answer is zero, though the exact source still runs every upward loop.
- **All ones:** Every axis-aligned submatrix is valid; this also triggers the enumeration's worst-case meaningful work.
- **One row:** Each run of ones contributes all contiguous subarrays within that run.
- **One column:** The method counts all vertical runs through the incremental minimum.
- **Infinity initialization:** `inf` must be available in the module environment; the first minimum converts it to a finite width.
- **No input mutation:** `mat` is read only, while widths are written to a separate matrix.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ the number of columns. Building `g` takes $O(mn)$ time and $O(mn)$ storage.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
