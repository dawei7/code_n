# Minimum Number of K Consecutive Bit Flips

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 995 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) |

## Problem Description

### Goal

You are given a binary array `nums` and an integer `k`. A k-bit flip selects a contiguous subarray of length `k` and changes all of its bits simultaneously: every `0` becomes `1`, and every `1` becomes `0`.

Return the minimum number of k-bit flips needed to leave no `0` anywhere in the array. A selected range must contain exactly `k` consecutive positions; if no sequence of such operations can turn the whole array into ones, return `-1`.

### Function Contract

**Inputs**

- `nums`: a binary list of length $N$, where $1\le N\le10^5$.
- `k`: the length of every flipped subarray, where $1\le\texttt{k}\le N$.

**Return value**

- The minimum number of k-bit flips that changes every bit to `1`, or `-1` when this is impossible.

### Examples

**Example 1**

- Input: `nums = [0, 1, 0], k = 1`
- Output: `2`
- Explanation: Flip the first and third individual bits.

**Example 2**

- Input: `nums = [1, 1, 0], k = 2`
- Output: `-1`
- Explanation: No sequence of length-two flips produces three ones.

**Example 3**

- Input: `nums = [0, 0, 0, 1, 0, 1, 1, 0], k = 3`
- Output: `3`
