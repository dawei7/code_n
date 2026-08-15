# Split and Merge Array Transformation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3690 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-and-merge-array-transformation/) |

## Problem Description

### Goal

Transform `nums1` into `nums2` using as few split-and-merge operations as possible. In one operation, choose a nonempty contiguous subarray, remove it without changing the order of its elements, and insert that whole block at any position in the remaining array. The insertion may occur at the beginning, at the end, or between two retained elements.

The two arrays have equal length, and `nums2` is a permutation of `nums1`, including the same multiplicities when values repeat. Return the minimum number of operations. Moving a block never reverses or internally rearranges it, although repeated operations may substantially change the overall order.

### Function Contract

**Inputs**

- `nums1`: The starting list of $n$ integers, where $2 \le n \le 6$ and each value lies from $-10^5$ through $10^5$.
- `nums2`: The target list of the same length and the same multiset of values as `nums1`.

**Return value**

Return the minimum number of legal split-and-merge operations needed to make `nums1` equal `nums2`.

### Examples

#### Example 1

- **Input:** `nums1 = [3, 1, 2], nums2 = [1, 2, 3]`
- **Output:** `1`

Removing the initial `[3]` and inserting it at the end reaches the target.

#### Example 2

- **Input:** `nums1 = [1, 1, 2, 3, 4, 5], nums2 = [5, 4, 3, 2, 1, 1]`
- **Output:** `3`

No sequence of fewer than three block moves reaches the reversed arrangement.

#### Example 3

- **Input:** `nums1 = [1, 2, 3], nums2 = [1, 2, 3]`
- **Output:** `0`

No operation is required when the arrays already match.
