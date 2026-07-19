# Maximum Erasure Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1695 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-erasure-value/) |

## Problem Description
### Goal

You are given an array `nums` of positive integers. Erase exactly one subarray whose elements are all unique. A subarray is a contiguous segment `nums[left:right + 1]`; elements cannot be skipped or reordered when choosing it.

The score earned by erasing the chosen subarray is the sum of its elements. Return the maximum score obtainable from any nonempty contiguous segment with no repeated value. Different occurrences of the same value conflict even when they are far apart inside the candidate segment.

### Function Contract
**Inputs**

- `nums`: a list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^4$

**Return value**

The largest sum among all nonempty subarrays whose values are pairwise distinct.

### Examples
**Example 1**

- Input: `nums = [4, 2, 4, 5, 6]`
- Output: `17`

The segment `[2, 4, 5, 6]` is unique and has the maximum sum.

**Example 2**

- Input: `nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]`
- Output: `8`

Either `[5, 2, 1]` or `[1, 2, 5]` achieves the best score.

**Example 3**

- Input: `nums = [1, 2, 3, 4]`
- Output: `10`

All values are unique, so erasing the entire array is optimal.
