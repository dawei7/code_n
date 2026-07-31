# Longest Alternating Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2765 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Longest Alternating Subarray](https://leetcode.com/problems/longest-alternating-subarray/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`. A contiguous subarray `s` of length $m$ is alternating only when $m > 1$, its first step rises by exactly one, and every later step reverses that difference. Thus `s[1] - s[0] = 1`, `s[2] - s[1] = -1`, `s[3] - s[2] = 1`, and the pattern continues through the final pair.

Equivalently, the subarray repeats its first two values as `[s[0], s[1], s[0], s[1], ...]` with `s[1] = s[0] + 1`. Return the maximum length among all alternating subarrays of `nums`, or return `-1` when none exists.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $2 \leq n \leq 100$ and $1 \leq \texttt{nums[i]} \leq 10^4$.

**Return value**

Return the length of the longest alternating contiguous subarray, or `-1` if no valid subarray of length at least two exists.

### Examples

**Example 1**

- Input: `nums = [2,3,4,3,4]`
- Output: `4`
- Explanation: The longest alternating subarray is `[3,4,3,4]`.

**Example 2**

- Input: `nums = [4,5,6]`
- Output: `2`
- Explanation: Both `[4,5]` and `[5,6]` satisfy the required first rise, but neither can extend.

**Example 3**

- Input: `nums = [21,9,5]`
- Output: `-1`
- Explanation: No adjacent pair rises by exactly one, so no alternating subarray can start.
