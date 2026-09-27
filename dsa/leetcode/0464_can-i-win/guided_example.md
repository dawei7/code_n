# Guided Example: Can I Win

We trace the step-by-step game-theoretic Minimax formulation, bitmask state encoding ($2^M \le 2^{20}$), immediate win conditions ($s + i \ge desiredTotal$), opponent forced-loss propagation ($\neg \text{dfs}(\dots)$), and symmetric complement counter-strategies on representative game setups:

- **Input:** $maxChoosableInteger = 10, \quad desiredTotal = 11$
- **Required output:** `false`
  - Available integers: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$
  - Total pool sum: $\frac{10 \times 11}{2} = 55 \ge 11$ (Game can be won)
- **Game-theoretic execution trace:**
  - Can Player 1 force a win on turn 1?
    - The maximum possible single choice is $10$.
    - Current total after turn 1: at most $10 < 11$. Player 1 cannot win on move 1.
  - Symmetrical Complement Strategy (Player 2's counter-move):
    - Whichever integer $x \in [1, 10]$ Player 1 selects on Turn 1:
    - Player 2 can select the exact complement:
      $$
      y = 11 - x
      $$
    - Because $11$ is odd, $x \ne 11 - x$ for all integers (no integer satisfies $2x = 11$).
    - Therefore, $y$ is distinct from $x$ and is guaranteed to be unused in the pool!
    - Resulting cumulative total after Player 2's turn:
      $$
      x + y = x + (11 - x) = \mathbf{11} \ge desiredTotal
      $$
    - Player 2 unconditionally reaches the target on Turn 2 regardless of Player 1's choice!
    - Player 1 has zero winning openings $\implies$ Return **`false`**.
- **Immediate Win Opening:** $maxChoosableInteger = 10, desiredTotal = 8 \implies$ Player 1 chooses $8 \ge 8$ on turn 1 $\implies \mathbf{true}$
- **Target Exceeds Pool Sum:** $maxChoosableInteger = 4, desiredTotal = 15$
  - Sum of $\{1, 2, 3, 4\} = 10 < 15 \implies$ Target unreachable by any player $\implies \mathbf{false}$
- **Zero Target:** $desiredTotal \le 0 \implies$ Target already met $\implies \mathbf{true}$

This instance demonstrates game theory in finite zero-sum combinatorial games, mathematically proves why complementary pairing guarantees second-player wins on odd totals, and derives $O(2^M)$ runtime and $O(2^M)$ space bounds via bitmask memoization.

---

## 1. Instance & Teaching Goal

Given $maxChoosableInteger = 10$ and $desiredTotal = 11$:
Two players take turns picking integers from the common pool $\{1, 2, \dots, 10\}$ without replacement.
The chosen numbers are added to a running sum.
The first player to make the running sum reach or exceed $desiredTotal$ wins.
Determine if the **first player** can force a win assuming both players play optimally.

```text
Pool of Numbers: { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
Target: 11

Player 1 Chooses x:      Player 2 Counters With (11 - x):
  Pick 1                  Picks 10 -> Sum = 1 + 10 = 11 (P2 Wins)
  Pick 2                  Picks 9  -> Sum = 2 + 9  = 11 (P2 Wins)
  ...                     ...
  Pick 10                 Picks 1  -> Sum = 10 + 1 = 11 (P2 Wins)

No matter what Player 1 opens with, Player 2 wins on move 2.
Result: false
```

### The Game-Theoretic Minimax Axiom
A game state is a **winning state** for the current player if there exists **at least one valid move** that either:
1. Reaches the target immediately ($s + i \ge desiredTotal$), or
2. Transitions the game into a state from which the opponent **cannot force a win** (a losing state for the next player).
If every available move transitions into a winning state for the opponent, the current state is a **losing state**.

---

## 2. Conceptual Foundation & Invariants

### 1. Bitmask State Representation:
Since $maxChoosableInteger = M \le 20$:
We represent the set of used numbers as a bitmask of length $M + 1$:
$$
mask = \sum_{i \in \text{used}} 2^i
$$
Number $i$ is available if $(mask \gg i) \ \& \ 1 == 0$.

### 2. Recursive Game Search:
Let $dfs(mask, s)$ return `True` if the player facing state $(mask, s)$ can force a win:
- For each unpicked number $i \in [1, M]$:
  - If $s + i \ge desiredTotal$:
    Current player wins immediately $\implies$ Return `True`.
  - If $\neg dfs(mask \mid (2^i), \; s + i)$:
    Picking $i$ leaves the opponent in a state from which they cannot win $\implies$ Current player wins $\implies$ Return `True`.
- If no such $i$ exists:
  Every move leads to an opponent win $\implies$ Return `False`.

### 3. Early Termination Invariants:
1. **Total Sum Inadequacy:** If $\sum_{i=1}^M i = \frac{M(M+1)}{2} < desiredTotal$, the target is mathematically unreachable by anyone. Return `False`.
2. **Zero or Negative Target:** If $desiredTotal \le 0$, the starting total $0 \ge desiredTotal$ is already satisfied. Return `True`.

> **Game Invariant.** A state is winning if and only if there exists a transition to an opponent losing state. Because games are finite and strictly acyclic, memoization over $mask$ uniquely determines the outcome without loops.

---

## 3. Step-by-Step Worked Execution

We trace $M = 10$ and $desiredTotal = 11$:

---

### Step 1: Pre-Condition Checks
- Total sum of pool:
  $$
  S = \frac{10 \times 11}{2} = 55
  $$
- Test $S \ge desiredTotal$: $55 \ge 11$ (Pass: Target is reachable).
- Test $desiredTotal > 0$: $11 > 0$ (Pass).

---

### Step 2: Evaluate Turn 1 Options for Player 1
Player 1 considers all possible opening choices $i \in [1, 10]$:
Can any choice reach $11$ immediately?
- Max choice is $i = 10 < 11$.
- No choice can win immediately.

---

### Step 3: Analyze Opponent Response (Player 2's Turn 2)
For each choice $x$ made by Player 1, Player 2 faces running sum $s = x$ with mask $2^x$:
- Player 2 wants to reach $11$, requiring remaining sum $11 - x$.
- Let $y = 11 - x$:
  - Since $1 \le x \le 10$, $1 \le 11 - x \le 10$, so $y \in [1, 10]$.
  - Is $y$ still available?
    - $y == x \iff 11 - x = x \iff 2x = 11 \iff x = 5.5 \notin \mathbb{Z}$.
    - Because $11$ is odd, $y \ne x$ always.
    - Therefore, $y$ was not chosen on turn 1 and remains available in the pool!
- Player 2 selects $y = 11 - x$:
  $$
  \text{New Total} = x + (11 - x) = \mathbf{11} \ge desiredTotal
  $$
- Player 2 wins on turn 2 for **every possible choice** of $x$.

---

### Step 4: Conclusion
Every branch available to Player 1 leads to an immediate win for Player 2.
Thus, $dfs(0, 0)$ evaluates to **`false`**.

---

## 4. Complete Execution Trace

| Player 1 Opening $x$ | Running Total $s$ | Complement $y = 11 - x$ | Is $y$ in Pool $[1, 10]$? | Is $y \ne x$? | P2 Win on Move 2? | P1 Can Win? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | $10$ | Yes | Yes ($10 \ne 1$) | **Yes ($1 + 10 = 11$)** | No |
| $2$ | $2$ | $9$ | Yes | Yes ($9 \ne 2$) | **Yes ($2 + 9 = 11$)** | No |
| $3$ | $3$ | $8$ | Yes | Yes ($8 \ne 3$) | **Yes ($3 + 8 = 11$)** | No |
| $4$ | $4$ | $7$ | Yes | Yes ($7 \ne 4$) | **Yes ($4 + 7 = 11$)** | No |
| $5$ | $5$ | $6$ | Yes | Yes ($6 \ne 5$) | **Yes ($5 + 6 = 11$)** | No |
| $6$ | $6$ | $5$ | Yes | Yes ($5 \ne 6$) | **Yes ($6 + 5 = 11$)** | No |
| $7$ | $7$ | $4$ | Yes | Yes ($4 \ne 7$) | **Yes ($7 + 4 = 11$)** | No |
| $8$ | $8$ | $3$ | Yes | Yes ($3 \ne 8$) | **Yes ($8 + 3 = 11$)** | No |
| $9$ | $9$ | $2$ | Yes | Yes ($2 \ne 9$) | **Yes ($9 + 2 = 11$)** | No |
| $10$| $10$ | $1$ | Yes | Yes ($1 \ne 10$)| **Yes ($10 + 1 = 11$)**| No |
| **All Branches**| — | — | — | — | — | **Result: `false`** |

---

## 5. Boundary Cases & Failure Modes

- **First Move Can Reach Target ($desiredTotal \le M$):** Player 1 picks $desiredTotal$ directly $\implies \mathbf{true}$.
- **Target Unattainable ($\sum_{i=1}^M i < desiredTotal$):** Even if all numbers are picked, the sum falls short $\implies \mathbf{false}$.
- **Initial Target Non-Positive ($desiredTotal \le 0$):** Target is satisfied before any move $\implies \mathbf{true}$.
- **Even Target Sum ($M=10, desiredTotal=12$):** Complement $12 - 6 = 6$ requires reusing 6, breaking the simple complement strategy; the full bitmask search resolves the optimal line.

---

## 6. Traps & Common Anti-Patterns

- **Including Running Sum in the Memoization Key:** The running sum $s$ is uniquely determined by the chosen numbers: $s = \sum_{k \in mask} k$. Memoizing on both $(mask, s)$ creates redundant state entries. Memoizing strictly on $mask$ reduces the state space to at most $2^M$.
- **Greedy Assumptions:** Assuming picking the largest available number is always optimal is false. In many positions, picking a smaller number forces the opponent into a range where all choices overshoot or allow a trap. Full minimax search is required.
- **Forgetting the Total Sum Pre-Check:** Running DFS when $desiredTotal > \sum_{i=1}^M i$ searches all $2^M$ leaf states before returning `False`, wasting significant time. The $O(1)$ pre-check avoids this entirely.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - There are $2^M$ possible subsets of chosen numbers.
  - For each state, we iterate over $M$ candidates.
  - Total Time: $\mathcal{O}(M \cdot 2^M)$. For $M \le 20$, $20 \times 2^{20} \approx 2 \times 10^7$ operations in the worst case, but heavily pruned by early winning branches, executing in $< 80$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(2^M)$ to memoize the boolean outcome for visited bitmasks.
  - Recursion stack depth is at most $M \le 20$.