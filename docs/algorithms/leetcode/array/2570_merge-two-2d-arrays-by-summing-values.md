# Merge Two 2D Arrays by Summing Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2570 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Two Pointers |
| Official Link | [merge-two-2d-arrays-by-summing-values](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) |

## Problem Description & Examples
### Goal
Given two 2D arrays representing sparse vectors where each element is a pair `[id, value]`, merge them into a single 2D array. If an `id` appears in both input arrays, sum their corresponding values. The resulting array must be sorted by `id` in ascending order.

### Function Contract
**Inputs**

- `nums1`: A list of lists, where each inner list contains two integers `[id, val]`.
- `nums2`: A list of lists, where each inner list contains two integers `[id, val]`.

**Return value**

- A list of lists representing the merged sparse vectors, sorted by `id`.

### Examples
**Example 1**

- Input: `nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]`
- Output: `[[1,6],[2,3],[3,2],[4,6]]`

**Example 2**

- Input: `nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]`
- Output: `[[1,3],[2,4],[3,6],[4,3],[5,5]]`

**Example 3**

- Input: `nums1 = [[1,1]], nums2 = [[1,2]]`
- Output: `[[1,3]]`

---

## Underlying Base Algorithm(s)
The problem can be solved efficiently using the **Two Pointers** technique. Since the input arrays are already sorted by `id`, we can traverse both arrays simultaneously, comparing the current `id`s and appending the smaller one (or summing if they match) to the result list. Alternatively, a **Hash Map** (or `collections.defaultdict`) can be used to aggregate values by `id` and then sort the keys.

---

## Complexity Analysis
- **Time Complexity**: `O(N + M)`, where `N` and `M` are the lengths of `nums1` and `nums2` respectively, as we iterate through each array exactly once.
- **Space Complexity**: `O(N + M)` to store the resulting merged array.
