# Guided Example: Maximal Square

We trace the step-by-step 2D dynamic programming grid recurrence, bottom-right corner invariant, and 1D rolling array optimization on representative binary character matrices:

- **Input:**
  $$
  \text{matrix} = \begin{bmatrix}
  \text{"1"} & \text{"0"} & \text{"1"} & \text{"0"} & \text{"0"} \\
  \text{"1"} & \text{"0"} & \text{"1"} & \text{"1"} & \text{"1"} \\
  \text{"1"} & \text{"1"} & \text{"1"} & \text{"1"} & \text{"1"} \\
  \text{"1"} & \text{"0"} & \text{"0"} & \text{"1"} & \text{"0"}
  \end{bmatrix}
  $$
- **Required output:** $4$ (Largest square of `'1'`s has side length $2$; area $= 2 \times 2 = 4$)
- **Checkerboard Instance:** $\text{matrix} = [[\text{"0"}, \text{"1"}], [\text{"1"}, \text{"0"}]] \implies 1$ (Only $1 \times 1$ squares possible)
- **All Zeroes Instance:** $\text{matrix} = [[\text{"0"}]] \implies 0$
- **Single One Instance:** $\text{matrix} = [[\text{"1"}]] \implies 1$

This instance demonstrates geometric subproblem decomposition in grid graphs, mathematically proves why the side length of an all-ones square ending at $(i, j)$ equals $\min(\text{top}, \text{left}, \text{top-left}) + 1$, details rolling 1D memory compression, and runs in $O(M \cdot N)$ time.

---

## 1. Instance & Teaching Goal

Given a $4 \times 5$ binary character matrix:
```text
1  0  1  0  0
1  0  1  1  1
1  1  1  1  1
1  0  0  1  0
```
Find the largest square containing only `'1'`s and compute its **area** ($\text{side}^2$).

Examining candidate square regions:
- There are multiple $1 \times 1$ squares.
- Look at rows $1 \dots 2$ and columns $2 \dots 4$:
  Submatrix $[1 \dots 2][2 \dots 3]$:
  $$
  \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \implies \text{Side } 2, \; \text{Area } 4
  $$
  Submatrix $[1 \dots 2][3 \dots 4]$:
  $$
  \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \implies \text{Side } 2, \; \text{Area } 4
  $$
- No $3 \times 3$ all-ones square exists (any $3 \times 3$ candidate contains at least one `'0'`).
The maximum square side is $2$, yielding area $2^2 = \mathbf{4}$.

A brute-force search enumerates all $(r, c)$ and expands side lengths $k$, taking $O(M \cdot N \cdot \min(M, N)^2)$ time.
Dynamic programming reduces this to a single $O(M \cdot N)$ pass by memoizing the maximum side length ending at each cell.

---

## 2. Conceptual Foundation & Invariants

### Dynamic Programming State Definition
Let $DP[i][j]$ represent the **side length of the largest all-ones square whose bottom-right corner is at cell $(i, j)$**.

### Transition Recurrence:
1. If $\text{matrix}[i][j] == \text{'0'}$:
   $$
   DP[i][j] = 0
   $$
   (A square of ones cannot end at a zero cell).
2. If $\text{matrix}[i][j] == \text{'1'}$:
   - For boundary cells ($i = 0$ or $j = 0$):
     $$
     DP[i][j] = 1
     $$
   - For internal cells ($i > 0$ and $j > 0$):
     $$
     DP[i][j] = \min\big(DP[i-1][j], \; DP[i][j-1], \; DP[i-1][j-1]\big) + 1
     $$

### Why the Minimum of Three Neighbors?
For a square of side $k$ to have its bottom-right corner at $(i, j)$:
- The cell directly above $(i-1, j)$ must end a square of side at least $k - 1$ (providing vertical height).
- The cell directly to the left $(i, j-1)$ must end a square of side at least $k - 1$ (providing horizontal width).
- The diagonal cell $(i-1, j-1)$ must end a square of side at least $k - 1$ (ensuring the interior is completely filled with ones).
If any of these three neighbors has side length $< k - 1$, a hole (a `'0'`) enters the square. Thus, the expansion is strictly constrained by the minimum of the three.

> **Invariant.** For all $i, j$, $DP[i][j]$ is strictly equal to the largest integer $k$ such that $\text{matrix}[i - r][j - c] == \text{'1'}$ for all $0 \le r, c < k$.

---

## 3. Step-by-Step Worked Execution

We compute the $DP$ table row by row for the $4 \times 5$ matrix:

### Row 0: `["1", "0", "1", "0", "0"]`
Boundary row ($i = 0$). $DP[0][j] = 1$ if $\text{matrix}[0][j] == \text{'1'}$ else $0$:
$$
DP[0] = [1, 0, 1, 0, 0] \quad (\max = 1)
$$

---

### Row 1: `["1", "0", "1", "1", "1"]`
- $j = 0$: Boundary $\implies DP[1][0] = 1$.
- $j = 1$: Value is `'0'` $\implies DP[1][1] = 0$.
- $j = 2$: Value `'1'`. Neighbors: $\text{top}=1, \text{left}=0, \text{diag}=0$.
  $$
  DP[1][2] = \min(1, 0, 0) + 1 = 0 + 1 = 1
  $$
- $j = 3$: Value `'1'`. Neighbors: $\text{top}=0, \text{left}=1, \text{diag}=1$.
  $$
  DP[1][3] = \min(0, 1, 1) + 1 = 0 + 1 = 1
  $$
- $j = 4$: Value `'1'`. Neighbors: $\text{top}=0, \text{left}=1, \text{diag}=0$.
  $$
  DP[1][4] = \min(0, 1, 0) + 1 = 0 + 1 = 1
  $$
Row 1 result: $DP[1] = [1, 0, 1, 1, 1]$.

---

### Row 2: `["1", "1", "1", "1", "1"]`
- $j = 0$: Boundary $\implies DP[2][0] = 1$.
- $j = 1$: Value `'1'`. Neighbors: $\text{top}=0, \text{left}=1, \text{diag}=1 \implies \min(0, 1, 1) + 1 = 1$.
- $j = 2$: Value `'1'`. Neighbors: $\text{top}=1, \text{left}=1, \text{diag}=0 \implies \min(1, 1, 0) + 1 = 1$.
- $j = 3$: Value `'1'`. Neighbors:
  - $\text{Top } DP[1][3] = 1$
  - $\text{Left } DP[2][2] = 1$
  - $\text{Diagonal } DP[1][2] = 1$
  $$
  DP[2][3] = \min(1, 1, 1) + 1 = 1 + 1 = \mathbf{2}!
  $$
- $j = 4$: Value `'1'`. Neighbors:
  - $\text{Top } DP[1][4] = 1$
  - $\text{Left } DP[2][3] = 2$
  - $\text{Diagonal } DP[1][3] = 1$
  $$
  DP[2][4] = \min(1, 2, 1) + 1 = 1 + 1 = \mathbf{2}!
  $$
Row 2 result: $DP[2] = [1, 1, 1, 2, 2]$. Maximum side length reached is $\mathbf{2}$!

---

### Row 3: `["1", "0", "0", "1", "0"]`
- $j = 0$: $DP[3][0] = 1$.
- $j = 1$: `'0'` $\implies 0$.
- $j = 2$: `'0'` $\implies 0$.
- $j = 3$: Value `'1'`. Neighbors: $\text{top}=2, \text{left}=0, \text{diag}=1 \implies \min(2, 0, 1) + 1 = 1$.
- $j = 4$: `'0'` $\implies 0$.
Row 3 result: $DP[3] = [1, 0, 0, 1, 0]$.

---

### Final Maximum Resolution:
$$
\text{max\_side} = \max_{i, j}(DP[i][j]) = 2
$$
$$
\text{Area} = \text{max\_side}^2 = 2^2 = \mathbf{4}
$$

---

## 4. Complete Execution Trace

```text
Input Matrix (4 x 5):
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

DP Table (Max Square Side at (i, j)):
Row 0: 1  0  1  0  0
Row 1: 1  0  1  1  1
Row 2: 1  1  1  2  2  <-- Peak side = 2 at (2, 3) and (2, 4)
Row 3: 1  0  0  1  0

Global Maximum Side: 2
Maximal Square Area: 2 * 2 = 4
```

| Cell $(i, j)$ | Matrix Char | Top Neighbor | Left Neighbor | Diagonal Neighbor | $DP[i][j]$ Calculation | Max Side So Far |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | `'1'` | - | - | - | Boundary $= 1$ | 1 |
| $(1, 2)$ | `'1'` | 1 | 0 | 0 | $\min(1, 0, 0) + 1 = 1$ | 1 |
| $(1, 3)$ | `'1'` | 0 | 1 | 1 | $\min(0, 1, 1) + 1 = 1$ | 1 |
| $(1, 4)$ | `'1'` | 0 | 1 | 0 | $\min(0, 1, 0) + 1 = 1$ | 1 |
| $(2, 2)$ | `'1'` | 1 | 1 | 0 | $\min(1, 1, 0) + 1 = 1$ | 1 |
| **$(2, 3)$** | **`'1'`** | **1** | **1** | **1** | **$\min(1, 1, 1) + 1 = \mathbf{2}$** | **2** |
| **$(2, 4)$** | **`'1'`** | **1** | **2** | **1** | **$\min(1, 2, 1) + 1 = \mathbf{2}$** | **2** |
| $(3, 3)$ | `'1'` | 2 | 0 | 1 | $\min(2, 0, 1) + 1 = 1$ | 2 |

---

## 5. Algorithmic Correctness

**Soundness.** If $DP[i][j] = k$, the cells $(i-1, j), (i, j-1)$, and $(i-1, j-1)$ each head all-ones squares of side at least $k - 1$. The union of these three overlapping $(k-1) \times (k-1)$ squares plus the bottom-right cell $(i, j)$ forms a complete, solid $k \times k$ block of ones with no missing cells.

**Completeness.** Any valid $k \times k$ square of ones has a unique bottom-right cell $(i, j)$. By mathematical induction, its neighbors must have $DP$ values at least $k - 1$, so the recurrence will correctly assign $DP[i][j] \ge k$.

---

## 6. Traps This Instance Exposes

- **Returning Side Length Instead of Area:** The problem asks for the **area** of the square ($\text{max\_side}^2$), not the side length! Returning $\text{max\_side}$ fails all non-trivial test cases.
- **Character Comparison vs Integer:** Elements are strings (`"0"` and `"1"`), not integers (`0` and `1`). Comparing `if matrix[i][j] == 1` fails in languages like Python where `"1" != 1`.
- **Memory Compression:** Storing the entire $M \times N$ matrix is not needed; a single 1D array of size $N + 1$ with a scalar `prev` (to store the diagonal element) solves the problem in $O(N)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns. Each cell is visited once and evaluated in $O(1)$ constant time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space using a 1D DP row array, or $O(1)$ extra space if mutating the input matrix in-place.