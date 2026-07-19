# Maximum Difference Between Increasing Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2016 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-difference-between-increasing-elements/) |

## Problem Description

### Goal

Given a zero-indexed integer array `nums`, choose indices $i$ and $j$ such
that $i<j$ and `nums[i] < nums[j]`. Among all such increasing pairs, maximize
the difference `nums[j] - nums[i]`.

The index order is mandatory: a smaller value that occurs after a larger value
cannot be used as the first endpoint of a pair with that earlier element. If
no pair satisfies both the index and strict-value conditions, return $-1$.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $2\le N\le1000$ and
  $1\le\texttt{nums[i]}\le10^9$.

**Return value**

Return the maximum positive later-minus-earlier difference, or `-1` when no
increasing pair exists.

### Examples

**Example 1**

- Input: `nums = [7, 1, 5, 4]`
- Output: `4`
- Explanation: Indices $1$ and $2$ produce $5-1=4$.

**Example 2**

- Input: `nums = [9, 4, 3, 2]`
- Output: `-1`
- Explanation: No later value is strictly larger than an earlier one.

**Example 3**

- Input: `nums = [1, 5, 2, 10]`
- Output: `9`
- Explanation: The first and last values produce $10-1=9$.
