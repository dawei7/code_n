# Minimum Subsequence in Non-Increasing Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1403 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/) |

## Problem Description

### Goal

Given an array `nums` of positive integers, select some of its elements as a subsequence so that their sum is strictly greater than the sum of all unselected elements. The relative positions do not constrain the returned presentation.

Use the minimum possible number of elements. If several minimum-length selections work, choose one with the greatest selected sum. Return the selected values arranged in non-increasing order.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 500$ and $1 \le \texttt{nums[i]} \le 100$.

**Return value**

- The minimum-length qualifying selection, using the maximum sum among ties and listed in non-increasing order.

### Examples

**Example 1**

- Input: `nums = [4,3,10,9,8]`
- Output: `[10,9]`

**Example 2**

- Input: `nums = [4,4,7,6,7]`
- Output: `[7,7,6]`

**Example 3**

- Input: `nums = [6]`
- Output: `[6]`
