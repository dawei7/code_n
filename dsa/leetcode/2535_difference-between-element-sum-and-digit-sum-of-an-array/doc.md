# Difference Between Element Sum and Digit Sum of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2535 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [difference-between-element-sum-and-digit-sum-of-an-array](https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Its element sum is the sum of the integers themselves, while its digit sum is the sum of every decimal digit appearing in those integers; repeated digits count each time they occur. A zero digit is still part of a number, but contributes zero to the digit sum.

Return the absolute difference between these two sums.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers. Its length is at most $2000$, and every value is at most $2000$.

**Return value**

- The nonnegative integer equal to the absolute difference between the element sum and digit sum.

### Examples

#### Example 1

- **Input:** `nums = [1, 15, 6, 3]`
- **Output:** `9`
- **Explanation:** The element sum is $25$, and the digit sum is $16$, so the absolute difference is $9$.

#### Example 2

- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `0`
- **Explanation:** Both sums equal $10$.
