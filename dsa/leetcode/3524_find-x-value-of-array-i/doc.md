# Find X Value of Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3524 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-x-value-of-array-i/) |

## Problem Description

### Goal

You are given an array of positive integers `nums` and a positive integer `k`. Perform one operation by removing a prefix and a suffix whose positions do not overlap, while leaving at least one array element. Either removed part may be empty, so every possible remaining array is a non-empty contiguous subarray of `nums`.

For each remainder $x$ with $0 \le x < k$, the x-value is the number of permitted operations for which the product of all remaining elements has remainder $x$ when divided by $k$. Return an array `result` of length $k$ in which `result[x]` is that count.

### Function Contract

**Inputs**

- `nums`: An array of positive integers.
- `k`: The positive modulus used to classify products.

The constraints are $1 \le \lvert\texttt{nums}\rvert \le 10^5$, $1 \le \texttt{nums[i]} \le 10^9$, and $1 \le k \le 5$.

**Return value**

- An integer array of length $k$ containing the number of non-empty contiguous subarrays for each product remainder.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 5], k = 3`
- Output: `[9, 2, 4]`

**Example 2**

- Input: `nums = [1, 2, 4, 8, 16, 32], k = 4`
- Output: `[18, 1, 2, 0]`

**Example 3**

- Input: `nums = [1, 1, 2, 1, 1], k = 2`
- Output: `[9, 6]`
