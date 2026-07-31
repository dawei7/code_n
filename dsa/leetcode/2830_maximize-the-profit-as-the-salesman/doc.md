# Maximize the Profit as the Salesman

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2830 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-profit-as-the-salesman/) |

## Problem Description
### Goal

There are `n` houses arranged on a number line and numbered from `0` through `n - 1`. You receive a list `offers`, where each entry `[start, end, gold]` describes a buyer who will purchase every house from `start` through `end`, inclusive, for the stated amount of gold.

You may accept any selection of offers, but two accepted buyers cannot purchase the same house. It is permitted to leave some houses unsold.

Return the maximum total gold obtainable from a valid selection of offers.

### Function Contract
**Inputs**

- `n`: The number of houses, where $1 \le n \le 10^5$; valid house indices are `0` through `n - 1`.
- `offers`: A list of $m$ triples `[start, end, gold]`, where $1 \le m \le 10^5$, $0 \le \texttt{start} \le \texttt{end} < n$, and $1 \le \texttt{gold} \le 10^3$.

**Return value**

Return the greatest sum of gold from offers whose inclusive house intervals are pairwise disjoint.

### Examples
**Example 1**

- Input: `n = 5, offers = [[0, 0, 1], [0, 2, 2], [1, 3, 2]]`
- Output: `3`
- Explanation: Accept `[0, 0, 1]` and `[1, 3, 2]`; their house ranges do not overlap and yield `3` gold.

**Example 2**

- Input: `n = 5, offers = [[0, 0, 1], [0, 2, 10], [1, 3, 2]]`
- Output: `10`
- Explanation: Taking the single offer covering houses `0` through `2` earns more than any compatible alternative.
