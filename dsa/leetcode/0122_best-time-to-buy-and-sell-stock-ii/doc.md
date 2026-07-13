# Best Time to Buy and Sell Stock II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 122 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) |

## Problem Description
### Goal
You are given daily prices for one stock in chronological order. You may buy and sell the stock as many times as useful, but you can hold at most one share at a time. Consequently, an existing share must be sold before another purchase can create a new transaction.

Return the maximum total profit across the entire period. Each transaction contributes its later sale price minus its purchase price, and choosing no transaction is valid when no gain is available. The result may combine gains from several separate rising intervals; it is not limited to the profit from one earliest purchase and one latest sale.

### Function Contract
**Inputs**

- `prices`: the stock price for each day in chronological order

**Return value**

The maximum total profit from any valid sequence of non-overlapping transactions.

### Examples
**Example 1**

- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `7`

**Example 2**

- Input: `prices = [1, 2, 3, 4, 5]`
- Output: `4`

**Example 3**

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Every rising edge is independently realizable profit**

Whenever today's price exceeds yesterday's, add that positive difference. It can be realized by holding stock across exactly that edge. A nonpositive edge contributes nothing because selling before the decline and buying afterward is never worse than holding through it.

**Adjacent rising-edge profits telescope into valley-to-peak profit**

For prices $a < b < c$, profit $c-a$ equals $(b-a) + (c-b)$. Therefore collecting daily rises is financially equivalent to one transaction from the valley to the peak. The apparent sell and rebuy on an intermediate day can be merged, so the one-stock-at-a-time rule is respected.

**Processed positive edges form an attainable optimal schedule**

After day `i`, the accumulated sum is the maximum profit achievable using only days through `i` while ending with no stock held.

**Trace climbs separated by declines**

For `[7,1,5,3,6,4]`, collect rises `1 -> 5` for `4` and `3 -> 6` for `3`. Declines separate the transactions, producing total `7`.

**Transaction profit decomposes into positive daily rises**

For a buy at day `a` and sale at day `b`, the profit telescopes into the sum of adjacent changes from `a` through `b`. Negative changes can be avoided by closing before the decline and reopening afterward, so an optimal schedule never needs to include them.

Every positive adjacent change can be realized as its own transaction, and consecutive rises may be merged into one transaction with the same total. Summing all positive changes is therefore attainable and at least as large as any legal schedule's decomposed profit.

#### Complexity detail

The algorithm examines each adjacent pair once, giving $O(n)$ time. The running profit is the only state, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Dynamic programming with hold/cash states:** is correct but unnecessary for the unlimited, fee-free contract.
- **Enumerate transaction schedules:** is exponential.
- **Keep only the single best rise:** solves Problem 121 and misses separated opportunities.
- Constant and decreasing prices yield zero. Same-day sell-and-buy boundaries between adjacent rises can be merged without changing profit.
- Transaction fees, cooldowns, or limits invalidate this simple edge decomposition and require additional state.

</details>
