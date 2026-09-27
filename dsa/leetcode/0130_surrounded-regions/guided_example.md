# Guided Example: Surrounded Regions

We trace the step-by-step boundary flood-fill inversion and in-place two-phase cell marking on a representative 2D grid:

- **Input:**
  $$
  \text{board} = \begin{bmatrix}
  \text{X} & \text{X} & \text{X} & \text{X} \\
  \text{X} & \text{O} & \text{O} & \text{X} \\
  \text{X} & \text{X} & \text{O} & \text{X} \\
  \text{X} & \text{O} & \text{X} & \text{X}
  \end{bmatrix}
  $$
- **Required output:**
  $$
  \begin{bmatrix}
  \text{X} & \text{X} & \text{X} & \text{X} \\
  \text{X} & \text{X} & \text{X} & \text{X} \\
  \text{X} & \text{X} & \text{X} & \text{X} \\
  \text{X} & \text{O} & \text{X} & \text{X}
  \end{bmatrix}
  $$
- **Degenerate Single-Cell Base:** $\text{board} = [[\text{"X"}]] \implies [[\text{"X"}]]$

This instance demonstrates inverting the problem (identifying un-capturable border-connected components rather than proving interior enclosure), temporary sentinel masking (`#`) in $O(1)$ extra space, and executing a dual-pass grid sweep to capture true surrounded regions.

---

## 1. Instance & Teaching Goal

You are given an $m \times n$ matrix `board` containing letters `'X'` and `'O'`.
Capture all regions that are 4-directionally surrounded by `'X'`. An `'O'` cell is surrounded if there is no path of adjacent `'O'` cells connecting it to any boundary of the board.

In the $4 \times 4$ instance:
- The `'O'` at row 3, column 1 (`board[3][1]`) lies directly on the bottom border. Because it touches the boundary, its region can never be surrounded.
- The three `'O'` cells at $(1, 1), (1, 2),$ and $(2, 2)$ form an interior cluster enclosed on all four orthogonal sides by `'X'`.
- After capturing, the interior cluster becomes `'X'`, while the boundary-connected `'O'` remains `'O'`.

Directly testing whether an arbitrary interior `'O'` is surrounded requires full component search while tracking boundary escape flags.
Inverting the logic provides an optimal solution:
**Start from all perimeter border cells**. Any `'O'` connected to the perimeter is permanently immune from capture. We mark these safe cells with a temporary marker, flip all remaining `'O'`s to `'X'`, and restore the safe marker back to `'O'`.

---

## 2. Conceptual Foundation & Invariants

### Two-Phase Boundary Inversion Protocol
Let $M$ be the number of rows and $N$ the number of columns.

#### Phase 1: Perimeter Flood-Fill (Mark Immune Cells)
1. Traverse all perimeter cells:
   - First and last rows ($r = 0$ and $r = M - 1$) for all $c \in [0, N - 1]$.
   - First and last columns ($c = 0$ and $c = N - 1$) for all $r \in [0, M - 1]$.
2. For any perimeter cell where $\text{board}[r][c] == \text{'O'}$:
   - Initiate DFS / BFS:
     - Mutate current cell to temporary sentinel: $\text{board}[r][c] \leftarrow \text{'\#'}$.
     - Recursively explore all 4 orthogonal neighbors $(r \pm 1, c)$ and $(r, c \pm 1)$.
     - Continue flood-filling as long as neighbors are inside bounds and contain `'O'`.

#### Phase 2: Board Sweep (Capture & Restore)
Iterate through every cell $(r, c)$ in the matrix:
- If $\text{board}[r][c] == \text{'O'}$:
  This cell was never reached from any border; it is surrounded.
  $$
  \text{board}[r][c] \leftarrow \text{'X'}
  $$
- If $\text{board}[r][c] == \text{'\#'}$:
  This cell was marked safe during Phase 1. Restore it:
  $$
  \text{board}[r][c] \leftarrow \text{'O'}
  $$

> **Invariant.** After Phase 1, a cell contains `board[r][c] == '#'` if and only if there exists a path of adjacent `'O'` cells connecting $(r, c)$ to the grid's outer boundary.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on the $4 \times 4$ board ($M = 4, N = 4$):

### Phase 1: Boundary Inspection

#### Row 0 (Top Boundary):
- `board[0][0...3] = ['X', 'X', 'X', 'X']`. No `'O'` cells.

#### Row 3 (Bottom Boundary):
- $c = 0$: `'X'`.
- $c = 1$: `'O'` found at $(3, 1)$!
  - **Launch DFS from $(3, 1)$:**
    - Mark safe: $\text{board}[3][1] \leftarrow \text{'\#'}$.
    - Check neighbor $(2, 1)$: $\text{board}[2][1] = \text{'X'}$ (blocked).
    - Check neighbor $(3, 0)$: $\text{board}[3][0] = \text{'X'}$ (blocked).
    - Check neighbor $(3, 2)$: $\text{board}[3][2] = \text{'X'}$ (blocked).
    - DFS completes for $(3, 1)$.
- $c = 2, 3$: `'X'`.

#### Column 0 (Left Boundary) & Column 3 (Right Boundary):
- All entries on left and right columns are `'X'`.

State of grid after Phase 1:
$$
\begin{bmatrix}
\text{X} & \text{X} & \text{X} & \text{X} \\
\text{X} & \text{O} & \text{O} & \text{X} \\
\text{X} & \text{X} & \text{O} & \text{X} \\
\text{X} & \mathbf{\#} & \text{X} & \text{X}
\end{bmatrix}
$$

---

### Phase 2: Full Grid Sweep

We scan every row $r \in [0, 3]$ and column $c \in [0, 3]$:
- Cell $(1, 1)$: contains `'O'`. Never reached from border $\implies$ Flip to $\text{'X'}$.
- Cell $(1, 2)$: contains `'O'`. Never reached from border $\implies$ Flip to $\text{'X'}$.
- Cell $(2, 2)$: contains `'O'`. Never reached from border $\implies$ Flip to $\text{'X'}$.
- Cell $(3, 1)$: contains sentinel `'\#'`. Immune border node $\implies$ Restore to $\text{'O'}$.
- All other cells contain `'X'` $\implies$ Unchanged.

Final board:
$$
\begin{bmatrix}
\text{X} & \text{X} & \text{X} & \text{X} \\
\text{X} & \mathbf{X} & \mathbf{X} & \text{X} \\
\text{X} & \text{X} & \mathbf{X} & \text{X} \\
\text{X} & \mathbf{O} & \text{X} & \text{X}
\end{bmatrix}
$$

---

## 4. Complete Execution Trace

```text
Initial Board:               Phase 1 (Border Flood):      Phase 2 (Capture & Restore):
  X  X  X  X                   X  X  X  X                   X  X  X  X
  X  O  O  X                   X  O  O  X                   X [X][X] X
  X  X  O  X                   X  X  O  X                   X  X [X] X
  X  O  X  X                   X [#] X  X                   X [O] X  X
```

| Phase | Cell Coordinate $(r, c)$ | Initial Cell State | Connected to Border? | Sentinel Action | Final Assigned Value |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $(3, 1)$ | `'O'` (Bottom border) | **Yes** | Mutate to `'#'` | `'#'` (Temporary) |
| 2 | $(1, 1)$ | `'O'` | No | Not reachable | **`'X'` (Captured)** |
| 2 | $(1, 2)$ | `'O'` | No | Not reachable | **`'X'` (Captured)** |
| 2 | $(2, 2)$ | `'O'` | No | Not reachable | **`'X'` (Captured)** |
| 2 | $(3, 1)$ | `'#'` | Yes | Restore from `'#'` | **`'O'` (Preserved)** |
| All | All other cells | `'X'` | - | Ignored | `'X'` |

### Region Connectivity Census

Each `'O'` in the instance, its four-directional component, and the reason for its fate:

| Cell $(r, c)$ | On the perimeter? | Orthogonal `'O'` neighbours | Four-directional component | Reaches a perimeter `'O'`? | Fate after Phase 2 |
|:---:|:---:|:---|:---|:---:|:---|
| $(1, 1)$ | No | $(1, 2)$ | $\{(1, 1), (1, 2), (2, 2)\}$ | No | Captured to `'X'` |
| $(1, 2)$ | No | $(1, 1)$, $(2, 2)$ | $\{(1, 1), (1, 2), (2, 2)\}$ | No | Captured to `'X'` |
| $(2, 2)$ | No | $(1, 2)$ | $\{(1, 1), (1, 2), (2, 2)\}$ | No | Captured to `'X'` |
| $(3, 1)$ | **Yes** (bottom row) | none — all three in-bounds neighbours are `'X'` | $\{(3, 1)\}$ | **Yes**, it is itself the source | Restored to `'O'` |

The three-cell component has no cell on the perimeter and its only boundary contact is with `'X'`, so the flood fill launched at $(3, 1)$ never reaches it. Note that the fill from $(3, 1)$ terminates immediately: its other neighbours $(3, 0)$ and $(3, 2)$ are `'X'`, so exactly one cell carries the `'#'` sentinel into Phase 2.

---

## 5. Algorithmic Correctness

**Soundness.** By definition, a region is surrounded if and only if none of its cells can reach the board perimeter via horizontal or vertical adjacent `'O'` steps. Because Phase 1 flood-fills from all perimeter `'O'`s, every un-surrounded cell is marked with `'#'`. Any remaining `'O'` cell in Phase 2 is mathematically guaranteed to be fully enclosed by `'X'`s, justifying its transformation into `'X'`.

**Completeness.** Perimeter scanning covers all four boundaries. DFS visits all connected components of safe cells. The final matrix scan visits every cell in the grid, ensuring no interior region escapes capture and no immune cell is erroneously overwritten.

---

## 6. Traps This Instance Exposes

- **Checking Boundaries from Interior Outward:** Exploring from each interior `'O'` to see if it reaches the boundary requires tracking visited sets and rolling back marks if a boundary is touched. Flood-filling from the perimeter inward eliminates all backtracking and edge-casing.
- **Using External Visited Matrices:** Allocating a visited boolean grid of size $M \times N$ uses $O(M \cdot N)$ auxiliary space. Mutating `board[r][c]` directly to `'#'` achieves in-place state tracking with $O(1)$ extra space.
- **Grid Dimensions Less Than 3:** If $M < 3$ or $N < 3$, every cell is on the perimeter or adjacent to it; no cell can be strictly surrounded. The algorithm naturally preserves all `'O'`s in such matrices.

### Boundary and Degenerate Instances

| Instance | Input condition | Expected | Why the two phases produce it |
|:---|:---|:---|:---|
| The $4 \times 4$ board of this lesson | One interior cluster of three `'O'`s plus one border `'O'` | Only $(1, 1)$, $(1, 2)$, $(2, 2)$ become `'X'` | The fill source $(3, 1)$ is isolated by `'X'`, so the interior cluster is never marked and is captured, while $(3, 1)$ is restored. |
| $\text{board} = [[\text{"X"}]]$ | A single cell, $M = N = 1$ | Unchanged | The cell is examined once as the whole top row and once as the whole left column; being `'X'` it launches no fill, and the sweep finds nothing to change. |
| $\text{board} = [[\text{"O"}, \text{"O"}], [\text{"O"}, \text{"O"}]]$ | $M = N = 2 < 3$, so no cell is interior | Unchanged | The fill started at $(0, 0)$ marks all four cells, and Phase 2 restores each sentinel to `'O'` instead of capturing it. |
| The $5 \times 5$ trial board | A four-cell border-connected chain, two isolated border `'O'`s, and one interior `'O'` at $(3, 3)$ | Only $(3, 3)$ becomes `'X'` | The chain $(0, 1) \to (1, 1) \to (1, 2) \to (2, 2)$ and the isolated cells $(2, 4)$ and $(3, 0)$ all touch a border, whereas $(3, 3)$ has four `'X'` neighbours. |
| $\text{board} = [[\text{"O"}, \text{"X"}, \text{"X"}], [\text{"X"}, \text{"O"}, \text{"X"}], [\text{"X"}, \text{"X"}, \text{"O"}]]$ | Three `'O'`s touching only diagonally | The centre becomes `'X'`; both corners stay `'O'` | The centre $(1, 1)$ has four `'X'` neighbours, and diagonal contact with $(0, 0)$ and $(2, 2)$ transmits no immunity because adjacency is four-directional. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M \times N$ is the grid size. Each cell is visited at most twice: once during the perimeter DFS flood-fill and once during the final grid sweep.
- **Auxiliary Space Complexity:** $O(M \cdot N)$ worst-case call stack depth for DFS recursion (or $O(\min(M, N))$ queue memory if implemented via BFS). Modifying the board in place uses $O(1)$ extra heap memory.
