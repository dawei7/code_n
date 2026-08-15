# Find the Number of Subarrays Where Boundary Elements Are Maximum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3113 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-the-number-of-subarrays-where-boundary-elements-are-maximum](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Count its contiguous subarrays whose first and last elements are equal to each other and also equal to the largest element anywhere in that subarray.

Both boundary conditions matter: matching endpoints do not qualify when a larger value lies between them. Every one-element subarray does qualify because its only element is simultaneously its first element, last element, and maximum. Return the total number of qualifying subarrays.

### Function Contract

Let $n$ be the length of `nums`.

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- The number of contiguous subarrays whose two boundary values both equal the subarray maximum.

### Examples

#### Example 1

- **Input:** `nums = [1,4,3,3,2]`
- **Output:** `6`
- **Explanation:** The five one-element subarrays qualify, as does the subarray `[3,3]`.

#### Example 2

- **Input:** `nums = [3,3,3]`
- **Output:** `6`
- **Explanation:** Every one of the six contiguous subarrays has boundary values equal to its maximum.

#### Example 3

- **Input:** `nums = [1]`
- **Output:** `1`
- **Explanation:** The single available subarray qualifies.
