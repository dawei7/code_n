# Guided Example: Bomb Enemy

We trace the step-by-step 4-directional line-of-sight prefix/suffix accumulation (Left, Right, Down, Up), wall-resetting enemy counters (`grid[i][j] == 'W' \implies t = 0`), empty-cell bomb placement filtering (`grid[i][j] == '0'`), and maximum enemy kill extraction on representative grid instances:

- **Input:** `grid = [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]`
- **Required output:** $3$
  - Placing a bomb at cell $(1, 1)$ (which is empty `'0'`):
    - Looking Left: kills enemy at $(1, 0)$ $\implies 1$ kill
    - Looking Right: blocked by wall `'W'` at $(1, 2)$, cannot reach enemy at $(1, 3)$ $\implies 0$ kills
    - Looking Up: kills enemy at $(0, 1)$ $\implies 1$ kill
    - Looking Down: kills enemy at $(2, 1)$ $\implies 1$ kill
    - Total enemy kills from cell $(1, 1)$: $1 + 0 + 1 + 1 = \mathbf{3}$
  - Comparison with other empty cells:
    - $(0, 0) \implies$ kills $(0, 1)$ and $(1, 0) \implies 2$
    - $(0, 2) \implies$ kills $(0, 1) \implies 1$
    - $(0, 3) \implies$ kills $(0, 1) \implies 1$
    - Maximum kills achievable: $\mathbf{3}$
- **All Wall Grid:** Every cell is `'W'` or no empty cells $\implies$ returns $0$
- **Unobstructed Line:** Single row `["E", "0", "E", "0", "E"]` allows bombing at $(0, 1)$ to kill all 3 enemies

This instance demonstrates 4-way prefix-sum matrix precomputation, proves how wall-bounded cumulative scans reduce $O(M \cdot N \cdot (M + N))$ brute-force rays to strictly $O(M \cdot N)$ linear time, and analyzes grid memory bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ matrix `grid` ($m = 3, n = 4$):
- `'0'`: Empty cell where a bomb may be planted.
- `'E'`: Enemy.
- `'W'`: Indestructible wall that completely blocks bomb blast propagation.
A bomb detonates along its entire row and column, terminating at walls or grid edges.
Find the maximum number of enemies destroyed by planting a single bomb in an **empty cell** (`'0'`):

```text
Grid Map (m=3, n=4):
Row 0:  [ 0,  E,  0,  0 ]
Row 1:  [ E,  B,  W,  E ]  <-- Plant Bomb at (1, 1)!
Row 2:  [ 0,  E,  0,  0 ]

Blast Rays from B at (1, 1):
  Up:    hits (0, 1) [Enemy]
  Down:  hits (2, 1) [Enemy]
  Left:  hits (1, 0) [Enemy]
  Right: stopped by Wall at (1, 2) -> (1, 3) protected!

Total Enemies Destroyed: 3
```

---

## 2. Conceptual Foundation & Invariants

### 1. The 4 Sweep Accumulator Matrix `g[m][n]`
Instead of casting rays from every empty cell (which costs $O(M + N)$ per cell, yielding $O(MN(M+N))$), we precalculate enemy coverage using **4 linear directional sweeps**:
1. **Left-to-Right Row Sweep:** Tracks enemies seen from the left, resetting to $0$ on `'W'`.
2. **Right-to-Left Row Sweep:** Tracks enemies seen from the right, resetting to $0$ on `'W'`.
3. **Top-to-Bottom Column Sweep:** Tracks enemies seen from above, resetting to $0$ on `'W'`.
4. **Bottom-to-Top Column Sweep:** Tracks enemies seen from below, resetting to $0$ on `'W'`.

### 2. Accumulation Protocol:
Initialize table $g = [[0] \times n \text{ for } \dots]$.
For each directional pass:
- Maintain running counter $t = 0$.
- For each visited cell:
  - If cell is `'W'`: $t \leftarrow 0$
  - If cell is `'E'`: $t \leftarrow t + 1$
  - Accumulate: $g[i][j] \mathrel{+}= t$

### 3. Final Candidate Filtering:
Select the maximum $g[i][j]$ exclusively among valid bomb placement sites:
$$
\text{Max Kills} = \max \big(\{g[i][j] \mid grid[i][j] == \text{'0'}\} \cup \{0\}\big)
$$

> **Invariant.** For any cell $(i, j)$, $g[i][j]$ after the 4 sweeps accurately stores the total count of enemies visible along row $i$ and column $j$ unobstructed by walls.

---

## 3. Step-by-Step Worked Execution

We trace the 4 directional sweeps on our $3 \times 4$ grid:

---

### Step 1: Horizontal Sweeps (Row by Row)
Focusing on Row 1: `['E', '0', 'W', 'E']`:
- **Left-to-Right ($j = 0 \dots 3$):**
  - $j = 0$ (`'E'`): $t = 1 \implies g[1][0] \mathrel{+}= 1$.
  - $j = 1$ (`'0'`): $t = 1 \implies g[1][1] \mathrel{+}= 1$.
  - $j = 2$ (`'W'`): Wall resets counter $\implies t = 0 \implies g[1][2] \mathrel{+}= 0$.
  - $j = 3$ (`'E'`): $t = 1 \implies g[1][3] \mathrel{+}= 1$.
- **Right-to-Left ($j = 3 \dots 0$):**
  - $j = 3$ (`'E'`): $t = 1 \implies g[1][3] \mathrel{+}= 1$.
  - $j = 2$ (`'W'`): Wall resets counter $\implies t = 0$.
  - $j = 1$ (`'0'`): $t = 0 \implies g[1][1] \mathrel{+}= 0$.
  - $j = 0$ (`'E'`): $t = 0 \implies g[1][0] \mathrel{+}= 0$.
- **Row 1 Horizontal Contribution to $(1, 1)$:** $1 + 0 = \mathbf{1}$ (Only $(1, 0)$ is reachable).

---

### Step 2: Vertical Sweeps (Column by Column)
Focusing on Column 1: `['E', '0', 'E']`:
- **Top-to-Bottom ($i = 0 \dots 2$):**
  - $i = 0$ (`'E'`): $t = 1 \implies g[0][1] \mathrel{+}= 1$.
  - $i = 1$ (`'0'`): $t = 1 \implies g[1][1] \mathrel{+}= 1$.
  - $i = 2$ (`'E'`): $t = 2 \implies g[2][1] \mathrel{+}= 2$.
- **Bottom-to-Top ($i = 2 \dots 0$):**
  - $i = 2$ (`'E'`): $t = 1 \implies g[2][1] \mathrel{+}= 1$.
  - $i = 1$ (`'0'`): $t = 1 \implies g[1][1] \mathrel{+}= 1$.
  - $i = 0$ (`'E'`): $t = 2 \implies g[0][1] \mathrel{+}= 2$.
- **Column 1 Vertical Contribution to $(1, 1)$:** $1 + 1 = \mathbf{2}$ (Enemies at $(0, 1)$ and $(2, 1)$).

---

### Step 3: Total Score at Candidate Cell $(1, 1)$
Sum of 4 directional sweeps for cell $(1, 1)$:
$$
g[1][1] = \text{Left}(1) + \text{Right}(0) + \text{Up}(1) + \text{Down}(1) = \mathbf{3}
$$

---

### Step 4: Evaluate All Empty Cells
Evaluating $g[i][j]$ for all $(i, j)$ where $grid[i][j] == \text{'0'}$:
- $g[0][0] = 2$ (hits $(0, 1)$ and $(1, 0)$)
- $g[0][2] = 1$ (hits $(0, 1)$)
- $g[0][3] = 1$ (hits $(0, 1)$)
- $g[1][1] = \mathbf{3}$ (hits $(1, 0), (0, 1), (2, 1)$)
- $g[2][0] = 2$ (hits $(2, 1)$ and $(1, 0)$)
- $g[2][2] = 1$ (hits $(2, 1)$)
- $g[2][3] = 1$ (hits $(2, 1)$)

Maximum kills:
$$
\max(g[i][j]) = \mathbf{3}
$$

---

## 4. Complete Execution Trace

```text
Directional Blast Breakdown for Target Cell (1, 1):
1. Left sweep   : 'E' at (1, 0)               -> +1
2. Right sweep  : blocked by 'W' at (1, 2)     -> +0
3. Down sweep   : 'E' at (0, 1)               -> +1
4. Up sweep     : 'E' at (2, 1)               -> +1

Sum for Cell (1, 1) = 1 + 0 + 1 + 1 = 3 (Maximum across all '0' cells)
```

| Empty Cell $(i, j)$ | Left Enemies | Right Enemies | Top Enemies | Bottom Enemies | Total Score $g[i][j]$ | Is Maximum? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | 0 | 1 | 0 | 1 | 2 | No |
| $(0, 2)$ | 1 | 0 | 0 | 0 | 1 | No |
| $(0, 3)$ | 1 | 0 | 0 | 0 | 1 | No |
| **$(1, 1)$** | **1** | **0** | **1** | **1** | **$\mathbf{3}$** | **Yes (Optimal Bomb)** |
| $(2, 0)$ | 0 | 1 | 0 | 0 | 1 | No |
| $(2, 2)$ | 1 | 0 | 0 | 0 | 1 | No |
| $(2, 3)$ | 1 | 0 | 0 | 0 | 1 | No |

---

## 5. Algorithmic Correctness

**Soundness.** A bomb kills enemies in four cardinal directions until stopped by a wall or grid border. Because walls reset the running prefix/suffix counter $t$ to $0$, no enemy located on the far side of a wall is added to $g[i][j]$. Summing the four directional counters accurately aggregates the exact number of enemies directly visible from $(i, j)$.

**Completeness.** Every row is swept left-to-right and right-to-left, and every column is swept top-to-bottom and bottom-to-top. All possible empty cells `'0'` are filtered and compared, guaranteeing that the global maximum kill count is discovered.

---

## 6. Traps This Instance Exposes

- **Placing Bomb on Non-Empty Cell:** Bombs can **only** be placed on empty cells (`'0'`). An enemy cell `'E'` might have a high score $g[i][j]$, but placing a bomb on top of an enemy is strictly forbidden.
- **Blast Blocked by Walls:** An enemy behind a wall (such as $(1, 3)$ behind wall $(1, 2)$) cannot be hit by a bomb at $(1, 1)$. Resetting $t = 0$ on `'W'` correctly handles wall occlusion.
- **No Valid Empty Cells:** If the entire grid contains only walls and enemies, no bomb can be placed. The `default=0` parameter in Python's `max()` ensures safe return of $0$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns.
  - Two horizontal sweeps over $M$ rows take $2 \times M \times N = O(MN)$ operations.
  - Two vertical sweeps over $N$ columns take $2 \times N \times M = O(MN)$ operations.
  - Final maximum scan over all cells takes $O(MN)$ operations.
  - Total runtime is strictly $O(MN)$, optimal for matrix processing.
- **Auxiliary Space Complexity:** $O(M \cdot N)$ auxiliary space for the cumulative matrix $g$.
