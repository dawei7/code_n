# Maximum Profit From Trading Stocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2291 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-profit-from-trading-stocks/) |

## Problem Description
### Goal
Two 0-indexed arrays, `present` and `future`, describe the same collection of
stocks. For stock $i$, `present[i]` is its price now and `future[i]` is its
price one year from now. A stock may be bought at most once, and every purchase
must be paid for from the fixed amount `budget` available today.

Choose which stocks to buy without spending more than the budget. After one
year, sell every chosen stock and return the maximum possible total profit,
where a chosen stock contributes `future[i] - present[i]`. Buying nothing is
allowed, so the result is never negative.

### Function Contract
**Inputs**

- `present`: Current prices for $n$ stocks.
- `future`: Prices for those same $n$ stocks one year later.
- `budget`: The maximum total current price that may be spent.

The arrays have equal length, $1 \le n \le 1000$; every price is between $0$
and $100$ inclusive; and $0 \le \texttt{budget} \le 1000$.

**Return value**

The greatest total future sale value minus total purchase cost among all
subsets whose purchase cost is at most `budget`.

### Examples
**Example 1**

- Input: `present = [5, 4, 6, 2, 3], future = [8, 5, 4, 3, 5], budget = 10`
- Output: `6`

**Example 2**

- Input: `present = [2, 2, 5], future = [3, 4, 10], budget = 6`
- Output: `5`

**Example 3**

- Input: `present = [3, 3, 12], future = [0, 3, 15], budget = 10`
- Output: `0`
