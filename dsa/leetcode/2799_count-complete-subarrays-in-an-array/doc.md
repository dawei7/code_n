# Count Complete Subarrays in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2799 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-complete-subarrays-in-an-array/) |

## Problem Description

### Goal

You are given an array `nums` containing positive integers. A non-empty contiguous subarray is called complete when it contains exactly as many distinct values as the entire input array.

Because every subarray draws values from `nums`, matching the distinct-value count means that the subarray contains every distinct value that appears anywhere in `nums`. Count all contiguous subarrays satisfying this condition and return the total.

### Function Contract

**Inputs**

- `nums`: A list of positive integers with $1 \le \lvert\texttt{nums}\rvert \le 1000$ and $1 \le \texttt{nums[i]} \le 2000$.

**Return value**

Return the number of non-empty contiguous subarrays whose set of distinct values equals the distinct-value set of `nums`.

### Examples

**Example 1**

- Input: `nums = [1, 3, 1, 2, 2]`
- Output: `4`
- Explanation: The complete subarrays are `[1, 3, 1, 2]`, `[1, 3, 1, 2, 2]`, `[3, 1, 2]`, and `[3, 1, 2, 2]`.

**Example 2**

- Input: `nums = [5, 5, 5, 5]`
- Output: `10`
- Explanation: The whole array has one distinct value, so every non-empty subarray is complete. There are $4 \cdot 5 / 2 = 10$ such subarrays.
