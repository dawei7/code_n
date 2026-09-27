# Guided Example: Perfect Squares

We trace the step-by-step unbounded knapsack dynamic programming recurrence, available square coin denomination expansion ($1^2, 2^2, \dots, m^2$), and subproblem value minimization on representative target integers:

- **Input:** $n = 12$
- **Required output:** $3$ (Decomposed into $4 + 4 + 4 = 12$; three square terms, strictly better than the greedy $9 + 1 + 1 + 1 = 12$ which uses four terms)
- **Sum of Two Squares:** $n = 13 \implies 2$ ($9 + 4 = 13$)
- **Direct Perfect Square:** $n = 16 \implies 1$ ($4^2 = 16$)
- **Legendre Four-Square Maximum:** $n = 7 \implies 4$ ($4 + 1 + 1 + 1 = 7$; by Lagrange's Four-Square Theorem, any integer can be expressed using at most 4 squares)

This instance demonstrates unbounded knapsack dynamic programming, proves why greedy selection of the largest square ($9$) yields suboptimal term counts ($4$ vs $3$), formalizes the 2D DP recurrence $f[i][j] = \min(f[i-1][j], f[i][j - i^2] + 1)$, and explores both DP ($O(n \sqrt{n})$) and mathematical number theory ($O(\sqrt{n})$ Legendre's three-square theorem).

---

## 1. Instance & Teaching Goal

Given an integer $n = 12$, find the **least number of perfect square numbers** that sum to $12$:
```text
Available squares <= 12: {1, 4, 9}

Greedy approach:
Take largest square <= 12: 9
Remaining: 12 - 9 = 3
Remaining squares: 1 + 1 + 1
Total terms: 9 + 1 + 1 + 1 -> 4 squares (Suboptimal!)

Optimal DP approach:
Decomposition: 4 + 4 + 4 = 12
Total terms: 3 squares (Optimal!)
Output: 3
```

### Why the Greedy Algorithm Fails
A greedy policy always subtracts the largest perfect square $\le$ current remainder.
For $n = 12$, the largest square is $9$, leaving $3$, which requires three $1$s ($9 + 1 + 1 + 1$, totaling 4 numbers).
However, using three $4$s ($4 + 4 + 4$) produces the same sum in only **3 numbers**!
Because greedy choice lacks optimal substructure, we must evaluate the optimal choice across all candidate square denominations using **unbounded knapsack dynamic programming**.

---

## 2. Conceptual Foundation & Invariants

### 2D Unbounded Knapsack DP Formulation
Let $m = \lfloor \sqrt{n} \rfloor$.
The available perfect squares are $\{1^2, 2^2, \dots, m^2\}$.
Define DP table $f[i][j]$ for $0 \le i \le m$ and $0 \le j \le n$:
> $f[i][j]$ = minimum number of squares needed to sum to $j$ using only squares from $\{1^2, 2^2, \dots, i^2\}$.

### Base Cases:
- $f[0][0] = 0$: Zero terms are needed to make sum 0.
- $f[0][j] = \infty$ for all $j \ge 1$: Impossible to form positive sum without any squares.

### Transition Recurrence:
For square $i$ (value $s = i^2$) and target sum $j$:
1. **Exclude square $i^2$:**
   Inherit the best solution using only squares up to $(i - 1)^2$:
   $$
   f[i][j] = f[i - 1][j]
   $$
2. **Include square $i^2$ (if $j \ge i^2$):**
   Use one copy of $i^2$ and transition to the remaining sum $j - i^2$ within the **same row** $i$ (since squares can be reused indefinitely):
   $$
   f[i][j] = \min(f[i][j], \; f[i][j - i^2] + 1)
   $$

The final answer is $f[m][n]$.

> **Invariant.** For every table entry $f[i][j]$, the value represents the exact minimal number of square terms from $\{1^2, \dots, i^2\}$ that sum to $j$.

---

## 3. Step-by-Step Worked Execution

We trace the DP table on $n = 12$:
$m = \lfloor \sqrt{12} \rfloor = 3$.
Square denominations:
- $i = 1: 1^2 = 1$
- $i = 2: 2^2 = 4$
- $i = 3: 3^2 = 9$

---

### Step 1: Base Row ($i = 0$, No Squares)
- $f[0][0] = 0$
- $f[0][1 \dots 12] = \infty$

---

### Step 2: Row $i = 1$ (Square $1^2 = 1$)
Using only $1$, every sum $j$ requires exactly $j$ ones:
$$
f[1][j] = j \quad \text{for } j \in [0, 12]
$$
Specifically, for target 12:
$$
f[1][12] = 12 \quad (12 \times 1)
$$

---

### Step 3: Row $i = 2$ (Square $2^2 = 4$)
Allowed squares: $\{1, 4\}$.
We transition $f[2][j] = \min(f[1][j], \; f[2][j - 4] + 1)$:
- $j = 0 \dots 3$: $j < 4 \implies f[2][j] = f[1][j] = j$.
- $j = 4$: $\min(f[1][4], f[2][0] + 1) = \min(4, 0 + 1) = \mathbf{1}$ (One $4$).
- $j = 5$: $\min(f[1][5], f[2][1] + 1) = \min(5, 1 + 1) = \mathbf{2}$ ($4 + 1$).
- $j = 8$: $\min(f[1][8], f[2][4] + 1) = \min(8, 1 + 1) = \mathbf{2}$ ($4 + 4$).
- $j = 12$:
  $$
  f[2][12] = \min(f[1][12], \; f[2][8] + 1) = \min(12, \; 2 + 1) = \mathbf{3}
  $$
  *(Achieved as $4 + 4 + 4$)*.

---

### Step 4: Row $i = 3$ (Square $3^2 = 9$)
Allowed squares: $\{1, 4, 9\}$.
We transition $f[3][j] = \min(f[2][j], \; f[3][j - 9] + 1)$:
- $j = 0 \dots 8$: $j < 9 \implies f[3][j] = f[2][j]$.
- $j = 9$: $\min(f[2][9], f[3][0] + 1) = \min(3, 0 + 1) = \mathbf{1}$ (One $9$).
- $j = 12$:
  $$
  f[3][12] = \min(f[2][12], \; f[3][3] + 1) = \min(3, \; 3 + 1) = \min(3, 4) = \mathbf{3}
  $$
  *(Comparing three $4$s (count 3) against $9 + 1 + 1 + 1$ (count 4); $3 < 4$, so $3$ is retained!)*.

---

### Step 5: Final Result Extraction
The value in the terminal cell $f[3][12]$ is $\mathbf{3}$.

---

## 4. Complete Execution Trace

```text
n = 12, m = 3
Squares: [1, 4, 9]

Row 1 (sq = 1):
  f[1][j] = j for all j -> f[1][12] = 12

Row 2 (sq = 4):
  f[2][4]  = min(4, f[2][0] + 1) = 1
  f[2][8]  = min(8, f[2][4] + 1) = 2
  f[2][12] = min(12, f[2][8] + 1) = 3  (4 + 4 + 4)

Row 3 (sq = 9):
  f[3][9]  = min(f[2][9], f[3][0] + 1) = min(3, 1) = 1
  f[3][12] = min(f[2][12], f[3][3] + 1) = min(3, 3 + 1) = 3

Final Result: 3
```

| Sum $j$ | Row 0 (No Sq) | Row 1 (Sq $= 1$) | Row 2 (Sq $\in \{1, 4\}$) | Row 3 (Sq $\in \{1, 4, 9\}$) | Best Square Decomposition |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | 0 | 0 | 0 | Empty |
| 1 | $\infty$ | 1 | 1 | 1 | $1$ |
| 4 | $\infty$ | 4 | 1 | 1 | $4$ |
| 8 | $\infty$ | 8 | 2 | 2 | $4 + 4$ |
| 9 | $\infty$ | 9 | 3 | 1 | $9$ |
| **12** | $\mathbf{\infty}$ | **12** | **3** | **$\mathbf{3}$** | **$4 + 4 + 4$** |

---

## 5. Algorithmic Correctness

**Soundness.** Every valid sum $j$ is produced by a combination of perfect squares. The recurrence explores all valid subproblems: either the current square $i^2$ is not used ($f[i-1][j]$), or it is used at least once ($f[i][j - i^2] + 1$). Taking the minimum guarantees that the recorded answer is strictly minimal among all valid square combinations.

**Completeness.** Since $1^2 = 1$ is always available, every positive integer $n$ can be formed by $n$ ones ($f[1][n] = n < \infty$). Therefore, every state is reachable, and the global minimum over all square subsets is exhaustively resolved.

---

## 6. Traps This Instance Exposes

- **The Greedy Trap ($12 \to 9 + 1 + 1 + 1$):** Subtracting the largest possible square at each step yields $4$ terms instead of the optimal $3$ ($4 + 4 + 4$). Dynamic programming or BFS is required to find the true minimum.
- **1D Space Optimization:** While the 2D table uses $O(n \sqrt{n})$ space, a 1D rolling array `dp[j] = min(dp[j], dp[j - s] + 1)` with forward iteration computes the identical result in $O(n)$ space.
- **Legendre's Three-Square Theorem:** By number theory, the answer is $4$ if and only if $n = 4^k (8m + 7)$. Checking whether $n$ is a perfect square ($1$), can be written as the sum of two squares ($2$), or fits $4^k(8m + 7)$ ($4$), solves the problem in $O(\sqrt{n})$ time and $O(1)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \sqrt{n})$. The table has $m = \lfloor \sqrt{n} \rfloor$ rows and $n + 1$ columns. Each of the $(n + 1) \sqrt{n}$ cells performs $O(1)$ arithmetic operations.
- **Auxiliary Space Complexity:** $O(n \sqrt{n})$ for the 2D DP matrix (or $O(n)$ if collapsed into a 1D array).
