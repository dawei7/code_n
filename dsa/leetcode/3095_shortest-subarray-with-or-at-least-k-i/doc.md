# Shortest Subarray With OR at Least K I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3095 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/) |

## Problem Description

### Goal

You are given an array `nums` whose elements are non-negative integers, together with a non-negative threshold `k`. A non-empty array is called **special** when the bitwise OR of all its elements is at least `k`.

Among every non-empty contiguous subarray of `nums`, find the minimum possible length of one that is special. Return that length, or return `-1` when no contiguous subarray can reach the threshold.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers, where $1 \le n \le 50$ and $0 \le \texttt{nums[i]} \le 50$.
- `k`: The required bitwise-OR threshold, satisfying $0 \le k < 64$.

A subarray must contain consecutive elements and must not be empty.

**Return value**

Return the length of the shortest subarray whose bitwise OR is at least `k`. Return `-1` if no such subarray exists.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `1`
- Explanation: The one-element subarray `[3]` has OR value `3`; `[2]` is another valid one-element choice.

**Example 2**

- Input: `nums = [2, 1, 8], k = 10`
- Output: `3`
- Explanation: The full array has OR value `11`, while neither a single element nor either length-two subarray reaches `10`.

**Example 3**

- Input: `nums = [1, 2], k = 0`
- Output: `1`
- Explanation: Every non-negative OR value is at least zero, so any single element is already special.
