# Maximum Profitable Triplets With Increasing Prices II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2921 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/) |

## Problem Description

### Goal

Two 0-indexed arrays, `prices` and `profits`, describe $n$ store items.
Item $i$ has price `prices[i]` and contributes `profits[i]` when selected.
Choose exactly three indices $i<j<k$ whose prices are also strictly increasing:
$\texttt{prices[i]}<\texttt{prices[j]}<\texttt{prices[k]}$.

The selected triplet earns
`profits[i] + profits[j] + profits[k]`. Return the greatest profit obtainable
from any triplet satisfying both the index and price orders. If no such three
items exist, return `-1`.

### Function Contract

**Inputs**

- `prices`: The price of each item in store order.
- `profits`: The positive profit associated with each corresponding item.

Let $n=\lvert\texttt{prices}\rvert=\lvert\texttt{profits}\rvert$ and
$P=\max_i\texttt{prices[i]}$. The constraints are $3\le n\le50{,}000$,
$1\le\texttt{prices[i]}\le5000$, and
$1\le\texttt{profits[i]}\le10^6$.

**Return value**

- The maximum profit of a valid increasing-price triplet, or `-1` when none
  exists.

### Examples

**Example 1**

- Input: `prices = [10, 2, 3, 4], profits = [100, 2, 7, 10]`
- Output: `19`
- Explanation: The profitable item at index 0 cannot begin a valid triplet.
  Indices 1, 2, and 3 have prices `2 < 3 < 4` and earn `2 + 7 + 10`.

**Example 2**

- Input: `prices = [1, 2, 3, 4, 5], profits = [1, 5, 3, 4, 6]`
- Output: `15`
- Explanation: Prices already increase with indices, so selecting the items
  at indices 1, 3, and 4 earns the three compatible profits `5 + 4 + 6`.

**Example 3**

- Input: `prices = [4, 3, 2, 1], profits = [33, 20, 19, 87]`
- Output: `-1`
- Explanation: No three indices have strictly increasing prices.
