# Guided Example: Search a 2D Matrix II

We trace the step-by-step top-right corner saddleback search, row/column dimensional elimination, and boundary termination on representative row-and-column sorted matrices:

- **Input:**
  $$
  \text{matrix} = \begin{bmatrix}
  1 & 4 & 7 & 11 & 15 \\
  2 & 5 & 8 & 12 & 19 \\
  3 & 6 & 9 & 16 & 22 \\
  10 & 13 & 14 & 17 & 24 \\
  18 & 21 & 23 & 26 & 30
  \end{bmatrix}, \quad \text{target} = 5
  $$
- **Required output:** `true` (Located at row $1$, column $1$)
- **Absent Target Instance:** $\text{target} = 20 \implies \text{false}$ (Walks along frontier until exiting bottom boundary)
- **Minimum Element Target:** $\text{target} = 1 \implies \text{true}$
- **Maximum Element Target:** $\text{target} = 30 \implies \text{true}$
- **Single Element Instance:** $\text{matrix} = [[5]], \quad \text{target} = 5 \implies \text{true}$

This instance demonstrates the saddleback search algorithm on 2D partially ordered sets, mathematically proves why the top-right (or bottom-left) corner functions as the root of a virtual Binary Search Tree, eliminates an entire row or column at each step, and runs in strictly $O(M + N)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an $M \times N$ matrix where:
- Each row is sorted in ascending order from left to right.
- Each column is sorted in ascending order from top to bottom.
Search for `target = 5`.

### The Corner Property: Why Not Top-Left?
- At the **top-left corner $(0, 0)$**: Both moving right and moving down increase values. If $\text{matrix}[0][0] < \text{target}$, we cannot know whether to explore right or down.
- At the **bottom-right corner $(M-1, N-1)$**: Both moving left and moving up decrease values. If $\text{matrix}[M-1][N-1] > \text{target}$, neither direction is prunable.
- At the **top-right corner $(0, N-1)$**:
  - Moving **left** strictly **decreases** values ($\text{matrix}[r][c-1] < \text{matrix}[r][c]$).
  - Moving **down** strictly **increases** values ($\text{matrix}[r+1][c] > \text{matrix}[r][c]$).

The top-right corner acts as the root of a **Binary Search Tree**!
- If the current value is **too large**, the entire current column below it is even larger $\implies$ prune column $c$ ($c \leftarrow c - 1$).
- If the current value is **too small**, the entire current row to its left is even smaller $\implies$ prune row $r$ ($r \leftarrow r + 1$).

Every comparison eliminates an entire row or column, guaranteeing convergence in at most $M + N$ steps.

---

## 2. Conceptual Foundation & Invariants

### Saddleback Search Protocol
Start at row $r = 0$, column $c = N - 1$:
While $r < M$ and $c \ge 0$:
1. **Target Found:**
   If $\text{matrix}[r][c] == \text{target}$:
   $$
   \text{return true}
   $$
2. **Value Greater Than Target ($\text{matrix}[r][c] > \text{target}$):**
   Because column $c$ is sorted top-to-bottom, every element in column $c$ from row $r$ to $M-1$ is $\ge \text{matrix}[r][c] > \text{target}$.
   Column $c$ cannot contain `target`.
   $$
   c \leftarrow c - 1 \quad (\text{Prune Column } c)
   $$
3. **Value Smaller Than Target ($\text{matrix}[r][c] < \text{target}$):**
   Because row $r$ is sorted left-to-right, every element in row $r$ from column $0$ to $c$ is $\le \text{matrix}[r][c] < \text{target}$.
   Row $r$ cannot contain `target`.
   $$
   r \leftarrow r + 1 \quad (\text{Prune Row } r)
   $$

If coordinates exit the matrix boundaries ($r == M$ or $c < 0$), return `false`.

> **Invariant.** At any step $(r, c)$, the target value (if it exists in the matrix) is guaranteed to lie within the submatrix spanning rows $[r, M-1]$ and columns $[0, c]$.

---

## 3. Step-by-Step Worked Execution

We trace the search for $\text{target} = 5$ in the $5 \times 5$ matrix:
Start at top-right corner: $r = 0, \, c = 4$.

### Step 1: Cell $(0, 4)$, Value $= 15$
- Compare: $\text{matrix}[0][4] = 15 > 5$.
- Value is too large. All entries below $15$ in column 4 ($19, 22, 24, 30$) are $> 15 > 5$.
- Eliminate Column 4:
  $$
  c \leftarrow 4 - 1 = 3
  $$
- Active candidate region: Rows $[0 \dots 4]$, Columns $[0 \dots 3]$.

---

### Step 2: Cell $(0, 3)$, Value $= 11$
- Compare: $\text{matrix}[0][3] = 11 > 5$.
- Value is too large. All entries below $11$ in column 3 ($12, 16, 17, 26$) are $> 11 > 5$.
- Eliminate Column 3:
  $$
  c \leftarrow 3 - 1 = 2
  $$
- Active candidate region: Rows $[0 \dots 4]$, Columns $[0 \dots 2]$.

---

### Step 3: Cell $(0, 2)$, Value $= 7$
- Compare: $\text{matrix}[0][2] = 7 > 5$.
- Value is too large. All entries below $7$ in column 2 ($8, 9, 14, 23$) are $> 7 > 5$.
- Eliminate Column 2:
  $$
  c \leftarrow 2 - 1 = 1
  $$
- Active candidate region: Rows $[0 \dots 4]$, Columns $[0 \dots 1]$.

---

### Step 4: Cell $(0, 1)$, Value $= 4$
- Compare: $\text{matrix}[0][1] = 4 < 5$.
- Value is too small. All entries to the left of $4$ in row 0 ($1$) are $< 4 < 5$.
- Eliminate Row 0:
  $$
  r \leftarrow 0 + 1 = 1
  $$
- Active candidate region: Rows $[1 \dots 4]$, Columns $[0 \dots 1]$.

---

### Step 5: Cell $(1, 1)$, Value $= 5$ (Match Found!)
- Compare: $\text{matrix}[1][1] = 5 == 5$.
- Target found at row $1$, column $1$!
- **Return `true`!**

---

## 4. Complete Execution Trace

```text
Start: (r=0, c=4), val=15 > 5 -> c = 3 (Eliminate col 4)
Step 2: (r=0, c=3), val=11 > 5 -> c = 2 (Eliminate col 3)
Step 3: (r=0, c=2), val=7  > 5 -> c = 1 (Eliminate col 2)
Step 4: (r=0, c=1), val=4  < 5 -> r = 1 (Eliminate row 0)
Step 5: (r=1, c=1), val=5 == 5 -> MATCH FOUND! Return True
```

| Step | Coordinate $(r, c)$ | Examined Value | Comparison vs Target ($5$) | Pruning Decision | Remaining Submatrix Bounds |
|:---:|:---:|:---:|:---:|:---|:---|
| **1** | $(0, 4)$ | 15 | $15 > 5$ | Eliminate Column 4 ($c \leftarrow 3$) | Rows $[0 \dots 4]$, Cols $[0 \dots 3]$ |
| **2** | $(0, 3)$ | 11 | $11 > 5$ | Eliminate Column 3 ($c \leftarrow 2$) | Rows $[0 \dots 4]$, Cols $[0 \dots 2]$ |
| **3** | $(0, 2)$ | 7 | $7 > 5$ | Eliminate Column 2 ($c \leftarrow 1$) | Rows $[0 \dots 4]$, Cols $[0 \dots 1]$ |
| **4** | $(0, 1)$ | 4 | $4 < 5$ | Eliminate Row 0 ($r \leftarrow 1$) | Rows $[1 \dots 4]$, Cols $[0 \dots 1]$ |
| **5** | **$(1, 1)$** | **5** | **$5 == 5$** | **Target matched!** | **Return `true`** |

### Contrast: Absent Target Search ($\text{target} = 20$)
- $(0, 4) = 15 < 20 \implies r = 1$
- $(1, 4) = 19 < 20 \implies r = 2$
- $(2, 4) = 22 > 20 \implies c = 3$
- $(2, 3) = 16 < 20 \implies r = 3$
- $(3, 3) = 17 < 20 \implies r = 4$
- $(4, 3) = 26 > 20 \implies c = 2$
- $(4, 2) = 23 > 20 \implies c = 1$
- $(4, 1) = 21 > 20 \implies c = 0$
- $(4, 0) = 18 < 20 \implies r = 5 > 4$ (Out of bounds $\implies$ **`false`**).

---

## 5. Algorithmic Correctness

**Soundness.** When $\text{matrix}[r][c] > \text{target}$, sorted columns ensure all $\text{matrix}[i][c] \ge \text{matrix}[r][c] > \text{target}$ for $i \ge r$. Column $c$ cannot hold `target`. When $\text{matrix}[r][c] < \text{target}$, sorted rows ensure all $\text{matrix}[r][j] \le \text{matrix}[r][c] < \text{target}$ for $j \le c$. Row $r$ cannot hold `target`. Discarding these regions is mathematically guaranteed never to eliminate the target.

**Completeness.** At each step, either $r$ increments or $c$ decrements. Since $r \in [0, M]$ and $c \in [-1, N-1]$, the search must either land on `target` or exit the grid within $M + N$ steps, proving absence.

---

## 6. Traps This Instance Exposes

- **Matrix Flattening Fallacy:** Unlike LeetCode 74 (where the first element of row $i+1$ is strictly greater than the last element of row $i$), here the rows and columns overlap in values. The matrix cannot be flattened into a 1D sorted array for a single $O(\log(MN))$ binary search.
- **Starting at Top-Left:** Starting at $(0, 0)$ offers no pruning direction when $\text{matrix}[0][0] < \text{target}$. The top-right $(0, N-1)$ or bottom-left $(M-1, 0)$ corners are the only two valid starting points.
- **Boundary Conditions:** The loop condition must check both upper and lower index boundaries (`r < M and c >= 0`).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M + N)$, where $M$ is the number of rows and $N$ is the number of columns. In each step, either $r$ is incremented or $c$ is decremented. The maximum number of steps before exiting the matrix is $M + N$. For a $1000 \times 1000$ matrix, this takes at most $2,000$ comparisons, compared to $1,000,000$ for a naive search.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory.