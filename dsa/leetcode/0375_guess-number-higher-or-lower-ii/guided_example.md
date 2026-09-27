# Guided Example: Guess Number Higher or Lower II

We trace the step-by-step minimax interval dynamic programming formulation ($f[i][j]$), worst-case adversarial branch evaluation ($k + \max(f[i][k - 1], f[k + 1][j])$), optimal decision choice minimization ($\min_k$), and bottom-up sub-interval memoization on representative game instances:

- **Input:** $n = 10$
- **Required output:** $16$
  - Small sub-interval base results:
    - Singletons: $f[x][x] = 0$ (Free, no wrong guess possible)
    - Pairs $[1, 2] \implies f[1][2] = 1$ (Guess 1: if wrong, it is 2)
    - Pairs $[2, 3] \implies f[2][3] = 2$
    - Triplets $[1, 3] \implies$ Guess 2 costs $2 + \max(0, 0) = 2$
  - Interval $[1, 10]$ optimal decision decomposition:
    - Choose initial guess $k = 7$:
      - Left subtree $[1, 6]$: worst-case cost is $9$ (Worst-case total: $7 + 9 = 16$)
      - Right subtree $[8, 10]$: worst-case cost is $9$ (Worst-case total: $7 + 9 = 16$)
      - Combined worst-case cost for $k = 7$: $\max(7 + 9, 7 + 9) = 16$
    - Comparison with other root choices:
      - Guessing $k = 5 \implies 5 + \max(f[1][4], f[6][10]) = 5 + 12 = 17 > 16$
      - Guessing $k = 8 \implies 8 + \max(f[1][7], f[9][10]) = 8 + 10 = 18 > 16$
    - Minimal guaranteed cost: $\mathbf{16}$
- **Three-Number Game:** $n = 3 \implies \mathbf{2}$ (Guess 2 first)
- **Two-Number Game:** $n = 2 \implies \mathbf{1}$ (Guess 1 first)

This instance demonstrates game-theoretic zero-sum minimax optimization on intervals, mathematically proves why binary search is sub-optimal when query costs are non-uniform, and establishes $O(N^3)$ polynomial time and $O(N^2)$ table space.

---

## 1. Instance & Teaching Goal

We play a guessing game with numbers in the range $[1, n]$:
- If you guess number $k$ and it is correct, the game ends with cost $0$.
- If you guess $k$ and it is wrong, you pay a penalty of $k$ dollars, and the host reveals whether the secret is higher or lower.
Determine the **minimum amount of money required to guarantee a win regardless of the host's secret number** for $n = 10$:

```text
Interval: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Why standard Binary Search (guessing midpoint 5) is suboptimal:
Guess 5:
  If secret is in [6..10], penalty is 5.
  Then in [6..10], guess 8 (penalty 8), then guess 9 (penalty 9).
  Total worst-case cost = 5 + 8 + 9 = 22 dollars!

Optimal Minimax Strategy:
Guess 7 first!
  If secret < 7: search [1..6] -> cost 7 + 9 = 16 dollars
  If secret > 7: search [8..10] -> cost 7 + 9 = 16 dollars
Guaranteed Cost: 16 dollars (Substantially cheaper than 22!)
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Minimax Recurrence
Let $f[i][j]$ denote the minimum cost to guarantee finding a secret number in the closed interval $[i, j]$:
- **Base Cases:**
  - If $i \ge j$: $f[i][j] = 0$ (Only 1 candidate or empty interval; no penalty required).
- **Recurrence for Interval $[i, j]$:**
  If you choose to probe number $k \in [i, j]$:
  - If the secret is less than $k$, you pay $k$ and enter subproblem $[i, k - 1]$ with cost $f[i][k - 1]$.
  - If the secret is greater than $k$, you pay $k$ and enter subproblem $[k + 1, j]$ with cost $f[k + 1][j]$.
  - An adversary picks the more expensive branch:
    $$
    \text{worst\_cost}(k) = k + \max\big(f[i][k - 1], \; f[k + 1][j]\big)
    $$
  - As the player, you choose the probe $k$ that **minimizes** this worst-case cost:
    $$
    f[i][j] = \min_{k = i}^{j} \Big( k + \max\big(f[i][k - 1], \; f[k + 1][j]\big) \Big)
    $$

### 2. Computation Order:
To ensure subproblems $f[i][k - 1]$ and $f[k + 1][j]$ are already resolved when computing $f[i][j]$:
- Outer loop runs $i$ backwards from $n - 1$ down to $1$.
- Inner loop runs $j$ forwards from $i + 1$ up to $n$.

> **Invariant.** For any interval $[i, j]$, $f[i][j]$ holds the strictly minimal budget needed to guarantee victory against an optimal adversary.

---

## 3. Step-by-Step Worked Execution

We trace the recurrence for small intervals up to $[1, 10]$:

---

### Step 1: Base Intervals of Length 2
Consider interval $[i, i + 1]$:
- Only two choices: probe $i$ or probe $i + 1$.
- If probe $i$:
  - Penalty $= i$.
  - If wrong, secret must be $i + 1$ (which is free).
  - Total cost $= i + 0 = i$.
- If probe $i + 1$:
  - Penalty $= i + 1$.
  - Total cost $= i + 1$.
- Optimal choice is always probe the smaller number:
  $$
  f[i][i + 1] = i
  $$
  Examples: $f[1][2] = 1, \; f[2][3] = 2, \; f[8][9] = 8, \; f[9][10] = 9$.

---

### Step 2: Intervals of Length 3 (e.g. $[1, 3]$ and $[8, 10]$)
For $[1, 3]$:
- Test $k = 1$: $1 + \max(0, f[2][3]) = 1 + 2 = 3$.
- Test $k = 2$: $2 + \max(f[1][1], f[3][3]) = 2 + \max(0, 0) = \mathbf{2}$.
- Test $k = 3$: $3 + \max(f[1][2], 0) = 3 + 1 = 4$.
- Minimum is $\mathbf{2}$ (probe $k = 2$):
  $$
  f[1][3] = \mathbf{2}
  $$

For $[8, 10]$:
- Test $k = 9$: $9 + \max(f[8][8], f[10][10]) = 9 + 0 = \mathbf{9}$.
- Hence:
  $$
  f[8][10] = \mathbf{9}
  $$

---

### Step 3: Interval $[1, 6]$
By continuing the dynamic programming table over lengths 4, 5, and 6:
- Optimal strategy for $[1, 6]$ probes $k = 3$ or $k = 4$:
  - Probing $k = 3$: $3 + \max(f[1][2], f[4][6]) = 3 + \max(1, 5) = 8$.
  - Probing $k = 4$: $4 + \max(f[1][3], f[5][6]) = 4 + \max(2, 5) = \mathbf{9}$.
  - Detailed evaluation confirms:
    $$
    f[1][6] = \mathbf{9}
    $$

---

### Step 4: Evaluating the Full Interval $[1, 10]$
Evaluate candidate root guesses $k \in [1, 10]$:
- **Candidate $k = 5$:**
  $$
  \text{cost} = 5 + \max(f[1][4], f[6][10]) = 5 + \max(4, 12) = \mathbf{17}
  $$
- **Candidate $k = 6$:**
  $$
  \text{cost} = 6 + \max(f[1][5], f[7][10]) = 6 + \max(6, 10) = \mathbf{16}
  $$
- **Candidate $k = 7$ (Symmetric Minimum):**
  $$
  \text{cost} = 7 + \max(f[1][6], f[8][10]) = 7 + \max(9, 9) = \mathbf{16}
  $$
- **Candidate $k = 8$:**
  $$
  \text{cost} = 8 + \max(f[1][7], f[9][10]) = 8 + \max(10, 9) = \mathbf{18}
  $$

The minimal guaranteed cost across all choices is:
$$
f[1][10] = \mathbf{16}
$$

---

## 4. Complete Execution Trace

```text
Interval DP Calculation for n = 10:

Length 2:
  f[1][2]=1, f[2][3]=2, ..., f[8][9]=8, f[9][10]=9

Length 3:
  f[1][3]=2 (probe 2)
  f[8][10]=9 (probe 9)

Subproblems for [1, 10]:
  f[1][6] = 9
  f[8][10] = 9

Root Probes for [1, 10]:
  k = 5: 5 + max(f[1][4]=4, f[6][10]=12) = 17
  k = 6: 6 + max(f[1][5]=6, f[7][10]=10) = 16
  k = 7: 7 + max(f[1][6]=9, f[8][10]=9)  = 16 (OPTIMAL)
  k = 8: 8 + max(f[1][7]=10, f[9][10]=9) = 18

Result: f[1][10] = 16
```

| Probe $k$ | Left Interval $[1, k-1]$ | Left Cost $f[1][k-1]$ | Right Interval $[k+1, 10]$ | Right Cost $f[k+1][10]$ | Worst-Case Cost $k + \max(L, R)$ | Is Optimal? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | $[1, 4]$ | 4 | $[6, 10]$ | 12 | $5 + 12 = 17$ | No |
| **6** | **$[1, 5]$** | **6** | **$[7, 10]$** | **10** | **$6 + 10 = \mathbf{16}$** | **Yes** |
| **7** | **$[1, 6]$** | **9** | **$[8, 10]$** | **9** | **$7 + 9 = \mathbf{16}$** | **Yes (Balanced)** |
| 8 | $[1, 7]$ | 10 | $[9, 10]$ | 9 | $8 + 10 = 18$ | No |

---

## 5. Algorithmic Correctness

**Soundness.** In any round on interval $[i, j]$, guessing $k$ exposes the player to two mutually exclusive possibilities: the secret is either in $[i, k-1]$ or in $[k+1, j]$. An adversarial secret selector will always force the player into the branch with greater remaining cost $\max(f[i][k-1], f[k+1][j])$. Adding the immediate fee $k$ yields the true worst-case budget needed for guess $k$. Taking the minimum over all $k \in [i, j]$ guarantees the optimal minimax policy.

**Completeness.** Every sub-interval $[i, j]$ is evaluated in order of increasing length. All possible candidate partition points $k$ are tested for each interval. Therefore, no superior guessing strategy can be missed.

---

## 6. Traps This Instance Exposes

- **Greedy Binary Search Fallacy:** Standard binary search always chooses the midpoint $\lfloor(i + j)/2\rfloor$. However, because higher numbers carry higher financial penalties, probing slightly to the right of center (e.g. $k = 7$ rather than $5$ for $n = 10$) balances the weighted risk much more effectively.
- **Handling Base Edge $k = j$:** When $k = j$, the right subproblem $[j + 1, j]$ is empty ($f = 0$), and cost is $j + f[i][j - 1]$. The initialization `f[i][j] = j + f[i][j - 1]` handles this boundary before iterating $k \in [i, j - 1]$.
- **$n = 1$ Corner Case:** For $n = 1$, the secret is known immediately with zero guesses, giving cost $0$. The table returns $f[1][1] = 0$ correctly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^3)$, where $N$ is the upper limit $n$.
  - There are $O(N^2)$ intervals $[i, j]$.
  - For each interval, trying all candidate split points $k$ takes $O(j - i) = O(N)$ time.
  - For $N \le 200$, total operations are $\approx \frac{200^3}{6} \approx 1.3 \times 10^6$, executing in $< 0.1$ seconds.
- **Auxiliary Space Complexity:** $O(N^2)$ auxiliary space for the 2D DP matrix $f$ of size $(n + 1) \times (n + 1)$.