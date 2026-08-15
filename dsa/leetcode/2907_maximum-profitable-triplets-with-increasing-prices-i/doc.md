# Maximum Profitable Triplets With Increasing Prices I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2907 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/) |

## Problem Description

### Goal

A store has $n$ items. Two 0-indexed arrays describe them: item $i$ has price `prices[i]` and yields profit `profits[i]`.

Choose exactly three items at indices $i<j<k$. Their prices must also be strictly increasing, so `prices[i] < prices[j] < prices[k]`. The value of a valid choice is `profits[i] + profits[j] + profits[k]`. Return the largest value obtainable from any valid triplet, or return `-1` when no three items meet both the index and price conditions.

### Function Contract

**Inputs**

- `prices`: An integer array of length $n$, where $3\le n\le 2000$ and $1\le\texttt{prices}[i]\le 10^6$.
- `profits`: An integer array of the same length, where $1\le\texttt{profits}[i]\le 10^6$.

The two arrays describe the same items by index.

**Return value**

Return the maximum total profit of a triplet whose indices and prices are both strictly increasing. Return `-1` if no such triplet exists.

### Examples

#### Example 1

- **Input:** `prices = [10, 2, 3, 4], profits = [100, 2, 7, 10]`
- **Output:** `19`
- **Explanation:** Index zero cannot start a valid triplet. Indices `[1, 2, 3]` have increasing prices and profit $2+7+10=19$.

#### Example 2

- **Input:** `prices = [1, 2, 3, 4, 5], profits = [1, 5, 3, 4, 6]`
- **Output:** `15`
- **Explanation:** Indices `[1, 3, 4]` give the largest valid profit, $5+4+6=15$.

#### Example 3

- **Input:** `prices = [4, 3, 2, 1], profits = [33, 20, 19, 87]`
- **Output:** `-1`
- **Explanation:** No three indices have strictly increasing prices.
