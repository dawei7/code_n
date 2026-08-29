# Guided Example: Find All Groups of Farmland

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"land": [[1, 0, 0], [0, 1, 1], [0, 1, 1]]}`
- **Required output:** `[[0, 0, 0, 0], [1, 1, 2, 2]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** `m x n` binary matrix `land` where a `0` represents a hectare of forested land and a `1` represents a hectare of farmland.

The objective is to compute `[[0, 0, 0, 0], [1, 1, 2, 2]]` from `{"land": [[1, 0, 0], [0, 1, 1], [0, 1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recognize only the top-left corner of a group

The outer loops inspect every matrix cell in row-major order. A farmland cell is the top-left corner of its rectangular group exactly when it has no farmland immediately above it and no farmland immediately to its left.

The source skips a cell when it is forest, when its left neighbor is farmland, or when its upper neighbor is farmland. The boundary checks `j > 0` and `i > 0` prevent accessing outside the matrix.

Any non-top-left cell in a rectangle is skipped. A cell below the rectangle's first row has farmland above it. A cell in the first row but right of the first column has farmland to its left. Only the actual top-left cell has neither.

This test replaces a visited matrix: the group is reported only at its unique top-left corner even though the input is never modified.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"land": [[1, 0, 0], [0, 1, 1], [0, 1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the bottom row

After discovering top-left coordinate `(i, j)`, the source initializes `x=i` and moves `x` downward while `land[x + 1][j] == 1`.

Because groups are solid rectangles, the first column of the group contains farmland on every row from top to bottom. When the loop stops, `x` is the bottom row coordinate.

The separation guarantee ensures the scan cannot accidentally continue directly into a different group: distinct groups are not four-directionally adjacent.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the rightmost column

The second while loop begins at `(x, j)`, the bottom-left cell, and moves `y` right while the next cell is farmland. When it stops, `y` is the rightmost column.

Why is scanning only the bottom row enough? The rectangle guarantee says every row of a group spans the same continuous columns. Therefore the right boundary found on the bottom row is also the right boundary for the entire group.

The result `[i, j, x, y]` is exactly top-left row, top-left column, bottom-right row, and bottom-right column.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0, 0, 0], [1, 1, 2, 2]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"land": [[1, 0, 0], [0, 1, 1], [0, 1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0, 0, 0], [1, 1, 2, 2]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **DFS or BFS:** Finds each connected component and its maximum coordinates in $O(MN)$ time, but uses a visited structure or mutates the grid.
- **Mark the whole rectangle as zero:** Also avoids duplicates, but changes the input and writes every farmland cell.
- **Visited matrix:** Preserves input but spends $O(MN)$ extra space unnecessarily under the rectangle guarantee.
- **Single-cell group:** Both scans stay in place and all four coordinates use that cell.
- **Group touching top edge:** The `i > 0` guard correctly treats the missing upper neighbor as forest.
- **Group touching left edge:** The `j > 0` guard handles it without negative indexing.
- **Group touching bottom or right edge:** Bounds in the while conditions stop safely.
- **All farmland:** Only `(0,0)` qualifies, and the scans find the full matrix rectangle.
- **No farmland:** Every cell is skipped and the result is empty.
- **Several separated rectangles:** Nonadjacency prevents one boundary scan from entering another group.
- **Rectangle guarantee:** Essential; an irregular component could make the bottom-row width unrepresentative of upper rows.
- **Any answer order:** Row-major discovery is valid even though no specific order is required.
- **Input side effects:** The exact solution does not mutate `land`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(MN)$. Let $M$ be the row count and $N$ the column count. The nested outer loops cost $O(MN)$. Boundary scans across all disjoint groups add at most linear work in the number of farmland boundary cells, so total time remains $O(MN)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
