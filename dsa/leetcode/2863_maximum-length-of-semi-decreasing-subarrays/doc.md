# Maximum Length of Semi-Decreasing Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2863 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Sorting, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/) |

## Problem Description

### Goal

Given an integer array `nums`, consider each nonempty contiguous subarray. A subarray is semi-decreasing when its first element is strictly greater than its last element. The elements between those endpoints may appear in any order and do not need to be decreasing.

Return the greatest length of a semi-decreasing subarray. If no pair of endpoints satisfies the strict inequality, return `0`; a one-element subarray does not qualify because its first and last values are equal.

### Function Contract

**Inputs**

- `nums`: The integer array in which to choose a contiguous subarray.

Let $n$ be the length of `nums`. The input satisfies $1 \le n \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- Return the maximum value of $j-i+1$ over indices $i<j$ with $\texttt{nums[i]} > \texttt{nums[j]}$, or `0` when no such pair exists.

### Examples

#### Example 1

- **Input:** `nums = [7, 6, 5, 4, 3, 2, 1, 6, 10, 11]`
- **Output:** `8`
- **Explanation:** The subarray from the first `7` through the later `6` has length $8$, and its first value is strictly greater than its last.

#### Example 2

- **Input:** `nums = [57, 55, 50, 60, 61, 58, 63, 59, 64, 60, 63]`
- **Output:** `6`
- **Explanation:** The subarray `[61, 58, 63, 59, 64, 60]` qualifies because $61>60$.

#### Example 3

- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `0`
- **Explanation:** No earlier element is strictly greater than a later element.
