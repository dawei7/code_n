# Longest Square Streak in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2501 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-square-streak-in-an-array/) |

## Problem Description
### Goal
You are given an integer array `nums`. A subsequence is formed by deleting any number of elements without changing the relative order of those retained.

A chosen subsequence is a square streak when it contains at least two elements and, after sorting it, every element except the first is the square of the preceding element. The selected values therefore form an increasing chain such as $x,x^2,x^4,\ldots$; their positions in the original array need not already follow that order because the definition sorts the chosen subsequence before testing it.

Return the length of the longest square streak that can be selected from `nums`, or return `-1` when no valid streak exists.

### Function Contract
**Inputs**

- `nums`: A list of $n$ integers, where $2 \le n \le 10^5$ and $2 \le \texttt{nums[i]} \le 10^5$.

**Return value**

The maximum number of values in a square streak, or `-1` if every possible chain has length less than two.

### Examples
**Example 1**

- Input: `nums = [4,3,6,16,8,2]`
- Output: `3`
- Explanation: Choose `[4,16,2]`; after sorting, it is `[2,4,16]`, and each later value is the square of the previous one.

**Example 2**

- Input: `nums = [2,3,5,6,7]`
- Output: `-1`
- Explanation: No value's square is also available, so no valid streak has two elements.

**Example 3**

- Input: `nums = [2,4,16,256,65536]`
- Output: `5`
- Explanation: All five values form one square streak.
