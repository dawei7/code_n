# Guided Example: Best Time to Buy and Sell Stock IV

We trace the step-by-step state-compressed dynamic programming recurrence tracking at most $k$ transactions on representative stock price series:

- **Input:** $k = 2, \quad \text{prices} = [3, 2, 6, 5, 0, 3]$
- **Required output:** $7$ (Buy at $2 \to$ sell at $6$ [profit $4$]; buy at $0 \to$ sell at $3$ [profit $3$]; total $4 + 3 = 7$)
- **Base Triangle Instance:** $k = 2, \quad \text{prices} = [2, 4, 1] \implies 2$ (Single trade achieves maximum)
- **Monotonically Decreasing Instance:** $k = 2, \quad \text{prices} = [5, 4, 3, 2, 1] \implies 0$ (Zero trades executed)
- **Large $k$ Shortcut ($k \ge N/2$):** Reduces to greedy infinite transactions $O(N)$.

This instance demonstrates modeling $k$-transaction limits using parallel buy/sell state vectors ($\text{buy}[j]$ and $\text{sell}[j]$ for $1 \le j \le k$), proves why $k \ge \lfloor N/2 \rfloor$ decouples transaction constraints, and operates in $O(N \cdot k)$ time and $O(k)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer $k = 2$ and a daily price array:
$$
\text{prices} = [3, 2, 6, 5, 0, 3]
$$
Find the maximum total profit achievable by executing at most $k = 2$ non-overlapping buy-and-sell transactions.

Evaluating trade pairs:
- If we execute only 1 transaction: buying at $0$ and selling at $6$ is chronologically impossible (day 4 occurs after day 2). The best single trade is buying at $2$ and selling at $6$ (profit $= 4$).
- With $k = 2$ transactions:
  - Transaction 1: Buy on Day 1 at price $2$, sell on Day 2 at price $6$ $\implies$ Profit $= 6 - 2 = 4$.
  - Transaction 2: Buy on Day 4 at price $0$, sell on Day 5 at price $3$ $\implies$ Profit $= 3 - 0 = 3$.
  - Total profit: $4 + 3 = \mathbf{7}$.

To generalize this to arbitrary $k$:
- Each transaction $j \in [1, k]$ transitions through two phases: **Holding Stock** ($\text{buy}[j]$) and **Holding Cash** ($\text{sell}[j]$).
- The funds available to buy the $j$-th stock are funded by the cumulative profits of the $(j-1)$-th completed sale ($\text{sell}[j-1]$).
- This establishes an elegant $O(k)$ DP recurrence per day.

---

## 2. Conceptual Foundation & Invariants

### The $k$-Transaction State Recurrence
For each transaction $j \in \{1, 2, \dots, k\}$:
- $\text{buy}[j]$: the maximum balance after buying the $j$-th stock (currently holding stock).
- $\text{sell}[j]$: the maximum balance after selling the $j$-th stock (currently holding cash).

#### 1. Greedy Shortcut for Large $k$:
If $k \ge \lfloor N / 2 \rfloor$, the transaction limit is non-binding because one can execute at most $\lfloor N / 2 \rfloor$ independent transactions. The problem simplifies to LeetCode 122 (greedy sum of all positive price steps):
$$
\text{profit} = \sum_{i=1}^{N-1} \max(0, \, \text{prices}[i] - \text{prices}[i-1])
$$

#### 2. Base State Initialization:
For $j = 1 \dots k$:
$$
\text{buy}[j] = -\infty, \quad \text{sell}[j] = 0
$$
With $\text{sell}[0] = 0$ (starting capital).

#### 3. Daily State Transitions:
For each day's price $P \in \text{prices}$:
For $j = 1 \dots k$:
$$
\text{buy}[j] = \max(\text{buy}[j], \, \text{sell}[j-1] - P)
$$
$$
\text{sell}[j] = \max(\text{sell}[j], \, \text{buy}[j] + P)
$$

> **Invariant.** At the end of day $i$, $\text{sell}[j]$ represents the global maximum profit achievable using at most $j$ completed buy-sell transactions within the prefix $\text{prices}[0 \dots i]$.

### What Each State Stores and Why Its Maximum Is Safe

The recurrence is short enough to hide its reasoning. Read as a table, each state declares exactly one decision — open a position, close a position, or do nothing — and the maximum keeps whichever choice dominates:

| State | Meaning at the end of day $i$ | Sources it is built from | Transition | Why the maximum preserves the optimum |
|:---|:---|:---|:---|:---|
| $\text{sell}[0]$ | starting capital with no completed trade | nothing | fixed at $0$ | every plan begins with no stock and no accumulated profit |
| $\text{buy}[j]$ | best balance while the $j$-th stock is held | yesterday's $\text{buy}[j]$ and today's $\text{sell}[j-1]$ | $\max(\text{buy}[j], \text{sell}[j-1] - P)$ | paying $P$ out of the proceeds of $j-1$ finished trades is the only legal way to open trade $j$; the retained value means not buying today |
| $\text{sell}[j]$ | best balance with at most $j$ trades completed | yesterday's $\text{sell}[j]$ and today's $\text{buy}[j]$ | $\max(\text{sell}[j], \text{buy}[j] + P)$ | selling today adds $P$ to an open position; the retained value means staying in cash |
| $\text{buy}[j]$ initialized | no stock is held before any trading | - | $-\infty$ | an unreachable state must lose every maximum; initializing it to $0$ would claim the stock was free |
| $\text{sell}[j]$ initialized | no profit has been realized | - | $0$ | doing nothing is always available and yields exactly nothing |

Two details of the table matter for correctness. First, the states are updated in increasing $j$ within one day, so $\text{sell}[j-1]$ already reflects today's sale when $\text{buy}[j]$ is computed — a same-day close-then-reopen, which earns $0$ and therefore never changes a maximum. Second, $\text{buy}[j]$ is read by $\text{sell}[j]$ in the same day, so a buy and a sell at the identical price $P$ is permitted and is worth exactly $0$, again harmless.

---

## 3. Step-by-Step Worked Execution

We trace the state arrays for $k = 2$ across $\text{prices} = [3, 2, 6, 5, 0, 3]$:

### Day 0 ($P = 3$):
- $\text{buy}[1] = \max(-\infty, 0 - 3) = \mathbf{-3}$; $\text{sell}[1] = \max(0, -3 + 3) = \mathbf{0}$.
- $\text{buy}[2] = \max(-\infty, 0 - 3) = \mathbf{-3}$; $\text{sell}[2] = \max(0, -3 + 3) = \mathbf{0}$.

---

### Day 1 ($P = 2$):
- $\text{buy}[1] = \max(-3, 0 - 2) = \mathbf{-2}$ *(Better buying price!)*; $\text{sell}[1] = \max(0, -2 + 2) = 0$.
- $\text{buy}[2] = \max(-3, 0 - 2) = \mathbf{-2}$; $\text{sell}[2] = \max(0, -2 + 2) = 0$.

---

### Day 2 ($P = 6$):
- $j = 1$:
  - $\text{buy}[1] = \max(-2, 0 - 6) = -2$.
  - $\text{sell}[1] = \max(0, -2 + 6) = \mathbf{4}$ *(First transaction locked in at profit 4)*.
- $j = 2$:
  - $\text{buy}[2] = \max(-2, \text{sell}[1] - 6) = \max(-2, 4 - 6) = -2$.
  - $\text{sell}[2] = \max(0, -2 + 6) = \mathbf{4}$.

---

### Day 3 ($P = 5$):
- $j = 1$: $\text{buy}[1] = -2$; $\text{sell}[1] = \max(4, -2 + 5) = 4$.
- $j = 2$:
  - $\text{buy}[2] = \max(-2, \text{sell}[1] - 5) = \max(-2, 4 - 5) = \mathbf{-1}$ *(Uses profit 4 from trade 1 to buy at 5)*.
  - $\text{sell}[2] = \max(4, -1 + 5) = 4$.

---

### Day 4 ($P = 0$):
- $j = 1$:
  - $\text{buy}[1] = \max(-2, 0 - 0) = \mathbf{0}$.
  - $\text{sell}[1] = \max(4, 0 + 0) = 4$.
- $j = 2$:
  - $\text{buy}[2] = \max(-1, \text{sell}[1] - 0) = \max(-1, 4 - 0) = \mathbf{4}$ *(Reinvests profit 4 to buy at price 0!)*.
  - $\text{sell}[2] = \max(4, 4 + 0) = 4$.

---

### Day 5 ($P = 3$):
- $j = 1$: $\text{buy}[1] = 0$; $\text{sell}[1] = \max(4, 0 + 3) = 4$.
- $j = 2$:
  - $\text{buy}[2] = \max(4, 4 - 3) = 4$.
  - $\text{sell}[2] = \max(4, \text{buy}[2] + 3) = \max(4, 4 + 3) = \mathbf{7}$!

Final maximum profit with at most 2 transactions is $\text{sell}[2] = \mathbf{7}$.

---

## 4. Complete Execution Trace

```text
Prices: [ 3,   2,   6,   5,   0,   3 ], k = 2

Day 0 (P=3): buy: [-3, -3], sell: [0, 0]
Day 1 (P=2): buy: [-2, -2], sell: [0, 0]
Day 2 (P=6): buy: [-2, -2], sell: [4, 4]  -> Lock trade 1 (2 -> 6 = 4)
Day 3 (P=5): buy: [-2, -1], sell: [4, 4]
Day 4 (P=0): buy: [ 0,  4], sell: [4, 4]  -> Reinvest trade 1 into price 0 (effective bal = 4)
Day 5 (P=3): buy: [ 0,  4], sell: [4, 7]  -> Sell trade 2 (4 + 3 = 7)

Final Output: 7
```

| Day | Price $P$ | $\text{buy}[1]$ | $\text{sell}[1]$ | $\text{buy}[2]$ | $\text{sell}[2]$ | Dominant Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | - | $-\infty$ | 0 | $-\infty$ | 0 | Base configuration |
| 0 | 3 | -3 | 0 | -3 | 0 | Candidate buy at 3 |
| 1 | 2 | -2 | 0 | -2 | 0 | Lower buy price at 2 |
| 2 | 6 | -2 | **4** | -2 | 4 | Complete trade 1 ($2 \to 6$) |
| 3 | 5 | -2 | 4 | -1 | 4 | Hold cash from trade 1 |
| 4 | 0 | 0 | 4 | **4** | 4 | Buy trade 2 at $0$ with profit $4$ |
| **5** | **3** | **0** | **4** | **4** | **7** | **Sell trade 2 at $3$ $\implies$ Total $7$** |

### Reading the Final States Back into Actual Trades

A DP value is only meaningful once it can be expanded into a concrete plan. On the last day the two cash states encode two different, fully specified schedules, and the gap between them is precisely the value of the second transaction:

| Final state | Value | The schedule it encodes | Why nothing better with that many trades exists |
|:---|:---:|:---|:---|
| $\text{sell}[1]$ | 4 | buy at $2$ on day 1, sell at $6$ on day 2 | the largest single rise anywhere in the series is $6 - 2 = 4$; the runner-up rise, $0 \to 3$, is worth only $3$ |
| $\text{sell}[2]$ | 7 | the same trade, then buy at $0$ on day 4 and sell at $3$ on day 5 | after the first trade the best rise that does not reuse days 1-2 is $3 - 0 = 3$, so $4 + 3$ is the only pairing that reaches $7$ |

The intermediate states explain why the second trade could not start earlier. On day 3 the price is $5$ and $\text{buy}[2]$ rises to $-1$, which is the balance of reinvesting the $4$ already earned against a $5$ purchase; holding that position into day 4 would have been worse than waiting, because the price falls to $0$ and the *same* $4$ then buys the stock outright, giving $\text{buy}[2] = 4$. Only a state that remembers the best balance can express that "wait for the cheaper entry" decision, and the price drop from $5$ to $0$ is exactly the trap a greedy second transaction would fall into.

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition obeys the constraints of the stock market: a stock cannot be sold without first being bought, and the $j$-th purchase is funded by the cumulative proceeds of the $(j-1)$-th sale. Taking the maximum at each step guarantees optimal substructure.

**Completeness.** By maintaining the optimal buy and sell values for all $1 \le j \le k$ simultaneously, the algorithm considers all possible partitionings of transactions across the timeline.

---

## 6. Traps This Instance Exposes

- **Memory Limit on Huge $k$:** When $k \ge 10^9$, allocating an array of size $k$ causes an Out-Of-Memory (OOM) error. Recognizing that $k \ge \lfloor N / 2 \rfloor$ allows unlimited transactions reduces runtime to $O(N)$ with $O(1)$ space.
- **Negative Balance Initialization:** Initializing $\text{buy}[j] = 0$ instead of $-\infty$ falsely assumes buying stock is free. $\text{buy}[j]$ must start at $-\infty$.
- **Same-Day Transitions:** Updating $\text{buy}[j]$ and $\text{sell}[j]$ on the same day allows buying and selling at price $P$ for net profit 0, which correctly leaves the maximum unchanged.

### Boundary Instances and What Each One Settles

The traced instance happens to make the transaction limit bite, which is the interesting case but not the only one. The degenerate and extreme settings each isolate one mechanism:

| Instance | Result | What the instance settles |
|:---|:---:|:---|
| $k = 0$, prices $= [3, 2, 6, 5, 0, 3]$ | 0 | no state above $j = 0$ can ever become reachable, so the answer is the starting capital |
| $k = 1$, prices $= [3, 2, 6, 5, 0, 3]$ | 4 | withholding the second transaction costs exactly $3$ on the same series, so the limit is genuinely binding here |
| $k = 2$, prices $= [1, 2, 3, 4, 5]$ | 4 | one trade from $1$ to $5$ beats any split, since splitting a rising run earns the same total; transactions are permission, not obligation |
| $k = 2$, prices $= [5, 4, 3, 2, 1]$ | 0 | every step is a fall, and the $-\infty$ initialization prevents a fictitious free purchase from creating paper profit |
| $k = 2$, prices $= [3, 3, 3]$ | 0 | a same-price round trip earns exactly $0$, so flat prices never raise the answer |
| $k = 2$, prices $= [1, 2, 1, 2, 1, 2]$ | 2 | with $N = 6$ the limit $k < \lfloor N/2 \rfloor = 3$ binds, and the two available trades capture only two of the three rises |
| $k = 3$, prices $= [1, 2, 1, 2, 1, 2]$ | 3 | at $k = \lfloor N/2 \rfloor$ the limit stops binding, and the answer equals the greedy sum $1 + 1 + 1$ |
| $k = 10$, prices $= [1, 2, 1, 4, 2, 7]$ | 9 | a $k$ far above $\lfloor N/2 \rfloor$ is answered by the greedy sum $1 + 3 + 5$ without allocating any state array of length $k$ |
| prices $= [7]$, any $k$ | 0 | one day admits no buy-then-sell pair, and the loop simply leaves every sell state at $0$ |

The pair $(k = 2, k = 3)$ on $[1, 2, 1, 2, 1, 2]$ is the cleanest demonstration of the shortcut: the array-based method would still need three transaction slots, while the threshold test recognises that the limit can no longer restrict anything and reduces the work to a single linear pass.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - If $k \ge \lfloor N / 2 \rfloor$: $O(N)$ via greedy linear pass.
  - If $k < \lfloor N / 2 \rfloor$: $O(N \cdot k)$ across $N$ days and $k$ transaction states.
- **Auxiliary Space Complexity:** $O(k)$ auxiliary memory for the compressed 1D state vectors `buy` and `sell`.
