# Maximum Linear Stock Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2898 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-linear-stock-score/) |

## Problem Description

### Goal

You are given a 1-indexed integer array `prices`, where `prices[i]` is a stock's price on day $i$. Select a nonempty subsequence of day indices in increasing order.

The selection is *linear* when every pair of consecutive selected days has the same change in price as the elapsed number of days. For selected indices `indexes[1], indexes[2], ..., indexes[k]`, this requires

$$
\texttt{prices[indexes[j]]}-\texttt{prices[indexes[j-1]]}
=\texttt{indexes[j]}-\texttt{indexes[j-1]}
$$

for every $1<j\le k$.

The score is the sum of the prices at all selected indices. Return the maximum score of any linear selection.

### Function Contract

**Inputs**

- `prices`: A nonempty array of positive daily stock prices.

The shared bounds are $1\le n\le 10^5$ and $1\le\texttt{prices[i]}\le 10^9$, where $n=\lvert\texttt{prices}\rvert$.

**Return value**

Return the greatest sum of prices obtainable from a nonempty linear subsequence of indices.

### Examples

#### Example 1

- **Input:** `prices = [1, 5, 3, 7, 8]`
- **Output:** `20`
- **Explanation:** Selecting days $2$, $4$, and $5$ gives price changes $2$ and $1$, matching the corresponding day gaps. The score is $5+7+8=20$.

#### Example 2

- **Input:** `prices = [5, 6, 7, 8, 9]`
- **Output:** `35`
- **Explanation:** Every consecutive price rises by one as the day index rises by one, so all five days form a linear selection.
