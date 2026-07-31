# Maximum Coins From K Consecutive Bags

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3413 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/) |

## Problem Description

### Goal

Imagine an infinite number line with one bag at every integer coordinate. The input `coins` contains non-overlapping segments `[l_i, r_i, c_i]`. Every bag at a coordinate from $l_i$ through $r_i$, inclusive, contains exactly $c_i$ coins; bags outside all segments contain none.

Choose any $k$ consecutive bags and collect all their coins. Return the greatest total obtainable over every possible placement of that length-$k$ interval.

### Function Contract

**Inputs**

- `coins`: The non-overlapping inclusive segments `[left, right, coins_per_bag]`.
- `k`: The positive number of consecutive bags to collect.

Let $n=\lvert\texttt{coins}\rvert$. The constraints are $1\le n\le10^5$, $1\le k\le10^9$, $1\le l_i\le r_i\le10^9$, and $1\le c_i\le1000$.

**Return value**

- The maximum coins contained in any inclusive integer interval of length $k$.

### Examples

**Example 1**

- Input: `coins = [[8, 10, 1], [1, 3, 2], [5, 6, 4]], k = 4`
- Output: `10`

Positions 3 through 6 contain `2 + 0 + 4 + 4 = 10` coins.

**Example 2**

- Input: `coins = [[1, 10, 3]], k = 2`
- Output: `6`

Any two positions inside the segment contain `3 + 3 = 6` coins.
