# Guided Example: Surface Area of 3D Shapes

We trace the step-by-step standalone tower surface calculation ($2 + 4v$), adjacent tower interface occlusion, pairwise shared face subtraction ($2 \times \min(v_1, v_2)$), and total exposed surface area derivation on representative 3D voxel grids:

- **Input:**
  $$
  grid = \begin{bmatrix}
  1 & 2 \\
  3 & 4
  \end{bmatrix}
  $$
- **Required output:** `34`
  - 3D voxel surface area rules:
    - On an $n \times n$ grid, cell $(i, j)$ contains a tower of $v = grid[i][j]$ unit cubes ($1 \times 1 \times 1$) stacked vertically.
    - All cubes placed on adjacent cells or vertically stacked within the same cell are glued together.
    - Objective: Find the **total exposed surface area** of the resulting 3D solid.
    - For $grid = [[1, 2], [3, 4]]$:
      - Standalone tower areas:
        - Tower $(0, 0)$ of height 1: $2 + 4(1) = 6$.
        - Tower $(0, 1)$ of height 2: $2 + 4(2) = 10$.
        - Tower $(1, 0)$ of height 3: $2 + 4(3) = 14$.
        - Tower $(1, 1)$ of height 4: $2 + 4(4) = 18$.
        - Sum of unglued standalone areas: $6 + 10 + 14 + 18 = 48$.
      - Hidden shared faces between adjacent towers:
        - Between $(0, 0)$ and $(0, 1)$: height $\min(1, 2) = 1 \implies 2 \times 1 = 2$ faces covered.
        - Between $(0, 0)$ and $(1, 0)$: height $\min(1, 3) = 1 \implies 2 \times 1 = 2$ faces covered.
        - Between $(0, 1)$ and $(1, 1)$: height $\min(2, 4) = 2 \implies 2 \times 2 = 4$ faces covered.
        - Between $(1, 0)$ and $(1, 1)$: height $\min(3, 4) = 3 \implies 2 \times 3 = 6$ faces covered.
        - Total occluded faces: $2 + 2 + 4 + 6 = 14$.
      - Total exposed surface area:
        $$
        48 - 14 = \mathbf{34}
        $$
- **The Standalone & Overlap Occlusion Invariant:**
  - **Standalone Tower Geometry:**
    - A solitary tower of height $v > 0$ unit cubes has:
      - $1$ top exposed face.
      - $1$ bottom exposed face.
      - $4$ lateral sides, each of area $v \times 1 = v$.
      - Standalone Area:
        $$
        A_{\text{standalone}}(v) = 2 + 4v \quad (\text{if } v > 0)
        $$
  - **Interface Subtraction Rule:**
    - When two towers of heights $v_1$ and $v_2$ stand adjacent to each other (sharing an edge of the grid), they press against each other along a vertical rectangle of height:
      $$
      h_{\text{shared}} = \min(v_1, v_2)
      $$
    - Because this shared interface covers faces on **both** towers, the gluing operation hides exactly:
      $$
      2 \times \min(v_1, v_2) \text{ exposed faces}
      $$
  - **Directional Accounting (Avoiding Double Subtraction):**
    - Scanning cells in standard raster order (left-to-right, top-to-bottom), each cell $(i, j)$ only needs to subtract shared faces with its **immediate top neighbor** $(i - 1, j)$ and **immediate left neighbor** $(i, j - 1)$.
    - This visits every boundary between adjacent towers exactly once!

---

## 1. Instance & Teaching Goal

Given $grid = [[1, 2], [3, 4]]$, track the exposed surface area additions and neighbor deductions cell by cell.

```text
Grid Heights:
  [1]  [2]
  [3]  [4]

Cell (0, 0) [v=1]:
  Standalone: 2 + 4(1) = 6
  Neighbors: None above or left. Running total = 6.

Cell (0, 1) [v=2]:
  Standalone: 2 + 4(2) = 10
  Left neighbor has v=1 -> overlap = 2 * min(2, 1) = 2
  Running total = 6 + 10 - 2 = 14.

Cell (1, 0) [v=3]:
  Standalone: 2 + 4(3) = 14
  Top neighbor has v=1 -> overlap = 2 * min(3, 1) = 2
  Running total = 14 + 14 - 2 = 26.

Cell (1, 1) [v=4]:
  Standalone: 2 + 4(4) = 18
  Top neighbor has v=2  -> overlap = 2 * min(4, 2) = 4
  Left neighbor has v=3 -> overlap = 2 * min(4, 3) = 6
  Running total = 26 + 18 - 4 - 6 = 34.
```

The teaching goal is to demonstrate how local pairwise adjacency subtractions prevent double-counting shared faces.

---

## 2. Conceptual Foundation & Invariants

### 1. Standalone Area Contribution:
For cell $(i, j)$ with height $v = grid[i][j]$:
$$
\text{Initial Area}(v) = \begin{cases}
2 + 4v & \text{if } v > 0 \\
0 & \text{if } v = 0
\end{cases}
$$

### 2. Interface Deduction:
$$
\text{Deduction}_{\text{top}} = 2 \times \min(v, \; grid[i - 1][j]) \quad (\text{if } i > 0)
$$
$$
\text{Deduction}_{\text{left}} = 2 \times \min(v, \; grid[i][j - 1]) \quad (\text{if } j > 0)
$$

---

## 3. Step-by-Step Worked Execution

We trace $grid = [[1, 2], [3, 4]]$:
Initialize $ans = 0$.

---

### Step 1: Cell $(0, 0)$ ($v = 1$)
- Height $v = 1 > 0$:
  $$
  ans \leftarrow ans + 2 + 4(1) = 0 + 6 = 6
  $$
- Top neighbor: $i = 0$ (no top neighbor).
- Left neighbor: $j = 0$ (no left neighbor).
- Running total: $ans = \mathbf{6}$.

---

### Step 2: Cell $(0, 1)$ ($v = 2$)
- Height $v = 2 > 0$:
  $$
  ans \leftarrow ans + 2 + 4(2) = 6 + 10 = 16
  $$
- Top neighbor: $i = 0$ (no top neighbor).
- Left neighbor $(0, 0)$ has height $grid[0][0] = 1$:
  $$
  ans \leftarrow ans - 2 \times \min(2, 1) = 16 - 2(1) = \mathbf{14}
  $$
- Running total: $ans = \mathbf{14}$.

---

### Step 3: Cell $(1, 0)$ ($v = 3$)
- Height $v = 3 > 0$:
  $$
  ans \leftarrow ans + 2 + 4(3) = 14 + 14 = 28
  $$
- Top neighbor $(0, 0)$ has height $grid[0][0] = 1$:
  $$
  ans \leftarrow ans - 2 \times \min(3, 1) = 28 - 2(1) = \mathbf{26}
  $$
- Left neighbor: $j = 0$ (no left neighbor).
- Running total: $ans = \mathbf{26}$.

---

### Step 4: Cell $(1, 1)$ ($v = 4$)
- Height $v = 4 > 0$:
  $$
  ans \leftarrow ans + 2 + 4(4) = 26 + 18 = 44
  $$
- Top neighbor $(0, 1)$ has height $grid[0][1] = 2$:
  $$
  ans \leftarrow ans - 2 \times \min(4, 2) = 44 - 4 = 40
  $$
- Left neighbor $(1, 0)$ has height $grid[1][0] = 3$:
  $$
  ans \leftarrow ans - 2 \times \min(4, 3) = 40 - 6 = \mathbf{34}
  $$
- Running total: $ans = \mathbf{34}$.

---

### Termination:
All grid cells processed.
- **Total Surface Area:** **`34`**.

---

## 4. Complete Execution Trace

| Cell $(i, j)$ | Height $v$ | Base Standalone Area | Top Neighbor Height | Top Deductions | Left Neighbor Height | Left Deductions | Net Running Area |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | $1$ | $+6$ | — | $0$ | — | $0$ | $6$ |
| $(0, 1)$ | $2$ | $+10$ | — | $0$ | $1$ | $-2$ | $14$ |
| $(1, 0)$ | $3$ | $+14$ | $1$ | $-2$ | — | $0$ | $26$ |
| **$(1, 1)$** | **$4$** | **$+18$** | **$2$** | **$-4$** | **$3$** | **$-6$** | **`34`** |

---

## 5. Boundary Cases & Failure Modes

- **Zero Heights (Empty Cells):** If $v = 0$, the tower contributes $0$ base area, and deductions are skipped or evaluate to $2 \times \min(0, \cdot) = 0$.
- **Ring of Cubes with Empty Center (Sample 2):** Interior faces facing the hole remain exposed because $grid[center] = 0 \implies \min(1, 0) = 0$, so no faces are subtracted.
- **Single Cube Grid ($[[1]]$):** Standalone area is $2 + 4(1) = 6$. No neighbors $\implies$ returns $6$.

---

## 6. Traps & Common Anti-Patterns

- **Checking All 4 Neighbors in Each Step:** Subtracting shared faces with top, bottom, left, and right neighbors during each cell's visit subtracts every shared interface twice, undercounting the surface area. Only checking top and left neighbors ensures exact single subtraction.
- **Forgetting Top and Bottom Faces:** Cubes have top and bottom faces ($+2$) in addition to the $4v$ vertical walls.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard raster scan over an $n \times n$ grid: $\mathcal{O}(n^2)$.
  - Each cell performs at most two neighbor comparisons: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(n^2)$, completing in $< 1$ ms for $n \le 50$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space using an accumulator register.
