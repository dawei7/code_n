# Guided Example: Best Time to Buy and Sell Stock

We trace the step-by-step prefix minimum price tracking and single-transaction profit maximization on representative volatile and monotonically declining price series:

- **Volatile Series Instance:** $\text{prices} = [7, 1, 5, 3, 6, 4] \implies 5$ (Buy at $1$, Sell at $6$)
- **Monotonically Declining Trap:** $\text{prices} = [7, 6, 4, 3, 1] \implies 0$ (No positive transaction possible)

This instance demonstrates dynamic prefix minimum tracking ($\text{min\_price} \leftarrow \min(\text{min\_price}, P[i])$), calculating opportunistic single-day gains ($P[i] - \text{min\_price}$), the isomorphism with Kadane's maximum subarray sum on daily differences ($\Delta P_i$), and achieving $O(N)$ time with $O(1)$ space.

---

## 1. Instance & Teaching Goal

You are given an array $\text{prices} = [7, 1, 5, 3, 6, 4]$ representing the price of a given stock on consecutive days:
- Day 0: $\$7$
- Day 1: $\$1$ (Optimal buy day)
- Day 2: $\$5$ (Potential profit: $5 - 1 = \$4$)
- Day 3: $\$3$ (Potential profit: $3 - 1 = \$2$)
- Day 4: $\$6$ (Optimal sell day: $6 - 1 = \$5$)
- Day 5: $\$4$ (Potential profit: $4 - 1 = \$3$)

You may complete at most **one** transaction (buy once, sell once on a strictly later day). The maximum achievable profit is $\$5$.

A naive brute-force approach checks every pair $(i, j)$ with $i < j$, taking $O(N^2)$ time.
However, for any fixed selling day $j$, the optimal day to buy is simply the day in the prefix $0 \le i < j$ with the absolute lowest price.
Maintaining a running prefix minimum allows computing the best profit on each day in $O(1)$ time, scanning the array in a single pass in $O(N)$ time and $O(1)$ memory.

---

## 2. Conceptual Foundation & Invariants

### Running Prefix Minimum Protocol
Maintain two scalar variables:
- $\text{min\_price} = \infty$ (the lowest price observed so far)
- $\text{max\_profit} = 0$ (the maximum profit found so far)

For each price $P$ in $\text{prices}$:
1. **Evaluate Potential Sale:**
   If we sell today at price $P$, our profit would be:
   $$
   \text{profit} = P - \text{min\_price}
   $$
   $$
   \text{max\_profit} \leftarrow \max(\text{max\_profit}, \, \text{profit})
   $$
2. **Update Prefix Minimum:**
   $$
   \text{min\_price} \leftarrow \min(\text{min\_price}, \, P)
   $$

### Kadane's Maximum Subarray Isomorphism
Observe that any price difference between day $j$ and day $i$ is the telescoping sum of consecutive daily changes:
$$
\text{prices}[j] - \text{prices}[i] = \sum_{k=i+1}^j (\text{prices}[k] - \text{prices}[k-1])
$$
Finding the maximum profit is mathematically equivalent to finding the maximum contiguous subarray sum over the array of daily differences $\Delta P = [-6, +4, -2, +3, -2]$.

> **Invariant.** Before inspecting day $k$, $\text{min\_price} = \min_{0 \le i < k} \text{prices}[i]$, and $\text{max\_profit}$ is the exact maximum profit achievable from any valid transaction executed strictly within the prefix $0 \dots k-1$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{prices} = [7, 1, 5, 3, 6, 4]$:

### Initialization
- $\text{min\_price} = \infty$
- $\text{max\_profit} = 0$

---

### Day 0: Price $= 7$
- Potential profit: $7 - \infty < 0 \implies \text{max\_profit} = 0$.
- Update minimum: $\text{min\_price} = \min(\infty, 7) = 7$.

---

### Day 1: Price $= 1$
- Potential profit: $1 - 7 = -6 \le 0 \implies \text{max\_profit} = 0$.
- Update minimum: $\text{min\_price} = \min(7, 1) = 1$.
- New valley established at $\$1$!

---

### Day 2: Price $= 5$
- Potential profit: $5 - \text{min\_price} = 5 - 1 = 4$.
- Update max profit: $\text{max\_profit} = \max(0, 4) = 4$.
- Update minimum: $\text{min\_price} = \min(1, 5) = 1$.

---

### Day 3: Price $= 3$
- Potential profit: $3 - \text{min\_price} = 3 - 1 = 2$.
- Update max profit: $\text{max\_profit} = \max(4, 2) = 4$.
- Update minimum: $\text{min\_price} = \min(1, 3) = 1$.

---

### Day 4: Price $= 6$
- Potential profit: $6 - \text{min\_price} = 6 - 1 = 5$.
- Update max profit: $\text{max\_profit} = \max(4, 5) = \mathbf{5}$.
- Update minimum: $\text{min\_price} = \min(1, 6) = 1$.

---

### Day 5: Price $= 4$
- Potential profit: $4 - \text{min\_price} = 4 - 1 = 3$.
- Update max profit: $\text{max\_profit} = \max(5, 3) = 5$.
- Update minimum: $\text{min\_price} = \min(1, 4) = 1$.

Iteration complete. Final maximum profit: $\mathbf{5}$.

---

## 4. Complete Execution Trace

### State Variable Trace Across All Days

| Day $i$ | Price $P[i]$ | Prior $\text{min\_price}$ | Potential Profit ($P[i] - \text{min\_price}$) | New $\text{max\_profit}$ | Updated $\text{min\_price}$ | Transaction Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 7 | $\infty$ | $-\infty$ | 0 | 7 | First day anchor |
| 1 | 1 | 7 | $-6$ | 0 | **1** | New lowest buy price found |
| 2 | 5 | 1 | $+4$ | 4 | 1 | Profitable sell candidate |
| 3 | 3 | 1 | $+2$ | 4 | 1 | Profit lower than current max |
| **4** | **6** | **1** | **$+5$** | **5** | **1** | **Global Maximum Achieved!** |
| 5 | 4 | 1 | $+3$ | 5 | 1 | Below peak profit |

### Contrast: Monotonically Declining Case ($[7, 6, 4, 3, 1]$)
- Every daily calculation yields $P[i] - \text{min\_price} \le 0$.
- $\text{max\_profit}$ remains at its initialized value of $0$.
- Output: $0$ (No profitable transaction).

---

## 5. Algorithmic Correctness

**Soundness.** For any day $j$, the highest profit achievable by selling on day $j$ is strictly $P[j] - \min_{0 \le i < j} P[i]$. By tracking the minimum price of all preceding days, every day's optimal transaction is evaluated.

**Completeness.** Since the global maximum profit is simply $\max_{j > i} (P[j] - P[i])$, taking the running maximum across all $j \in [1, N-1]$ explores all non-empty transaction pairs without omitting the optimal one.

---

## 6. Traps This Instance Exposes

- **Selling Before Buying (Temporal Arrow of Time):** You cannot simply subtract the global minimum from the global maximum! In `prices = [7, 6, 4, 3, 1]`, global min is $1$ and global max is $7$, but $7$ occurs *before* $1$. The buy day must strictly precede the sell day.
- **Negative Profit Prohibition:** If stock prices strictly decline, the problem specifies returning $0$, not a negative loss. Initializing $\text{max\_profit} = 0$ prevents negative values.
- **Single Element Input:** If length is 1, no trade is possible; returns 0.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of days. The array is traversed once in a single forward pass, with $O(1)$ operations per element.
- **Auxiliary Space Complexity:** $O(1)$ extra space, using only two scalar variables ($\text{min\_price}$ and $\text{max\_profit}$).