# Find K Pairs with Smallest Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 373 |
| Difficulty | Medium |
| Topics | Array, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) |

## Problem Description
### Goal
Given two integer arrays `nums1` and `nums2` sorted in non-decreasing order, every cross-array index pair `(i, j)` produces the value pair `[nums1[i], nums2[j]]` with sum `nums1[i] + nums2[j]`. Select the globally smallest such pair sums.

Return exactly `k` value pairs because the input guarantees `1 <= k <= len(nums1) * len(nums2)`. Distinct index pairs remain separate candidates even when duplicate values make their outputs equal. Return the pairs in any order; any tied choices at the final cutoff are acceptable. Avoid generating and sorting the full Cartesian product when only a small prefix is requested.

### Function Contract
**Inputs**

- `nums1`: a nondecreasing integer list
- `nums2`: a nondecreasing integer list
- `k`: the maximum number of pairs to return

**Return value**

- Any collection of `min(k, len(nums1) * len(nums2))` value pairs having globally smallest sums. Pair order and choices tied at the cutoff may vary.

### Examples
**Example 1**

- Input: `nums1 = [1,7,11], nums2 = [2,4,6], k = 3`
- Output: `[[1,2],[1,4],[1,6]]`

**Example 2**

- Input: `nums1 = [1,1,2], nums2 = [1,2,3], k = 2`
- Output: `[[1,1],[1,1]]`

**Example 3**

- Input: `nums1 = [1,2], nums2 = [3], k = 3`
- Output: `[[1,3],[2,3]]`
