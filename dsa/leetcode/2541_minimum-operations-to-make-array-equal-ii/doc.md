# Minimum Operations to Make Array Equal II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2541 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-operations-to-make-array-equal-ii](https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/) |

## Problem Description

### Goal

Two integer arrays, `nums1` and `nums2`, have the same length `n`. One operation chooses two indices `i` and `j`, adds `k` to `nums1[i]`, and subtracts `k` from `nums1[j]`. The indices are chosen for the same operation, so every change transfers one unit of size `k` between positions while preserving the array's total sum.

Make `nums1[i] == nums2[i]` at every index using as few operations as possible. Return that minimum count, or `-1` when no sequence of allowed transfers can make the arrays equal.

### Function Contract

**Inputs**

- `nums1`: The equal-length integer array that operations may modify.
- `nums2`: The target integer array.
- `k`: The nonnegative amount added and subtracted in each operation.

The common length satisfies $2 \leq n \leq 10^5$. Array values lie between $0$ and $10^9$, and $0 \leq k \leq 10^5$.

**Return value**

Return the minimum number of operations needed to transform `nums1` into `nums2`, or `-1` if the transformation is impossible.

### Examples

#### Example 1

- **Input:** `nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3`
- **Output:** `2`
- **Explanation:** Transfer one unit from index 0 to index 2, then one from index 3 to index 2.

#### Example 2

- **Input:** `nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1`
- **Output:** `-1`
- **Explanation:** The two totals differ, while every operation preserves the total.
