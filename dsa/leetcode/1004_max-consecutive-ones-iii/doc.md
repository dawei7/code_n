# Max Consecutive Ones III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1004 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/max-consecutive-ones-iii/) |

## Problem Description

### Goal

You are given a binary array `nums` and an integer `k`. You may flip at most `k` entries whose value is `0`, changing each selected entry to `1`.

Return the maximum number of consecutive `1`s that can appear after those flips. Because the chosen positions must contribute to one contiguous run, the task is equivalently to find the longest subarray containing at most `k` zeroes; every zero in that subarray can be flipped, while its existing ones remain unchanged.

### Function Contract

**Inputs**

- `nums`: a binary array of length $N$, where $1\le N\le10^5$ and every element is either `0` or `1`.
- `k`: the maximum number of zeroes that may be flipped, where $0\le k\le N$.

**Return value**

- The maximum length of a contiguous run of `1`s obtainable by flipping at most `k` zeroes.

### Examples

**Example 1**

- Input: `nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2`
- Output: `6`
- Explanation: Flipping the zero at index `5` and the final zero creates a consecutive run of six ones from indices `5` through `10`.

**Example 2**

- Input: `nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3`
- Output: `10`
- Explanation: The subarray from indices `2` through `11` contains exactly three zeroes, so all ten of its entries can become `1`.

**Example 3**

- Input: `nums = [1, 1, 1], k = 0`
- Output: `3`
- Explanation: No flip is needed because the entire array is already one consecutive run of ones.
