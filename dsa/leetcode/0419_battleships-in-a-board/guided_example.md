# Guided Example: Battleships in a Board

We trace the step-by-step top-left anchor identification, local neighbor inspection (top and left), duplicate segment suppression, and single-pass $O(1)$ memory counting on representative naval grid matrices:

- **Input:**
  $$
  board = \begin{bmatrix}
  \text{'X'} & \text{'.'} & \text{'.'} & \text{'X'} \\
  \text{'.'} & \text{'.'} & \text{'.'} & \text{'X'} \\
  \text{'.'} & \text{'.'} & \text{'.'} & \text{'X'}
  \end{bmatrix}
  $$
- **Required output:** `2`
  - Dimensions: $m = 3, n = 4$
  - Cell evaluations:
    - $(0, 0) = \text{'X'}$:
      - Above: out of bounds ($i = 0$)
      - Left: out of bounds ($j = 0$)
      - Both predecessor cells are absent $\implies$ **Anchor of Battleship 1!** $ans \leftarrow 1$
    - $(0, 3) = \text{'X'}$:
      - Above: out of bounds ($i = 0$)
      - Left: $(0, 2) = \text{'.'}$ (not `'X'`)
      - Both predecessor cells are not `'X'` $\implies$ **Anchor of Battleship 2!** $ans \leftarrow 2$
    - $(1, 3) = \text{'X'}$:
      - Above: $(0, 3) = \text{'X'}$ $\implies$ Part of existing vertical ship $\implies$ **Skip**
    - $(2, 3) = \text{'X'}$:
      - Above: $(1, 3) = \text{'X'}$ $\implies$ Part of existing vertical ship $\implies$ **Skip**
    - All other cells are `'.'` $\implies$ **Skip**
  - Total battleships detected: $\mathbf{2}$
- **Horizontal Ship Instance:** $board = [[\text{'X'}, \text{'X'}, \text{'X'}]] \implies (0, 0)$ is anchor ($ans=1$), $(0, 1)$ and $(0, 2)$ skipped $\implies \mathbf{1}$
- **Empty Water Instance:** $board = [[\text{'.'}]] \implies \mathbf{0}$

This instance demonstrates canonical representative anchor counting on grid components, mathematically proves why inspecting only top and left neighbors uniquely enumerates each $1 \times k$ and $k \times 1$ ship, and achieves $O(MN)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ matrix $board$ where cells are either `'X'` (battleship) or `'.'` (water):
Battleships can only be placed horizontally ($1 \times k$) or vertically ($k \times 1$).
No two battleships are adjacent horizontally or vertically (there is always at least one water cell separating distinct ships).
Count the number of battleships on the board **in a single pass, without modifying the board, and using only $O(1)$ extra memory**.

```text
Board (3 rows x 4 columns):

      0    1    2    3
   +----+----+----+----+
 0 | X* | .  | .  | X* |   -> (0,0) is a 1x1 ship; (0,3) is the head of a 3x1 ship
   +----+----+----+----+
 1 | .  | .  | .  | X  |   -> (1,3) continues ship from (0,3)
   +----+----+----+----+
 2 | .  | .  | .  | X  |   -> (2,3) continues ship from (1,3)
   +----+----+----+----+

(* denotes the top-left anchor of each battleship)
Total Battleships: 2
```

### Why Traditional Graph Traversals Fail the Contract
- **DFS / BFS Flood Fill:** Visiting a component and sinking it (modifying `'X' \to '.'`) alters the board, violating the read-only constraint.
- **Visited Matrix:** Allocating a `vis[m][n]` boolean matrix uses $O(MN)$ auxiliary memory, violating the $O(1)$ space requirement.
- **Top-Left Anchor Insight:** Every battleship (whether horizontal or vertical) has exactly **one** cell that is topmost and leftmost. Counting only this unique anchor cell counts every battleship exactly once.

---

## 2. Conceptual Foundation & Invariants

### 1. The Anchor Characterization:
Let cell $(i, j)$ contain an `'X'`:
- If $(i, j)$ belongs to a **vertical** battleship ($k \times 1$):
  - The uppermost cell has no `'X'` above it: $i == 0$ or $board[i-1][j] \ne \text{'X'}$.
  - All subsequent cells below it ($i+1, i+2, \dots$) have an `'X'` directly above.
- If $(i, j)$ belongs to a **horizontal** battleship ($1 \times k$):
  - The leftmost cell has no `'X'` to its left: $j == 0$ or $board[i][j-1] \ne \text{'X'}$.
  - All subsequent cells to its right ($j+1, j+2, \dots$) have an `'X'` directly to the left.

### 2. The Anchor Predicate:
A cell $(i, j)$ is the unique top-left anchor of a battleship if and only if:
$$
board[i][j] == \text{'X'}
$$
$$
\land \quad (i == 0 \lor board[i-1][j] \ne \text{'X'})
$$
$$
\land \quad (j == 0 \lor board[i][j-1] \ne \text{'X'})
$$

> **Bijection Invariant.** There is a strict one-to-one correspondence (bijection) between the set of battleships on the board and the set of cells satisfying the Anchor Predicate.

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 4$ board across all row indices $i \in [0, 2]$ and column indices $j \in [0, 3]$:

---

### Row 0:
- **$(0, 0) = \text{'X'}$:**
  - Above: $i = 0$ (no cell above) $\implies$ Pass.
  - Left: $j = 0$ (no cell to left) $\implies$ Pass.
  - Both tests pass $\implies$ **Anchor #1 found!**
  - $ans \leftarrow 0 + 1 = \mathbf{1}$.
- **Water cells $(0, 1)$ and $(0, 2)$:**
  - Cells contain `'.'` $\implies$ Ignored.
- **$(0, 3) = \text{'X'}$:**
  - Above: $i = 0$ (no cell above) $\implies$ Pass.
  - Left: $(0, 2) = \text{'.'}$ (not `'X'`) $\implies$ Pass.
  - Both tests pass $\implies$ **Anchor #2 found!**
  - $ans \leftarrow 1 + 1 = \mathbf{2}$.

---

### Row 1:
- **Water cells $(1, 0)$, $(1, 1)$, and $(1, 2)$:** Ignored.
- **$(1, 3) = \text{'X'}$:**
  - Above check: $board[1-1][3] = board[0][3] = \text{'X'}$.
  - Preceding cell in same column is `'X'`.
  - Condition fails: $(1, 3)$ is a continuation of a vertical ship, not an anchor.
  - Skip without incrementing $ans$.

---

### Row 2:
- **Water cells $(2, 0)$, $(2, 1)$, and $(2, 2)$:** Ignored.
- **$(2, 3) = \text{'X'}$:**
  - Above check: $board[2-1][3] = board[1][3] = \text{'X'}$.
  - Preceding cell in same column is `'X'`.
  - Condition fails: continuation cell.
  - Skip without incrementing $ans$.

---

### Termination:
All $3 \times 4 = 12$ cells processed. Total anchors counted: $ans = \mathbf{2}$.

---

## 4. Complete Execution Trace

| Coordinate $(i, j)$ | Cell Value | Cell Above $(i-1, j)$ | Cell to Left $(i, j-1)$ | Top-Left Anchor Test | Anchor Decision | Total Ships $ans$ |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| $(0, 0)$ | `'X'` | Out of bounds | Out of bounds | Top edge $\land$ Left edge | **Anchor #1** | **$1$** |
| $(0, 1)$ | `'.'` | — | — | Water cell | Skip | $1$ |
| $(0, 2)$ | `'.'` | — | — | Water cell | Skip | $1$ |
| $(0, 3)$ | `'X'` | Out of bounds | `'.'` | Top edge $\land$ Left is water | **Anchor #2** | **$2$** |
| $(1, 0)$ | `'.'` | — | — | Water cell | Skip | $2$ |
| $(1, 1)$ | `'.'` | — | — | Water cell | Skip | $2$ |
| $(1, 2)$ | `'.'` | — | — | Water cell | Skip | $2$ |
| $(1, 3)$ | `'X'` | **`'X'`** | `'.'` | **Above is `'X'` (Vertical body)** | **Skip** | $2$ |
| $(2, 0)$ | `'.'` | — | — | Water cell | Skip | $2$ |
| $(2, 1)$ | `'.'` | — | — | Water cell | Skip | $2$ |
| $(2, 2)$ | `'.'` | — | — | Water cell | Skip | $2$ |
| $(2, 3)$ | `'X'` | **`'X'`** | `'.'` | **Above is `'X'` (Vertical body)** | **Skip** | **$2$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Cell Board ($board = [[\text{'X'}]]$):** Both above and left are out of bounds. Correctly identified as anchor $\implies \mathbf{1}$.
- **All Water Board ($board = [[\text{'.'}, \text{'.'}]]$):** No `'X'` exists $\implies \mathbf{0}$.
- **Adjacent Battleships Invariant:** The problem guarantees no two battleships touch each other (not even diagonally or adjacently). If diagonal touches were allowed, connected component algorithms would be required; under the problem contract, checking only immediate orthogonal predecessors is provably sufficient.
- **Ship Touching Right/Bottom Borders:** Handled naturally because the anchor is strictly on the top-left; right and bottom boundaries never interfere with anchor detection.

---

## 6. Traps & Common Anti-Patterns

- **Mutating the Input Grid:** Overwriting visited `'X'` with `'.'` destroys the input data, which violates common API contracts and testing harnesses.
- **Checking All 4 Neighbors:** Looking right and down is unnecessary and leads to double-counting or needing a visited set. Checking only the past (top and left) ensures decisions are made strictly on already-scanned predecessor state.
- **Index Out-of-Bounds:** Forgetting to guard $i > 0$ and $j > 0$ before accessing $board[i-1][j]$ or $board[i][j-1]$ causes index errors on boundary rows/columns.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The algorithm iterates over each of the $M \times N$ cells exactly once.
  - For each cell, at most two neighbor lookups are performed in $O(1)$ time.
  - Total Time: $\mathcal{O}(M \cdot N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. The algorithm maintains only a single integer accumulator $ans$ and loop index counters. Zero heap allocations or recursion stacks.
