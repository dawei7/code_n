### 1. Description

You are given an array `prices` where $\text{prices}[i]$ is the price of a given stock on the $i^{\text{th}}$ day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

### 2. Function Contract

**Inputs**

- `prices`: The stock prices in chronological order.

**Return value**

Return the maximum profit obtainable with zero, one, or two non-overlapping transactions.

### 3. Note

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### 4. Examples

#### Example 1

- **Input:** $prices = [3,3,5,0,0,3,1,4]$
- **Output:** `6`
- **Explanation:** Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

#### Example 2

- **Input:** $prices = [1,2,3,4,5]$
- **Output:** `4`
- **Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

#### Example 3

- **Input:** $prices = [7,6,4,3,1]$
- **Output:** `0`
- **Explanation:** In this case, no transaction is done, i.e. max profit = 0.

### 5. Constraints

- $1 \le \text{prices.length} \le 10^{5}$

- $0 \le \text{prices}[i] \le 10^{5}$
