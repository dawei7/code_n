# Best Time to Buy and Sell Stock V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3573 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/) |

## Problem Description

### Goal

An integer array `prices` records one stock's price on consecutive days. Complete at most `k` non-overlapping transactions to maximize total profit. A transaction may be normal—buy on day $i$ and sell on a later day $j$ for `prices[j] - prices[i]`—or a short sale—sell on day $i$ and buy back on a later day $j$ for `prices[i] - prices[j]`.

Every opened transaction must be closed before another begins. The day used to sell or buy back and close a transaction cannot also be used to open the next transaction, so consecutive transactions must use disjoint trading days.

### Function Contract

**Inputs**

- `prices`: An integer array of length $n$, where $2\le n\le10^3$ and $1\le\texttt{prices[i]}\le10^9$.
- `k`: The maximum number of transactions, where $1\le k\le\lfloor n/2\rfloor$.

**Return value**

Return the maximum total profit obtainable from at most `k` completed normal or short-selling transactions.

### Examples

#### Example 1

- **Input:** `prices = [1,7,9,8,2], k = 2`
- **Output:** `14`
- **Explanation:** Buy at `1` and sell at `9` for `8`, then short at `8` and buy back at `2` for `6`.

#### Example 2

- **Input:** `prices = [12,16,19,19,8,1,19,13,9], k = 3`
- **Output:** `36`
- **Explanation:** A normal trade from `12` to `19`, a short sale from `19` to `8`, and a normal trade from `1` to `19` earn `7 + 11 + 18`.

---
