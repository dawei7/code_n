# Guided Example: Coin Change

We trace the step-by-step unbounded knapsack dynamic programming formulation, transition between excluding vs reusing denomination $x$ ($f[i][j] = \min(f[i-1][j], f[i][j-x] + 1)$), infinity sentinel reachability, and optimal coin count extraction on representative money amount instances:

- **Input:** $\text{coins} = [1, 2, 5], \quad \text{amount} = 11$
- **Required output:** $3$
  - Optimal coin combination: $5 + 5 + 1 = 11$ (Uses 3 coins: two $5$s and one $1$)
  - Suboptimal greedy combination: $5 + 5 + 1 = 11$ (happens to match here, but greedy fails in general)
- **Greedy Failure Counterexample:** $\text{coins} = [1, 3, 4], \text{amount} = 6$:
  - Greedy picks largest first: $4 + 1 + 1$ ($3$ coins)
  - True optimal DP: $3 + 3$ ($2$ coins)
- **Unreachable Amount Base Case:** $\text{coins} = [2], \text{amount} = 3 \implies -1$ (Odd amount cannot be formed from even coins)
- **Zero Amount Base Case:** $\text{amount} = 0 \implies 0$ (Requires 0 coins)

This instance demonstrates unbounded knapsack recurrence relations, contrasts local greedy heuristics against global dynamic programming, proves why reading $f[i][j-x]$ from the current row models infinite coin supplies, and analyzes $O(M \cdot A)$ time and space bounds.

---

## 1. Instance & Teaching Goal

Given coin denominations $\text{coins} = [1, 2, 5]$ ($M = 3$) and target $\text{amount} = 11$:
Find the **minimum number of coins** needed to make up that amount, assuming an unlimited supply of each coin type. If that amount of money cannot be made up by any combination of the coins, return $-1$.

```text
Denominations: [1, 2, 5]
Target Amount: 11

Possible Combinations:
- Eleven 1-coins:              11 coins
- Five 2-coins + One 1-coin:    6 coins
- Two 5-coins + One 1-coin:     3 coins  (OPTIMAL!)

Output: 3
```

### Why Greedy Selection Fails
A common greedy instinct is to pick the largest possible denomination first:
- On $\text{coins} = [1, 3, 4]$ and $\text{amount} = 6$:
  Greedy selects $4$, leaving $2$, then takes $1$ and $1$ $\implies 3$ coins ($4 + 1 + 1$).
  However, taking two $3$-coins achieves $3 + 3 = 6$ using only **2 coins**!
- Because arbitrary coin systems may not be canonical, global Dynamic Programming is required.

---

## 2. Conceptual Foundation & Invariants

### 2D DP State Definition
Let $f[i][j]$ be the minimum number of coins needed to form amount $j$ using only a subset of the first $i$ coin denominations ($\text{coins}[0 \dots i-1]$):
- Dimensions: $(M + 1) \times (\text{amount} + 1)$.
- Sentinel: Initialized to $\infty$ (unreachable).

### Boundary Conditions:
- $f[0][0] = 0$: Amount $0$ requires $0$ coins.
- $f[0][j] = \infty$ for all $j \ge 1$: Impossible to form positive amounts without coins.

### Recurrence for Denomination $x = \text{coins}[i - 1]$:
For each amount $j \in [0, \text{amount}]$:
1. **Exclude Coin $x$:**
   $$
   f[i][j] = f[i - 1][j]
   $$
2. **Include At Least One Coin $x$ (if $j \ge x$):**
   $$
   f[i][j] = \min(f[i][j], \; f[i][j - x] + 1)
   $$
   *(Notice that $f[i][j - x]$ reads from row $i$, NOT row $i - 1$. This directly models an **unlimited supply**, allowing denomination $x$ to be used multiple times).*

> **Invariant.** For any cell $f[i][j]$, its value is the exact minimum number of coins from the first $i$ denominations required to sum to $j$, or $\infty$ if $j$ is unreachable.

---

## 3. Step-by-Step Worked Execution

We trace the DP table on $\text{coins} = [1, 2, 5]$ and $\text{amount} = 11$:
Table initialized with $f[0][0] = 0$ and all other entries $\infty$.

---

### Step 1: Row $i = 1$, Coin $x = 1$
Only coin available is $1$. Every amount $j$ requires exactly $j$ coins:
$$
f[1][j] = j \quad \text{for all } j \in [0, 11]
$$
- $f[1][11] = 11$.

---

### Step 2: Row $i = 2$, Coin $x = 2$
Coins available: $\{1, 2\}$.
- For even amounts $j = 2k$, we can use $k$ coins of denomination $2$:
  - $j = 2: \min(f[1][2]=2, \; f[2][0]+1=1) = \mathbf{1}$.
  - $j = 4: \min(f[1][4]=4, \; f[2][2]+1=2) = \mathbf{2}$.
  - $j = 6: \min(f[1][6]=6, \; f[2][4]+1=3) = \mathbf{3}$.
  - $j = 8: \min(f[1][8]=8, \; f[2][6]+1=4) = \mathbf{4}$.
  - $j = 10: \min(f[1][10]=10, \; f[2][8]+1=5) = \mathbf{5}$.
- For odd amounts $j = 2k + 1$:
  - $j = 1: 1$
  - $j = 3: \min(f[1][3]=3, \; f[2][1]+1=2) = \mathbf{2}$ ($2 + 1$).
  - $j = 5: \min(f[1][5]=5, \; f[2][3]+1=3) = \mathbf{3}$ ($2 + 2 + 1$).
  - $j = 7: \min(f[1][7]=7, \; f[2][5]+1=4) = \mathbf{4}$.
  - $j = 9: \min(f[1][9]=9, \; f[2][7]+1=5) = \mathbf{5}$.
  - $j = 11: \min(f[1][11]=11, \; f[2][9]+1=6) = \mathbf{6}$ ($5 \times 2 + 1$).

---

### Step 3: Row $i = 3$, Coin $x = 5$
Coins available: $\{1, 2, 5\}$.
- Amounts $j < 5$ cannot use coin $5$: values remain unchanged from row 2 ($f[3][j] = f[2][j]$).
- $j = 5: \min(f[2][5]=3, \; f[3][0] + 1 = 0 + 1 = 1) = \mathbf{1}$ (Single coin of 5).
- $j = 6: \min(f[2][6]=3, \; f[3][1] + 1 = 1 + 1 = 2) = \mathbf{2}$ ($5 + 1$).
- $j = 7: \min(f[2][7]=4, \; f[3][2] + 1 = 1 + 1 = 2) = \mathbf{2}$ ($5 + 2$).
- $j = 8: \min(f[2][8]=4, \; f[3][3] + 1 = 2 + 1 = 3) = \mathbf{3}$ ($5 + 2 + 1$).
- $j = 9: \min(f[2][9]=5, \; f[3][4] + 1 = 2 + 1 = 3) = \mathbf{3}$ ($5 + 2 + 2$).
- $j = 10: \min(f[2][10]=5, \; f[3][5] + 1 = 1 + 1 = 2) = \mathbf{2}$ ($5 + 5$).
- **$j = 11$ (Target!):**
  $$
  f[3][11] = \min\big(f[2][11]=6, \; f[3][11 - 5] + 1\big) = \min(6, \; f[3][6] + 1) = \min(6, \; 2 + 1) = \mathbf{3}
  $$
  (Combination: $5 + 5 + 1 = 11$).

---

### Step 4: Final Value Extraction
$f[3][11] = 3 < \infty$, so the answer is:
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

```text
coins = [1, 2, 5], amount = 11

Row 0 (no coins):  f[0][0] = 0, all f[0][1..11] = inf
Row 1 (coin 1):    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Row 2 (coins 1,2): [0, 1, 1, 2, 2, 3, 3, 4, 4, 5,  5,  6]
Row 3 (coins 1,2,5):
  j=5:  min(3, f[3][0]+1=1) = 1
  j=6:  min(3, f[3][1]+1=2) = 2
  j=7:  min(4, f[3][2]+1=2) = 2
  j=8:  min(4, f[3][3]+1=3) = 3
  j=9:  min(5, f[3][4]+1=3) = 3
  j=10: min(5, f[3][5]+1=2) = 2
  j=11: min(6, f[3][6]+1=3) = 3

Result: f[3][11] = 3
```

| Target Amount $j$ | Row 1: Coins $\{1\}$ | Row 2: Coins $\{1, 2\}$ | Row 3: Coins $\{1, 2, 5\}$ | Optimal Coins Used | Minimum Coins $f[3][j]$ |
|:---:|:---:|:---:|:---:|:---|:---:|
| 0 | 0 | 0 | 0 | None | 0 |
| 1 | 1 | 1 | 1 | $1$ | 1 |
| 2 | 2 | 1 | 1 | $2$ | 1 |
| 3 | 3 | 2 | 2 | $2 + 1$ | 2 |
| 4 | 4 | 2 | 2 | $2 + 2$ | 2 |
| 5 | 5 | 3 | **1** | $5$ | **1** |
| 6 | 6 | 3 | **2** | $5 + 1$ | **2** |
| 7 | 7 | 4 | **2** | $5 + 2$ | **2** |
| 8 | 8 | 4 | **3** | $5 + 2 + 1$ | **3** |
| 9 | 9 | 5 | **3** | $5 + 2 + 2$ | **3** |
| 10 | 10 | 5 | **2** | $5 + 5$ | **2** |
| **11** | 11 | 6 | **3** | **$5 + 5 + 1$** | **$\mathbf{3}$ (Target)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every state $f[i][j]$ is derived either by omitting denomination $x$ (inheriting the optimal count from $f[i-1][j]$) or by using at least one coin of value $x$ (yielding $1 + f[i][j-x]$). Because all evaluated states correspond to valid coin combinations, any non-infinity value is mathematically sound.

**Completeness.** At each step, every subproblem explores all possible multiples of the newly introduced coin denomination. Because the recurrence evaluates the minimum over all valid choices in topological order of amounts, no coin combination can achieve a smaller count than $f[m][amount]$. If $f[m][amount] = \infty$, no combination exists, and the function correctly returns $-1$.

---

## 6. Traps This Instance Exposes

- **Greedy Trap:** Always choosing the largest coin fails on non-canonical systems (e.g. $[1, 3, 4]$ with amount $6$ yields $3$ with greedy, but $2$ with DP).
- **0/1 Knapsack vs Unbounded Knapsack:** In 0/1 knapsack, each item can be used once, requiring transition from the previous row $f[i-1][j-x]$. In coin change, coins are unlimited, requiring transition from the **current** row $f[i][j-x]$.
- **Sentinel Initialization:** Unreachable states must be initialized to $\infty$. Using $-1$ or $0$ during recurrence breaks $\min$ comparisons.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot A)$, where $M = \text{len}(coins)$ and $A = \text{amount}$. The DP table has $(M + 1) \times (A + 1)$ cells, and each cell is computed in $O(1)$ arithmetic operations.
- **Auxiliary Space Complexity:** $O(M \cdot A)$ for the full 2D table (or $O(A)$ if optimized to a 1D rolling array).
