# Guided Example: Max Increase to Keep City Skyline

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]}`
- **Required output:** `35`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a city composed of `n x n` blocks, where each block contains a single building shaped like a vertical square prism. You are given a **0-indexed** `n x n` integer matrix `grid` where $\text{grid}[r][c]$ represents the **height** of the building located in the block at row `r` and column `c`.

The objective is to compute `35` from `{"grid": [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce each skyline to row and column maxima

Looking from east or west, only the tallest building in each row determines that row's visible outer height. Looking from north or south, only the tallest building in each column matters.

Therefore the four directional skylines are preserved exactly when:

- every row keeps its original maximum;
- every column keeps its original maximum.

The method records those limits before changing anything:

`row_max[i] = max(grid[i])`

and:

`col_max[j] = max(grid[r][j] for every row r)`.

`zip(*grid)` transposes rows into column tuples, so the column comprehension can apply `max` directly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Derive one building's highest allowed height

Building `grid[i][j]` belongs to row `i` and column `j`.

To preserve the row skyline, its new height cannot exceed `row_max[i]`. To preserve the column skyline, it cannot exceed `col_max[j]`.

Both restrictions must hold, so the largest feasible height is:

$$
\min(row\_max[i],col\_max[j]).
$$

Any higher value would exceed at least one original maximum and visibly raise that direction's skyline.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why raising to the minimum does not lower or change a maximum

The algorithm only increases heights; it never lowers the building that originally realized a row or column maximum.

Setting one cell no higher than both original limits cannot create a new larger row or column maximum. The original maximum-height cells remain, so neither maximum can decrease.

Thus the computed ceiling is feasible for that cell.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `35` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `35` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan columns by index:** Avoid `zip` and compute each column maximum with nested indexing. It has the same $O(n^2)$ time and $O(n)$ stored maxima.
- **Try incremental increases:** Repeatedly raising buildings obscures the direct upper bound and may take time proportional to height differences.
- **Use only row maxima:** It can violate north/south skylines.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the square grid dimension. Computing all row maxima examines $n^2$ values. Transposing and computing column maxima also processes $n^2$ values. The final sum visits every cell once. Total time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
