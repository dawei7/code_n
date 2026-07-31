# Maximize Sum of At Most K Distinct Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3684 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/) |

## Problem Description
### Goal

Given an array `nums` of positive integers, choose at most `k` elements whose values are pairwise distinct. Among all valid choices, maximize the sum of the selected values.

Return the chosen values themselves, arranged in strictly descending order. Repeated occurrences of a value offer only one eligible choice because the selected numbers must be distinct. If fewer than `k` distinct values exist, return every distinct value; positivity ensures that adding another available value always increases the sum.

### Function Contract

**Inputs**

- `nums`: a non-empty list of $n$ positive integers, where $1\le n\le100$ and each value is at most $10^9$.
- `k`: the maximum number of selected elements, satisfying $1\le k\le n$.

Let $U$ be the number of distinct values in `nums`.

**Return value**

Return the largest $\min(k,U)$ distinct values in strictly descending order.

### Examples

**Example 1**

- Input: `nums = [84, 93, 100, 77, 90], k = 3`
- Output: `[100, 93, 90]`

These three distinct values produce the maximum sum 283.

**Example 2**

- Input: `nums = [84, 93, 100, 77, 93], k = 3`
- Output: `[100, 93, 84]`

The repeated 93 can be selected only once.

**Example 3**

- Input: `nums = [1, 1, 1, 2, 2, 2], k = 6`
- Output: `[2, 1]`

Only two distinct values are available, so the result contains fewer than `k` elements.
