### 1. Description

You are given an array `prices` where $\text{prices}[i]$ is the price of a given stock on the $$i^{\text{th}}$$ day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

### 2. Function Contract

**Inputs**

- `prices`: A nonempty array of daily stock prices.

**Return value**

Return the maximum total profit achievable while respecting the cooldown and single-position rules.

### 3. Note

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### 4. Examples

#### Example 1

- **Input:** $prices = [1,2,3,0,2]$
- **Output:** `3`
- **Explanation:** transactions = [buy, sell, cooldown, buy, sell]
#### Example 2

- **Input:** $prices = [1]$
- **Output:** `0`

### 5. Constraints

- $1 \le \text{prices.length} \le 5000$

- $0 \le \text{prices}[i] \le 1000$