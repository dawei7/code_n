# Guided Example: Unique Paths

We trace the step-by-step 2D dynamic programming grid addition and combinatorial derivation on a representative grid instance:

- **Input:** $m = 3, n = 7$
- **Required output:** $28$

This instance demonstrates grid path counting with restricted moves (Right and Down), the addition rule from neighboring predecessor cells ($DP[r][c] = DP[r-1][c] + DP[r][c-1]$), connection to Pascal's Triangle, and closed-form binomial coefficient evaluation $\binom{m+n-2}{m-1}$.

---

## 1. Instance & Teaching Goal

A robot is located at the top-left corner of an $m \times n$ grid ($m = 3$ rows, $n = 7$ columns). The robot can only move either **down** or **right** at any point in time. The robot is trying to reach the bottom-right corner at $(m - 1, n - 1) = (2, 6)$.

A naive recursive exploration branches into two choices at every step, causing exponential $O(2^{m+n})$ time.
Because any path entering $(r, c)$ must arrive either from directly above $(r - 1, c)$ or from directly to the left $(r, c - 1)$, the total paths to $(r, c)$ is simply the sum of paths to those two neighbors. This dynamic programming recurrence runs in $O(m \cdot n)$ time (or $O(n)$ space), and can also be solved in $O(m)$ time using combinations.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Dynamic Programming Recurrence
Let $DP[r][c]$ be the number of unique paths from $(0, 0)$ to $(r, c)$.
1. **Base Cases:**
   - The top row $r = 0$ can only be reached by moving continuously right:
     $$
     DP[0][c] = 1 \quad \forall c \in [0, n - 1]
     $$
   - The leftmost column $c = 0$ can only be reached by moving continuously down:
     $$
     DP[r][0] = 1 \quad \forall r \in [0, m - 1]
     $$
2. **Transition:**
   For any interior cell $(r, c)$ where $r \ge 1$ and $c \ge 1$:
   $$
   DP[r][c] = DP[r - 1][c] + DP[r][c - 1]
   $$

### Method 2: Combinatorial Closed Form
To reach $(m - 1, n - 1)$ from $(0, 0)$:
- The robot must make exactly $m - 1$ down moves ($D$).
- The robot must make exactly $n - 1$ right moves ($R$).
- The total number of steps is fixed at:
  $$
  S = (m - 1) + (n - 1) = m + n - 2
  $$
- The problem is equivalent to choosing which $m - 1$ steps out of $S$ total steps are down moves:
  $$
  \text{Paths} = \binom{m + n - 2}{m - 1} = \frac{(m + n - 2)!}{(m - 1)! \, (n - 1)!}
  $$
For $m = 3, n = 7$:
$$
\binom{3 + 7 - 2}{3 - 1} = \binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28
$$

> **Invariant.** Cell $DP[r][c]$ contains the exact number of monotonic lattice paths from $(0, 0)$ to $(r, c)$, matching entry $\binom{r+c}{r}$ in Pascal's Triangle.

---

## 3. Step-by-Step Worked Execution

We construct the DP grid for $m = 3, n = 7$:

### Row 0 Initialization
- $DP[0][c] = 1$ for all $c \in [0, 6]$:
  $$
  [1, 1, 1, 1, 1, 1, 1]
  $$

---

### Row 1 Computation
- $DP[1][0] = 1$ (base case).
- $c = 1: DP[1][1] = DP[0][1] + DP[1][0] = 1 + 1 = 2$.
- $c = 2: DP[1][2] = DP[0][2] + DP[1][1] = 1 + 2 = 3$.
- $c = 3: DP[1][3] = DP[0][3] + DP[1][2] = 1 + 3 = 4$.
- $c = 4: DP[1][4] = DP[0][4] + DP[1][3] = 1 + 4 = 5$.
- $c = 5: DP[1][5] = DP[0][5] + DP[1][4] = 1 + 5 = 6$.
- $c = 6: DP[1][6] = DP[0][6] + DP[1][5] = 1 + 6 = 7$.
Row 1 values: $[1, 2, 3, 4, 5, 6, 7]$.

---

### Row 2 Computation
- $DP[2][0] = 1$ (base case).
- $c = 1: DP[2][1] = DP[1][1] + DP[2][0] = 2 + 1 = 3$.
- $c = 2: DP[2][2] = DP[1][2] + DP[2][1] = 3 + 3 = 6$.
- $c = 3: DP[2][3] = DP[1][3] + DP[2][2] = 4 + 6 = 10$.
- $c = 4: DP[2][4] = DP[1][4] + DP[2][3] = 5 + 10 = 15$.
- $c = 5: DP[2][5] = DP[1][5] + DP[2][4] = 6 + 15 = 21$.
- $c = 6: DP[2][6] = DP[1][6] + DP[2][5] = 7 + 21 = \mathbf{28}$.
Row 2 values: $[1, 3, 6, 10, 15, 21, 28]$.

Destination reached at $(2, 6)$ with value $28$.

### The Same Numbers with a Single Rolling Row

The full matrix is never required: one array of length $n$ is enough, because `dp[c]` still holds the row above when column $c$ is processed, while `dp[c-1]` has already been overwritten with the current row. Each update `dp[c] += dp[c-1]` therefore reproduces the recurrence exactly.

| Column $c$ | Row-1 pass: carry `dp[c]` (row 0) | Row-1 pass: left `dp[c-1]` | Row-1 pass: `dp[c]` after | Row-2 pass: carry `dp[c]` (row 1) | Row-2 pass: left `dp[c-1]` | Row-2 pass: `dp[c]` after |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | none (boundary) | 1 | 1 | none (boundary) | 1 |
| 1 | 1 | 1 | 2 | 2 | 1 | 3 |
| 2 | 1 | 2 | 3 | 3 | 3 | 6 |
| 3 | 1 | 3 | 4 | 4 | 6 | 10 |
| 4 | 1 | 4 | 5 | 5 | 10 | 15 |
| 5 | 1 | 5 | 6 | 6 | 15 | 21 |
| 6 | 1 | 6 | 7 | 7 | 21 | **28** |

The final column is identical to row 2 of the matrix, confirming that discarding the earlier rows loses no information: row 1 was needed only as the "above" operand of row 2.

---

## 4. Complete Execution Trace

### 2D DP Table Matrix ($3 \times 7$)

| Row $\downarrow$ / Col $\to$ | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Row 0** | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **Row 1** | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| **Row 2** | 1 | 3 | 6 | 10 | 15 | 21 | **28 (Target)** |

---

## 5. Algorithmic Correctness

**Soundness.** Since the robot can only arrive at $(r, c)$ from either $(r - 1, c)$ or $(r, c - 1)$, and those two sets of paths are mutually exclusive (one ends in a down move, the other in a right move), by the sum rule of combinatorics the number of paths is strictly $DP[r-1][c] + DP[r][c-1]$.

**Completeness.** Computing cells in row-major order guarantees that both dependencies $(r-1, c)$ and $(r, c-1)$ are fully solved before evaluating $(r, c)$. The final cell $(m-1, n-1)$ is reachable and accounts for all paths.

---

## 6. Traps This Instance Exposes

- **Space Optimization to 1D Array:** Storing the full $M \times N$ matrix is unnecessary. Maintaining a single row of size $n$, updating `dp[c] += dp[c-1]`, achieves identical results in $O(n)$ memory.
- **Factorial Overflow in Combinatorics:** Computing $\frac{N!}{K!(N-K)!}$ via direct factorials can exceed integer limits in fixed-width languages. Computing iteratively $\prod_{i=1}^K \frac{N - K + i}{i}$ prevents intermediate numerical overflow.
- **Single Row or Column Grid:** If $m = 1$ or $n = 1$, the robot has only 1 path (moving purely right or purely down). The formula yields $\binom{0}{0} = 1$, correctly handling this edge case.

The package's whole case set is governed by one quantity, the number of down moves $m - 1$ chosen among $S = m + n - 2$ total steps:

| Instance | $m$ | $n$ | Steps $S = m + n - 2$ | Down moves $m - 1$ | Binomial form | Expected output |
|:---|:---:|:---:|:---:|:---:|:---|:---:|
| Only rightward moves | 1 | 8 | 7 | 0 | $\binom{7}{0} = 1$ | 1 |
| Tall grid | 3 | 2 | 3 | 2 | $\binom{3}{2} = 3$ | 3 |
| Wide grid (main trace) | 3 | 7 | 8 | 2 | $\binom{8}{2} = 28$ | 28 |
| Small square | 4 | 4 | 6 | 3 | $\binom{6}{3} = 20$ | 20 |
| Larger square | 10 | 10 | 18 | 9 | $\binom{18}{9} = 48620$ | 48620 |

Every $m, n \ge 1$ produces a non-empty grid with exactly one monotone route family, and $\binom{m+n-2}{m-1}$ degenerates to $1$ at $m = 1$ or $n = 1$, which is why no special branch is needed for a degenerate grid.

---

## 7. Complexity Derivation

- **Dynamic Programming Complexity:**
  - Time: $O(m \cdot n)$ to compute all cells in the grid.
  - Space: $O(n)$ auxiliary memory using a 1D running row.
- **Combinatorial Method Complexity:**
  - Time: $O(\min(m, n))$ multiplications.
  - Space: $O(1)$ auxiliary memory.
