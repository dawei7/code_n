# Guided Example: Max Increase to Keep City Skyline

We trace the step-by-step orthogonal skyline profile projections (East-West row maxima $row\_max[i]$ and North-South column maxima $col\_max[j]$), point-wise upper bound ceiling invariant ($\min(row\_max[i], col\_max[j])$), cell height delta accumulation ($\Delta = \min(R_i, C_j) - grid[i][j]$), and global structural volume maximization on representative 2D architectural grids:

- **Input:**
  $$
  grid = \begin{bmatrix}
  3 & 0 & 8 & 4 \\
  2 & 4 & 5 & 7 \\
  9 & 2 & 6 & 3 \\
  0 & 3 & 1 & 0
  \end{bmatrix}
  $$
- **Required output:** `35`
  - Skyline preservation rules:
    - In an $n \times n$ city, each cell $(i, j)$ has a building of height $grid[i][j]$.
    - The skyline from the East or West is determined by the maximum height in each row:
      $$
      row\_max[i] = \max_{0 \le j < n} grid[i][j]
      $$
    - The skyline from the North or South is determined by the maximum height in each column:
      $$
      col\_max[j] = \max_{0 \le i < n} grid[i][j]
      $$
    - You may increase the height of any building as long as neither the row maximum nor the column maximum changes.
    - Objective: Find the **maximum total sum of height increases** across all buildings.
    - For the input grid ($4 \times 4$):
      - Row maxima: $row\_max = [8, 7, 9, 3]$
      - Column maxima: $col\_max = [9, 4, 8, 7]$
      - Each building $(i, j)$ can grow up to $\min(row\_max[i], col\_max[j])$.
      - Total height added across all 16 buildings is **35**.
- **Point-Wise Ceiling & Independence Invariant:**
  - **The Coordinate Ceiling:**
    - To preserve the skyline of row $i$, building $(i, j)$ cannot exceed $row\_max[i]$:
      $$
      h_{\text{new}}(i, j) \le row\_max[i]
      $$
    - To preserve the skyline of column $j$, building $(i, j)$ cannot exceed $col\_max[j]$:
      $$
      h_{\text{new}}(i, j) \le col\_max[j]
      $$
    - Therefore, the tightest upper bound on building $(i, j)$ is the minimum of these two skyline constraints:
      $$
      h_{\text{max}}(i, j) = \min(row\_max[i], \; col\_max[j])
      $$
  - **Decoupled Cell Growth:**
    - Because each cell $(i, j)$ is bounded strictly by row $i$ and column $j$'s initial maximums, increasing building $(i, j)$ to $h_{\text{max}}(i, j)$ never reduces or tightens the ceiling of any other building!
    - The maximum additional height for building $(i, j)$ is:
      $$
      \Delta(i, j) = \min(row\_max[i], \; col\_max[j]) - grid[i][j]
      $$
    - Global maximum increase is simply the sum over all cells:
      $$
      ans = \sum_{i = 0}^{n - 1} \sum_{j = 0}^{n - 1} \left( \min(row\_max[i], \; col\_max[j]) - grid[i][j] \right)
      $$
- **Step-by-Step Worked Execution Trace on the $4 \times 4$ City:**
  - **Phase 0: Precompute Skyline Vectors:**
    - Row maxima:
      - Row 0: $\max(3, 0, 8, 4) = \mathbf{8}$
      - Row 1: $\max(2, 4, 5, 7) = \mathbf{7}$
      - Row 2: $\max(9, 2, 6, 3) = \mathbf{9}$
      - Row 3: $\max(0, 3, 1, 0) = \mathbf{3}$
      $$
      row\_max = [8, \; 7, \; 9, \; 3]
      $$
    - Column maxima:
      - Col 0: $\max(3, 2, 9, 0) = \mathbf{9}$
      - Col 1: $\max(0, 4, 2, 3) = \mathbf{4}$
      - Col 2: $\max(8, 5, 6, 1) = \mathbf{8}$
      - Col 3: $\max(4, 7, 3, 0) = \mathbf{7}$
      $$
      col\_max = [9, \; 4, \; 8, \; 7]
      $$
  - **Phase 1: Calculate Increases Row by Row:**
    - **Row 0 ($row\_max[0] = 8$):**
      - $(0, 0): \min(8, 9) - 3 = 8 - 3 = \mathbf{5}$
      - $(0, 1): \min(8, 4) - 0 = 4 - 0 = \mathbf{4}$
      - $(0, 2): \min(8, 8) - 8 = 8 - 8 = \mathbf{0}$
      - $(0, 3): \min(8, 7) - 4 = 7 - 4 = \mathbf{3}$
      - Row 0 increase: $5 + 4 + 0 + 3 = \mathbf{12}$.
    - **Row 1 ($row\_max[1] = 7$):**
      - $(1, 0): \min(7, 9) - 2 = 7 - 2 = \mathbf{5}$
      - $(1, 1): \min(7, 4) - 4 = 4 - 4 = \mathbf{0}$
      - $(1, 2): \min(7, 8) - 5 = 7 - 5 = \mathbf{2}$
      - $(1, 3): \min(7, 7) - 7 = 7 - 7 = \mathbf{0}$
      - Row 1 increase: $5 + 0 + 2 + 0 = \mathbf{7}$.
    - **Row 2 ($row\_max[2] = 9$):**
      - $(2, 0): \min(9, 9) - 9 = 9 - 9 = \mathbf{0}$
      - $(2, 1): \min(9, 4) - 2 = 4 - 2 = \mathbf{2}$
      - $(2, 2): \min(9, 8) - 6 = 8 - 6 = \mathbf{2}$
      - $(2, 3): \min(9, 7) - 3 = 7 - 3 = \mathbf{4}$
      - Row 2 increase: $0 + 2 + 2 + 4 = \mathbf{8}$.
    - **Row 3 ($row\_max[3] = 3$):**
      - $(3, 0): \min(3, 9) - 0 = 3 - 0 = \mathbf{3}$
      - $(3, 1): \min(3, 4) - 3 = 3 - 3 = \mathbf{0}$
      - $(3, 2): \min(3, 8) - 1 = 3 - 1 = \mathbf{2}$
      - $(3, 3): \min(3, 7) - 0 = 3 - 0 = \mathbf{3}$
      - Row 3 increase: $3 + 0 + 2 + 3 = \mathbf{8}$.
  - **Phase 2: Total Skyline Increase Summation:**
    $$
    ans = 12 + 7 + 8 + 8 = \mathbf{35}
    $$
- **Uniform Grid Trace ($grid = [[5, 5], [5, 5]]$):**
  - All $row\_max = 5$, all $col\_max = 5$.
  - Upper bound is 5 for all cells $\implies$ increase is $\mathbf{0}$.
- **Single Dominant Peak Trace ($grid = [[0, 0], [0, 9]]$):**
  - $row\_max = [0, 9], col\_max = [0, 9]$.
  - Cell $(0, 0)$: $\min(0, 0) - 0 = 0$.
  - Cell $(0, 1)$: $\min(0, 9) - 0 = 0$.
  - Cell $(1, 0)$: $\min(9, 0) - 0 = 0$.
  - Cell $(1, 1)$: $\min(9, 9) - 9 = 0$.
  - Increase is $\mathbf{0}$ because non-zero increase would alter the 0-skylines.

This instance demonstrates tropical convex geometry and sub-modular capacity constraints on discrete product spaces, mathematically proves why pointwise infimum over 1D marginal projections defines the maximal envelope preserving coordinate projections, and derives $O(N^2)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ building height grid:
Increase building heights as much as possible **without changing** the row or column maximums (skylines).
Return the **total height increase**.

```text
grid:
  3 0 8 4  -> row max = 8
  2 4 5 7  -> row max = 7
  9 2 6 3  -> row max = 9
  0 3 1 0  -> row max = 3
  v v v v
  9 4 8 7  (col max)

Each building (i, j) can grow to min(row_max[i], col_max[j]):
  (0, 0): min(8, 9) = 8 -> grows from 3 to 8 (+5)
  (0, 1): min(8, 4) = 4 -> grows from 0 to 4 (+4)
  (0, 2): min(8, 8) = 8 -> 8 to 8 (+0)
  (0, 3): min(8, 7) = 7 -> 4 to 7 (+3)
  ...

Total increase = 35
Result: 35
```

### The Invariant of the Decoupled Ceiling
- To preserve the row skyline, building $(i, j) \le row\_max[i]$.
- To preserve the column skyline, building $(i, j) \le col\_max[j]$.
- Since constraints are independent, optimal height is $\min(row\_max[i], col\_max[j])$.

---

## 2. Conceptual Foundation & Invariants

### 1. Marginal Skyline Projections:
$$
R_i = \max_{0 \le j < n} grid[i][j], \quad C_j = \max_{0 \le i < n} grid[i][j]
$$

### 2. Envelope Difference Summation:
$$
ans = \sum_{i = 0}^{n - 1} \sum_{j = 0}^{n - 1} \Big( \min(R_i, C_j) - grid[i][j] \Big)
$$

> **Tropical Projection Invariant.** The matrix $M_{ij} = \min(R_i, C_j)$ is the unique maximal element in the tropical convex set of matrices having marginals $R$ and $C$. The total increase is the $L_1$ metric distance $\|M - grid\|_1$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Precompute Maxima
- $R = [8, 7, 9, 3]$.
- $C = [9, 4, 8, 7]$.

---

### Step 2: Row 0 Increases
- $\min(8, 9) - 3 = 5$
- $\min(8, 4) - 0 = 4$
- $\min(8, 8) - 8 = 0$
- $\min(8, 7) - 4 = 3$
- Subtotal: $12$.

---

### Step 3: Rows 1, 2, 3 Increases
- Row 1: $5 + 0 + 2 + 0 = 7$.
- Row 2: $0 + 2 + 2 + 4 = 8$.
- Row 3: $3 + 0 + 2 + 3 = 8$.

---

### Step 4: Output
- $12 + 7 + 8 + 8 = \mathbf{35}$.

---

## 4. Complete Execution Trace

| Row $i$ | Initial Heights $grid[i]$ | Row Max $R_i$ | Target Heights $\min(R_i, C_j)$ | Added Heights $\Delta$ | Row Increase Sum |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `[3, 0, 8, 4]` | $8$ | `[8, 4, 8, 7]` | `[5, 4, 0, 3]` | $12$ |
| $1$ | `[2, 4, 5, 7]` | $7$ | `[7, 4, 7, 7]` | `[5, 0, 2, 0]` | $7$ |
| $2$ | `[9, 2, 6, 3]` | $9$ | `[9, 4, 8, 7]` | `[0, 2, 2, 4]` | $8$ |
| **$3$** | **`[0, 3, 1, 0]`** | **$3$** | **`[3, 3, 3, 3]`** | **`[3, 0, 2, 3]`** | **$8$** |
| **Total** | — | — | — | — | **`35`** |

---

## 5. Boundary Cases & Failure Modes

- **$1 \times 1$ Grid ($[[5]]$):** $R_0 = 5, C_0 = 5 \implies \min(5, 5) - 5 = 0$.
- **Flat City (All Equal Heights):** Cannot increase any building $\implies 0$.
- **Zeros in Grid:** Non-boundary buildings at 0 can grow up to $\min(R_i, C_j)$.
- **Strictly Dominated Lines:** If a row has max 0, no building in that row can increase.

---

## 6. Traps & Common Anti-Patterns

- **Recomputing Maxima Inside the Nested Loop ($O(N^3)$):** Computing `max(row)` and `max(col)` inside every cell lookup causes quadratic redundant operations. Precomputing vectors $row\_max$ and $col\_max$ in $O(N^2)$ ensures clean linear matrix traversal.
- **Thinking Buildings Shadow Each Other:** Buildings do not obstruct lines of sight in between; the skyline is simply the maximum height along that orthogonal axis.
- **Subtracting Target from Initial:** The increase is target minus initial ($\min(R_i, C_j) - grid[i][j]$), which is always $\ge 0$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding row maxima: $\mathcal{O}(N^2)$.
  - Finding column maxima: $\mathcal{O}(N^2)$.
  - Summing differences across $N \times N$ cells: $\mathcal{O}(N^2)$.
  - Total Time: strictly $\mathcal{O}(N^2)$ where $N \le 50 \implies \le 2500$ operations. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to store $row\_max$ and $col\_max$ arrays.
