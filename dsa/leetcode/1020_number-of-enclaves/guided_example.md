# Guided Example: Number of Enclaves

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `grid`, where `0` represents a sea cell and `1` represents a land cell.

The objective is to compute `3` from `{"grid": [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn reachability into a boundary search

The matrix can be viewed as an undirected graph. Every land cell is a vertex, and two land vertices are connected when their cells share an edge. Diagonal contact does not create an edge because movement is limited to the four cardinal directions.

A land cell is not an enclave precisely when its connected component touches the boundary. Once a path reaches a boundary land cell, one more move can leave the grid. Conversely, a path cannot leave the grid without first reaching a cell in the first row, last row, first column, or last column. The question can therefore be restated:

Find all land connected to boundary land, discard it, and count the land that remains.

This reverse viewpoint is easier than starting a search from every land cell and asking whether that individual search escapes. All boundary-connected cells can be discovered together, and each cell needs to be visited at most once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the DFS changes land into water

The nested function `dfs(i, j)` is called only for a known in-bounds land cell. Its first operation, `grid[i][j] = 0`, marks that cell as visited by turning it into water. This serves two purposes at once:

- The cell is known to be boundary-reachable, so it must not contribute to the final enclave count.
- Future searches will see zero and will not visit the same cell again.

No separate `visited` matrix is necessary. This is safe because the final answer depends only on how many enclosed land cells remain, not on preserving the input matrix.

Marking happens before exploring neighbors. If two adjacent land cells call each other recursively, the first one has already become zero before the second search looks back. That ordering prevents an infinite recursion cycle.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The nested function `dfs(i, j)` is called only for a known i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the four directions are generated

The tuple `dirs = (-1, 0, 1, 0, -1)` encodes row and column offsets compactly. Applying `pairwise(dirs)` produces the consecutive pairs `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`. These mean up, right, down, and left.

For each pair `(a, b)`, the neighbor is `(x, y) = (i + a, j + b)`. The condition

`0 <= x < m and 0 <= y < n and grid[x][y]`

first proves that the coordinates are inside the matrix and then checks whether the cell contains one. Python evaluates `and` from left to right and short-circuits, so `grid[x][y]` is never accessed for an invalid coordinate. A value of one is truthy and triggers recursion; zero is false and is ignored.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Breadth-first search from the boundary:** Put :** - **Breadth-first search from the boundary:** Put every boundary land cell into a queue, mark it, and expand through four-directional neighbors. This has the same `O(RC)` time and `O(RC)` worst-case space while avoiding recursion-depth concerns.
- **Separate visited matrix:** Mark boundary-connected land in an `R \times C` Boolean structure rather than changing `grid`. This preserves the caller's input but always allocates `O(RC)` explicit memory.
- **Explore every component:** A DFS can count each land component and record whether any cell touches the boundary. Add its size only when it does not. This is correct and linear, but needs more per-component state than deleting all boundary-reachable land first.
- **Union-find:** Join adjacent land cells and connect boundary land to a virtual outside vertex. Count cells not joined to outside. It works, but parent and rank arrays add complexity and `O(RC)` storage without improving the time bound.
- **Do not use diagonal movement:** A diagonal chain of ones is not connected under this problem's rules. Only the four offsets produced by `pairwise(dirs)` are legal.
- **All water:** No DFS starts, and the final sum is zero.
- **All land:** Boundary DFS reaches every cell, changes the whole grid to zero, and returns zero enclaves.
- **One row or one column:** Every land cell lies on the boundary and is erased. Repeated boundary indices are harmless because erased cells fail later truth tests.
- **Isolated interior land:** A one surrounded on four sides by water is never reached from a boundary seed and contributes one.
- **A narrow connection to the boundary:** Even a one-cell-wide land corridor makes the entire connected component non-enclosed. DFS follows that corridor and erases all connected land.
- **Input mutation:** The exact solution intentionally changes `grid`. If the surrounding application needs the original matrix afterward, it must pass a copy or use a visited structure instead.
- **Recursive depth:** The mathematical algorithm supports up to `RC` connected cells, but a runtime with a small recursion limit may need the iterative BFS or DFS form to avoid stack overflow.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let `R = m` be the number of rows and `C = n` be the number of columns. The boundary loops examine `2C + 2R` positions. Across all DFS calls, each land cell is entered at most once because it becomes zero immediately. Each entered cell checks exactly four directions. The final nested summation examines all `RC` cells. These contributions give `O(RC)` total time, matching the manifest.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
