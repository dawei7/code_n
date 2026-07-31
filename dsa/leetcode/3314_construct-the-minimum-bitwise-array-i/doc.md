# Construct the Minimum Bitwise Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3314 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/) |

## Problem Description

### Goal

You are given an array `nums` containing $n$ prime integers. Construct an array `ans` of the same length so that, at every index `i`, the bitwise OR of `ans[i]` and its successor `ans[i] + 1` equals `nums[i]`.

Choose each `ans[i]` independently and make it the smallest non-negative integer that satisfies `ans[i] | (ans[i] + 1) == nums[i]`. If no non-negative integer can produce a particular prime under this operation, store `-1` at that index instead.

### Function Contract

**Inputs**

- `nums`: An array of $n$ prime integers, where $1\leq n\leq100$ and $2\leq\texttt{nums[i]}\leq1000$.

**Return value**

Return an integer array of length $n$ containing the minimum valid value for every prime, or `-1` when no such value exists.

### Examples

**Example 1**

- Input: `nums = [2, 3, 5, 7]`
- Output: `[-1, 1, 4, 3]`

No pair of consecutive non-negative integers has OR equal to 2. For 7, the minimum choice is 3 because `3 | 4 == 7`.

**Example 2**

- Input: `nums = [11, 13, 31]`
- Output: `[9, 12, 15]`

For example, `9 | 10 == 11`, and no smaller non-negative value produces 11.

**Example 3**

- Input: `nums = [17, 19, 23]`
- Output: `[16, 17, 19]`
