# Longest Even Odd Subarray With Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2760 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Longest Even Odd Subarray With Threshold](https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums` and an integer `threshold`, find the maximum length of a contiguous non-empty subarray `nums[l:r + 1]` satisfying all three rules below:

- Its first value `nums[l]` is even.
- Every pair of adjacent values inside the subarray has different parity.
- Every value in the subarray is at most `threshold`.

Return the longest achievable length. If no even value at or below the threshold can begin a valid subarray, return `0`.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \leq n \leq 100$ and $1 \leq \texttt{nums[i]} \leq 100$.
- `threshold`: An integer with $1 \leq \texttt{threshold} \leq 100$.

**Return value**

Return the length of the longest contiguous subarray that begins with an even value, alternates parity at every step, and contains no value greater than `threshold`.

### Examples

**Example 1**

- Input: `nums = [3,2,5,4]`, `threshold = 5`
- Output: `3`
- Explanation: The subarray `[2,5,4]` starts with an even value, alternates parity, and stays within the threshold.

**Example 2**

- Input: `nums = [1,2]`, `threshold = 2`
- Output: `1`
- Explanation: The one-element subarray `[2]` satisfies every condition.

**Example 3**

- Input: `nums = [2,3,4,5]`, `threshold = 4`
- Output: `3`
- Explanation: `[2,3,4]` is valid, but including `5` would exceed the threshold.
