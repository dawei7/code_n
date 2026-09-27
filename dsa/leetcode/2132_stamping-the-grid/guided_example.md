# Guided Example: Stamping the Grid

We trace the step-by-step execution of the optimal 2D prefix-sum and 2D difference-array stamp coverage approach on a representative problem instance:

- **Input Grid (`grid`):**
  $$\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
- **Stamp Dimensions:** $\text{stampHeight} = 2, \text{stampWidth} = 2$
- **Expected Output:** `true`

This instance illustrates how 2D prefix sums verify obstacle-free rectangular stamp placements in $\mathcal{O}(1)$ time, how 2D difference arrays accumulate overlapping stamp coverage in linear time, and how checking non-zero coverage across all empty cells guarantees feasibility.

---

## 1. Problem Overview & Representative Instance

We are given an $m \times n$ binary matrix `grid` where `0` denotes an empty cell and `1` denotes an occupied obstacle cell. We are also given stamp dimensions $h = \text{stampHeight}$ and $w = \text{stampWidth}$.
We may place any number of $h \times w$ stamps subject to the following rules:
1. Every stamp must lie entirely within the matrix boundaries.
2. A stamp cannot cover any cell containing a `1`.
3. Stamps may freely overlap with one another.
4. Every empty cell (`0`) must be covered by at least one stamp.

Consider our $2 \times 3$ grid of all zeros with $h = 2, w = 2$:
- Dimensions: $m = 2, n = 3$.
- Candidate top-left corners: $(0, 0)$ and $(0, 1)$.
- Stamp at $(0, 0)$ covers columns $0$ and $1$ across rows $0$ and $1$.
- Stamp at $(0, 1)$ covers columns $1$ and $2$ across rows $0$ and $1$.
- The union of both stamps covers all six cells, successfully satisfying the goal.

---

## 2. Mathematical & Algorithmic Principles

### Monotonic Maximality Principle
Because stamp placement does not consume scarce resources and stamps are permitted to overlap arbitrarily, placing a stamp at every valid position is an optimal dominant strategy. A cell $(r, c)$ can be covered if and only if it is covered by the union of all valid stamp placements.

### 2D Prefix Sum for Obstacle Querying
Let $P[r][c]$ denote the number of obstacles in subgrid $[0 \dots r-1] \times [0 \dots c-1]$:

$$P[r][c] = \text{grid}[r-1][c-1] + P[r-1][c] + P[r][c-1] - P[r-1][c-1]$$

For any proposed stamp position with top-left $(r, c)$ and bottom-right $(r + h - 1, c + w - 1)$:

$$\text{Obstacles} = P[r+h][c+w] - P[r][c+w] - P[r+h][c] + P[r][c]$$

The placement is legal if and only if $\text{Obstacles} = 0$.

### 2D Difference Array for Coverage Propagation
To record coverage across the entire $h \times w$ rectangle in $\mathcal{O}(1)$ time, we use a 2D difference array $D$:
- $D[r][c] \leftarrow D[r][c] + 1$
- $D[r][c + w] \leftarrow D[r][c + w] - 1$
- $D[r + h][c] \leftarrow D[r + h][c] - 1$
- $D[r + h][c + w] \leftarrow D[r + h][c + w] + 1$

Accumulating the 2D prefix sums of $D$ yields the exact coverage count $C[r][c]$ for every cell. If any cell has $\text{grid}[r][c] = 0$ and $C[r][c] = 0$, that cell is uncovered, and we return `false`.

| Algorithmic Stage | Data Structure | Operation / Purpose | Time Complexity |
|---|---|---|---|
| Obstacle Detection | 2D Prefix Sum $P$ | Query rectangular obstacle counts | $\mathcal{O}(1)$ per candidate |
| Stamp Registration | 2D Difference Array $D$ | Add $+1$ coverage across $h \times w$ subgrid | $\mathcal{O}(1)$ per placement |
| Coverage Evaluation | Prefix sum on $D$ | Reconstruct cell coverage counts $C[r][c]$ | $\mathcal{O}(m \cdot n)$ total |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Grid dimensions: $m = 2, n = 3$. Stamp dimensions: $h = 2, w = 2$.

### Step 1: Obstacle Prefix Sum $P$
Because `grid` contains all zeros, $P$ is identically zero everywhere:
- All obstacle range queries evaluate to $0$.

### Step 2: Evaluating Candidate Stamp Top-Left Corners
Valid top-left row indices: $0 \le r \le m - h = 2 - 2 = 0$.
Valid top-left column indices: $0 \le c \le n - w = 3 - 2 = 1$.

#### Placement 1: Top-left at $(0, 0)$
- Bottom-right corner: $(0 + 2 - 1, 0 + 2 - 1) = (1, 1)$.
- Obstacle count: $0$. Placement is valid!
- Apply difference updates for rectangle $[0, 1] \times [0, 1]$:
  - $D[0][0] += 1$
  - $D[0][2] -= 1$
  - $D[2][0] -= 1$
  - $D[2][2] += 1$

#### Placement 2: Top-left at $(0, 1)$
- Bottom-right corner: $(0 + 2 - 1, 1 + 2 - 1) = (1, 2)$.
- Obstacle count: $0$. Placement is valid!
- Apply difference updates for rectangle $[0, 1] \times [1, 2]$:
  - $D[0][1] += 1$
  - $D[0][3] -= 1$
  - $D[2][1] -= 1$
  - $D[2][3] += 1$

### Step 3: Prefix Sum Reconstruction of Difference Array $D$
We accumulate $D$ into the coverage matrix $C$:
- Row 0:
  - $C[0][0] = 1$
  - $C[0][1] = 1 + 1 = 2$ (covered by both stamps)
  - $C[0][2] = 2 - 1 = 1$
- Row 1:
  - $C[1][0] = 1$
  - $C[1][1] = 2$
  - $C[1][2] = 1$

Coverage Matrix $C$:
$$\begin{pmatrix} 1 & 2 & 1 \\ 1 & 2 & 1 \end{pmatrix}$$

### Step 4: Verification of Empty Cells
We check each cell:
- $(0, 0)$: $\text{grid} = 0$, $C = 1 > 0$ (Covered)
- $(0, 1)$: $\text{grid} = 0$, $C = 2 > 0$ (Covered)
- $(0, 2)$: $\text{grid} = 0$, $C = 1 > 0$ (Covered)
- $(1, 0)$: $\text{grid} = 0$, $C = 1 > 0$ (Covered)
- $(1, 1)$: $\text{grid} = 0$, $C = 2 > 0$ (Covered)
- $(1, 2)$: $\text{grid} = 0$, $C = 1 > 0$ (Covered)

Every empty cell has $C[r][c] \ge 1$. Output: `true`.

---

## 4. Comprehensive State Trace

The evaluation metrics across all matrix cells are detailed below:

| Grid Cell $(r, c)$ | Obstacle Value | Candidate Corner? | Stamp Placement | Recovered Coverage $C[r][c]$ | Final Status |
|---|---|---|---|---|---|
| $(0, 0)$ | $0$ | Yes (Valid) | $[0, 1] \times [0, 1]$ | $1$ | Covered |
| $(0, 1)$ | $0$ | Yes (Valid) | $[0, 1] \times [1, 2]$ | $2$ | Covered |
| $(0, 2)$ | $0$ | No ($c > n - w$) | None | $1$ | Covered |
| $(1, 0)$ | $0$ | No ($r > m - h$) | None | $1$ | Covered |
| $(1, 1)$ | $0$ | No ($r > m - h$) | None | $2$ | Covered |
| $(1, 2)$ | $0$ | No ($r > m - h$) | None | $1$ | Covered |

Every cell with `grid[r][c] == 0` satisfies $C[r][c] \ge 1$, confirming complete coverage.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** A stamp placement at $(r, c)$ is legal if and only if all cells in $[r, r+h-1] \times [c, c+w-1]$ contain $0$. The 2D prefix sum evaluates the sum of this subgrid in $\mathcal{O}(1)$ time. If the sum is zero, no obstacles are touched. Updating the 2D difference array increments exactly the cells within this subgrid by $1$. When all legal stamps are stamped, $C[r][c]$ reflects the exact number of stamps covering cell $(r, c)$.

**Completeness.** Since adding a stamp never restricts or invalidates other stamps, testing all possible top-left corners creates the maximal possible coverage. If an empty cell remains with $C[r][c] = 0$ after taking the union of all valid stamps, no subset of stamps could ever cover it, guaranteeing zero false positives and zero false negatives.

---

## 6. Edge Cases & Anti-Patterns

- **Stamp Larger than Grid ($h > m$ or $w > n$):** If the stamp dimensions exceed grid dimensions, no stamps can be placed. If the grid contains any empty cells (`0`), the algorithm correctly returns `false`.
- **Completely Occupied Grid:** If all cells contain `1`, no empty cells require coverage, correctly returning `true`.
- **Isolated Empty Pockets:** If an empty cell is surrounded by obstacles such that no $h \times w$ rectangle fits over it, its coverage remains $0$, correctly triggering `false`.
- **Anti-Pattern — Direct Painting of Rectangles:** Iterating over every cell of the stamp upon each placement costs $\mathcal{O}(m \cdot n \cdot h \cdot w)$ time, exceeding time limits on $1000 \times 1000$ matrices. The 2D difference array reduces update cost to $\mathcal{O}(1)$ per placement.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \cdot n)$, where $m$ and $n$ are the matrix dimensions. Building the 2D prefix sum takes $\mathcal{O}(m \cdot n)$. Testing all candidate stamp positions takes $\mathcal{O}((m - h + 1)(n - w + 1)) \le \mathcal{O}(m \cdot n)$ operations. Prefix accumulation of the difference array takes $\mathcal{O}(m \cdot n)$. Overall time is strictly linear in the number of matrix cells.
- **Auxiliary Space Complexity:** $\mathcal{O}(m \cdot n)$ auxiliary space to store the prefix sum matrix and difference matrix.
