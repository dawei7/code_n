# Number of Pairs Satisfying Inequality

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2426 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Official Link | [number-of-pairs-satisfying-inequality](https://leetcode.com/problems/number-of-pairs-satisfying-inequality/) |

## Problem Description & Examples
### Goal
Given two integer arrays `nums1` and `nums2` of the same length and an integer `diff`, count the number of index pairs `(i, j)` such that `0 <= i < j < n` and the inequality `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff` holds true.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.
- `diff`: An integer representing the allowed tolerance.

**Return value**

- An integer representing the total count of valid pairs `(i, j)` that satisfy the given inequality.

### Examples
**Example 1**

- Input: `nums1 = [3, 2, 5], nums2 = [2, 2, 1], diff = 1`
- Output: `3`

**Example 2**

- Input: `nums1 = [3, -1], nums2 = [-2, 2], diff = -1`
- Output: `0`

---

## Underlying Base Algorithm(s)
The inequality `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff` can be rearranged to `(nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff`. By defining a new array `arr` where `arr[k] = nums1[k] - nums2[k]`, the problem reduces to finding pairs `(i, j)` such that `i < j` and `arr[i] - arr[j] <= diff`, or `arr[i] - diff <= arr[j]`. This is a classic variation of the "Count Inversions" problem, which can be solved efficiently using a modified Merge Sort or a Binary Indexed Tree (Fenwick Tree) with coordinate compression.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the input arrays. This is achieved by the divide-and-conquer approach of Merge Sort.
- **Space Complexity**: `O(n)` to store the auxiliary array used during the merge process.
