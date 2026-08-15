# Maximum Subarray With Equal Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3411 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Sliding Window, Enumeration, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Call an array `arr` product equivalent when the product of all its elements equals the product of their greatest common divisor and least common multiple:

$$
\prod_{x\in\texttt{arr}}x
=
\gcd(\texttt{arr})\cdot\operatorname{lcm}(\texttt{arr}).
$$

Return the length of the longest contiguous subarray of `nums` that is product equivalent.

### Function Contract

**Inputs**

- `nums`: The positive integer array to search.

The constraints are $2\le\lvert\texttt{nums}\rvert\le100$ and $1\le\texttt{nums[i]}\le10$.

**Return value**

- The maximum length of a product-equivalent contiguous subarray.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 1, 2, 1, 1, 1]`
- **Output:** `5`

The subarray `[1, 2, 1, 1, 1]` has product 2, GCD 1, and LCM 2.

#### Example 2

- **Input:** `nums = [2, 3, 4, 5, 6]`
- **Output:** `3`

The subarray `[3, 4, 5]` is product equivalent.

#### Example 3

- **Input:** `nums = [1, 2, 3, 1, 4, 5, 1]`
- **Output:** `5`
