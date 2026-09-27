# Guided Example: Stone Game

We trace the step-by-step game-theoretic minimax dynamic programming, alternating parity coloring proof, zero-sum score differential recurrence, and first-player guaranteed win derivation on representative stone pile rows:

- **Input:**
  $$
  piles = [5, 3, 4, 5]
  $$
- **Required output:** `true`
  - Rules of the game:
    - Alice and Bob play a game with an **even number of piles** $n = 4$ arranged in a row.
    - Each pile $i$ contains $piles[i]$ stones.
    - The total number of stones $\sum piles[i] = 5 + 3 + 4 + 5 = 17$ is strictly **odd** (ties are impossible).
    - Players take turns, with **Alice going first**.
    - On a player's turn, they must take all stones from either the **first pile** or the **last pile** of the remaining row.
    - The game ends when all piles are taken. The player with the most stones wins.
    - Objective: Return `true` if and only if Alice wins assuming both players play optimally.
    - For $piles = [5, 3, 4, 5]$:
      - Total stones: $17$. A player needs $\ge 9$ stones to win.
      - Alice can choose the even-indexed piles (indices $0$ and $2$): $5 + 4 = 9$ stones.
      - Bob can only obtain odd-indexed piles (indices $1$ and $3$): $3 + 5 = 8$ stones.
      - Alice scores $9 > 8$, guaranteeing victory!
      - Result: **`true`**.
- **The Parity Coloring Strategy & Minimax Invariants:**
  - **The Parity Invariant (Why Alice Always Wins):**
    - Color the piles alternately with two colors based on index parity:
      $$
      \text{Even Piles} = \{piles[0], piles[2], \dots\}, \quad \text{Odd Piles} = \{piles[1], piles[3], \dots\}
      $$
    - Because the total sum is odd, the two partition sums cannot be equal:
      $$
      \sum \text{Even Piles} \ne \sum \text{Odd Piles}
      $$
    - Therefore, one parity set strictly outweighs the other.
    - Since $n$ is even, the two endpoints at the start are index $0$ (Even) and index $n - 1$ (Odd).
    - If Alice wants to take all Even piles:
      - She takes index $0$ (Even).
      - The remaining ends are index $1$ (Odd) and index $n - 1$ (Odd). Bob is forced to take an Odd pile!
      - Whichever Odd pile Bob takes, he exposes an adjacent Even pile for Alice to take on her next turn!
    - By induction, **Alice can choose to take all Even piles or all Odd piles at will**.
    - Because she picks the heavier set, **Alice is mathematically guaranteed to win every game**!
  - **Interval Dynamic Programming Formulation:**
    - To quantify the exact margin of victory, let $dp[i][j]$ denote the maximum net stone advantage (current player's score minus opponent's score) on subsegment $piles[i \dots j]$:
      $$
      dp[i][j] = \max(piles[i] - dp[i + 1][j], \; piles[j] - dp[i][j - 1])
      $$
    - Base case: $dp[i][i] = piles[i]$.
    - If $dp[0][n - 1] > 0$, Alice wins.

---

## 1. Instance & Teaching Goal

Given $piles = [5, 3, 4, 5]$, evaluate both the combinatorial parity proof and the full minimax DP table to derive Alice's margin of victory.

```text
Piles: [5, 3, 4, 5]
Index:  0  1  2  3

Parity Analysis:
  Even index sum: piles[0] + piles[2] = 5 + 4 = 9
  Odd index sum:  piles[1] + piles[3] = 3 + 5 = 8
  Since 9 > 8, Alice forces all even piles and wins by at least 1 stone!

Minimax DP:
  dp[0][3] computes optimal net difference.
  dp[0][3] = max(5 - dp[1][3], 5 - dp[0][2]) = max(5 - 4, 5 - 4) = 1 > 0
  Alice wins!
```

The teaching goal is to demonstrate both the non-constructive parity coloring proof and the constructive interval DP recurrence.

---

## 2. Conceptual Foundation & Invariants

### 1. Zero-Sum Differential Metric:
Let $S_A$ and $S_B$ be Alice's and Bob's final scores.
The game is zero-sum: $S_A + S_B = \text{Total}$.
Alice wins if and only if $S_A - S_B > 0$.

### 2. Bellman Minimax Equation:
For subsegment $piles[i \dots j]$:
$$
dp[i][j] = \begin{cases}
piles[i] & \text{if } i = j \\
\max\left(piles[i] - dp[i + 1][j], \; piles[j] - dp[i][j - 1]\right) & \text{if } i < j
\end{cases}
$$

---

## 3. Step-by-Step Worked Execution

We trace $piles = [5, 3, 4, 5]$ using interval DP:

---

### Phase 1: Subproblems of Length 1 (Base Cases)
- $dp[0][0] = piles[0] = 5$
- $dp[1][1] = piles[1] = 3$
- $dp[2][2] = piles[2] = 4$
- $dp[3][3] = piles[3] = 5$

---

### Phase 2: Subproblems of Length 2
- **Interval $[0, 1]$ ($[5, 3]$):**
  $$
  dp[0][1] = \max(5 - dp[1][1], \; 3 - dp[0][0]) = \max(5 - 3, \; 3 - 5) = \mathbf{2}
  $$
- **Interval $[1, 2]$ ($[3, 4]$):**
  $$
  dp[1][2] = \max(3 - dp[2][2], \; 4 - dp[1][1]) = \max(3 - 4, \; 4 - 3) = \mathbf{1}
  $$
- **Interval $[2, 3]$ ($[4, 5]$):**
  $$
  dp[2][3] = \max(4 - dp[3][3], \; 5 - dp[2][2]) = \max(4 - 5, \; 5 - 4) = \mathbf{1}
  $$

---

### Phase 3: Subproblems of Length 3
- **Interval $[0, 2]$ ($[5, 3, 4]$):**
  - Pick left ($5$): $5 - dp[1][2] = 5 - 1 = 4$.
  - Pick right ($4$): $4 - dp[0][1] = 4 - 2 = 2$.
  - $dp[0][2] = \max(4, 2) = \mathbf{4}$.
- **Interval $[1, 3]$ ($[3, 4, 5]$):**
  - Pick left ($3$): $3 - dp[2][3] = 3 - 1 = 2$.
  - Pick right ($5$): $5 - dp[1][2] = 5 - 1 = 4$.
  - $dp[1][3] = \max(2, 4) = \mathbf{4}$.

---

### Phase 4: Subproblem of Length 4 (Full Game $[0, 3]$)
- Candidate 1: Alice takes left pile $piles[0] = 5$:
  - Remaining interval $[1, 3]$ leaves Bob with advantage $dp[1][3] = 4$.
  - Net score: $5 - dp[1][3] = 5 - 4 = \mathbf{1}$.
- Candidate 2: Alice takes right pile $piles[3] = 5$:
  - Remaining interval $[0, 2]$ leaves Bob with advantage $dp[0][2] = 4$.
  - Net score: $5 - dp[0][2] = 5 - 4 = \mathbf{1}$.
- Both choices yield:
  $$
  dp[0][3] = \max(1, 1) = \mathbf{1}
  $$
- Because $dp[0][3] = 1 > 0$, Alice wins by at least $1$ stone!
- **Return: `true`**.

---

## 4. Complete Execution Trace

| Interval Length | Segment $[i, j]$ | Subarray Piles | Option A (Pick $piles[i]$) | Option B (Pick $piles[j]$) | Optimal Net Difference $dp[i][j]$ | Leading Player |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $[0, 0]$ | $[5]$ | — | — | $5$ | Current |
| $1$ | $[1, 1]$ | $[3]$ | — | — | $3$ | Current |
| $1$ | $[2, 2]$ | $[4]$ | — | — | $4$ | Current |
| $1$ | $[3, 3]$ | $[5]$ | — | — | $5$ | Current |
| $2$ | $[0, 1]$ | $[5, 3]$ | $5 - 3 = 2$ | $3 - 5 = -2$ | $2$ | Current |
| $2$ | $[1, 2]$ | $[3, 4]$ | $3 - 4 = -1$ | $4 - 3 = 1$ | $1$ | Current |
| $2$ | $[2, 3]$ | $[4, 5]$ | $4 - 5 = -1$ | $5 - 4 = 1$ | $1$ | Current |
| $3$ | $[0, 2]$ | $[5, 3, 4]$ | $5 - 1 = 4$ | $4 - 2 = 2$ | $4$ | Current |
| $3$ | $[1, 3]$ | $[3, 4, 5]$ | $3 - 1 = 2$ | $5 - 1 = 4$ | $4$ | Current |
| **$4$** | **$[0, 3]$** | **$[5, 3, 4, 5]$** | **$5 - 4 = 1$** | **$5 - 4 = 1$** | **`1`** | **`Alice (true)`** |

---

## 5. Boundary Cases & Failure Modes

- **Two Piles Only ($n = 2$, e.g. $[3, 7]$):** Alice takes $\max(piles[0], piles[1]) = 7$, leaving Bob with $3$. Alice wins $7 - 3 = 4 > 0 \implies$ returns `true`.
- **Heavier Odd Parity (e.g. $[3, 7, 2, 3]$):** Even sum is $3 + 2 = 5$; odd sum is $7 + 3 = 10$. Alice takes right pile $piles[3] = 3$ (odd), forcing Bob into even piles. Alice takes $7$ next, securing $10 > 5 \implies$ returns `true`.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Endpoint Selection:** Simply picking $\max(piles[i], piles[j])$ is locally tempting but globally flawed. For example, in $[3, 9, 1, 2]$, picking $3$ over $2$ exposes $9$ to Bob, causing Alice to lose. Alice must look ahead via DP.
- **Unnecessary Search Space Expansion:** Attempting full game tree minimax with depth $N$ without memoization explodes to $\mathcal{O}(2^N)$ paths. The interval DP collapses this to $\mathcal{O}(N^2)$ states.
- **Overcomplicating the Constant-Time Answer:** Under the specific constraints ($N$ is even, sum is odd, Alice starts), Alice is mathematically proven to always win $\implies$ constant-time return of `true` is valid.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Dynamic Programming: $\mathcal{O}(N^2)$ states with $\mathcal{O}(1)$ transitions $\implies \mathcal{O}(N^2)$.
  - Analytical Parity Proof: $\mathcal{O}(1)$ constant time.
  - Both run well under $1$ ms for $N \le 500$.
- **Auxiliary Space Complexity:**
  - DP memoization table: $\mathcal{O}(N^2)$ space (reducible to $\mathcal{O}(N)$ using 1D rolling buffers), or $\mathcal{O}(1)$ via direct return.