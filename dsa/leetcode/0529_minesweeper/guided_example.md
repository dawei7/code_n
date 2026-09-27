# Guided Example: Minesweeper

We trace the step-by-step click event dispatch, direct mine detonation handling ($'M' \to 'X'$), 8-directional Moore neighborhood adjacency mine counting ($\sum \mathbf{1}[\text{neighbor} == \text{'M'}] \in [0, 8]$), digit boundary freezing ($'1' \dots '8'$), and recursive blank flood-fill expansion ($'E' \to 'B'$) on representative grid layouts:

- **Input:**
  - Board dimensions: $4 \times 5$
  - Initial matrix:
    $$
    board = \begin{bmatrix}
    E & E & E & E & E \\
    E & E & M & E & E \\
    E & E & E & E & E \\
    E & E & E & E & E
    \end{bmatrix}
    $$
  - User click coordinate: $click = [3, 0]$ (bottom-left corner)
- **Required output:**
  $$
  \begin{bmatrix}
  B & 1 & E & 1 & B \\
  B & 1 & M & 1 & B \\
  B & 1 & 1 & 1 & B \\
  B & B & B & B & B
  \end{bmatrix}
  $$
- **Minesweeper Rule Engine:**
  1. If clicked cell is a mine (`'M'`), change it to `'X'` (Game Over).
  2. If clicked cell is empty (`'E'`), count all adjacent mines in its 8 surrounding Moore neighbors.
  3. If adjacent mine count $cnt > 0$, label the cell with digit string $\text{str}(cnt)$ and **halt expansion** along this path.
  4. If adjacent mine count $cnt == 0$, label the cell with blank `'B'` and **recursively reveal** all adjacent unrevealed empty squares (`'E'`).
- **Flood fill execution trace from $click = [3, 0]$:**
  - **Step 1 (Visit $(3, 0)$):**
    - Inspect 8 neighbors of $(3, 0)$: $(2, 0), (2, 1), (3, 1)$.
    - None of these are mines $\implies cnt = 0$.
    - Mark $board[3][0] \leftarrow \mathbf{\text{'B'}}$.
    - Recursively explore unrevealed neighbors $(2, 0), (2, 1), (3, 1)$.
  - **Step 2 (Explore Region Bottom Row $i = 3$):**
    - Cell $(3, 1)$: neighbors have no mines $\implies$ becomes `'B'`.
    - Cell $(3, 2)$: neighbors contain $(2, 1), (2, 2), (2, 3), (3, 1), (3, 3)$.
      - Notice: Mine is at $(1, 2)$. Distance from $(3, 2)$ is $\Delta r = 2$, which is outside the 1-hop Moore neighborhood ($\max(|\Delta r|, |\Delta c|) \le 1$).
      - Neighbors of $(3, 2)$ have 0 mines $\implies$ becomes `'B'`.
    - Cells $(3, 3)$ and $(3, 4)$ have no adjacent mines $\implies$ become `'B'`.
  - **Step 3 (Explore Row $i = 2$ Around the Mine at $(1, 2)$):**
    - Cell $(2, 1)$:
      - Neighbors: includes cell $(1, 2)$, which is a mine (`'M'`)!
      - Total adjacent mines: $cnt = \mathbf{1}$.
      - Since $cnt > 0$, write digit:
        $$
        board[2][1] \leftarrow \mathbf{\text{'1'}}
        $$
      - **Halt expansion from $(2, 1)$!** Do not recurse into its neighbors.
    - Cell $(2, 2)$:
      - Adjacent to mine directly above it at $(1, 2)$ $\implies cnt = \mathbf{1}$.
      - Mark $board[2][2] \leftarrow \mathbf{\text{'1'}}$. Halt expansion!
    - Cell $(2, 3)$:
      - Adjacent diagonally to mine at $(1, 2)$ $\implies cnt = \mathbf{1}$.
      - Mark $board[2][3] \leftarrow \mathbf{\text{'1'}}$. Halt expansion!
  - **Step 4 (Explore Columns 0 and 4):**
    - Left column: $(1, 0)$ has $cnt = 0 \implies \text{'B'}$; $(0, 0)$ has $cnt = 0 \implies \text{'B'}$.
    - Right column: $(1, 4)$ has $cnt = 0 \implies \text{'B'}$; $(0, 4)$ has $cnt = 0 \implies \text{'B'}$.
  - **Step 5 (Boundary Cells Next to $(1, 2)$):**
    - $(0, 1)$ touches mine $(1, 2) \implies$ becomes `'1'`.
    - $(1, 1)$ touches mine $(1, 2) \implies$ becomes `'1'`.
    - $(1, 3)$ touches mine $(1, 2) \implies$ becomes `'1'`.
    - $(0, 3)$ touches mine $(1, 2) \implies$ becomes `'1'`.
    - $(0, 2)$ is adjacent to mine $(1, 2)$ directly below it, but was never visited because all perimeter paths halted at `'1'` digits!
      It remains unrevealed empty `'E'`.
  - Final revealed board matches expected matrix.
- **Direct Mine Click Instance ($click = [1, 2]$):**
  - $board[1][2] == \text{'M'} \implies board[1][2] \leftarrow \mathbf{\text{'X'}}$ immediately $\implies$ Game over.

This instance demonstrates cellular automaton flood-fill with perimeter threshold boundaries, mathematically proves why numerical cells act as recursive firewalls preventing unearned reveals, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a 2D character grid $board$ representing a Minesweeper board:
- `'M'` represents an unrevealed mine.
- `'E'` represents an unrevealed empty square.
- `'B'` represents a revealed blank square with 0 adjacent mines.
- `'1'` to `'8'` represent revealed squares with that many adjacent mines.
- `'X'` represents a detonated mine.
Process a user click at coordinate $[i, j]$ according to Minesweeper rules and return the updated board.

```text
Board with Mine at (1, 2):
  [ E,  E,  E,  E,  E ]
  [ E,  E, [M], E,  E ]
  [ E,  E,  E,  E,  E ]
  [ E,  E,  E,  E,  E ]

Click at (3, 0):
  (3, 0) has 0 mines nearby -> Expands as 'B'!
  Blank area cascades until it touches squares adjacent to (1, 2).
  Squares adjacent to (1, 2) become '1' and STOP the cascade.
```

### The Perimeter Firewall Principle
In Minesweeper:
- Blank squares (`'B'`) have zero adjacent mines. They are completely safe and propagate the flood-fill recursively in all 8 directions.
- Numbered squares (`'1'` through `'8'`) border at least one mine.
- **Numbered squares act as firewalls**: they reveal their count, but **they do not propagate the search further**!
- This ensures that empty spaces on the other side of a mine are never accidentally revealed without direct player interaction.

---

## 2. Conceptual Foundation & Invariants

### 1. Moore Neighborhood (8 Directions):
For cell $(i, j)$, its neighbors $(x, y)$ satisfy:
$$
x \in [i-1, i+1], \quad y \in [j-1, j+1], \quad (x, y) \ne (i, j)
$$
constrained to valid grid coordinates $0 \le x < m$ and $0 \le y < n$.

### 2. State Transition Function $dfs(i, j)$:
1. Count surrounding mines:
   $$
   cnt = \sum_{(x, y) \in \text{Neighbors}(i, j)} \mathbf{1}[board[x][y] == \text{'M'}]
   $$
2. **If $cnt > 0$:**
   $$
   board[i][j] \leftarrow \text{str}(cnt)
   $$
   Halt search on this branch.
3. **If $cnt == 0$:**
   $$
   board[i][j] \leftarrow \text{'B'}
   $$
   For each neighbor $(x, y)$:
   If $board[x][y] == \text{'E'}$, invoke $dfs(x, y)$.

> **Reveal Termination Invariant.** A cell changes from `'E'` to `'B'` if and only if all 8 neighbors are mine-free; otherwise it becomes a terminating digit in $\{'1', \dots, '8'\}$, strictly confining flood-fill to connected zero-density components.

---

## 3. Step-by-Step Worked Execution

We trace $click = [3, 0]$ with mine at $(1, 2)$:

---

### Step 1: Initial Click Check
- $board[3][0] = \text{'E'} \ne \text{'M'}$.
- Invoke $dfs(3, 0)$.

---

### Step 2: Evaluate $(3, 0)$
- Neighbors of $(3, 0)$: $(2, 0), (2, 1), (3, 1)$.
- Count of mines in neighbors: $cnt = 0$.
- Mark $board[3][0] = \mathbf{\text{'B'}}$.
- Recurse into unrevealed empty neighbors.

---

### Step 3: Cascading Flood-Fill on Row 3 and Row 2
- $(3, 1) \to cnt = 0 \implies \text{'B'}$.
- $(3, 2) \to cnt = 0 \implies \text{'B'}$.
- $(3, 3) \to cnt = 0 \implies \text{'B'}$.
- $(3, 4) \to cnt = 0 \implies \text{'B'}$.

---

### Step 4: Encountering Perimeter Cells
- **Inspect $(2, 1)$:**
  - Moore neighbors include $(1, 2)$, which is `'M'`.
  - Mine count: $cnt = 1$.
  - Assign digit:
    $$
    board[2][1] \leftarrow \mathbf{\text{'1'}}
    $$
  - Do NOT recurse.
- **Inspect $(2, 2)$:**
  - Directly below mine at $(1, 2)$.
  - $cnt = 1 \implies board[2][2] \leftarrow \mathbf{\text{'1'}}$. Stop.
- **Inspect $(2, 3)$:**
  - Diagonally below mine at $(1, 2)$.
  - $cnt = 1 \implies board[2][3] \leftarrow \mathbf{\text{'1'}}$. Stop.

---

### Step 5: Complete Upper and Corner Branches
- Column 0 and Column 4 propagate blanks `'B'` upwards.
- Cells $(1, 1), (0, 1), (1, 3), (0, 3)$ touch $(1, 2) \implies$ each becomes `'1'`.
- Cell $(0, 2)$ is shielded behind the `'1'` border $\implies$ remains unvisited `'E'`.

---

## 4. Complete Execution Trace

| Cell Visited $(i, j)$ | Adjacent Mines Count $cnt$ | New State Assigned | Recurse to Neighbors? | Explanation |
|:---:|:---:|:---:|:---:|:---|
| $(3, 0)$ | $0$ | `'B'` | Yes | Safe blank square |
| $(3, 1)$ | $0$ | `'B'` | Yes | Safe blank square |
| $(2, 1)$ | $1$ | **`'1'`** | **No** | **Border firewall: adjacent to $(1, 2)$** |
| $(2, 2)$ | $1$ | **`'1'`** | **No** | **Border firewall: adjacent to $(1, 2)$** |
| $(2, 3)$ | $1$ | **`'1'`** | **No** | **Border firewall: adjacent to $(1, 2)$** |
| $(1, 0)$ | $0$ | `'B'` | Yes | Safe blank square |
| $(1, 1)$ | $1$ | **`'1'`** | **No** | Border firewall |
| $(1, 2)$ | — | `'M'` | — | Unclicked mine (untouched) |

---

## 5. Boundary Cases & Failure Modes

- **Direct Mine Click ($click == [r_m, c_m]$):** Immediately changes that cell to `'X'` and returns without revealing any other cell.
- **Clicking a Square Already Adjacent to a Mine:** If the player clicks $(2, 1)$ directly, $cnt = 1 \implies$ turns into `'1'` and halts immediately without revealing any blanks.
- **Entire Board Mine-Free:** Cascades across all $m \times n$ squares $\implies$ all become `'B'`.
- **Corner or Edge Clicks:** Coordinate clamping $0 \le x < m, 0 \le y < n$ prevents array out-of-bounds.

---

## 6. Traps & Common Anti-Patterns

- **Checking 4 Directions Instead of 8:** Minesweeper uses Moore neighborhoods (8 directions, including all 4 diagonals). Diagonal mines must be counted.
- **Recursing from Numbered Cells:** Continuing the DFS from a cell with $cnt > 0$ reveals cells through mine boundaries, destroying the game mechanics.
- **Re-visiting Already Revealed Cells:** Guarding recursion with `board[x][y] == 'E'` prevents infinite cycles between adjacent blank squares.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In the worst case (all empty), each of the $M \times N$ squares is visited at most once.
  - At each square, checking its 8 neighbors takes $O(1)$ operations.
  - Total Time: $\mathcal{O}(M \cdot N)$. For a $50 \times 50$ board, finishes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ recursion call stack space in the worst-case snake cascade.
