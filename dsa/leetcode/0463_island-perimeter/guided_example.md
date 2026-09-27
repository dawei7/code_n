# Guided Example: Island Perimeter

We trace the step-by-step land cell unit contribution ($+4$), shared internal edge cancellation ($-2$ per adjacent land pair), directional forward/downward neighbor checks, and boundary perimeter summation on representative 2D grid islands:

- **Input:**
  $$
  grid = \begin{bmatrix}
  0 & 1 & 0 & 0 \\
  1 & 1 & 1 & 0 \\
  0 & 1 & 0 & 0 \\
  1 & 1 & 0 & 0
  \end{bmatrix}
  $$
- **Required output:** `16`
  - Dimensions: $m = 4, \; n = 4$
  - Land cell tally: $7$ total land cells ($1$s)
  - Theoretical maximum perimeter (all isolated):
    $$
    7 \times 4 = 28
    $$
  - **Shared Edge Scan (Down and Right neighbors):**
    - Cell $(0, 1)$: Down neighbor $(1, 1)$ is land $\implies$ Shared edge! $ans -= 2$
    - Cell $(1, 0)$: Right neighbor $(1, 1)$ is land $\implies$ Shared edge! $ans -= 2$
    - Cell $(1, 1)$:
      - Right neighbor $(1, 2)$ is land $\implies$ Shared edge! $ans -= 2$
      - Down neighbor $(2, 1)$ is land $\implies$ Shared edge! $ans -= 2$
    - Cell $(1, 2)$: Down neighbor is water, Right is water $\implies$ No shared edges
    - Cell $(2, 1)$: Down neighbor $(3, 1)$ is land $\implies$ Shared edge! $ans -= 2$
    - Cell $(3, 0)$: Right neighbor $(3, 1)$ is land $\implies$ Shared edge! $ans -= 2$
    - Cell $(3, 1)$: No down or right land neighbors
  - Total shared internal edges: $6$ shared boundaries
  - Net perimeter calculation:
    $$
    \text{Perimeter} = (7 \times 4) - (6 \times 2) = 28 - 12 = \mathbf{16}
    $$
- **Single Land Cell Instance:** $grid = [[1]] \implies 1 \times 4 - 0 = \mathbf{4}$
- **Two Adjacent Cells Instance:** $grid = [[1, 1]] \implies (2 \times 4) - (1 \times 2) = 8 - 2 = \mathbf{6}$

This instance demonstrates geometric boundary analysis on 2D discrete meshes, mathematically proves why shared internal borders cancel in pairs of $2$, and derives $O(M \times N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a 2D integer matrix $grid$ where `1` represents land and `0` represents water:
Grid cells are connected horizontally/vertically.
There is exactly one island.
Determine the **perimeter of the island**.

```text
Visualizing the Grid Map:
  [ 0,  1,  0,  0 ]
  [ 1,  1,  1,  0 ]
  [ 0,  1,  0,  0 ]
  [ 1,  1,  0,  0 ]

Counting External Edges:
  - Top row exposed edges:     3
  - Bottom row exposed edges:  3
  - Left column exposed edges: 5
  - Right column exposed edges: 5
  Total Perimeter = 16
```

### The Edge Cancellation Principle
- An isolated square of land has 4 perimeter sides.
- When two land squares are glued together side-by-side:
  - The right side of the first square and the left side of the second square meet inside the island.
  - Because they are submerged internally, **both** sides cease to be part of the outer perimeter!
  - Therefore, every shared edge between two adjacent land squares subtracts **exactly 2** from the gross perimeter:
    $$
    \text{Perimeter} = 4 \times (\text{Land Squares}) - 2 \times (\text{Shared Borders})
    $$

---

## 2. Conceptual Foundation & Invariants

### 1. Dual Counting Avoidance:
If we checked all 4 directions (up, down, left, right) for every cell:
Each shared border between cell $A$ and cell $B$ would be observed twice (once from $A$ to $B$, and once from $B$ to $A$), requiring subtracting 1 each time.
Instead, by scanning **only forward and downward** (right neighbor $j + 1$ and bottom neighbor $i + 1$):
Every adjacent pair is encountered **exactly once**.
For each forward/downward neighbor that is also land, we subtract $2$.

### 2. Algorithmic Transition:
For each cell $(i, j)$ in the $m \times n$ grid:
- If $grid[i][j] == 1$:
  - Add $4$ to $ans$.
  - If $i < m - 1$ and $grid[i + 1][j] == 1$: subtract $2$.
  - If $j < n - 1$ and $grid[i][j + 1] == 1$: subtract $2$.

> **Border Invariance.** The total exposed perimeter equals the sum of unshared external boundary segments, which is strictly preserved under pairwise cancellation of adjacent unit square edges.

---

## 3. Step-by-Step Worked Execution

We trace the $4 \times 4$ grid:
Initialize $ans = 0$.

---

### Row 0:
- $(0, 0) = 0$: Water. Skip.
- $(0, 1) = 1$: Land!
  - $ans \leftarrow ans + 4 = \mathbf{4}$.
  - Down neighbor $(1, 1) = 1$: $ans \leftarrow 4 - 2 = \mathbf{2}$.
  - Right neighbor $(0, 2) = 0$: No cancellation.
- $(0, 2), (0, 3) = 0$: Skip.
*Row 0 Subtotal:* $ans = 2$.

---

### Row 1:
- $(1, 0) = 1$: Land!
  - $ans \leftarrow 2 + 4 = 6$.
  - Down neighbor $(2, 0) = 0$: No cancellation.
  - Right neighbor $(1, 1) = 1$: $ans \leftarrow 6 - 2 = \mathbf{4}$.
- $(1, 1) = 1$: Land!
  - $ans \leftarrow 4 + 4 = 8$.
  - Down neighbor $(2, 1) = 1$: $ans \leftarrow 8 - 2 = \mathbf{6}$.
  - Right neighbor $(1, 2) = 1$: $ans \leftarrow 6 - 2 = \mathbf{4}$.
- $(1, 2) = 1$: Land!
  - $ans \leftarrow 4 + 4 = 8$.
  - Down neighbor $(2, 2) = 0$: No cancellation.
  - Right neighbor $(1, 3) = 0$: No cancellation.
- $(1, 3) = 0$: Skip.
*Row 1 Subtotal:* $ans = 8$.

---

### Row 2:
- $(2, 1) = 1$: Land!
  - $ans \leftarrow 8 + 4 = 12$.
  - Down neighbor $(3, 1) = 1$: $ans \leftarrow 12 - 2 = \mathbf{10}$.
  - Right neighbor $(2, 2) = 0$: No cancellation.
*Row 2 Subtotal:* $ans = 10$.

---

### Row 3:
- $(3, 0) = 1$: Land!
  - $ans \leftarrow 10 + 4 = 14$.
  - Down neighbor out-of-bounds.
  - Right neighbor $(3, 1) = 1$: $ans \leftarrow 14 - 2 = \mathbf{12}$.
- $(3, 1) = 1$: Land!
  - $ans \leftarrow 12 + 4 = \mathbf{16}$.
  - Down neighbor out-of-bounds.
  - Right neighbor $(3, 2) = 0$: No cancellation.
*Row 3 Subtotal:* $ans = 16$.

---

### Final Result:
Total perimeter: **`16`**.

---

## 4. Complete Execution Trace

| Land Cell $(i, j)$ | Initial Addition | Right Neighbor $(i, j+1)$ | Down Neighbor $(i+1, j)$ | Deductions Made | Running Perimeter $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 1)$ | $+4$ | Water ($0$) | **Land ($1$)** | $-2$ (Down) | $2$ |
| $(1, 0)$ | $+4$ | **Land ($1$)** | Water ($0$) | $-2$ (Right) | $4$ |
| $(1, 1)$ | $+4$ | **Land ($1$)** | **Land ($1$)** | $-4$ (Right + Down) | $4$ |
| $(1, 2)$ | $+4$ | Water ($0$) | Water ($0$) | $0$ | $8$ |
| $(2, 1)$ | $+4$ | Water ($0$) | **Land ($1$)** | $-2$ (Down) | $10$ |
| $(3, 0)$ | $+4$ | **Land ($1$)** | Boundary | $-2$ (Right) | $12$ |
| $(3, 1)$ | $+4$ | Water ($0$) | Boundary | $0$ | **$16$** |
| **Final** | — | — | — | — | **$16$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Cell ($1 \times 1$ with $[[1]]$):** Adds 4, bounds checks prevent neighbor access $\implies \mathbf{4}$.
- **Straight Line of Land ($1 \times 4$ with $[[1, 1, 1, 1]]$):** 4 cells $\times 4 = 16$. Three internal right edges $\implies 16 - 2(3) = \mathbf{10}$.
- **Solid $2 \times 2$ Block of Land:** 4 cells $\times 4 = 16$. Four internal shared edges (two horizontal, two vertical) $\implies 16 - 2(4) = \mathbf{8}$.
- **Lakes Inside Island:** Internal water holes automatically add to the outer cell border perimeter because water cells do not trigger the $-2$ shared edge subtraction.

---

## 6. Traps & Common Anti-Patterns

- **Subtracting 1 Instead of 2:** When encountering an adjacent pair, each shared edge submerges two unit segments (one for each square). Subtracting only 1 severely overcounts perimeter.
- **Checking All 4 Neighbors and Subtracting 2:** If you check Up, Down, Left, Right and subtract 2, every shared edge is subtracted twice (total $-4$). Either check 2 directions and subtract 2, or check 4 directions and subtract 1.
- **Out-of-Bounds Indexing:** Checking $i + 1$ or $j + 1$ at grid boundaries throws index errors if not protected by $i < m - 1$ and $j < n - 1$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The grid of size $M \times N$ is traversed once via a nested loop.
  - Each cell performs $O(1)$ arithmetic operations.
  - Total Time: $\mathcal{O}(M \times N)$. For a $100 \times 100$ grid, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space using a single accumulator integer.
