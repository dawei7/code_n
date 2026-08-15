# Number of Smooth Descent Periods of a Stock

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2110 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Two Pointers, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [number-of-smooth-descent-periods-of-a-stock](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/) |

## Problem Description

### Goal

You are given an integer array `prices`, where `prices[i]` is a stock's price on day $i$. A smooth descent period is one or more contiguous days. After its first day, every price in the period must be lower than the immediately preceding price by exactly $1$.

Count every contiguous period satisfying that rule and return the total. The first day of a period has no preceding-day requirement, so each individual day is itself a valid one-day smooth descent period. Equal prices, larger drops, and price increases break any longer period crossing that boundary.

### Function Contract

**Inputs**

- `prices`: An integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{prices[i]} \le 10^5$.

**Return value**

Return the number of contiguous smooth descent periods in `prices`.

### Examples

#### Example 1

- **Input:** `prices = [3, 2, 1, 4]`
- **Output:** `7`
- **Explanation:** The four one-day periods, `[3, 2]`, `[2, 1]`, and `[3, 2, 1]` are valid.

#### Example 2

- **Input:** `prices = [8, 6, 7, 7]`
- **Output:** `4`
- **Explanation:** Only the four one-day periods qualify; the drop from $8$ to $6$ is not exactly $1$.

#### Example 3

- **Input:** `prices = [1]`
- **Output:** `1`
