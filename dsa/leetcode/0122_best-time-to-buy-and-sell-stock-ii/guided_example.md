# Guided Example: Best Time to Buy and Sell Stock II

We trace the step-by-step greedy peak-valley accumulation and two-state DP state machine on representative multi-transaction stock price series:

- **Input:** $\text{prices} = [7, 1, 5, 3, 6, 4]$
- **Required output:** $7$ (Transactions: $5 - 1 = 4$ and $6 - 3 = 3 \implies 4 + 3 = 7$)
- **Monotonically Ascending Base:** $\text{prices} = [1, 2, 3, 4, 5] \implies 4$ ($5 - 1 = 4$)

This instance demonstrates decomposing multi-day holding periods into independent single-day positive slope segments ($\sum \max(0, P[i] - P[i-1])$), proves why greedy slope harvesting matches global multi-transaction optimality, and contrasts the greedy summation against a formal two-state DP state machine (`hold` vs `cash`) in $O(N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

You are given an array of stock prices:
$$
\text{prices} = [7, 1, 5, 3, 6, 4]
$$
You may complete as many transactions as you like (i.e. buy one and sell one share of the stock multiple times). You can only hold at most one share at any time.

Visualizing the price trajectory:
- Day 0 to 1: Drop $7 \to 1$ ($\Delta = -6$, avoid)
- Day 1 to 2: Rise $1 \to 5$ ($\Delta = +4$, harvest)
- Day 2 to 3: Drop $5 \to 3$ ($\Delta = -2$, avoid)
- Day 3 to 4: Rise $3 \to 6$ ($\Delta = +3$, harvest)
- Day 4 to 5: Drop $6 \to 4$ ($\Delta = -2$, avoid)
Total accumulated profit: $4 + 3 = 7$.

Many learners believe multi-transaction problems require finding valleys and peaks via complex lookahead or graph search.
However, because buying on day $A$ and selling on day $C$ across day $B$ satisfies:
$$
(P_C - P_A) = (P_C - P_B) + (P_B - P_A)
$$
holding across any multi-day upward trend is mathematically identical to buying and selling on every consecutive day where $P_{i} > P_{i-1}$.
Thus, greedily harvesting every positive adjacent delta $\max(0, P[i] - P[i-1])$ guarantees global optimality.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Greedy Slope Accumulation
For each day $i$ from $1$ to $N - 1$:
If the price increased relative to yesterday ($P[i] > P[i-1]$), capture the gain:
$$
\text{profit} \leftarrow \text{profit} + (P[i] - P[i - 1])
$$
If the price decreased or remained unchanged ($P[i] \le P[i-1]$), add $0$.

### Method 2: Two-State DP State Machine
Let:
- $\text{cash}$: the maximum profit on the current day when holding $0$ shares.
- $\text{hold}$: the maximum profit on the current day when holding $1$ share.

For each price $P$:
1. **Transition to Hold (Buy or Retain):**
   $$
   \text{hold}' = \max(\text{hold}, \, \text{cash} - P)
   $$
2. **Transition to Cash (Sell or Retain):**
   $$
   \text{cash}' = \max(\text{cash}, \, \text{hold} + P)
   $$

Both methods yield identical outputs. Method 1 computes the sum in a single streamlined pass.

> **Invariant.** After processing day $i$, the greedy accumulator equals the sum of all strictly positive slopes in the price sequence up to day $i$, which is mathematically the maximum profit attainable under infinite allowable transactions.

---

## 3. Step-by-Step Worked Execution

We trace Greedy Slope Accumulation on $\text{prices} = [7, 1, 5, 3, 6, 4]$ ($N = 6$):

### Initialization
- $\text{total\_profit} = 0$.

---

### Step 1: Day 0 to Day 1 ($7 \to 1$)
- Difference: $P[1] - P[0] = 1 - 7 = -6$.
- Difference is negative $\implies$ skip (do not hold stock during downslide).
- $\text{total\_profit} = 0$.

---

### Step 2: Day 1 to Day 2 ($1 \to 5$)
- Difference: $P[2] - P[1] = 5 - 1 = +4$.
- Positive slope!
- Update: $\text{total\_profit} \leftarrow 0 + 4 = 4$.

---

### Step 3: Day 2 to Day 3 ($5 \to 3$)
- Difference: $P[3] - P[2] = 3 - 5 = -2$.
- Difference is negative $\implies$ skip.
- $\text{total\_profit} = 4$.

---

### Step 4: Day 3 to Day 4 ($3 \to 6$)
- Difference: $P[4] - P[3] = 6 - 3 = +3$.
- Positive slope!
- Update: $\text{total\_profit} \leftarrow 4 + 3 = 7$.

---

### Step 5: Day 4 to Day 5 ($6 \to 4$)
- Difference: $P[5] - P[4] = 4 - 6 = -2$.
- Difference is negative $\implies$ skip.
- $\text{total\_profit} = 7$.

End of price array.
Maximum total profit: $\mathbf{7}$.

---

## 4. Complete Execution Trace

### Daily Slope Evaluation Table

```text
Price:
 7
  \      5             6
   \    / \           / \
    \  /   \         /   \
     1       3      4
Delta:
   [-6] [+4]  [-2]  [+3] [-2]
Take:
    0   +4     0    +3    0  => Total = 7
```

| Day Transition | Yesterday $P[i-1]$ | Today $P[i]$ | Delta $\Delta P$ | Positive? | Profit Increment | Cumulative Profit |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Day $0 \to 1$ | 7 | 1 | $-6$ | No | $0$ | 0 |
| **Day $1 \to 2$** | **1** | **5** | **$+4$** | **Yes** | **$+4$** | **4** |
| Day $2 \to 3$ | 5 | 3 | $-2$ | No | $0$ | 4 |
| **Day $3 \to 4$** | **3** | **6** | **$+3$** | **Yes** | **$+3$** | **7** |
| Day $4 \to 5$ | 6 | 4 | $-2$ | No | $0$ | 7 |
| **Final** | - | - | - | - | - | **7 (Result)** |

### The Same Instance Under the Two-State DP

Method 2 never looks at a slope directly, so replaying the same prices through it
is the check that the greedy decomposition and the state machine agree. Both
transitions read the *previous* day's values; `hold` is started at $-\infty$ so
that day 0's purchase is the only way to enter a holding state:

| Day $i$ | $P[i]$ | `hold` before | `cash` before | New `hold` $= \max(\text{hold},\, \text{cash} - P)$ | New `cash` $= \max(\text{cash},\, \text{hold} + P)$ | Position held after day $i$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 7 | $-\infty$ | 0 | $\max(-\infty, 0 - 7) = -7$ | $\max(0, -\infty + 7) = 0$ | one share bought at $7$ |
| 1 | 1 | $-7$ | 0 | $\max(-7, 0 - 1) = -1$ | $\max(0, -7 + 1) = 0$ | one share bought at $1$, the cheaper entry |
| 2 | 5 | $-1$ | 0 | $\max(-1, 0 - 5) = -1$ | $\max(0, -1 + 5) = 4$ | flat, with the $1 \to 5$ climb banked |
| 3 | 3 | $-1$ | 4 | $\max(-1, 4 - 3) = 1$ | $\max(4, -1 + 3) = 4$ | one share bought at $3$ |
| 4 | 6 | $1$ | 4 | $\max(1, 4 - 6) = 1$ | $\max(4, 1 + 6) = 7$ | flat, with the $3 \to 6$ climb banked |
| 5 | 4 | $1$ | 7 | $\max(1, 7 - 4) = 3$ | $\max(7, 1 + 4) = 7$ | flat at the maximum $7$ |

Two rows carry the whole idea. On day 3 the DP pays $3$ out of the banked $4$ to
hold a share again, which is what turns day 4's price $6$ into the second $+3$
segment. On day 5 the same transition would spend $4$ of the banked $7$ on a
falling price, leaving `hold` $= 3$; the state machine still prefers `cash` $= 7$,
so the final answer is exactly the greedy total.

---

## 5. Algorithmic Correctness

**Soundness.** Let any sequence of transactions buy at $b_1$, sell at $s_1$, buy at $b_2$, sell at $s_2$, etc. Because $s_k - b_k = \sum_{j=b_k}^{s_k-1} (P_{j+1} - P_j)$, the profit of any set of valid transactions is bounded above by the sum of all positive daily changes $\sum_{P_{j+1} > P_j} (P_{j+1} - P_j)$.

**Completeness.** Since an investor can buy on day $j$ and sell on day $j+1$ whenever $P_{j+1} > P_j$, the sum of all positive differences is achievable by executing consecutive 1-day transactions. Thus, the greedy sum is both achievable and an upper bound, proving exact global optimality.

---

## 6. Traps This Instance Exposes

- **Searching for Global Peaks/Valleys:** Attempting to identify macroscopic peaks and valleys with lookahead loops introduces complex boundary edge cases (e.g. plateaus, multiple identical prices, ending on an upswing). Summing adjacent positive differences achieves the identical result with zero edge cases.
- **Thinking Same-Day Buy/Sell Is Disallowed:** If the price strictly rises ($1 \to 2 \to 3$), summing $(2-1) + (3-2) = 2$ represents buying at 1 and selling at 3, or selling at 2 and immediately rebuying at 2. The rules explicitly permit this.

Every shape below is decided by the same rule — add a slope only when it is
strictly positive — so plateaus, drops, and single-day edges need no special
handling. The slope column is the complete list of deltas for that input:

| Scenario | Input | Slopes $\Delta P$ | Required result | Why the accumulator returns it |
|:---|:---|:---|:---:|:---|
| Always rising | $[1, 2, 3, 4, 5]$ | $+1, +1, +1, +1$ | $4$ | All four slopes are harvested, which equals the single holding trade $5 - 1$ |
| Always falling | $[7, 6, 4, 3, 1]$ | $-1, -2, -1, -2$ | $0$ | No slope is positive, so the accumulator never leaves its initial value |
| Two days only | $[2, 5]$ | $+3$ | $3$ | The shortest legal transaction has one slope, and it is positive |
| Separated climbs | $[2, 1, 2, 0, 1, 3]$ | $-1, +1, -2, +1, +2$ | $4$ | Only $+1$ and $+1, +2$ are harvested; the drops contribute nothing but do not block the later climbs |
| Plateau in the middle | $[1, 3, 3, 4]$ | $+2, 0, +1$ | $3$ | A zero slope is not strictly positive, so it adds $0$; the two rises still total $3$ |
| Single day | $[5]$ | none | $0$ | There is no adjacent pair, so the loop body never runs |

Note that the separated-climbs row is the one that rules out a "find the global
valley and global peak" shortcut: the best plan here uses two disjoint climbs and
a temporary dip between them.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of days. The algorithm performs a single pass of $N - 1$ scalar comparisons and additions.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only a single accumulator register.
