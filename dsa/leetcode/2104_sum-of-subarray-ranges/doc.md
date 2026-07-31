# Sum of Subarray Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2104 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [sum-of-subarray-ranges](https://leetcode.com/problems/sum-of-subarray-ranges/) |

## Problem Description

### Goal

You are given an integer array `nums`. A subarray is a contiguous, non-empty sequence of its elements. The range of one such subarray is the difference between that subarray's largest element and smallest element; a one-element subarray consequently has range zero.

Consider every possible subarray of `nums`, calculate each of their ranges independently, and return the sum of all those values. Equal elements and negative values follow the same definition: only the maximum and minimum within each selected contiguous interval determine its contribution.

### Function Contract

**Inputs**

- `nums`: An integer array with length $n$, where $1 \le n \le 1000$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the sum of the ranges of all non-empty contiguous subarrays of `nums`.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `4`
- Explanation: The three single-element subarrays contribute zero. The ranges of `[1, 2]`, `[2, 3]`, and `[1, 2, 3]` are respectively $1$, $1$, and $2$, whose sum is $4$.

**Example 2**

- Input: `nums = [1, 3, 3]`
- Output: `4`
- Explanation: The only positive contributions are $2$ from `[1, 3]` and $2$ from `[1, 3, 3]`.

**Example 3**

- Input: `nums = [4, -2, -3, 4, 1]`
- Output: `59`
