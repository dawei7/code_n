# Number of Ways Where Square of Number Is Equal to Product of Two Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1577 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Two Pointers |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) |

## Problem Description
### Goal

Given two integer arrays, `nums1` and `nums2`, count index triplets of two symmetric types. A type-1 triplet selects one index `i` from `nums1` and two ordered-by-index positions `j < k` from `nums2` such that the square of `nums1[i]` equals `nums2[j] * nums2[k]`.

A type-2 triplet reverses the arrays: it selects one index `i` from `nums2` and positions `j < k` from `nums1`, requiring the square of `nums2[i]` to equal `nums1[j] * nums1[k]`.

Return the total number of type-1 and type-2 triplets. Indices define the triplets, so equal values at different positions contribute separately, while each unordered pair inside one array is counted once through the condition $j<k$.

### Function Contract
**Inputs**

- `nums1`: An integer array of length $N$, where $1 \le N \le 100$.
- `nums2`: An integer array of length $M$, where $1 \le M \le 100$.
- Every array value is between $1$ and $10^5$, inclusive.

**Return value**

Return the total number of valid index triplets of both types.

### Examples
**Example 1**

- Input: `nums1 = [7, 4], nums2 = [5, 2, 8, 9]`
- Output: `1`

**Example 2**

- Input: `nums1 = [1, 1], nums2 = [1, 1, 1]`
- Output: `9`

**Example 3**

- Input: `nums1 = [7, 7, 8, 3], nums2 = [1, 2, 9, 7]`
- Output: `2`
