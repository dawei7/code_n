# Guided Example: Predict the Winner

We trace the step-by-step game-theoretic Minimax formulation, relative score advantage metric ($Score_{current} - Score_{opponent}$), interval dynamic programming transitions ($dfs(i, j) = \max(nums[i] - dfs(i+1, j), nums[j] - dfs(i, j-1))$), zero-sum terminal evaluation ($\ge 0$), and backward game tree induction on representative game boards:

- **Input:** $nums = [1, 5, 2]$
- **Required output:** `false`
  - Array length: $N = 3$ (Player 1 moves first)
  - Game rules:
    - A player may choose either the left endpoint $nums[i]$ or the right endpoint $nums[j]$.
    - Both players play optimally to maximize their own total score.
    - Player 1 wins if $Score(P_1) \ge Score(P_2)$.
- **Minimax interval evaluation trace:**
  - Let $dfs(i, j)$ be the maximum net score differential ($P_{current} - P_{opponent}$) achievable on subarray $nums[i \dots j]$.
  - **Subproblems of Length 1 (Base Cases):**
    - $dfs(0, 0) = nums[0] = 1$
    - $dfs(1, 1) = nums[1] = 5$
    - $dfs(2, 2) = nums[2] = 2$
  - **Subproblems of Length 2:**
    - Interval $[1, 5]$ (indices $0 \dots 1$):
      - Pick left ($1$): advantage $= 1 - dfs(1, 1) = 1 - 5 = -4$
      - Pick right ($5$): advantage $= 5 - dfs(0, 0) = 5 - 1 = +4$
      - $dfs(0, 1) = \max(-4, 4) = \mathbf{+4}$
    - Interval $[5, 2]$ (indices $1 \dots 2$):
      - Pick left ($5$): advantage $= 5 - dfs(2, 2) = 5 - 2 = +3$
      - Pick right ($2$): advantage $= 2 - dfs(1, 1) = 2 - 5 = -3$
      - $dfs(1, 2) = \max(3, -3) = \mathbf{+3}$
  - **Root Interval $[1, 5, 2]$ (indices $0 \dots 2$, Player 1's Opening Move):**
    - Choice A (Pick left endpoint $nums[0] = 1$):
      - Remaining subarray for Player 2: $[5, 2]$ (indices $1 \dots 2$)
      - Player 2 will achieve advantage $dfs(1, 2) = +3$
      - Player 1's net differential:
        $$
        nums[0] - dfs(1, 2) = 1 - 3 = \mathbf{-2}
        $$
    - Choice B (Pick right endpoint $nums[2] = 2$):
      - Remaining subarray for Player 2: $[1, 5]$ (indices $0 \dots 1$)
      - Player 2 will achieve advantage $dfs(0, 1) = +4$
      - Player 1's net differential:
        $$
        nums[2] - dfs(0, 1) = 2 - 4 = \mathbf{-2}
        $$
    - Optimal opening move:
      $$
      dfs(0, 2) = \max(-2, -2) = \mathbf{-2}
      $$
  - Winning condition check:
    $$
    dfs(0, 2) \ge 0 \iff -2 \ge 0 \quad (\mathbf{False})
    $$
  - Player 2 strictly wins by $2$ points. Return **`false`**.
- **First Player Secures Advantage Instance:** $nums = [1, 5, 233, 7]$
  - Even length array: Player 1 can force picking all odd-indexed or all even-indexed numbers.
  - Picking $7$ secures access to $233 \implies dfs(0, 3) > 0 \implies \mathbf{true}$
- **Single Element Game:** $nums = [10] \implies dfs(0, 0) = 10 \ge 0 \implies \mathbf{true}$
- **Equal Scores Tie:** $nums = [1, 1] \implies dfs(0, 1) = 1 - 1 = 0 \ge 0 \implies \mathbf{true}$ (Player 1 wins ties)

This instance demonstrates zero-sum sequential game theory with backward induction, mathematically proves why relative difference formulation reduces states from 4 dimensions to 2, and derives $O(N^2)$ runtime and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 5, 2]$:
Two players take turns choosing numbers from either the left or right end of the array.
Each player adds the chosen number to their cumulative score.
Return `true` if **Player 1 can win** the game (or tie), assuming both players play optimally.

```text
Game Board: [ 1,  5,  2 ]

Player 1 Move 1:
  Option A: Take 1 -> Leaves [5, 2]. Player 2 takes 5 -> P1 gets 1+2=3, P2 gets 5 (P2 wins!)
  Option B: Take 2 -> Leaves [1, 5]. Player 2 takes 5 -> P1 gets 2+1=3, P2 gets 5 (P2 wins!)

Both branches leave Player 1 with score 3 and Player 2 with score 5.
Player 1 loses -> false
```

### The Relative Difference Formulation
Instead of tracking two separate scores $(Score_1, Score_2)$:
We define the state as the **net score differential** of the player whose turn it is:
$$
\Delta = \text{Current Player's Score} - \text{Opponent's Score}
$$
- If the current player chooses $nums[i]$, they earn $nums[i]$ points.
- On the subsequent subproblem $nums[i + 1 \dots j]$, the roles swap: the opponent becomes the active player and earns a net differential of $dfs(i + 1, j)$.
- Therefore, the current player's net differential becomes:
  $$
  \text{Net Differential} = nums[i] - dfs(i + 1, j)
  $$
- This compresses the two-player game into a single elegant recursive recurrence.

---

## 2. Conceptual Foundation & Invariants

### 1. The Minimax Dynamic Programming Recurrence:
Let $dfs(i, j)$ be the maximum net score advantage achievable on subarray $nums[i \dots j]$:
$$
dfs(i, j) =
\begin{cases}
0 & \text{if } i > j \\
nums[i] & \text{if } i == j \\
\max\Big(nums[i] - dfs(i + 1, j), \; nums[j] - dfs(i, j - 1)\Big) & \text{if } i < j
\end{cases}
$$

### 2. Victory Condition:
Player 1 starts on the entire array $nums[0 \dots n - 1]$:
- If $dfs(0, n - 1) > 0$: Player 1 strictly beats Player 2.
- If $dfs(0, n - 1) == 0$: The game ends in a tie. By game rules, Player 1 wins ties!
- Therefore, Player 1 wins if and only if:
  $$
  dfs(0, n - 1) \ge 0
  $$

> **Zero-Sum Optimal Play Invariant.** At every sub-interval $[i, j]$, the active player selects the endpoint that maximizes their own margin of victory, which simultaneously minimizes the opponent's margin.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 5, 2]$ ($n = 3$):

---

### Step 1: Base Intervals of Length 1 ($i == j$)
- $dfs(0, 0) = nums[0] = \mathbf{1}$
- $dfs(1, 1) = nums[1] = \mathbf{5}$
- $dfs(2, 2) = nums[2] = \mathbf{2}$

---

### Step 2: Intervals of Length 2 ($j - i = 1$)

1. **Interval $[0, 1]$ (Subarray $[1, 5]$):**
   - Take Left ($1$): $nums[0] - dfs(1, 1) = 1 - 5 = -4$.
   - Take Right ($5$): $nums[1] - dfs(0, 0) = 5 - 1 = +4$.
   - Optimal choice:
     $$
     dfs(0, 1) = \max(-4, 4) = \mathbf{+4}
     $$

2. **Interval $[1, 2]$ (Subarray $[5, 2]$):**
   - Take Left ($5$): $nums[1] - dfs(2, 2) = 5 - 2 = +3$.
   - Take Right ($2$): $nums[2] - dfs(1, 1) = 2 - 5 = -3$.
   - Optimal choice:
     $$
     dfs(1, 2) = \max(3, -3) = \mathbf{+3}
     $$

---

### Step 3: Full Interval $[0, 2]$ (Subarray $[1, 5, 2]$)
Evaluate Player 1's two opening choices:
- **Choice 1: Take Left ($nums[0] = 1$):**
  Leaves $[1, 2]$ for Player 2:
  $$
  nums[0] - dfs(1, 2) = 1 - 3 = \mathbf{-2}
  $$
- **Choice 2: Take Right ($nums[2] = 2$):**
  Leaves $[0, 1]$ for Player 2:
  $$
  nums[2] - dfs(0, 1) = 2 - 4 = \mathbf{-2}
  $$
- Optimal Decision:
  $$
  dfs(0, 2) = \max(-2, -2) = \mathbf{-2}
  $$

---

### Step 4: Final Win Evaluation
Test $dfs(0, 2) \ge 0$:
$$
-2 \ge 0 \quad (\mathbf{False})
$$
Player 1 cannot win. Return **`false`**.

---

## 4. Complete Execution Trace

| Subarray Range $[i, j]$ | Subarray Values | Choice Left: $nums[i] - dfs(i+1, j)$ | Choice Right: $nums[j] - dfs(i, j-1)$ | Optimal Difference $dfs(i, j)$ | Active Player Advantage |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $[0, 0]$ | $[1]$ | — | — | **$+1$** | $+1$ |
| $[1, 1]$ | $[5]$ | — | — | **$+5$** | $+5$ |
| $[2, 2]$ | $[2]$ | — | — | **$+2$** | $+2$ |
| $[0, 1]$ | $[1, 5]$ | $1 - 5 = -4$ | $5 - 1 = \mathbf{+4}$ | **$+4$** | $+4$ |
| $[1, 2]$ | $[5, 2]$ | $5 - 2 = \mathbf{+3}$ | $2 - 5 = -3$ | **$+3$** | $+3$ |
| **$[0, 2]$** | **$[1, 5, 2]$** | $1 - 3 = \mathbf{-2}$ | $2 - 4 = \mathbf{-2}$ | **$-2$** | **$-2$ (P1 Loses)** |

---

## 5. Boundary Cases & Failure Modes

- **Even Length Parity Trick:** Whenever $N$ is even, Player 1 can choose to take all even-indexed numbers or all odd-indexed numbers, guaranteeing at least a tie or win ($\mathbf{true}$ unconditionally for even $N$).
- **Single Element Array ($N = 1$):** Player 1 takes the only number and immediately wins $\implies \mathbf{true}$.
- **All Elements Equal ($[2, 2, 2]$):** Player 1 takes 2, Player 2 takes 2, Player 1 takes 2 $\implies 4 - 2 = 2 \ge 0 \implies \mathbf{true}$.
- **Tie Score:** If $Score(P_1) == Score(P_2)$, $dfs = 0 \ge 0 \implies \mathbf{true}$.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Endpoint Selection:** Taking the larger available endpoint immediately is a naive greedy trap: picking 2 instead of 1 in $[2, 100, 1]$ gives the opponent immediate access to 100. Minimax looks ahead across all future turns.
- **Tracking Both Scores in State (`(i, j, score1, score2)`):** Tracking two scores blows up the state space to $O(N^2 \cdot S^2)$, causing Memory Limit Exceeded. Using the relative difference reduces the state to just two pointers $(i, j)$.
- **Strict Inequality on Win Condition:** Writing `dfs > 0` returns false on ties. The problem specifies that Player 1 wins if scores are equal, requiring `dfs >= 0`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of distinct states $(i, j)$ with $0 \le i \le j < N$ is $\frac{N(N + 1)}{2} = O(N^2)$.
  - Each state performs $O(1)$ arithmetic operations.
  - Total Time: $\mathcal{O}(N^2)$. For $N \le 20$, $N^2 \le 400$ operations, running in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ memoization cache table.