### 1. Description

You are given an integer array `prices` where $\text{prices}[i]$ is the price of a given stock on the $i^{\text{th}}$ day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times.

### 2. Function Contract

**Inputs**

- `k`: The maximum number of completed transactions.
- `prices`: The stock price for each successive day.

**Return value**

Return the greatest total profit achievable under the transaction limit.

### 3. Note

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### 4. Examples

#### Example 1

- **Input:** $k = 2, prices = [2,4,1]$
- **Output:** `2`
- **Explanation:** Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

#### Example 2

- **Input:** $k = 2, prices = [3,2,6,5,0,3]$
- **Output:** `7`
- **Explanation:** Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

### 5. Constraints

- $1 \le k \le 100$

- $1 \le \text{prices.length} \le 1000$

- $0 \le \text{prices}[i] \le 1000$
