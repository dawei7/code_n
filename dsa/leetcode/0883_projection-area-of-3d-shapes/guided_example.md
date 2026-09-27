# Guided Example: Projection Area of 3D Shapes

We trace the step-by-step orthogonal projection decomposition across three coordinate planes ($xy, yz, zx$), non-zero footprint counting, row-wise maximum silhouette aggregation, column-wise maximum silhouette aggregation, and total surface projection area summation on representative 3D voxel grids:

- **Input:**
  $$
  grid = \begin{bmatrix}
  1 & 2 \\
  3 & 4
  \end{bmatrix}
  $$
- **Required output:** `17`
  - 3D voxel geometry & projections:
    - On an $n \times n$ grid, each cell $(i, j)$ contains a vertical tower of $1 \times 1 \times 1$ unit cubes with height $v = grid[i][j]$.
    - We project the shape orthogonally onto three perpendicular planes:
      1. **$xy$-plane (Top View / Footprint):** Looking down from $+z$.
      2. **$yz$-plane (Side View / Row Silhouettes):** Looking along the $x$-axis.
      3. **$zx$-plane (Front View / Column Silhouettes):** Looking along the $y$-axis.
    - Objective: Return the total area of all three projections combined.
    - For $grid = [[1, 2], [3, 4]]$:
      - Top ($xy$): All 4 grid cells have height $> 0 \implies \text{Area}_{xy} = 4$.
      - Side ($yz$): Row 0 max is $2$, Row 1 max is $4 \implies \text{Area}_{yz} = 2 + 4 = 6$.
      - Front ($zx$): Column 0 max is $3$, Column 1 max is $4 \implies \text{Area}_{zx} = 3 + 4 = 7$.
      - Total projection area: $4 + 6 + 7 = \mathbf{17}$.
- **The Orthogonal Projection Invariant:**
  - **$xy$-Plane (Ground Footprint):**
    - The vertical height does not matter as long as at least one cube is present.
    - Each cell $(i, j)$ with $grid[i][j] > 0$ contributes exactly $1$ square unit to the ground shadow:
      $$
      \text{Area}_{xy} = \sum_{i=0}^{n-1} \sum_{j=0}^{n-1} \mathbb{I}[grid[i][j] > 0]
      $$
  - **$yz$-Plane (Row Silhouettes):**
    - When viewed from the side along row $i$, cubes at different columns $j$ overlap.
    - The shadow height cast by row $i$ is determined entirely by the **tallest tower in row $i$**:
      $$
      \text{Area}_{yz} = \sum_{i=0}^{n-1} \max_{0 \le j < n} (grid[i][j])
      $$
  - **$zx$-Plane (Column Silhouettes):**
    - When viewed from the front along column $j$, cubes at different rows $i$ overlap.
    - The shadow height cast by column $j$ is determined entirely by the **tallest tower in column $j$**:
      $$
      \text{Area}_{zx} = \sum_{j=0}^{n-1} \max_{0 \le i < n} (grid[i][j])
      $$
  - Total projection area is the direct algebraic sum of these three independent plane projections.

---

## 1. Instance & Teaching Goal

Given the $2 \times 2$ height map:
$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$
Derive each of the three orthogonal projection shadows.

```text
Top View (xy-plane):
  [1] [2]   -> 4 non-zero cells
  [3] [4]   Area = 4

Side View (yz-plane, along rows):
  Row 0: max(1, 2) = 2
  Row 1: max(3, 4) = 4
  Area = 2 + 4 = 6

Front View (zx-plane, along columns):
  Col 0: max(1, 3) = 3
  Col 1: max(2, 4) = 4
  Area = 3 + 4 = 7

Total Projection Area = 4 + 6 + 7 = 17
```

The teaching goal is to demonstrate how multi-view architectural drawing projections reduce to independent 1D reductions over rows and columns.

---

## 2. Conceptual Foundation & Invariants

### 1. Mathematical Area Formula:
$$
\text{Total Area} = \underbrace{\sum_{i=0}^{n-1} \sum_{j=0}^{n-1} [grid[i][j] > 0]}_{\text{Top (xy)}} + \underbrace{\sum_{i=0}^{n-1} \max_j (grid[i][j])}_{\text{Side (yz)}} + \underbrace{\sum_{j=0}^{n-1} \max_i (grid[i][j])}_{\text{Front (zx)}}
$$

---

## 3. Step-by-Step Worked Execution

We trace $grid = [[1, 2], [3, 4]]$:

---

### Step 1: Compute Top View Area ($xy$-plane)
- Cell $(0, 0) = 1 > 0 \implies +1$
- Cell $(0, 1) = 2 > 0 \implies +1$
- Cell $(1, 0) = 3 > 0 \implies +1$
- Cell $(1, 1) = 4 > 0 \implies +1$
$$
\text{Area}_{xy} = 1 + 1 + 1 + 1 = \mathbf{4}
$$

---

### Step 2: Compute Side View Area ($yz$-plane)
- Row $0$: heights $[1, 2]$. Maximum height: $\max(1, 2) = 2$.
- Row $1$: heights $[3, 4]$. Maximum height: $\max(3, 4) = 4$.
$$
\text{Area}_{yz} = 2 + 4 = \mathbf{6}
$$

---

### Step 3: Compute Front View Area ($zx$-plane)
- Column $0$: heights $[1, 3]$. Maximum height: $\max(1, 3) = 3$.
- Column $1$: heights $[2, 4]$. Maximum height: $\max(2, 4) = 4$.
$$
\text{Area}_{zx} = 3 + 4 = \mathbf{7}
$$

---

### Step 4: Sum All Three Projections
$$
\text{Total Area} = \text{Area}_{xy} + \text{Area}_{yz} + \text{Area}_{zx} = 4 + 6 + 7 = \mathbf{17}
$$

---

## 4. Complete Execution Trace

| Coordinate Plane | View Direction | Entity Evaluated | Heights Considered | Projected Area Contribution |
|:---:|:---:|:---:|:---:|:---:|
| $xy$ (Top) | Along $-z$ | All 4 cells | $[1, 2, 3, 4]$ (all $> 0$) | $4$ |
| $yz$ (Side) | Along $+x$ | Row $0$ | $[1, 2]$ | $\max(1, 2) = 2$ |
| $yz$ (Side) | Along $+x$ | Row $1$ | $[3, 4]$ | $\max(3, 4) = 4$ |
| $zx$ (Front) | Along $+y$ | Column $0$ | $[1, 3]$ | $\max(1, 3) = 3$ |
| $zx$ (Front) | Along $+y$ | Column $1$ | $[2, 4]$ | $\max(2, 4) = 4$ |
| **Combined** | **All 3 Planes** | **Full Grid** | **Sum of all projections** | **`4 + 6 + 7 = 17`** |

---

## 5. Boundary Cases & Failure Modes

- **Cells with Height $0$:** A cell with $0$ cubes contributes $0$ to the $xy$ footprint. If an entire row has height $0$, row max is $0$.
- **$1 \times 1$ Grid (`[[2]]`):**
  - $xy$: $1$ (since $2 > 0$).
  - $yz$: $2$ (row max).
  - $zx$: $2$ (column max).
  - Total: $1 + 2 + 2 = 5$.
- **Flat Surface (All heights equal $1$ on $n \times n$):**
  - $xy$: $n^2$.
  - $yz$: $n \times 1 = n$.
  - $zx$: $n \times 1 = n$.
  - Total: $n^2 + 2n$.

---

## 6. Traps & Common Anti-Patterns

- **Counting Cube Faces (Exposed Surface Area):** This problem asks for the **shadow projection area**, not the full 3D surface area. Internal faces or hidden steps do not increase shadow size.
- **Transposing Manually with Nested Arrays:** Running column maximums during the row scan or using `zip(*grid)` computes column maximums cleanly without memory duplication.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single pass over all $n \times n$ cells: $\mathcal{O}(n^2)$.
  - Tallying non-zeros, row maxes, and column maxes takes $\mathcal{O}(1)$ per cell.
  - Total Time: strictly $\mathcal{O}(n^2)$, completing in $< 1$ ms for $n \le 50$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ additional memory if streaming column maximums in-place (or $\mathcal{O}(n)$ to store column maximums).
