# Find the Number of Good Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3164 |
| Difficulty | Medium |
| Topics | Array, Hash Table |
| Official Link | [find-the-number-of-good-pairs-ii](https://leetcode.com/problems/find-the-number-of-good-pairs-ii/) |

## Problem Description & Examples
### Goal
Given two integer arrays `nums1` and `nums2` and an integer `k`, identify the total count of "good pairs" (i, j). A pair (i, j) is considered good if `nums1[i]` is divisible by the product of `nums2[j]` and `k`. That is, `nums1[i] % (nums2[j] * k) == 0`.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.
- `k`: An integer multiplier.

**Return value**

- An integer representing the total count of indices (i, j) such that `nums1[i]` is divisible by `nums2[j] * k`.

### Examples
**Example 1**

- Input: `nums1 = [1, 3, 4], nums2 = [1, 3, 4], k = 1`
- Output: `5`

**Example 2**

- Input: `nums1 = [1, 2, 4, 12], nums2 = [2, 4], k = 3`
- Output: `2`

**Example 3**

- Input: `nums1 = [10, 20], nums2 = [1, 2], k = 2`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a Frequency Map (Hash Table) approach. By counting the occurrences of each number in `nums1`, we can iterate through each unique divisor `d = nums2[j] * k`. For each divisor, we iterate through its multiples up to the maximum value present in `nums1`, checking if those multiples exist in our frequency map. This avoids the O(N*M) brute force approach.

---

## Complexity Analysis
- **Time Complexity**: O(N + M + V log V), where N is the length of `nums1`, M is the length of `nums2`, and V is the maximum value in `nums1`. The harmonic series summation ensures the inner loop runs efficiently.
- **Space Complexity**: O(V), where V is the maximum value in `nums1`, used to store the frequency map.
