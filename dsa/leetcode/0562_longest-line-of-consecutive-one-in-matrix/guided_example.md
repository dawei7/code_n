# Guided Example: Longest Line of Consecutive One in Matrix

We trace the step-by-step 4-directional dynamic programming state expansion (vertical $a$, horizontal $b$, main diagonal $c$, anti-diagonal $d$), zero-padded sentinel boundary framing ($m+2 \times n+2$), directional recurrence transitions, and global maximum line length tracking on representative binary matrices:

- **Input:**
  $$
  mat = \begin{bmatrix}
  0 & 1 & 1 & 0 \\
  0 & 1 & 1 & 0 \\
  0 & 0 & 0 & 1
  \end{bmatrix}
  $$
- **Required output:** `3`
  - Grid dimensions: $m = 3$ rows, $n = 4$ columns.
  - Objective: Find the maximum length of a continuous line of `1`s running in any of the four principal directions:
    1. **Horizontal** (left to right)
    2. **Vertical** (top to bottom)
    3. **Diagonal** (top-left to bottom-right, $\searrow$)
    4. **Anti-Diagonal** (top-right to bottom-left, $\swarrow$)
- **4-Directional DP State Decomposition:**
  - For each cell $(i, j)$ in 1-based padded coordinates ($1 \le i \le m, 1 \le j \le n$):
    - If $mat[i-1][j-1] == 0$: All directional lengths reset to $0$.
    - If $mat[i-1][j-1] == 1$:
      - **Vertical line:** Extends from the cell directly above $(i-1, j)$:
        $$
        a[i][j] = a[i-1][j] + 1
        $$
      - **Horizontal line:** Extends from the cell directly to the left $(i, j-1)$:
        $$
        b[i][j] = b[i][j-1] + 1
        $$
      - **Main Diagonal ($\searrow$):** Extends from the top-left neighbor $(i-1, j-1)$:
        $$
        c[i][j] = c[i-1][j-1] + 1
        $$
      - **Anti-Diagonal ($\swarrow$):** Extends from the top-right neighbor $(i-1, j+1)$:
        $$
        d[i][j] = d[i-1][j+1] + 1
        $$
      - Update global maximum: $ans \leftarrow \max(ans, a[i][j], b[i][j], c[i][j], d[i][j])$.
- **Execution trace on the $3 \times 4$ grid:**
  - **Row 0 ($i = 1$ in padded grid): $mat[0] = [0, 1, 1, 0]$:**
    - Cell $(0, 1)$ is `1` ($i=1, j=2$):
      - $a = 1, \; b = 1, \; c = 1, \; d = 1 \implies ans = 1$.
    - Cell $(0, 2)$ is `1` ($i=1, j=3$):
      - $a = 1$.
      - Horizontal from $(0, 1)$: $b[1][3] = b[1][2] + 1 = 1 + 1 = \mathbf{2}$.
      - $c = 1, \; d = 1$.
      - Max so far: $ans \leftarrow \max(1, 2) = \mathbf{2}$.
  - **Row 1 ($i = 2$ in padded grid): $mat[1] = [0, 1, 1, 0]$:**
    - Cell $(1, 1)$ is `1` ($i=2, j=2$):
      - Vertical from $(0, 1)$: $a[2][2] = a[1][2] + 1 = 1 + 1 = \mathbf{2}$.
      - Horizontal: $b = 1$.
      - Main diagonal from $(0, 0)$: $c[2][2] = c[1][1] + 1 = 0 + 1 = 1$.
      - Anti-diagonal from $(0, 2)$: $d[2][2] = d[1][3] + 1 = 1 + 1 = \mathbf{2}$.
    - Cell $(1, 2)$ is `1` ($i=2, j=3$):
      - Vertical from $(0, 2)$: $a[2][3] = a[1][3] + 1 = 1 + 1 = \mathbf{2}$.
      - Horizontal from $(1, 1)$: $b[2][3] = b[2][2] + 1 = 1 + 1 = \mathbf{2}$.
      - Main diagonal from $(0, 1)$:
        $$
        c[2][3] = c[1][2] + 1 = 1 + 1 = \mathbf{2}
        $$
      - Anti-diagonal: $d = 1$.
  - **Row 2 ($i = 3$ in padded grid): $mat[2] = [0, 0, 0, 1]$:**
    - Cell $(2, 3)$ is `1` ($i=3, j=4$):
      - Vertical: $a = 0 + 1 = 1$.
      - Horizontal: $b = 0 + 1 = 1$.
      - Main diagonal extending from $(1, 2)$ (which had $c = 2$):
        $$
        c[3][4] = c[2][3] + 1 = 2 + 1 = \mathbf{3}
        $$
      - Anti-diagonal: $d = 0 + 1 = 1$.
      - Update global maximum:
        $$
        ans \leftarrow \max(2, 3) = \mathbf{3}
        $$
  - Traversal completes.
  - Final longest line length: **`3`** (The continuous main diagonal: $(0, 1) \to (1, 2) \to (2, 3)$).
- **Anti-Diagonal Winner Instance:**
  $$
  mat = \begin{bmatrix}
  0 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 0
  \end{bmatrix}
  $$
  - Anti-diagonal $d$ chains from $(0, 2) \to (1, 1) \to (2, 0) \implies \mathbf{3}$.
- **All Zeros Matrix:**
  - No 1s present $\implies ans = \mathbf{0}$.
- **All Ones $N \times N$ Matrix:**
  - Main diagonal length reaches $\mathbf{N}$.

This instance demonstrates multidirectional recurrence propagation across 2D Cartesian topologies, mathematically proves why tracking four directional vectors avoids redundant ray tracing, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ binary matrix $mat$:
Find the length of the **longest line of consecutive ones** in the matrix.
The line can be:
- Horizontal ($\rightarrow$)
- Vertical ($\downarrow$)
- Diagonal ($\searrow$)
- Anti-Diagonal ($\swarrow$)

```text
Matrix:
  [ 0,  1,  1,  0 ]
  [ 0,  1,  1,  0 ]
  [ 0,  0,  0,  1 ]

Highlighted Main Diagonal:
  (0, 1) = 1
         \
          (1, 2) = 1
                 \
                  (2, 3) = 1

Length = 3 consecutive ones
```

### Eliminating Redundant Raycasting with 4-Way DP
- A naive approach would trace outward in 4 directions from every `1` cell, resulting in repeated scans and $O((M \cdot N) \cdot \max(M, N))$ runtime.
- By utilizing dynamic programming, every cell $(i, j)$ queries only its **immediate predecessor** in each of the 4 directions.
- A single raster pass computes all 4 lengths for every cell in $O(1)$ time per cell, guaranteeing strictly linear $O(M \cdot N)$ time!

---

## 2. Conceptual Foundation & Invariants

### 1. Sentinel Padding:
Allocate four 2D DP arrays of size $(m + 2) \times (n + 2)$ initialized to $0$:
- Vertical: $a[i][j]$
- Horizontal: $b[i][j]$
- Diagonal: $c[i][j]$
- Anti-Diagonal: $d[i][j]$
The extra rows and columns eliminate all boundary-check branching (`if i > 0`, `if j < n - 1`, etc.).

### 2. Recurrence Equations (for $mat[i-1][j-1] == 1$):
$$
\begin{aligned}
a[i][j] &= a[i-1][j] + 1 \\
b[i][j] &= b[i][j-1] + 1 \\
c[i][j] &= c[i-1][j-1] + 1 \\
d[i][j] &= d[i-1][j+1] + 1
\end{aligned}
$$

### 3. Global Tracking:
$$
ans \leftarrow \max(ans, \; a[i][j], \; b[i][j], \; c[i][j], \; d[i][j])
$$

> **Top-Down Predecessor Invariant.** Processing the matrix row-by-row guarantees that the top, left, top-left, and top-right neighbors of $(i, j)$ are fully evaluated before cell $(i, j)$ is processed.

---

## 3. Step-by-Step Worked Execution

We trace cell $(2, 3)$ in padded coordinates ($mat[2][3] = 1$ at row 2, col 3):

---

### Step 1: Predecessor Lookup
- Above neighbor $(1, 3)$: $mat[1][3] = 0 \implies a[2][4] = 0$.
  $a[3][4] = 0 + 1 = 1$.
- Left neighbor $(2, 2)$: $mat[2][2] = 0 \implies b[3][3] = 0$.
  $b[3][4] = 0 + 1 = 1$.
- Top-Left neighbor $(1, 2)$: $c[2][3] = \mathbf{2}$.
  $$
  c[3][4] = c[2][3] + 1 = 2 + 1 = \mathbf{3}
  $$
- Top-Right neighbor $(1, 4)$: $mat[1][4]$ out of bounds $\implies 0$.
  $d[3][4] = 0 + 1 = 1$.

---

### Step 2: Directional Comparison
- Directions at $(2, 3)$:
  - Vertical: $1$
  - Horizontal: $1$
  - Diagonal: $\mathbf{3}$
  - Anti-Diagonal: $1$
- Update running maximum:
  $$
  ans \leftarrow \max(2, 3) = \mathbf{3}
  $$

---

## 4. Complete Execution Trace

| Padded Cell $(i, j)$ | Matrix Value | Vertical $a$ | Horizontal $b$ | Diagonal $c$ | Anti-Diagonal $d$ | Running Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(1, 2)$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ |
| $(1, 3)$ | $1$ | $1$ | $2$ | $1$ | $1$ | $2$ |
| $(2, 2)$ | $1$ | $2$ | $1$ | $1$ | $2$ | $2$ |
| $(2, 3)$ | $1$ | $2$ | $2$ | $2$ | $1$ | $2$ |
| **$(3, 4)$** | **$1$** | **$1$** | **$1$** | **$3$** | **$1$** | **`3`** |
| **Result** | — | — | — | Peak: Diagonal | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Cell ($[[1]]$):** $a = b = c = d = 1 \implies ans = 1$.
- **No Ones ($[[0, 0], [0, 0]]$):** Condition `if mat[i-1][j-1]` never triggers $\implies ans = 0$.
- **Anti-Diagonal on Right Edge:** Padded width $n + 2$ ensures that looking at $(i-1, j+1)$ when $j = n$ accesses index $n + 1$ without IndexError.
- **Narrow $1 \times N$ or $M \times 1$ Matrices:** Handled seamlessly by horizontal and vertical recurrence terms.

---

## 6. Traps & Common Anti-Patterns

- **Missing Anti-Diagonal Direction:** Forgetting to check top-right predecessor $(i-1, j+1)$ fails on matrices where lines slant upward-right ($\swarrow$ / $\nearrow$).
- **Index Out of Range on Anti-Diagonal:** Looking up $(i-1, j+1)$ on the rightmost column crashes standard unpadded arrays. Padding the column dimension by $+2$ provides a protective zero border.
- **Resetting Across Zeros:** If a cell is 0, its DP values must remain 0. Leaving stale non-zero values carries streaks across broken gaps.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Two nested loops iterate over $M$ rows and $N$ columns.
  - Inside the loop, 4 additions and a 4-way maximum take $\mathcal{O}(1)$ operations.
  - Total Time: strictly linear $\mathcal{O}(M \cdot N)$. For $M \cdot N = 10^4$, finishes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space for the four $(M+2) \times (N+2)$ DP tables (can be compressed to $O(N)$ with rolling rows).
