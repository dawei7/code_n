# Find the Median of the Uniqueness Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3134 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/) |

## Problem Description

### Goal

You are given an integer array `nums`. For every contiguous subarray `nums[i..j]`, compute the number of distinct values it contains. Collect all of these counts and sort them in non-decreasing order; the resulting sequence is the **uniqueness array** of `nums`.

Return the median of the uniqueness array. The median is the middle value after sorting. When the sequence has even length and therefore has two middle values, use the smaller one.

### Function Contract

Let $n$ be the length of `nums`, let

$$
T = \frac{n(n+1)}{2}
$$

be the number of contiguous subarrays, and let $D$ be the number of distinct values in `nums`.

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- Return the lower median of the $T$ distinct-count values in the uniqueness array.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `1`
- Explanation: The sorted distinct counts are `[1, 1, 1, 2, 2, 3]`. The two middle values are `1` and `2`, so the smaller one is returned.

**Example 2**

- Input: `nums = [3, 4, 3, 4, 5]`
- Output: `2`
- Explanation: The uniqueness array is `[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]`, whose median is `2`.

**Example 3**

- Input: `nums = [4, 3, 5, 4]`
- Output: `2`
- Explanation: The uniqueness array is `[1, 1, 1, 1, 2, 2, 2, 3, 3, 3]`; its lower median is `2`.
