# Guided Example: Best Time to Buy and Sell Stock with Cooldown

We trace the step-by-step state machine dynamic programming formulation, holding vs unheld state transitions, mandatory 1-day cooldown leapfrog indexing ($i + 2$), and optimal profit extraction on representative stock price instances:

- **Input:** $\text{prices} = [1, 2, 3, 0, 2]$
- **Required output:** $3$
  - Day 0: Buy at price $1$ ($\text{cash} = -1$)
  - Day 1: Sell at price $2$ ($\text{cash} = -1 + 2 = +1$)
  - Day 2: Mandatory Cooldown (Cannot buy)
  - Day 3: Buy at price $0$ ($\text{cash} = 1 - 0 = +1$)
  - Day 4: Sell at price $2$ ($\text{cash} = 1 + 2 = +3$)
  - Transaction sequence: $[\text{Buy}, \text{Sell}, \text{Cooldown}, \text{Buy}, \text{Sell}]$, total profit $= \mathbf{3}$
- **Alternative Hold to Peak:** Buying on Day 0 ($1$) and selling on Day 2 ($3$) gives profit $2$, which is strictly suboptimal compared to $3$
- **Monotonically Decreasing Prices:** $\text{prices} = [5, 4, 3, 2, 1] \implies 0$ (No transaction yields positive profit)
- **Single Day Horizon:** $\text{prices} = [1] \implies 0$ (Cannot complete a buy-sell cycle)

This instance demonstrates dynamic programming state transitions with temporal delay constraints, contrasts naive exponential decision branching against memoized subproblem evaluation, proves why selling on day $i$ restricts the next buy to day $i + 2$, and executes in $O(N)$ linear time and $O(1)$ auxiliary state machine memory.

---

## 1. Instance & Teaching Goal

Given daily stock prices:
$$
\text{prices} = [1, 2, 3, 0, 2] \quad (N = 5)
$$
Maximize total profit under two constraints:
1. You may not hold multiple shares simultaneously (must sell before buying again).
2. **Cooldown Rule:** After selling on day $i$, you cannot buy on day $i + 1$ (the earliest next buy is day $i + 2$).

```text
Day:        0     1     2     3     4
Price:      1     2     3     0     2
Action:    Buy   Sell Cooldown Buy  Sell
Balance:   -1    +1     +1    +1    +3

Total Profit: 3
```

### The Cooldown Tradeoff
Without cooldown, one could buy on day 0 ($1$), sell on day 2 ($3$), buy on day 3 ($0$), sell on day 4 ($2$) for profit $(3-1) + (2-0) = 4$.
With cooldown:
- Selling on day 2 ($3$) forces cooldown on day 3 ($0$), preventing buying at the absolute dip $0$!
- Selling early on day 1 ($2$) allows cooldown on day 2 ($3$), freeing day 3 to buy at $0$ and sell at $2$, capturing $(2-1) + (2-0) = 3$.
The optimal policy requires strategic sacrifice of intermediate peaks to capture larger future troughs.

---

## 2. Conceptual Foundation & Invariants

### State Machine Formulation
At any day $i$, the agent occupies one of three states:
1. **$\text{hold}[i]$:** Currently holding one share of stock.
   - Either continue holding the stock from yesterday ($\text{hold}[i-1]$),
   - Or buy today, which requires being in the unheld cooldown-cleared state yesterday ($\text{reset}[i-1] - \text{prices}[i]$):
   $$
   \text{hold}[i] = \max(\text{hold}[i-1], \; \text{reset}[i-1] - \text{prices}[i])
   $$
2. **$\text{sold}[i]$:** Just sold the share of stock today. Enters mandatory cooldown tomorrow:
   $$
   \text{sold}[i] = \text{hold}[i-1] + \text{prices}[i]
   $$
3. **$\text{reset}[i]$:** Not holding stock and free to buy today (did not sell yesterday):
   $$
   \text{reset}[i] = \max(\text{reset}[i-1], \; \text{sold}[i-1])
   $$

```text
State Transitions:
     +-----------------(Rest)------------------+
     |                                         |
     v                                         |
+---------+         Buy          +--------+    |
|  reset  | -------------------> |  hold  |    |
+---------+                      +--------+    |
     ^                                |        |
     |           Sell                 |        |
     | -------------------------------+        |
     |                                         |
+---------+                                    |
|  sold   | -----------------------------------+
+---------+              Cooldown (1 day)
```

### Equivalent Memoized DFS Formulation `dfs(i, holding)`:
- `dfs(i, 0)` (Not holding): $\max(\text{skip}: \text{dfs}(i + 1, 0), \; \text{buy}: -\text{prices}[i] + \text{dfs}(i + 1, 1))$.
- `dfs(i, 1)` (Holding): $\max(\text{skip}: \text{dfs}(i + 1, 1), \; \text{sell}: \text{prices}[i] + \mathbf{\text{dfs}(i + 2, 0)})$.
  *(The term $i + 2$ automatically enforces the 1-day cooldown!)*

> **Invariant.** For any day $i$, $\max(\text{sold}[i], \text{reset}[i])$ represents the globally optimal profit achievable over the prefix $[0, i]$ with no active stock holding.

---

## 3. Step-by-Step Worked Execution

We trace the state machine on $\text{prices} = [1, 2, 3, 0, 2]$:
Base conditions at Day 0:
- $\text{hold} = -1$ (Bought at price 1)
- $\text{sold} = -\infty$ (Cannot sell on day 0)
- $\text{reset} = 0$ (Did nothing)

---

### Step 1: Day 1 ($\text{price} = 2$)
- $\text{hold} = \max(-1, \; 0 - 2) = \max(-1, -2) = \mathbf{-1}$.
- $\text{sold} = \text{hold}_{\text{prev}} + 2 = -1 + 2 = \mathbf{+1}$.
- $\text{reset} = \max(0, \; -\infty) = \mathbf{0}$.
- *State:* $\text{hold} = -1, \; \text{sold} = 1, \; \text{reset} = 0$.

---

### Step 2: Day 2 ($\text{price} = 3$)
- $\text{hold} = \max(-1, \; \text{reset}_{\text{prev}} - 3) = \max(-1, \; 0 - 3) = \mathbf{-1}$.
- $\text{sold} = \text{hold}_{\text{prev}} + 3 = -1 + 3 = \mathbf{+2}$.
- $\text{reset} = \max(\text{reset}_{\text{prev}}, \; \text{sold}_{\text{prev}}) = \max(0, 1) = \mathbf{+1}$ *(Cooldown from Day 1 sale completes!)*.
- *State:* $\text{hold} = -1, \; \text{sold} = 2, \; \text{reset} = 1$.

---

### Step 3: Day 3 ($\text{price} = 0$)
- $\text{hold} = \max(-1, \; \text{reset}_{\text{prev}} - 0) = \max(-1, \; 1 - 0) = \mathbf{+1}$ *(Buy at dip price 0 using cash from Day 1 sale!)*.
- $\text{sold} = \text{hold}_{\text{prev}} + 0 = -1 + 0 = \mathbf{-1}$.
- $\text{reset} = \max(\text{reset}_{\text{prev}}, \; \text{sold}_{\text{prev}}) = \max(1, 2) = \mathbf{+2}$.
- *State:* $\text{hold} = 1, \; \text{sold} = -1, \; \text{reset} = 2$.

---

### Step 4: Day 4 ($\text{price} = 2$)
- $\text{hold} = \max(1, \; \text{reset}_{\text{prev}} - 2) = \max(1, \; 2 - 2) = \mathbf{+1}$.
- $\text{sold} = \text{hold}_{\text{prev}} + 2 = 1 + 2 = \mathbf{+3}$ *(Sell stock bought on Day 3 for $+2$ profit!)*.
- $\text{reset} = \max(2, -1) = \mathbf{+2}$.
- *State:* $\text{hold} = 1, \; \text{sold} = 3, \; \text{reset} = 2$.

---

### Step 5: Final Profit Extraction
The optimal terminal profit without unliquidated holdings is:
$$
\text{Max Profit} = \max(\text{sold}, \; \text{reset}) = \max(3, 2) = \mathbf{3}
$$

---

## 4. Complete Execution Trace

```text
prices = [1, 2, 3, 0, 2]

Day 0 (price=1): hold = -1, sold = -inf, reset = 0
Day 1 (price=2): hold = -1, sold = 1,    reset = 0
Day 2 (price=3): hold = -1, sold = 2,    reset = 1
Day 3 (price=0): hold =  1, sold = -1,   reset = 2  <- Buy at 0 enabled by Day 1 sell!
Day 4 (price=2): hold =  1, sold = 3,    reset = 2  <- Sell at 2 -> Profit = 3

Optimal Profit = 3
```

| Day $i$ | Price | Transition Decision | $\text{hold}[i]$ | $\text{sold}[i]$ | $\text{reset}[i]$ | Optimal Cash Balance |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 0 | 1 | Buy at 1 | **-1** | $-\infty$ | 0 | -1 |
| 1 | 2 | Sell at 2 | -1 | **+1** | 0 | +1 |
| 2 | 3 | Cooldown active | -1 | +2 | **+1** | +2 |
| **3** | **0** | **Buy at 0 (from reset 1)** | **+1** | -1 | +2 | +2 |
| **4** | **2** | **Sell at 2 (from hold 1)** | +1 | **+3** | +2 | **+3 (Global Max)** |

---

## 5. Algorithmic Correctness

**Soundness.** The state recurrence partitions all possible trading strategies into mutually exclusive, exhaustive states (`hold`, `sold`, `reset`). The cooldown rule is strictly satisfied because transitions from `sold` must pass through `reset` before entering `hold` on a subsequent day. Because no invalid transaction order can be formed, any accumulated profit is valid.

**Completeness.** By evaluating all feasible transitions (buy, sell, hold, cooldown) at every step and taking the maximum, dynamic programming guarantees that no profitable transaction path is overlooked. The final maximum over non-holding states ($\max(\text{sold}, \text{reset})$) yields the exact global optimum.

---

## 6. Traps This Instance Exposes

- **Selling at Peak vs Selling Early for Dip:** Greedily holding from day 0 to day 2 achieves profit $3 - 1 = 2$. However, selling on day 1 for profit $2 - 1 = 1$ allows buying on day 3 at price $0$, netting total profit $(2-1) + (2-0) = 3$. Local greed fails; global DP is necessary.
- **Ending in `hold` State:** Ending the simulation holding stock represents unrealized cost rather than profit. The final answer must always be taken over unheld states ($\max(\text{sold}, \text{reset})$).
- **Index Bounds in $i + 2$ Recurrence:** When implementing via DFS, jumping to $i + 2$ upon selling can exceed array length $N$. The base case must guard with `if i >= len(prices): return 0`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ linear time, where $N$ is the number of days in `prices`. Each day evaluates three $O(1)$ state transitions.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory when using the three scalar variables (`hold`, `sold`, `reset`). (Or $O(N)$ memory if using memoized DFS recursion).