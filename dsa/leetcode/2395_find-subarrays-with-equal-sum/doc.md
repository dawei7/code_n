# Find Subarrays With Equal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2395 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-subarrays-with-equal-sum/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, consider every contiguous subarray
whose length is exactly 2. Each such subarray is identified by its starting
index and has the sum `nums[i] + nums[i + 1]`.

Determine whether two of these length-2 subarrays have equal sums while
starting at different indices. The subarrays may overlap, and even two
subarrays with identical contents count as different when they occupy
different positions. Return `true` when such a pair exists and `false`
otherwise.

### Function Contract

**Inputs**

- `nums`: A list of integers with $2 \le n \le 1000$, where
  $n = \lvert\texttt{nums}\rvert$ and
  $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return `True` if there are distinct starting indices $i$ and $j$ such that
`nums[i] + nums[i + 1] == nums[j] + nums[j + 1]`; otherwise return `False`.

### Examples

**Example 1**

- Input: `nums = [4, 2, 4]`
- Output: `True`
- Explanation: The pairs at indices 0 and 1 both sum to 6.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `False`
- Explanation: The adjacent-pair sums are 3, 5, 7, and 9, all distinct.

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `True`
- Explanation: The two overlapping subarrays have the same contents and sum,
  but their different starting indices make them distinct subarrays.
