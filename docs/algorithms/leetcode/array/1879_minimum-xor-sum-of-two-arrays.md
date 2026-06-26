# Minimum XOR Sum of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1879 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Official Link | [minimum-xor-sum-of-two-arrays](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/) |

## Problem Description & Examples
### Goal
Permute `nums2` and pair it with `nums1` by index. Minimize the sum of pairwise XOR values.

### Function Contract
**Inputs**

- `nums1`: the first integer array.
- `nums2`: the second integer array of the same length.

**Return value**

Return the minimum possible XOR sum.

### Examples
**Example 1**

- Input: `nums1 = [1,2], nums2 = [2,3]`
- Output: `2`

**Example 2**

- Input: `nums1 = [1,0,3], nums2 = [5,3,4]`
- Output: `8`

**Example 3**

- Input: `nums1 = [2,4,6], nums2 = [1,3,5]`
- Output: `9`

---

## Underlying Base Algorithm(s)
Use bitmask assignment DP. The mask records which elements of `nums2` are already used. If `i` bits are set, choose the element of `nums2` to pair with `nums1[i]`, and minimize `(nums1[i] XOR nums2[j]) + dp(mask with j used)`.

---

## Complexity Analysis
- **Time Complexity**: `O(n * 2^n)`
- **Space Complexity**: `O(2^n)`
