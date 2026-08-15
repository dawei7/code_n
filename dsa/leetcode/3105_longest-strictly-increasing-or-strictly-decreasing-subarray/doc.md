# Longest Strictly Increasing or Strictly Decreasing Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3105 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [longest-strictly-increasing-or-strictly-decreasing-subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/) |

## Problem Description

### Goal

Given an integer array `nums`, consider its nonempty contiguous subarrays. A subarray is strictly increasing when every element after the first is greater than its predecessor. It is strictly decreasing when every element after the first is smaller than its predecessor.

Return the length of the longest subarray that satisfies either of these two strict monotonicity conditions. Equal adjacent values cannot belong to the same strictly increasing or strictly decreasing run.

### Function Contract

**Inputs**

- `nums`: An array of $n$ integers, where $1 \le n \le 50$ and $1 \le \texttt{nums[i]} \le 50$.

**Return value**

- The maximum length of a contiguous subarray that is either strictly increasing or strictly decreasing.

### Examples

#### Example 1

- **Input:** `nums = [1, 4, 3, 3, 2]`
- **Output:** `2`
- **Explanation:** The longest strictly increasing run is `[1, 4]`; `[4, 3]` and `[3, 2]` are strictly decreasing runs of the same length. The equal middle pair separates the latter two runs.

#### Example 2

- **Input:** `nums = [3, 3, 3, 3]`
- **Output:** `1`
- **Explanation:** Equal adjacent values are neither strictly increasing nor strictly decreasing, so only one-element subarrays qualify.

#### Example 3

- **Input:** `nums = [3, 2, 1]`
- **Output:** `3`
- **Explanation:** The entire array is strictly decreasing.
