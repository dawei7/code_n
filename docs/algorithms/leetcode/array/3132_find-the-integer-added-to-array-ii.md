# Find the Integer Added to Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3132 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Sorting, Enumeration |
| Official Link | [find-the-integer-added-to-array-ii](https://leetcode.com/problems/find-the-integer-added-to-array-ii/) |

## Problem Description & Examples
### Goal
Given two integer arrays `nums1` and `nums2`, determine the smallest integer `x` such that `nums2` can be formed by taking `nums1`, adding `x` to every element, and then removing exactly two elements from the resulting array.

### Function Contract
**Inputs**

- `nums1`: A list of integers (length `n`).
- `nums2`: A list of integers (length `n - 2`).

**Return value**

- An integer representing the smallest possible value of `x` that satisfies the condition.

### Examples
**Example 1**

- Input: `nums1 = [4,20,16,12,8]`, `nums2 = [14,18,10]`
- Output: `-2`
- Explanation: After adding -2 to `nums1`, we get `[2, 18, 14, 10, 6]`. Removing 2 and 6 leaves `[18, 14, 10]`, which matches `nums2`.

**Example 2**

- Input: `nums1 = [3,5,5,3]`, `nums2 = [7,7]`
- Output: `2`
- Explanation: After adding 2 to `nums1`, we get `[5, 7, 7, 5]`. Removing 5 and 5 leaves `[7, 7]`, which matches `nums2`.

**Example 3**

- Input: `nums1 = [1,1,1,1]`, `nums2 = [1,1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved by sorting both arrays. Since we must remove exactly two elements from `nums1`, the potential difference `x` must be one of the values derived from `nums2[0] - nums1[i]` for `i` in `[0, 1, 2]`. We iterate through these three possible candidates for `x` and verify if the remaining elements of `nums1` (after adding `x`) can form `nums2` using a two-pointer approach.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` due to sorting, where `n` is the length of `nums1`. The verification step takes `O(n)` and is performed a constant number of times.
- **Space Complexity**: `O(1)` or `O(n)` depending on the sorting implementation's space requirements.
