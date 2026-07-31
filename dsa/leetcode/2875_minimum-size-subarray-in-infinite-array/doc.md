# Minimum Size Subarray in Infinite Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2875 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Size Subarray in Infinite Array](https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and a positive integer `target`. Construct a 0-indexed infinite array by appending the elements of `nums` repeatedly, so every copy appears in the same order as the original array.

Find the length of the shortest contiguous subarray of this infinite sequence whose elements sum to exactly `target`. The subarray may remain within one copy of `nums`, cross a boundary between consecutive copies, or contain several complete copies. Return $-1$ when no such subarray exists.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers forming the repeating pattern.
- `target`: The positive sum that the selected subarray must equal exactly.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 10^5$, $1 \le \texttt{nums[i]} \le 10^5$, and $1 \le \texttt{target} \le 10^9$.

**Return value**

- The minimum length of a contiguous subarray in the infinite repetition whose sum is `target`, or $-1$ if none exists.

### Examples

**Example 1**

- Input: `nums = [1,2,3], target = 5`
- Output: `2`
- Explanation: In `[1,2,3,1,2,3,...]`, the elements `[2,3]` sum to $5$ and no length-one subarray does.

**Example 2**

- Input: `nums = [1,1,1,2,3], target = 4`
- Output: `2`
- Explanation: The pair consisting of the final `3` in one copy and the first `1` in the next copy has sum $4$.

**Example 3**

- Input: `nums = [2,4,6,8], target = 3`
- Output: `-1`
- Explanation: Every subarray sum is even, so no subarray can sum to $3$.
