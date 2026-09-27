# Guided Example: Largest Plus Sign

We trace the step-by-step 2D grid mine mapping ($grid[r][c] = 0$), 4-directional consecutive ones arm length accumulation (left, right, up, down), 4-way minimum arm bottleneck bound ($order(r, c) = \min(L, R, U, D)$), symmetric dual-pointer row/column scanning, and global maximum order plus sign identification on representative spatial grids:

- **Input:** $n = 5, \quad mines = [[4, 2]]$
- **Required output:** `2`
  - Plus sign geometry & order specifications:
    - An $n \times n$ grid initially consists entirely of `1`s, with specific obstacle cells marked as `0` (`mines`).
    - An axis-aligned plus sign of **order $k$** centered at $(r, c)$ consists of:
      - The center cell $(r, c)$ with value 1.
      - Four arms extending left, right, up, and down, each consisting of $k - 1$ contiguous cells of value 1.
      - Total length along both axes: $2k - 1$.
      - If $k = 1$, the plus sign is just a single cell of value 1.
    - Objective: Find the **maximum order $k$** among all possible centers $(r, c)$. If no 1s exist, return `0`.
    - For $n = 5$ with a mine at $(4, 2)$:
      - Center candidate $(2, 2)$:
        - Up arm: cells $(1, 2), (0, 2) \implies$ extends 2 steps (total length 3).
        - Left arm: cells $(2, 1), (2, 0) \implies$ extends 2 steps (total length 3).
        - Right arm: cells $(2, 3), (2, 4) \implies$ extends 2 steps (total length 3).
        - Down arm: cell $(3, 2)$ is 1, but cell $(4, 2)$ is a mine (`0`)! The down arm is blocked at distance 1.
        - Bottleneck arm:
          $$
          \text{order}(2, 2) = \min(\text{Left}: 3, \; \text{Right}: 3, \; \text{Up}: 3, \; \text{Down}: 2) = \mathbf{2}
          $$
      - An order 3 plus sign would require down arm reaching $(4, 2)$, which is obstructed.
      - Maximum achievable order is **2**.
- **4-Directional Arm Minimum & Dynamic Programming Invariant:**
  - **The Bottleneck Property:**
    - The largest order plus sign centered at any cell $(r, c)$ is strictly constrained by the **shortest** of its 4 contiguous arms of 1s:
      $$
      order(r, c) = \min\big(left[r][c], \; right[r][c], \; up[r][c], \; down[r][c]\big)
      $$
    - If cell $(r, c)$ is a mine, its order is 0.
  - **Simultaneous Symmetric Scanning:**
    - Initialize an $n \times n$ table $dp[r][c]$ to $n$ (or 0 for mines).
    - For each row/column index $i \in [0, n - 1]$:
      - Scan bidirectional coordinates $j \in [0, n - 1]$ and $k = n - 1 - j$:
        - Accumulate running count of 1s:
          $$
          left = (left + 1) \text{ if } dp[i][j] > 0 \text{ else } 0
          $$
          $$
          right = (right + 1) \text{ if } dp[i][k] > 0 \text{ else } 0
          $$
          $$
          up = (up + 1) \text{ if } dp[j][i] > 0 \text{ else } 0
          $$
          $$
          down = (down + 1) \text{ if } dp[k][i] > 0 \text{ else } 0
          $$
        - Refine $dp$ at each point by taking the minimum:
          $$
          dp[i][j] \leftarrow \min(dp[i][j], \; left)
          $$
          $$
          dp[i][k] \leftarrow \min(dp[i][k], \; right)
          $$
          $$
          dp[j][i] \leftarrow \min(dp[j][i], \; up)
          $$
          $$
          dp[k][i] \leftarrow \min(dp[k][i], \; down)
          $$
    - After all 4 directional sweeps, each cell $dp[r][c]$ contains the exact bottleneck order.
    - Global answer:
      $$
      ans = \max_{r, c} dp[r][c]
      $$
- **Step-by-Step Worked Execution Trace on Center $(2, 2)$ ($n = 5$):**
  - Grid dimensions: $5 \times 5$, mine at $(4, 2)$.
  - **Step 1: Measure Left Arm from Column 0 to Column 4 along Row 2:**
    - $(2, 0) = 1 \implies left = 1$.
    - $(2, 1) = 1 \implies left = 2$.
    - $(2, 2) = 1 \implies left = \mathbf{3}$.
    - $(2, 3) = 1 \implies left = 4$.
    - $(2, 4) = 1 \implies left = 5$.
    - Left count at $(2, 2)$ is $3$.
  - **Step 2: Measure Right Arm from Column 4 down to Column 0 along Row 2:**
    - $(2, 4) = 1 \implies right = 1$.
    - $(2, 3) = 1 \implies right = 2$.
    - $(2, 2) = 1 \implies right = \mathbf{3}$.
    - Right count at $(2, 2)$ is $3$.
  - **Step 3: Measure Up Arm from Row 0 to Row 4 along Column 2:**
    - $(0, 2) = 1 \implies up = 1$.
    - $(1, 2) = 1 \implies up = 2$.
    - $(2, 2) = 1 \implies up = \mathbf{3}$.
    - Up count at $(2, 2)$ is $3$.
  - **Step 4: Measure Down Arm from Row 4 up to Row 0 along Column 2:**
    - $(4, 2) = 0 \implies \mathbf{Mine!} \quad down = 0$.
    - $(3, 2) = 1 \implies down = 1$.
    - $(2, 2) = 1 \implies down = 1 + 1 = \mathbf{2}$.
    - $(1, 2) = 1 \implies down = 3$.
    - Down count at $(2, 2)$ is $2$.
  - **Step 5: Compute Center $(2, 2)$ Order:**
    - Take the minimum across all 4 cardinal directions:
      $$
      order(2, 2) = \min(left: 3, \; right: 3, \; up: 3, \; down: 2) = \mathbf{2}
      $$
  - **Step 6: Inspect Global Optimum:**
    - All other potential centers closer to the grid boundaries have at most arm length 2.
    - No cell can achieve order $\ge 3$ because $(2, 2)$ is the only cell with margin 2 from all 4 boundaries, and its down arm is curtailed by the mine.
    - Maximum order across the entire grid:
      $$
      ans = \mathbf{2}
      $$
- **Single Mined Cell Grid Trace ($n = 1, mines = [[0, 0]]$):**
  - Cell $(0, 0)$ is 0.
  - $dp[0][0] = 0 \implies ans = \mathbf{0}$.
- **Unobstructed Grid ($n = 5, mines = []$):**
  - Symmetric center $(2, 2)$ has $L = 3, R = 3, U = 3, D = 3$.
  - Order is $\min(3, 3, 3, 3) = \mathbf{3}$.

This instance demonstrates multidirectional dynamic programming and spatial cross-neighborhood minimization, mathematically proves why pointwise minimum over 4 directional distance fields computes the exact radius of maximal cross-polytopes, and derives $O(N^2)$ runtime and $O(N^2)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ grid with obstacles (`mines`):
Find the **order of the largest plus sign** of 1s (center and 4 arms of length $k-1$).
Return 0 if no 1s exist.

```text
n = 5, mine at (4, 2)

Grid:
  1 1 1 1 1
  1 1 1 1 1
  1 1 1 1 1  <- Center at (2, 2)
  1 1 1 1 1
  1 1 0 1 1  <- Mine at (4, 2) blocks the down arm!

At center (2, 2):
  Up arm:    extends to (0, 2) -> length 3
  Left arm:  extends to (2, 0) -> length 3
  Right arm: extends to (2, 4) -> length 3
  Down arm:  blocked by (4, 2) -> length 2

Order = min(3, 3, 3, 2) = 2.
Result: 2
```

### The Invariant of the 4-Directional Minimum
- The maximum order of a plus sign centered at $(r, c)$ equals the minimum consecutive 1s extending left, right, up, and down: $order(r, c) = \min(L, R, U, D)$.
- Accumulating running counts in each direction allows finding all arm lengths in $O(N^2)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Directional Arm Extension:
For each cell $(r, c)$ with $grid[r][c] = 1$:
$$
L(r, c) = L(r, c - 1) + 1, \quad R(r, c) = R(r, c + 1) + 1
$$
$$
U(r, c) = U(r - 1, c) + 1, \quad D(r, c) = D(r + 1, c) + 1
$$

### 2. Center Order Evaluation:
$$
order(r, c) = \min(L(r, c), \; R(r, c), \; U(r, c), \; D(r, c))
$$
$$
ans = \max_{r, c} order(r, c)
$$

> **Cross-Polytope Metric Invariant.** The order of an axis-aligned plus sign centered at $x \in \mathbb{Z}^2$ is the maximal radius $k$ such that the discrete $L_1$ cross-polytope star $S_k(x) = \{x \pm m e_i \mid 0 \le m < k, \; i \in \{1, 2\}\}$ is contained in the free domain $V \setminus mines$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 5, mines = [[4, 2]]$ at center $(2, 2)$:

---

### Step 1: Initialize
- Set $(4, 2)$ to 0.

---

### Step 2: Compute Arms at $(2, 2)$
- Left: 3 cells $(2, 0), (2, 1), (2, 2) \implies L = 3$.
- Right: 3 cells $(2, 4), (2, 3), (2, 2) \implies R = 3$.
- Up: 3 cells $(0, 2), (1, 2), (2, 2) \implies U = 3$.
- Down: mine at $(4, 2) \implies$ only 2 cells $(3, 2), (2, 2) \implies D = 2$.

---

### Step 3: Minimum Arm
- $\min(3, 3, 3, 2) = \mathbf{2}$.

---

### Step 4: Output
$$
ans = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Candidate Center $(r, c)$ | Left Arm $L$ | Right Arm $R$ | Up Arm $U$ | Down Arm $D$ | Bottleneck Order $\min(L, R, U, D)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(2, 2)$ | $3$ | $3$ | $3$ | **$2$ (blocked by mine)** | **`2`** |
| $(1, 2)$ | $3$ | $3$ | $2$ (boundary) | $3$ | $2$ |
| $(2, 1)$ | $2$ | $4$ | $3$ | $3$ | $2$ |
| $(2, 3)$ | $4$ | $2$ | $3$ | $3$ | $2$ |
| **Max** | — | — | — | — | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **All Mined Grid ($n = 1, mines = [[0, 0]]$):** No 1s $\implies$ returns 0.
- **Empty Mines ($mines = []$):** Center has $\lceil n / 2 \rceil$ in all directions $\implies$ order $\lceil n / 2 \rceil$.
- **Mines along Perimeter:** Reduces arm lengths for interior cells reaching the boundary.
- **Order 1 (Isolated Single 1):** Cell with 1 surrounded by mines has order 1.

---

## 6. Traps & Common Anti-Patterns

- **Expanding Arms Radially for Every Cell ($O(N^3)$):** Expanding outwards from every candidate center takes $O(N)$ per cell, leading to $O(N^3)$ total time ($500^3 = 1.25 \times 10^8$, dangerously close to TLE). 4-directional DP precomputation runs in strictly $O(N^2)$.
- **Using 4 Separate $N \times N$ Matrices:** Allocating 4 full matrices uses excessive memory. A single $dp$ array updated in-place via $\min$ achieves the exact same result in $\mathcal{O}(N^2)$ space.
- **Off-By-One on Plus Sign Order:** A plus sign of order $k$ has arm length $k - 1$ plus the center cell, so total consecutive 1s in that direction equals $k$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass to mark mines in $dp$: $\mathcal{O}(|mines|)$.
  - Outer loop runs $N$ times; inner loop sweeps $N$ elements across 4 directions: $\mathcal{O}(N^2)$.
  - Total Time: strictly $\mathcal{O}(N^2)$ where $N \le 500 \implies \le 2.5 \times 10^5$ operations. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ memory for the $dp$ grid matrix.