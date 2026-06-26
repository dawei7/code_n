# Count Good Triplets in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2179 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Official Link | [count-good-triplets-in-an-array](https://leetcode.com/problems/count-good-triplets-in-an-array/) |

## Problem Description & Examples
### Goal
Count triples of distinct values that appear in the same relative order in two permutations of `0` through `n - 1`.

### Function Contract
**Inputs**

- `nums1`: a permutation of `0..n-1`.
- `nums2`: another permutation of the same values.

**Return value**

The number of value triples ordered consistently in both permutations.

### Examples
**Example 1**

- Input: `nums1 = [2, 0, 1, 3]`, `nums2 = [0, 1, 2, 3]`
- Output: `1`

**Example 2**

- Input: `nums1 = [4, 0, 1, 3, 2]`, `nums2 = [4, 1, 0, 2, 3]`
- Output: `4`

**Example 3**

- Input: `nums1 = [0, 1, 2]`, `nums2 = [0, 1, 2]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Map each value to its position in `nums2`, then transform `nums1` into that position sequence. For every position as the middle of a triplet, count earlier mapped positions that are smaller and later mapped positions that are larger using Fenwick trees or segment trees. Add the product of those two counts.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
