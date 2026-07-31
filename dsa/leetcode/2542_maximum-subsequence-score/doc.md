# Maximum Subsequence Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2542 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-subsequence-score](https://leetcode.com/problems/maximum-subsequence-score/) |

## Problem Description

### Goal

Two 0-indexed integer arrays, `nums1` and `nums2`, have the same length `n`. Choose exactly `k` indices from `{0, 1, ..., n - 1}`; deleting the remaining indices forms the required subsequence of indices.

For a chosen set, add the corresponding `nums1` values and multiply that sum by the minimum corresponding `nums2` value. Return the maximum score obtainable over every choice of exactly `k` indices.

### Function Contract

**Inputs**

- `nums1`: The nonnegative values that contribute to the selected sum.
- `nums2`: The nonnegative values whose selected minimum is the multiplier.
- `k`: The positive number of indices that must be selected.

The arrays have equal length $n$, where $1 \leq n \leq 10^5$ and $1 \leq k \leq n$. Every array value is at most $10^5$.

**Return value**

Return the maximum possible product of the selected `nums1` sum and selected `nums2` minimum.

### Examples

**Example 1**

- Input: `nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3`
- Output: `12`
- Explanation: Selecting indices 0, 2, and 3 gives sum $6$ and minimum multiplier $2$.

**Example 2**

- Input: `nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1`
- Output: `30`
- Explanation: Selecting only index 2 gives $3 \cdot 10=30$.
