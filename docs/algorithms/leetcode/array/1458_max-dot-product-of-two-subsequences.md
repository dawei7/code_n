# Max Dot Product of Two Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1458 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [max-dot-product-of-two-subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) |

## Problem Description & Examples
### Goal
Choose a non-empty subsequence from each array, keeping order, so the dot product of the two chosen subsequences is as large as possible.

### Function Contract
**Inputs**

- `nums1`: the first integer list.
- `nums2`: the second integer list.

**Return value**

The maximum dot product of two non-empty subsequences.

### Examples
**Example 1**

- Input: `nums1 = [2,1,-2,5], nums2 = [3,0,-6]`
- Output: `18`

**Example 2**

- Input: `nums1 = [3,-2], nums2 = [2,-6,7]`
- Output: `21`

**Example 3**

- Input: `nums1 = [-1,-1], nums2 = [1,1]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Dynamic programming similar to sequence alignment. At each pair, either start/take a pair, extend a previous chosen product, or skip one side; initialize so a non-empty pair is required.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)`, reducible to `O(n)`.
