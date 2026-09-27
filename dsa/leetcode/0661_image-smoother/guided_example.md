# Guided Example: Image Smoother

We trace the step-by-step $3 \times 3$ box filter convolution, Moore neighborhood boundary clipping ($x \in [i-1, i+1], y \in [j-1, j+1]$), boundary-dependent cell cardinality ($4$ for corners, $6$ for edges, $9$ for interior), local intensity summation ($s = \sum img[x][y]$), and integer floor division ($\lfloor s / cnt \rfloor$) on representative 2D grayscale image matrices:

- **Input:**
  $$
  img = \begin{bmatrix}
  1 & 1 & 1 \\
  1 & 0 & 1 \\
  1 & 1 & 1
  \end{bmatrix}
  $$
- **Required output:**
  $$
  \begin{bmatrix}
  0 & 0 & 0 \\
  0 & 0 & 0 \\
  0 & 0 & 0
  \end{bmatrix}
  $$
  - Image smoothing specification:
    - Apply a $3 \times 3$ moving average filter over every cell $(i, j)$.
    - For each cell, consider all valid grid cells in the $3 \times 3$ bounding box centered at $(i, j)$:
      $$
      \mathcal{N}(i, j) = \{(x, y) \mid i - 1 \le x \le i + 1, \; j - 1 \le y \le j + 1, \; 0 \le x < m, \; 0 \le y < n\}
      $$
    - The smoothed intensity is the integer floor of the average:
      $$
      ans[i][j] = \left\lfloor \frac{\sum_{(x, y) \in \mathcal{N}(i, j)} img[x][y]}{|\mathcal{N}(i, j)|} \right\rfloor
      $$
- **Spatial Topology & Boundary Clamping Invariant:**
  - **Variable Neighborhood Cardinality ($cnt$):**
    - **Interior Cells (surrounded on all sides):** Exactly $3 \times 3 = \mathbf{9}$ cells in neighborhood.
    - **Edge Cells (along top, bottom, left, right borders):** Exactly $2 \times 3 = \mathbf{6}$ cells in neighborhood.
    - **Corner Cells (the four extremities of the grid):** Exactly $2 \times 2 = \mathbf{4}$ cells in neighborhood.
  - **Integer Floor Truncation:**
    - Any fractional average $\frac{s}{cnt}$ is strictly floored downwards (e.g. $\lfloor 3 / 4 \rfloor = 0$, $\lfloor 8 / 9 \rfloor = 0$).
- **Step-by-Step Worked Execution Trace on the $3 \times 3$ Matrix:**
  - Dimensions: $m = 3, n = 3$.
  - **Corner Cell $(0, 0)$:**
    - Bounding box: $x \in [0, 1], y \in [0, 1]$.
    - Valid neighbors ($cnt = 4$):
      - $(0, 0) = 1$
      - $(0, 1) = 1$
      - $(1, 0) = 1$
      - $(1, 1) = 0$
    - Sum:
      $$
      s = 1 + 1 + 1 + 0 = \mathbf{3}
      $$
    - Average calculation:
      $$
      ans[0][0] = \left\lfloor \frac{3}{4} \right\rfloor = \mathbf{0}
      $$
  - **Edge Cell $(0, 1)$:**
    - Bounding box: $x \in [0, 1], y \in [0, 2]$.
    - Valid neighbors ($cnt = 6$):
      - Row 0: $(0, 0)=1, (0, 1)=1, (0, 2)=1$ (sum $= 3$)
      - Row 1: $(1, 0)=1, (1, 1)=0, (1, 2)=1$ (sum $= 2$)
    - Total sum:
      $$
      s = 3 + 2 = \mathbf{5}
      $$
    - Average calculation:
      $$
      ans[0][1] = \left\lfloor \frac{5}{6} \right\rfloor = \mathbf{0}
      $$
  - **Corner Cell $(0, 2)$:**
    - Symmetrically identical to $(0, 0)$:
      $$
      s = 3, \quad cnt = 4 \implies \left\lfloor \frac{3}{4} \right\rfloor = \mathbf{0}
      $$
  - **Edge Cell $(1, 0)$:**
    - Valid neighbors ($cnt = 6$):
      - Col 0: $(0, 0)=1, (1, 0)=1, (2, 0)=1$
      - Col 1: $(0, 1)=1, (1, 1)=0, (2, 1)=1$
    - Sum: $s = 3 + 2 = 5$.
    - Floor average:
      $$
      ans[1][0] = \left\lfloor \frac{5}{6} \right\rfloor = \mathbf{0}
      $$
  - **Center Interior Cell $(1, 1)$:**
    - Bounding box: all 9 cells of the matrix ($cnt = 9$).
    - Sum of all elements:
      $$
      s = (8 \times 1) + (1 \times 0) = \mathbf{8}
      $$
    - Average calculation:
      $$
      ans[1][1] = \left\lfloor \frac{8}{9} \right\rfloor = \mathbf{0}
      $$
  - **Remaining Cells by Symmetry:**
    - $(1, 2)$: Edge cell $\implies \lfloor 5 / 6 \rfloor = \mathbf{0}$.
    - $(2, 0)$: Corner cell $\implies \lfloor 3 / 4 \rfloor = \mathbf{0}$.
    - $(2, 1)$: Edge cell $\implies \lfloor 5 / 6 \rfloor = \mathbf{0}$.
    - $(2, 2)$: Corner cell $\implies \lfloor 3 / 4 \rfloor = \mathbf{0}$.
  - **Step 6: Matrix Reconstruction:**
    - Every single cell in the filtered image evaluates to $0$ due to floor division:
      $$
      ans = \begin{bmatrix}
      \mathbf{0} & \mathbf{0} & \mathbf{0} \\
      \mathbf{0} & \mathbf{0} & \mathbf{0} \\
      \mathbf{0} & \mathbf{0} & \mathbf{0}
      \end{bmatrix}
      $$
- **Uniform Constant Image ($img = [[100, 100], [100, 100]]$):**
  - All neighbors are $100$.
  - For every cell: sum is $4 \times 100 = 400$, count is 4.
  - Average: $400 / 4 = \mathbf{100}$.

This instance demonstrates discrete 2D spatial convolution and border boundary conditions, mathematically proves why variable-kernel normalization preserves energy bounds while truncating fractional intensities, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ grayscale image:
Apply a $3 \times 3$ box filter smoothing algorithm.
Each cell becomes the **floor of the average** of itself and its valid surrounding neighbors.

```text
Input:
  [ 1, 1, 1 ]
  [ 1, 0, 1 ]
  [ 1, 1, 1 ]

Corner (0, 0): 4 neighbors -> sum = 1+1+1+0 = 3 -> floor(3/4) = 0
Edge   (0, 1): 6 neighbors -> sum = 1+1+1+1+0+1 = 5 -> floor(5/6) = 0
Center (1, 1): 9 neighbors -> sum = 8 -> floor(8/9) = 0

Result: all 0s!
```

### The Invariant of the Moore Neighborhood
- The active window around $(i, j)$ includes all $(x, y)$ such that $|x - i| \le 1$ and $|y - j| \le 1$.
- Only coordinate pairs falling strictly within $[0, m - 1] \times [0, n - 1]$ are summed and counted.

---

## 2. Conceptual Foundation & Invariants

### 1. Convolution Filter Kernel:
For cell $(i, j)$:
$$
ans[i][j] = \left\lfloor \frac{\sum_{x = \max(0, i-1)}^{\min(m-1, i+1)} \sum_{y = \max(0, j-1)}^{\min(n-1, j+1)} img[x][y]}{\sum_{x = \max(0, i-1)}^{\min(m-1, i+1)} \sum_{y = \max(0, j-1)}^{\min(n-1, j+1)} 1} \right\rfloor
$$

### 2. Boundary Neighborhood Sizes:
$$
|\mathcal{N}(i, j)| = \begin{cases} 4 & \text{if corner cell} \\ 6 & \text{if non-corner border cell} \\ 9 & \text{if interior cell} \end{cases}
$$
(For $1 \times k$ or $1 \times 1$ edge cases, neighborhood adapts to 1, 2, or 3).

> **Uniform Spatial Clamping Invariant.** Restricting coordinate iteration to the closed interval intersection $[i-1, i+1] \cap [0, m-1]$ enforces Dirichlet boundary conditions without requiring artificial zero-padding arrays.

---

## 3. Step-by-Step Worked Execution

We trace cell types in the $3 \times 3$ sample:

---

### Step 1: Corner $(0, 0)$
- Range: $x \in [0, 1], y \in [0, 1]$.
- Cells: $(0,0)=1, (0,1)=1, (1,0)=1, (1,1)=0$.
- $s = 3, cnt = 4 \implies \lfloor 3 / 4 \rfloor = \mathbf{0}$.

---

### Step 2: Edge $(0, 1)$
- Range: $x \in [0, 1], y \in [0, 2]$.
- $s = 5, cnt = 6 \implies \lfloor 5 / 6 \rfloor = \mathbf{0}$.

---

### Step 3: Center $(1, 1)$
- Range: all 9 cells.
- $s = 8, cnt = 9 \implies \lfloor 8 / 9 \rfloor = \mathbf{0}$.

---

### Step 4: Output Assembly
- All cells evaluate to **$0$**.

---

## 4. Complete Execution Trace

| Cell $(i, j)$ | Cell Type | Valid Neighborhood Size $cnt$ | Neighbor Values Summed | Total Sum $s$ | $\lfloor s / cnt \rfloor$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | Corner | $4$ | $1 + 1 + 1 + 0$ | $3$ | **`0`** |
| $(0, 1)$ | Edge | $6$ | $1 + 1 + 1 + 1 + 0 + 1$ | $5$ | **`0`** |
| $(0, 2)$ | Corner | $4$ | $1 + 1 + 0 + 1$ | $3$ | **`0`** |
| $(1, 0)$ | Edge | $6$ | $1 + 1 + 1 + 0 + 1 + 1$ | $5$ | **`0`** |
| **$(1, 1)$** | **Center** | **$9$** | **8 ones + 1 zero** | **$8$** | **`0`** |
| $(1, 2)$ | Edge | $6$ | $1 + 0 + 1 + 1 + 1 + 1$ | $5$ | **`0`** |
| $(2, 0)$ | Corner | $4$ | $1 + 0 + 1 + 1$ | $3$ | **`0`** |
| $(2, 1)$ | Edge | $6$ | $1 + 0 + 1 + 1 + 1 + 1$ | $5$ | **`0`** |
| $(2, 2)$ | Corner | $4$ | $0 + 1 + 1 + 1$ | $3$ | **`0`** |

---

## 5. Boundary Cases & Failure Modes

- **$1 \times 1$ Image ($[[5]]$):** Single cell, 1 neighbor $\implies 5 / 1 = 5$.
- **$1 \times N$ Row Image:** Interior cells have 3 neighbors, endpoints have 2.
- **Large Dynamic Range ($[0, 255]$):** Fits comfortably in standard 32-bit integers.
- **In-Place Mutation Bug:** Modifying the input matrix directly contaminates neighbor calculations for subsequent cells. Always write results to a separate output matrix or encode state in higher bits.

---

## 6. Traps & Common Anti-Patterns

- **Dividing by Constant 9:** Assuming all cells have 9 neighbors corrupts boundary cells (e.g. dividing a corner sum of 3 by 9 gives $\lfloor 3/9 \rfloor = 0$, but corner count must be 4).
- **Floating Point Rounding:** Using `round()` in Python can round half to even (e.g. `round(2.5) = 2`), whereas integer floor division `//` strictly truncates towards $-\infty$.
- **Modifying the Input Array In-Place Without Bit Packing:** Overwriting $img[x][y]$ alters the values seen by neighboring cells. Write to a new matrix `ans`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $M \times N$ cells in the grid.
  - Each cell inspects at most 9 neighbors: strictly $\le 9$ operations per cell.
  - Total Time: $\mathcal{O}(M \cdot N)$. For a $200 \times 200$ image, executes $\approx 3.6 \times 10^5$ operations, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space for the output matrix (or $\mathcal{O}(1)$ extra space with 8-bit in-place encoding).
