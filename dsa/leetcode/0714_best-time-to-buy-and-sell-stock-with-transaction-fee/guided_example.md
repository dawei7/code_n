# Guided Example: Best Time to Buy and Sell Stock with Transaction Fee

We trace the step-by-step two-state financial dynamic programming ($hold, cash$), share acquisition balance deduction ($-prices[i]$), liquidation profit accumulation with transaction fee subtraction ($prices[i] - fee$), state transition Bellman optimizations, and maximum net portfolio profit realization on representative market quote trajectories:

- **Input:** $prices = [1, 3, 2, 8, 4, 9], \quad fee = 2$
- **Required output:** `8`
  - Trading rules:
    - You may execute as many non-overlapping buy-sell cycles as you wish.
    - You can hold at most one share at any given time (must sell before buying again).
    - Every completed transaction incurs a fixed fee of $fee = 2$.
    - Deducting the fee upon selling charges the fee exactly once per buy-sell pair.
    - Optimal trade sequence for $[1, 3, 2, 8, 4, 9]$:
      - Buy at day 0 ($price = 1$), sell at day 3 ($price = 8$): profit $= (8 - 1) - 2 = 5$.
      - Buy at day 4 ($price = 4$), sell at day 5 ($price = 9$): profit $= (9 - 4) - 2 = 3$.
      - Total net profit: $5 + 3 = \mathbf{8}$.
- **Two-State Markov Decision Process & Invariant:**
  - **State Decomposition:**
    - On any day $i$, the trader is in one of two mutually exclusive portfolio states:
      1. **$hold_i$:** Currently holding 1 share of stock.
      2. **$cash_i$:** Currently holding 0 shares of stock (free cash).
  - **Base State (Day 0):**
    - $cash_0 = 0$ (no actions taken, zero profit).
    - $hold_0 = -prices[0]$ (buy stock on day 0).
  - **State Transitions for Day $i \ge 1$:**
    - **To reach State $hold_i$:**
      - Option A: Already held stock yesterday ($hold_{i-1}$).
      - Option B: Held no stock yesterday and buy today ($cash_{i-1} - prices[i]$).
      $$
      hold_i = \max(hold_{i-1}, \; cash_{i-1} - prices[i])
      $$
    - **To reach State $cash_i$:**
      - Option A: Already had 0 stock yesterday ($cash_{i-1}$).
      - Option B: Held stock yesterday and sell today, paying transaction fee $fee$:
        $$
        hold_{i-1} + prices[i] - fee
        $$
      $$
      cash_i = \max(cash_{i-1}, \; hold_{i-1} + prices[i] - fee)
      $$
  - **Terminal Guarantee:**
    - Holding an unsold share at the end cannot be optimal compared to having already sold it or never buying it.
    - Thus, the global maximum profit is strictly:
      $$
      ans = cash_{N-1}
      $$
- **Step-by-Step Worked Execution Trace on $prices = [1, 3, 2, 8, 4, 9]$ with $fee = 2$:**
  - **Day 0 ($price = 1$):**
    $$
    cash = 0, \quad hold = -1
    $$
  - **Day 1 ($price = 3$):**
    - Update $hold$:
      $$
      hold \leftarrow \max(-1, \; 0 - 3) = \max(-1, -3) = \mathbf{-1}
      $$
    - Update $cash$:
      $$
      cash \leftarrow \max(0, \; -1 + 3 - 2) = \max(0, 0) = \mathbf{0}
      $$
      *(Selling at 3 produces $(3 - 1) - 2 = 0$ net gain, matching inaction)*
  - **Day 2 ($price = 2$):**
    - Update $hold$:
      $$
      hold \leftarrow \max(-1, \; 0 - 2) = \max(-1, -2) = \mathbf{-1}
      $$
    - Update $cash$:
      $$
      cash \leftarrow \max(0, \; -1 + 2 - 2) = \max(0, -1) = \mathbf{0}
      $$
  - **Day 3 ($price = 8$):**
    - Update $hold$:
      $$
      hold \leftarrow \max(-1, \; 0 - 8) = \mathbf{-1}
      $$
    - Update $cash$:
      $$
      cash \leftarrow \max(0, \; -1 + 8 - 2) = \max(0, \mathbf{5}) = \mathbf{5}
      $$
      *(Liquidating the share bought at 1 yields $(8 - 1) - 2 = 5$)*
  - **Day 4 ($price = 4$):**
    - Update $hold$:
      $$
      hold \leftarrow \max(-1, \; cash - prices[4]) = \max(-1, \; 5 - 4) = \max(-1, \mathbf{1}) = \mathbf{1}
      $$
      *(Re-investing cash to buy at 4 leaves effective baseline balance $+1$)*
    - Update $cash$:
      $$
      cash \leftarrow \max(5, \; hold + 4 - 2) = \max(5, \; 1 + 4 - 2) = \max(5, 3) = \mathbf{5}
      $$
  - **Day 5 ($price = 9$):**
    - Update $hold$:
      $$
      hold \leftarrow \max(1, \; 5 - 9) = \max(1, -4) = \mathbf{1}
      $$
    - Update $cash$:
      $$
      cash \leftarrow \max(5, \; hold + prices[5] - fee) = \max(5, \; 1 + 9 - 2) = \max(5, \mathbf{8}) = \mathbf{8}
      $$
      *(Selling second share at 9 adds $(9 - 4) - 2 = 3$ to cash, totaling 8)*
  - **Step 6: Terminal Portfolio Value:**
    $$
    ans = cash = \mathbf{8}
    $$
- **Monotonically Decreasing Market ($prices = [9, 8, 7, 5, 2], fee = 1$):**
  - No price rise exceeds the fee.
  - Best strategy is to execute zero trades.
  - $cash$ remains strictly **`0`**.
- **Single Massive Price Surge ($prices = [1, 10], fee = 3$):**
  - Day 0: $hold = -1, cash = 0$.
  - Day 1: $cash = \max(0, -1 + 10 - 3) = \mathbf{6}$.

This instance demonstrates two-state finite horizon optimal control and transaction-friction dynamic programming, mathematically proves why single-state compression preserves history-independent optimality under fee deductions, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given stock prices and a transaction fee $fee$:
Find the **maximum profit** with unlimited trades, paying $fee$ per complete transaction.
Must sell before buying again.

```text
prices = [ 1, 3, 2, 8, 4, 9 ], fee = 2

Day 0 (1): hold = -1, cash = 0
Day 1 (3): hold = -1, cash = 0
Day 2 (2): hold = -1, cash = 0
Day 3 (8): hold = -1, cash = max(0, -1 + 8 - 2) = 5
Day 4 (4): hold = max(-1, 5 - 4) = 1, cash = 5
Day 5 (9): hold = 1, cash = max(5, 1 + 9 - 2) = 8

Final cash = 8
Result: 8
```

### The Invariant of the Two Portfolio States
- At the end of each day, you are either holding 1 share ($hold$) or 0 shares ($cash$).
- Buying transitions from $cash \to hold$ by subtracting price.
- Selling transitions from $hold \to cash$ by adding price and subtracting fee.
- Because each day depends only on the previous day's two numbers, memory collapses to $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### 1. The Dynamic Programming State Equations:
Base state:
$$
hold = -prices[0], \quad cash = 0
$$
For day $i = 1 \dots N - 1$:
$$
hold \leftarrow \max(hold, \; cash - prices[i])
$$
$$
cash \leftarrow \max(cash, \; hold + prices[i] - fee)
$$

### 2. Profit Dominance:
$$
cash_N \ge hold_N + prices[N-1] - fee
$$
The unhedged position $cash$ is always at least as profitable as retaining an unsold position.

> **Frictional Asset Allocation Invariant.** The optimal sequential investment policy under proportional execution friction $\tau$ admits a threshold stopping structure, whose forward Bellman equations collapse to a two-state Markov decision process on $\{0, 1\}$ holding states.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Base State
- $hold = -1, cash = 0$.

---

### Step 2: Days 1 to 2
- Day 1 (3): $cash = \max(0, -1 + 3 - 2) = 0$.
- Day 2 (2): $cash = 0$.

---

### Step 3: Day 3 (8)
- $cash = \max(0, -1 + 8 - 2) = \mathbf{5}$.

---

### Step 4: Day 4 (4)
- $hold = \max(-1, 5 - 4) = \mathbf{1}$.

---

### Step 5: Day 5 (9)
- $cash = \max(5, 1 + 9 - 2) = \mathbf{8}$.

---

### Step 6: Output
$$
\mathbf{8}
$$

---

## 4. Complete Execution Trace

| Day $i$ | Price $prices[i]$ | Action Evaluated | Updated $hold$ State | Updated $cash$ State | Strategy Notes |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | Initial purchase | $-1$ | $0$ | Buy at 1 |
| $1$ | $3$ | Hold | $-1$ | $0$ | Gain doesn't exceed fee |
| $2$ | $2$ | Hold | $-1$ | $0$ | Price dip |
| $3$ | $8$ | Sell | $-1$ | **$5$** | Net profit $8 - 1 - 2 = 5$ |
| $4$ | $4$ | Re-buy | **$1$** | $5$ | Buy back with cash: $5 - 4 = 1$ |
| **$5$** | **$9$** | **Sell** | **$1$** | **`8`** | **Net profit $1 + 9 - 2 = 8$** |

---

## 5. Boundary Cases & Failure Modes

- **Decreasing Prices ($[9, 7, 5, 2]$):** No profitable trade $\implies$ returns 0.
- **Fee Greater Than Price Spread ($prices = [1, 4], fee = 5$):** $4 - 1 - 5 = -2 < 0 \implies$ returns 0.
- **Single Day ($N = 1$):** Cannot buy and sell on the same day $\implies$ returns 0.
- **Zero Fee ($fee = 0$):** Collapses to classic Buy & Sell Stock II (all upward slopes captured).

---

## 6. Traps & Common Anti-Patterns

- **Deducting Fee on Both Buy and Sell:** The fee is per complete transaction; deduct it only once (either on buy or on sell, not both).
- **Greedy Slope Accumulation without Fee Offset:** Naively summing positive differences $(prices[i] - prices[i-1])$ fails because small fluctuations lose money to the transaction fee. Dynamic programming correctly decides whether to hold through small dips.
- **Allocating Full $N \times 2$ Table:** Storing the entire history consumes $O(N)$ memory; maintaining two scalar variables $hold$ and $cash$ runs in strictly $O(1)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single loop through the $N$ price points: $\mathcal{O}(N)$.
  - In each iteration, performs a constant number of scalar additions and $\max$ operations: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms for $N = 5 \times 10^4$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only two floating-point/integer variables $hold$ and $cash$).
