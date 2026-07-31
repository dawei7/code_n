# Best Time to Buy and Sell Stock using Strategy

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3652 |
| Difficulty | Medium |
| Topics | Array, Sliding Window, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/) |

## Problem Description
### Goal

For each day `i`, `prices[i]` is a stock price and `strategy[i]` is an independent trading coefficient: `-1` buys one unit, `0` holds, and `1` sells one unit. The total profit is

$$
\sum_i \texttt{strategy[i]}\cdot\texttt{prices[i]}.
$$

There are no budget or inventory restrictions, so this sum completely defines the result. You may leave the strategy unchanged or modify one block of exactly `k` consecutive days, where `k` is even. In the chosen block, replace the first `k / 2` actions with `0` and the last `k / 2` actions with `1`.

Return the maximum profit obtainable after at most one such modification.

### Function Contract
**Inputs**

- `prices`: Positive daily prices of length $n$, each at most $10^5$.
- `strategy`: An array of the same length containing only `-1`, `0`, and `1`.
- `k`: An even block length satisfying $2\le k\le n$.

The shared length satisfies $2\le n\le10^5$.

**Return value**

Return the maximum possible sum of action-price products, using zero or one modification.

### Examples
**Example 1**

- Input: `prices = [4,2,8]`, `strategy = [-1,0,1]`, `k = 2`
- Output: `10`
- Explanation: Modifying days 0 and 1 produces `[0,1,1]`, whose profit is `0 + 2 + 8`.

**Example 2**

- Input: `prices = [5,4,3]`, `strategy = [1,1,0]`, `k = 2`
- Output: `9`
- Explanation: Both possible modifications reduce the original profit, so making no modification is optimal.
