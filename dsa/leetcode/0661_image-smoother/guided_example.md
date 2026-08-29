# Guided Example: Image Smoother

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"img": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}`
- **Required output:** `[[0, 0, 0], [0, 0, 0], [0, 0, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

The objective is to compute `[[0, 0, 0], [0, 0, 0], [0, 0, 0]]` from `{"img": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute each output pixel from the original neighborhood

For every cell `(i, j)`, the smoother considers the rectangle covering row indices `i - 1` through `i + 1` and column indices `j - 1` through `j + 1`. That rectangle has at most nine positions:

- the cell itself;
- up to eight horizontally, vertically, or diagonally adjacent cells.

Positions outside the image do not exist and must not contribute either to the sum or to the divisor.

The exact solution creates a separate output matrix `ans`. This is important because every result must be based on the original `img` values. Writing smoothed values back into `img` immediately would let later neighborhoods read a mixture of original and already modified pixels.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"img": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Visit every target position

The outer loops enumerate all `m * n` coordinates:

- `i` selects an output row;
- `j` selects an output column.

For each target, `s` starts as the neighborhood sum zero and `cnt` starts as the number of included cells zero.

Two small loops then try every candidate coordinate `(x, y)` in the surrounding three-by-three region. The condition:

`0 <= x < m and 0 <= y < n`

accepts exactly the coordinates inside the matrix. For each accepted coordinate, increment `cnt` and add `img[x][y]` to `s`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the divisor must be counted rather than assumed

An interior pixel of a sufficiently large image has nine valid cells in its neighborhood. A corner normally has four and a non-corner boundary pixel normally has six. However, those familiar counts change for one-row or one-column images. Explicitly counting valid cells handles every shape uniformly.

The current cell `(i, j)` is always inside the image, so `cnt` is never zero. Division is therefore safe without a special fallback.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0, 0], [0, 0, 0], [0, 0, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"img": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0, 0], [0, 0, 0], [0, 0, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two-dimensional prefix sums:** Precompute rectangular sums so each clipped neighborhood sum can be queried with four prefix references. This remains `O(RC)` overall but introduces another `O(RC)` table and more indexing complexity for a fixed three-by-three window.
- **In-place bit encoding:** Since original and smoothed values fit within known ranges, store both in different bit regions of each cell, then extract results in a second pass. This can reduce auxiliary space but is less readable and depends on value bounds.
- **Rolling row buffers:** Retain only enough original rows to compute the next output row. This reduces extra working memory when output can be written progressively, but careful ordering is required.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R * C)$. Let `R` be the number of rows and `C` the number of columns.
- **Auxiliary Space Complexity:** $O(R \cdot C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
