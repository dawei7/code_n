# Find the Minimum Possible Sum of a Beautiful Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2834 |
| Difficulty | Medium |
| Topics | Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/) |

## Problem Description

### Goal

Given positive integers `n` and `target`, form an array `nums` containing exactly `n` pairwise distinct positive integers. The array is beautiful when no two elements at distinct indices add up to `target`. A value may equal half of an even `target`: because all values are distinct, that value cannot occupy two different positions and pair with itself.

Among every array satisfying these conditions, determine the smallest possible sum of its elements. The requested array itself does not need to be returned. Since the mathematical minimum can be very large, return the sum modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The required array length, where $1 \le n \le 10^9$.
- `target`: The forbidden sum, where $1 \le \texttt{target} \le 10^9$.

**Return value**

Return the minimum possible sum of a beautiful array of length `n`, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `n = 2, target = 3`
- **Output:** `4`
- **Explanation:** `[1, 3]` is beautiful and has the minimum sum $4$.

#### Example 2

- **Input:** `n = 3, target = 3`
- **Output:** `8`
- **Explanation:** `[1, 3, 4]` is beautiful and has the minimum sum $8$.

#### Example 3

- **Input:** `n = 1, target = 1`
- **Output:** `1`
- **Explanation:** The one-element array `[1]` is beautiful.
