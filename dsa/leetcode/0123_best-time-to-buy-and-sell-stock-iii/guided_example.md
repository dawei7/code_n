# Guided Example: Best Time to Buy and Sell Stock III

We trace the step-by-step 4-state dynamic programming state machine and bidirectional prefix-suffix partition on representative price series with an at-most-two-transaction constraint:

- **Input:** $\text{prices} = [3, 3, 5, 0, 0, 3, 1, 4]$
- **Required output:** $6$ (Transactions: $3 - 0 = 3$ and $4 - 1 = 3 \implies 3 + 3 = 6$)
- **Single-Transaction Optimal:** $\text{prices} = [1, 2, 3, 4, 5] \implies 4$ (At most two allows choosing one single transaction)

This instance demonstrates modeling the $K=2$ transaction limit as an ordered 4-state Markov-like state machine (`buy1`, `sell1`, `buy2`, `sell2`), establishing dependency chaining without overlap, contrasting against bidirectional prefix-suffix scanning, and compressing auxiliary memory to strictly $O(1)$ space.

---

## 1. Instance & Teaching Goal

You are given an array of stock prices:
$$
\text{prices} = [3, 3, 5, 0, 0, 3, 1, 4]
$$
Find the maximum profit you can achieve with **at most two transactions**. You cannot hold multiple shares simultaneously (you must sell before buying again).

Consider potential transaction plans:
1. One big transaction: Buy at $0$ (day 3), sell at $4$ (day 7) $\implies 4 - 0 = \$4$.
2. Two non-optimal transactions: Buy at $3$, sell at $5$ ($\$2$); buy at $0$, sell at $3$ ($\$3$) $\implies 2 + 3 = \$5$.
3. Two optimal transactions:
   - First trade: Buy at $0$ (day 4), sell at $3$ (day 5) $\implies 3 - 0 = \$3$.
   - Second trade: Buy at $1$ (day 6), sell at $4$ (day 7) $\implies 4 - 1 = \$3$.
   - Combined profit: $3 + 3 = \$6$.

A brute-force search over all pairs of non-overlapping intervals takes $O(N^2)$ time.
We analyze two linear $O(N)$ solutions:
- **Prefix-Suffix Bisection ($O(N)$ Space):** Compute the best 1-trade profit on prefix $0 \dots i$ and suffix $i \dots N-1$, then maximize their sum.
- **4-State DP Machine ($O(1)$ Space):** Track effective balances across the 4 transaction milestones as prices stream in.

---

## 2. Conceptual Foundation & Invariants

### The 4-State Machine DP Protocol
At any point in time, an investor must be in one of four distinct states:
1. $\text{buy1}$: Max balance after buying the first share (spending $P$).
2. $\text{sell1}$: Max balance after selling the first share (earning $P$).
3. $\text{buy2}$: Max balance after buying the second share (reinvesting profit from $\text{sell1}$ minus $P$).
4. $\text{sell2}$: Max balance after selling the second share (earning $P$).

#### Initialization:
- $\text{buy1} = -\infty$ (cannot hold stock without buying)
- $\text{sell1} = 0$ (starting with zero trades)
- $\text{buy2} = -\infty$
- $\text{sell2} = 0$

#### Daily State Transitions for Price $P$:
1. $\text{buy1} \leftarrow \max(\text{buy1}, \, -P)$
2. $\text{sell1} \leftarrow \max(\text{sell1}, \, \text{buy1} + P)$
3. $\text{buy2} \leftarrow \max(\text{buy2}, \, \text{sell1} - P)$
4. $\text{sell2} \leftarrow \max(\text{sell2}, \, \text{buy2} + P)$

Notice that updating in this order allows a stock to be bought and sold on the same day if optimal, which gracefully covers cases where $0$ or $1$ transaction is better than $2$.

> **Invariant.** After processing day $i$, $\text{sell2}$ represents the absolute maximum net profit achievable using at most two legal non-overlapping transactions within the prefix $\text{prices}[0 \dots i]$.

---

## 3. Step-by-Step Worked Execution

We trace the 4-state registers on $\text{prices} = [3, 3, 5, 0, 0, 3, 1, 4]$:

### Day 0: Price $= 3$
- $\text{buy1} = \max(-\infty, -3) = -3$
- $\text{sell1} = \max(0, -3 + 3) = 0$
- $\text{buy2} = \max(-\infty, 0 - 3) = -3$
- $\text{sell2} = \max(0, -3 + 3) = 0$

---

### Day 1: Price $= 3$
- Values unchanged: $\text{buy1} = -3, \text{sell1} = 0, \text{buy2} = -3, \text{sell2} = 0$.

---

### Day 2: Price $= 5$
- $\text{buy1} = \max(-3, -5) = -3$
- $\text{sell1} = \max(0, -3 + 5) = \mathbf{2}$ (First trade profit: $5 - 3 = 2$)
- $\text{buy2} = \max(-3, 2 - 5) = \max(-3, -3) = -3$
- $\text{sell2} = \max(0, -3 + 5) = \mathbf{2}$

---

### Day 3: Price $= 0$
- $\text{buy1} = \max(-3, -0) = \mathbf{0}$ (Better buy price for 1st trade: $\$0$)
- $\text{sell1} = \max(2, 0 + 0) = 2$
- $\text{buy2} = \max(-3, 2 - 0) = \mathbf{2}$ (Reinvesting $\$2$ profit at price $\$0$)
- $\text{sell2} = \max(2, 2 + 0) = 2$

---

### Day 4: Price $= 0$
- Values unchanged: $\text{buy1} = 0, \text{sell1} = 2, \text{buy2} = 2, \text{sell2} = 2$.

---

### Day 5: Price $= 3$
- $\text{buy1} = \max(0, -3) = 0$
- $\text{sell1} = \max(2, 0 + 3) = \mathbf{3}$ (Buy at 0, sell at 3)
- $\text{buy2} = \max(2, 3 - 3) = 2$
- $\text{sell2} = \max(2, 2 + 3) = \mathbf{5}$ (Reinvested at 0, sold at 3 $\implies 2 + 3 = 5$)

---

### Day 6: Price $= 1$
- $\text{buy1} = \max(0, -1) = 0$
- $\text{sell1} = \max(3, 0 + 1) = 3$
- $\text{buy2} = \max(2, 3 - 1) = \mathbf{2}$ (Buy second share at 1 using trade 1's \$3 profit: balance $3 - 1 = 2$)
- $\text{sell2} = \max(5, 2 + 1) = 5$

---

### Day 7: Price $= 4$
- $\text{buy1} = \max(0, -4) = 0$
- $\text{sell1} = \max(3, 0 + 4) = 4$
- $\text{buy2} = \max(2, 4 - 4) = 2$
- $\text{sell2} = \max(5, 2 + 4) = \mathbf{6}$ (Selling 2nd share at 4: balance $2 + 4 = 6$)

Final result: $\text{sell2} = \mathbf{6}$.

---

## 4. Complete Execution Trace

### 4-State Register Evolution Table

| Day $i$ | Price $P$ | $\text{buy1} = \max(\text{buy1}, -P)$ | $\text{sell1} = \max(\text{sell1}, \text{buy1}+P)$ | $\text{buy2} = \max(\text{buy2}, \text{sell1}-P)$ | $\text{sell2} = \max(\text{sell2}, \text{buy2}+P)$ | Strategic Insight |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | - | $-\infty$ | 0 | $-\infty$ | 0 | Uncommitted baseline |
| 0 | 3 | -3 | 0 | -3 | 0 | First buy opportunity at 3 |
| 1 | 3 | -3 | 0 | -3 | 0 | Redundant price |
| 2 | 5 | -3 | 2 | -3 | 2 | First peak: \$2 profit |
| 3 | 0 | **0** | 2 | **2** | 2 | Plunge to 0: resets buy basis |
| 4 | 0 | 0 | 2 | 2 | 2 | Stable bottom |
| 5 | 3 | 0 | 3 | 2 | **5** | Second trade sell candidate |
| 6 | 1 | 0 | 3 | 2 | 5 | Dip to 1: optimal 2nd buy point |
| **7** | **4** | **0** | **4** | **2** | **6** | **Sell second share: Max Profit = 6** |

### The Prefix-Suffix Bisection on the Same Prices

The $O(N)$-space alternative named in the introduction never tracks a state
machine; it fixes a split day and solves two independent single-transaction
problems. Because the two trades may not overlap, a split after day $i$ uses the
prefix $0 \dots i$ for the first trade and the suffix $i+1 \dots 7$ for the
second:

| Split after day $i$ | Prefix $0 \dots i$ | Best single trade in the prefix | Suffix $i+1 \dots 7$ | Best single trade in the suffix | Prefix $+$ suffix |
|:---:|:---|:---:|:---|:---:|:---:|
| 0 | `[3]` | $0$ | `[3, 5, 0, 0, 3, 1, 4]` | $4$ | $4$ |
| 1 | `[3, 3]` | $0$ | `[5, 0, 0, 3, 1, 4]` | $4$ | $4$ |
| 2 | `[3, 3, 5]` | $2$ | `[0, 0, 3, 1, 4]` | $4$ | $\mathbf{6}$ |
| 3 | `[3, 3, 5, 0]` | $2$ | `[0, 3, 1, 4]` | $4$ | $\mathbf{6}$ |
| 4 | `[3, 3, 5, 0, 0]` | $2$ | `[3, 1, 4]` | $3$ | $5$ |
| 5 | `[3, 3, 5, 0, 0, 3]` | $3$ | `[1, 4]` | $3$ | $\mathbf{6}$ |
| 6 | `[3, 3, 5, 0, 0, 3, 1]` | $3$ | `[4]` | $0$ | $3$ |
| no split | whole array, one trade | $4$ | empty | $0$ | $4$ |

Three different splits reach $6$, and they are genuinely different plans. Split
$2$ pairs $3 \to 5$ with $0 \to 4$; split $3$ pairs the same first trade with
$0 \to 4$ starting a day later; and split $5$ pairs $0 \to 3$ with $1 \to 4$,
which is the plan the 4-state registers settle on. The state machine therefore
achieves the bisection's optimum of $6$ while never materialising either prefix
or suffix array, which is why its auxiliary space is $O(1)$.

---

## 5. Algorithmic Correctness

**Soundness.** Every transaction sequence of length $\le 2$ must execute an initial purchase, an initial sale, an optional second purchase, and an optional second sale. Because $\text{buy2}$ subtracts $P$ directly from $\text{sell1}$, it strictly preserves the net profit generated by the first completed trade.

**Completeness.** By evaluating transitions at each day, the recurrence considers all points in time where the first trade could close and the second trade could open. If doing only 1 transaction is optimal, $\text{buy2}$ and $\text{sell2}$ mirror $\text{buy1}$ and $\text{sell1}$ (zero-profit dummy second trade), naturally returning the 1-trade optimum.

---

## 6. Traps This Instance Exposes

- **Overlapping Transactions:** The problem prohibits holding two shares concurrently. In the state machine, $\text{buy2}$ can only consume capital from $\text{sell1}$, guaranteeing that trade 1 has completed before trade 2 commences.
- **Order of Variable Updates:** Updating `buy1`, `sell1`, `buy2`, `sell2` sequentially using the newly computed values within the same iteration allows buying and selling on the exact same day without causing illegal temporal inversions.
- **Forgetting 1-Trade or 0-Trade Cases:** If prices strictly drop ($[5, 4, 3, 2, 1]$), all selling states remain $0$, correctly returning $0$.

The remaining boundaries are decided by the same four registers; the interesting
column is the best split, because it shows whether the second transaction is worth
opening at all:

| Scenario | Input | Best single trade | Best split value | Required result | Why |
|:---|:---|:---:|:---:|:---:|:---|
| Single day | $[3]$ | $0$ | none exists | $0$ | No later day can follow a purchase, so `sell1` and `sell2` stay at their initial $0$ |
| Identical prices | $[3, 3]$ | $0$ | $0$ | $0$ | Every transition nets $0$, which never improves on the initialised values |
| Strictly falling | $[7, 6, 4, 3, 1]$ | $0$ | $0$ | $0$ | Each price is lower than the last, so no purchase is ever followed by a gain |
| Strictly rising | $[1, 2, 3, 4, 5]$ | $4$ | $3$ twice (splits after days 1 and 2) | $4$ | Splitting the climb caps the total at $1 + 2 = 3$, so the machine keeps the single $1 \to 5$ trade worth $4$ |
| Two short rises | $[2, 1, 2, 0, 1]$ | $1$ | $2$ (split after day 2) | $2$ | The second rise $0 \to 1$ is only collectable if the first trade closes before it, and the machine allows exactly that |
| Two separated wins | $[2, 4, 1, 7, 5, 3, 6, 4]$ | $6$ | $9$ (splits after days 3, 4, 5) | $9$ | $1 \to 7$ and $3 \to 6$ are disjoint, so both are collected; the second trade is mandatory here |

The strictly-rising row is the trap worth remembering: a machine that always
forces two transactions would report $3$ instead of $4$, which is exactly why
`sell2` is initialised to $0$ and allowed to inherit `sell1`'s value.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of $\text{prices}$. A single forward pass executes 4 constant-time updates per day.
- **Auxiliary Space Complexity:** $O(1)$ extra space, using only 4 scalar variables.
