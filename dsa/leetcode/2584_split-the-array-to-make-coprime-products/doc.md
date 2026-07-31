# Split the Array to Make Coprime Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2584 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Split the Array to Make Coprime Products](https://leetcode.com/problems/split-the-array-to-make-coprime-products/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums` of length $n$, consider splitting it after an index $i$ where $0 \leq i \leq n-2$. The left side then contains `nums[0]` through `nums[i]`, and the right side contains all remaining elements.

A split is valid when the product of the left side and the product of the right side are coprime: their greatest common divisor is $1$. Both sides must be non-empty, so the final index can never be a split position.

Return the smallest index that produces a valid split. Return `-1` when no valid position exists.

### Function Contract

**Inputs**

- `nums`: The positive integers whose contiguous prefix and suffix products are compared.

Let $n = \lvert\texttt{nums}\rvert$ and $M = \max(\texttt{nums})$. The constraints are $1 \leq n \leq 10^4$ and $1 \leq M \leq 10^6$.

**Return value**

- The smallest valid split index in $[0,n-2]$, or `-1` if no such index exists.

### Examples

**Example 1**

- Input: `nums = [4,7,8,15,3,5]`
- Output: `2`
- Explanation: The two products are $224$ and $225$, whose greatest common divisor is $1$.

**Example 2**

- Input: `nums = [4,7,15,8,3,5]`
- Output: `-1`
- Explanation: Every possible prefix product shares a prime factor with its corresponding suffix product.
