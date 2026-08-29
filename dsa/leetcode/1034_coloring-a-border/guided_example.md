# Guided Example: Coloring A Border

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 1], [1, 2]], "row": 0, "col": 0, "color": 3}`
- **Required output:** `[[3, 3], [3, 2]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` integer matrix `grid`, and three integers `row`, `col`, and `color`. Each value in the grid represents the color of the grid square at that location.

The objective is to compute `[[3, 3], [3, 2]]` from `{"grid": [[1, 1], [1, 2]], "row": 0, "col": 0, "color": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First identify the selected component

The operation applies only to the four-directionally connected component containing `grid[row][col]`. Let `c` be that starting color. A cell belongs to the component exactly when it can be reached from the start through adjacent cells whose original color is `c`.

Depth-first search explores that component. The helper `dfs(i, j, c)` is called only for a cell known to have color `c` before it is visited. It marks `vis[i][j] = true` immediately, preventing cycles in the grid graph.

The search never crosses into a different color. Such a neighbor is evidence that the current component cell is on the border, but it is not recursively visited.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 1], [1, 2]], "row": 0, "col": 0, "color": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What makes a component cell a border cell

The source gives two independent border conditions:

- At least one of the cell's four neighbors lies outside the grid.
- At least one in-bounds neighbor is not in the selected component.

The DFS checks both while examining the four directions. Whenever either condition is found, it sets `grid[i][j] = color`.

A cell can trigger the assignment several times through different neighbors. Repeating the same assignment is harmless. The method does not need a separate Boolean such as `is_border` because writing the target color immediately records the final action.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generate four-directional movement

Applying `pairwise` to `(-1, 0, 1, 0, -1)` produces offsets for up, right, down, and left.

For each offset, `x = i + a` and `y = j + b` identify a neighbor. The bounds test `0 <= x < m and 0 <= y < n` separates real grid neighbors from directions that leave the matrix.

If the coordinate is out of bounds, the current cell lies on the outer boundary of the grid, so it is recolored.

If it is in bounds and unvisited, its value decides what happens. Original color `c` means it belongs to the component and DFS continues there. A different value means the neighbor lies outside the component, so the current cell is a border cell and is recolored.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[3, 3], [3, 2]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 1], [1, 2]], "row": 0, "col": 0, "color": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[3, 3], [3, 2]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first search:** Discover the component with a queue and evaluate the same border conditions. It has identical `O(P)` bounds and avoids recursion-depth limits.
- **Collect border coordinates first:** Traverse without changing colors, store every border cell, then recolor them afterward. This makes mutation reasoning simpler but needs an additional border list of up to `O(P)`.
- **Use a special temporary color as visited state:** Negate or otherwise encode visited cells in `grid`, then restore interiors and apply the final color. This can avoid a Boolean matrix but becomes delicate when colors and target values overlap.
- **Copy the grid:** Writing into a separate output matrix preserves the caller's input but adds another `O(P)` allocation.
- **One-cell grid:** Every direction leaves the grid, so the only cell is a border and is recolored.
- **One-row or one-column component:** Every component cell lies on the matrix boundary and must be recolored.
- **Component fills the grid:** Outer cells change; cells with four in-bounds component neighbors remain unchanged.
- **Single-cell component inside the grid:** All four neighbors have a different color, so that lone component cell is a border.
- **New color equals original color:** Assignments make no visible change, but traversal and returned grid remain correct.
- **Neighbor already recolored:** Its visited flag proves component membership, preventing mutation from creating a false border.
- **Diagonal contact:** It does not join components and is not examined because adjacency is four-directional.
- **Different-color neighbor:** It remains untouched; only the current selected-component cell is recolored.
- **Input mutation:** The exact method changes `grid` in place. Callers needing the original values afterward must pass a copy.
- **Recursive depth:** A component containing up to 2500 cells can create a deep call chain in an unfavorable shape; iterative BFS or DFS is safer when the runtime has a low recursion limit.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P)$. Let `P = m \cdot n` be the number of grid cells. The DFS visits at most every cell in the selected component once and checks four directions per visit, giving `O(P)` worst-case time. The constant four does not affect the bound.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
