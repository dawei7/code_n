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

### The Same Recurrence Held in a Single Row of Memory

The whole $4 \times 5$ table is never needed: row $i$ is finished before row $i + 1$ starts, so one array of $N + 1 = 6$ cells plus one saved scalar reproduces every value above. The convention is that `dp[j + 1]` holds the current row's value for column $j$, `dp[0]` is a permanent sentinel $0$ standing for the missing left neighbour at $j = 0$, and the scalar `prev` carries $DP[i-1][j-1]$, the diagonal. Each step reads the old `dp[j + 1]` as the top neighbour, the just-written `dp[j]` as the left neighbour, and `prev` as the diagonal.

| Cell $(i, j)$ | Char | Top = saved old `dp[j+1]` | Left = `dp[j]` | Diagonal = `prev` | $DP[i][j]$ | `dp` array after the update |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| $(0, 0)$ | `'1'` | 0 | 0 (sentinel) | 0 (no previous row) | $\min(0,0,0)+1 = 1$ | $[0, 1, 0, 0, 0, 0]$ |
| $(0, 1)$ | `'0'` | not consulted | not consulted | not consulted | 0 | $[0, 1, 0, 0, 0, 0]$ |
| $(0, 2)$ | `'1'` | 0 | 0 | 0 | $\min(0,0,0)+1 = 1$ | $[0, 1, 0, 1, 0, 0]$ |
| $(0, 3)$ | `'0'` | not consulted | not consulted | not consulted | 0 | $[0, 1, 0, 1, 0, 0]$ |
| $(0, 4)$ | `'0'` | not consulted | not consulted | not consulted | 0 | $[0, 1, 0, 1, 0, 0]$ |
| $(1, 0)$ | `'1'` | 1 | 0 (sentinel) | 0 (row-start reset) | $\min(1,0,0)+1 = 1$ | $[0, 1, 0, 1, 0, 0]$ |
| $(1, 1)$ | `'0'` | not consulted | not consulted | not consulted | 0 | $[0, 1, 0, 1, 0, 0]$ |
| $(1, 2)$ | `'1'` | 1 | 0 | 0 | $\min(1,0,0)+1 = 1$ | $[0, 1, 0, 1, 0, 0]$ |
| $(1, 3)$ | `'1'` | 0 | 1 | 1 | $\min(0,1,1)+1 = 1$ | $[0, 1, 0, 1, 1, 0]$ |
| $(1, 4)$ | `'1'` | 0 | 1 | 0 | $\min(0,1,0)+1 = 1$ | $[0, 1, 0, 1, 1, 1]$ |
| $(2, 0)$ | `'1'` | 1 | 0 (sentinel) | 0 (row-start reset) | $\min(1,0,0)+1 = 1$ | $[0, 1, 0, 1, 1, 1]$ |
| $(2, 1)$ | `'1'` | 0 | 1 | 1 | $\min(0,1,1)+1 = 1$ | $[0, 1, 1, 1, 1, 1]$ |
| $(2, 2)$ | `'1'` | 1 | 1 | 0 | $\min(1,1,0)+1 = 1$ | $[0, 1, 1, 1, 1, 1]$ |
| $(2, 3)$ | `'1'` | 1 | 1 | 1 | $\min(1,1,1)+1 = \mathbf{2}$ | $[0, 1, 1, 1, 2, 1]$ |
| $(2, 4)$ | `'1'` | 1 | 2 | 1 | $\min(1,2,1)+1 = \mathbf{2}$ | $[0, 1, 1, 1, 2, 2]$ |
| $(3, 0)$ | `'1'` | 1 | 0 (sentinel) | 0 (row-start reset) | $\min(1,0,0)+1 = 1$ | $[0, 1, 1, 1, 2, 2]$ |
| $(3, 1)$ | `'0'` | not consulted | not consulted | not consulted | 0 | $[0, 1, 0, 1, 2, 2]$ |
| $(3, 2)$ | `'0'` | not consulted | not consulted | not consulted | 0 | $[0, 1, 0, 0, 2, 2]$ |
| $(3, 3)$ | `'1'` | 2 | 0 | 1 | $\min(2,0,1)+1 = 1$ | $[0, 1, 0, 0, 1, 2]$ |
| $(3, 4)$ | `'0'` | not consulted | not consulted | not consulted | 0 | $[0, 1, 0, 0, 1, 0]$ |

Reading down the array column reproduces $DP[0] = [1,0,1,0,0]$, $DP[1] = [1,0,1,1,1]$, $DP[2] = [1,1,1,2,2]$ and $DP[3] = [1,0,0,1,0]$, shifted one position to the right by the sentinel.

Two ordering facts make this compression safe. The diagonal must be captured *before* position $j + 1$ is overwritten, because that position is exactly where the diagonal for the next column lives; and a `'0'` cell must still write $0$ into its position, because otherwise the stale entry left there from the previous row would be read as the top neighbour one row later. In this instance that second rule has no visible effect — position $2$ is cleared at $(3, 1)$ and position $3$ at $(3, 2)$, and row 3 is the last row — but the identical omission on a five-row matrix would let a dead $1$ from row 2 survive into row 4. The left neighbour needs no such care: `dp[j]` has already been rewritten with the current row's value by the time column $j$ is processed, which is precisely the value the recurrence wants.

---

## 5. Algorithmic Correctness

**Soundness.** If $DP[i][j] = k$, the cells $(i-1, j), (i, j-1)$, and $(i-1, j-1)$ each head all-ones squares of side at least $k - 1$. The union of these three overlapping $(k-1) \times (k-1)$ squares plus the bottom-right cell $(i, j)$ forms a complete, solid $k \times k$ block of ones with no missing cells.

**Completeness.** Any valid $k \times k$ square of ones has a unique bottom-right cell $(i, j)$. By mathematical induction, its neighbors must have $DP$ values at least $k - 1$, so the recurrence will correctly assign $DP[i][j] \ge k$.

**Boundary cases, and the single cell that decides each one.** The degenerate inputs are not special cases in the recurrence; they are the recurrence evaluated at cells whose neighbours are sentinels. The table names the deciding cell for each, so the answer can be predicted without running anything.

| Scenario | Matrix | Answer (side, then area) | Deciding cell, and why it settles the answer |
|:---|:---|:---|:---|
| All-zero $1 \times 1$ | `[["0"]]` | side 0, area 0 | $(0,0)$ is `'0'`, so no entry is ever written; the running maximum stays 0 and the area is $0^2 = 0$ |
| Single one $1 \times 1$ | `[["1"]]` | side 1, area 1 | $(0,0)$ is simultaneously a boundary row and a boundary column, so its value is 1 with no neighbour consulted at all |
| Checkerboard $2 \times 2$ | `[["0","1"],["1","0"]]` | side 1, area 1 | The only interior cell is $(1,1)$, and it is `'0'`, so the top-left dependency is broken there; the two ones survive only as boundary cells worth 1, which is why a diagonal run of ones is worthless here |
| Single row of ones (constructed) | `[["1","1","1"]]` | side 1, area 1 | Every cell has $i = 0$, so all three are boundary cells worth 1; the side can never exceed $\min(M, N) = 1$ no matter how long the run of ones is |
| The $4 \times 5$ instance traced above | the matrix in section 1 | side 2, area 4 | $(2,3)$ and $(2,4)$ both reach 2 and every $3 \times 3$ window contains a `'0'`, so no cell can reach 3 |
| Full $3 \times 3$ of ones | `[["1","1","1"],["1","1","1"],["1","1","1"]]` | side 3, area 9 | $(2,2)$ is the only cell whose three neighbours all equal 2, giving $\min(2,2,2) + 1 = 3$; the boundary row and column stay at 1, so the maximum is decided strictly inside the grid |

---

## 6. Traps This Instance Exposes

- **Returning Side Length Instead of Area:** The problem asks for the **area** of the square ($\text{max\_side}^2$), not the side length! Returning $\text{max\_side}$ fails all non-trivial test cases.
- **Character Comparison vs Integer:** Elements are strings (`"0"` and `"1"`), not integers (`0` and `1`). Comparing `if matrix[i][j] == 1` fails in languages like Python where `"1" != 1`.
- **Memory Compression:** Storing the entire $M \times N$ matrix is not needed; a single 1D array of size $N + 1$ with a scalar `prev` (to store the diagonal element) solves the problem in $O(N)$ space.

**Alternative formulations, and the detail each one puts at risk.** All five methods return $4$ for the traced instance, so the choice is about cost and about which invariant must hold exactly.

| Approach | Mechanism | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---:|:---:|:---|
| Expansion from every top-left corner | For each cell, grow the side while the newly added row and column contain only ones | $O(M \cdot N \cdot \min(M, N)^2)$ | $O(1)$ | Correct without any table, but at the largest permitted grid ($300 \times 300$) it performs on the order of $8 \times 10^{9}$ cell checks |
| Full 2D table with a sentinel border | Store $(M+1) \times (N+1)$ values whose first row and first column are permanently 0, so the three-neighbour minimum needs no boundary test | $O(M \cdot N)$ | $O(M \cdot N)$ | Removes every edge case from the transition, which is exactly why it is easy to get right, but it materialises all $90{,}000$ entries when only one row is ever needed |
| Rolling 1D row | Keep one array of $N + 1$ cells plus the saved diagonal, rewriting the array row by row | $O(M \cdot N)$ | $O(N)$ | The diagonal must be copied out before its position is overwritten, and `'0'` cells must still clear their slot, or a dead value from the previous row is read as a top neighbour |
| Binary search on the side with 2D prefix sums | Ask whether a $k \times k$ all-ones square exists in $O(1)$ per position using summed-area tables, and binary-search $k$ | $O(M \cdot N \cdot \log \min(M, N))$ | $O(M \cdot N)$ | Legitimate only because feasibility is monotone — every square of side $k$ contains one of side $k - 1$ — so the predicate never flips back; the price is a logarithmic factor and prefix memory, and the resulting side must still be squared |
| Per-row column heights with a monotonic stack | Maintain each column's run of consecutive ones, and for each bar take the widest interval in which every column height is at least that bar's height; the best square from that rectangle is $\min(h, w)^2$ | $O(M \cdot N)$ | $O(N)$ | The usual histogram objective is the rectangle area $h \cdot w$, which answers a different question; using it unchanged over-reports the area, and the square objective must be applied bar by bar |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns. Each cell is visited once and evaluated in $O(1)$ constant time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space using a 1D DP row array, or $O(1)$ extra space if mutating the input matrix in-place.
