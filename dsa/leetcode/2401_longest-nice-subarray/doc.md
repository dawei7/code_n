# Longest Nice Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2401 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-nice-subarray/) |

## Problem Description

### Goal

Given an array of positive integers, call a contiguous subarray nice when the
bitwise AND of every pair of elements at different positions is zero. In other
words, no binary bit position may be set in two different elements of the
chosen subarray.

Return the length of the longest nice subarray. The elements must remain
contiguous in their original order. Every one-element subarray is nice because
it contains no pair of distinct positions, so the answer is always at least
one.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where
  $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the maximum length of a contiguous interval in which
`nums[i] & nums[j] == 0` for every two distinct indices in the interval.

### Examples

**Example 1**

- Input: `nums = [1, 3, 8, 48, 10]`
- Output: `3`
- Explanation: `[3, 8, 48]` is nice because each of its three pairwise AND
  results is zero.

**Example 2**

- Input: `nums = [3, 1, 5, 11, 13]`
- Output: `1`
- Explanation: Every adjacent extension introduces a shared set bit, while any
  single element is valid.

**Example 3**

- Input: `nums = [1, 2, 4, 8]`
- Output: `4`
- Explanation: Each value uses a different bit, so the entire array is nice.
