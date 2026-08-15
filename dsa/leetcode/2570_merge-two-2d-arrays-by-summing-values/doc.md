# Merge Two 2D Arrays by Summing Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2570 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [merge-two-2d-arrays-by-summing-values](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) |

## Problem Description

### Goal

Two two-dimensional arrays, `nums1` and `nums2`, store `[id, value]` records. Within each array every `id` is unique, and the records are already sorted in strictly ascending order by `id`.

Merge the records into one ascending array. Include every `id` that occurs in either input exactly once. Its output value is the sum of its values from both arrays, treating a missing contribution as zero. Return the resulting `[id, value]` records in ascending `id` order.

### Function Contract

**Inputs**

- `nums1`: Between $1$ and $200$ unique `[id, value]` pairs sorted by strictly increasing `id`.
- `nums2`: Between $1$ and $200$ unique `[id, value]` pairs sorted by strictly increasing `id`.

Each `id` and `value` is between $1$ and $1000$, inclusive.

**Return value**

- One sorted list of `[id, summed_value]` pairs containing the union of both input ID sets.

### Examples

#### Example 1

- **Input:** `nums1 = [[1, 2], [2, 3], [4, 5]], nums2 = [[1, 4], [3, 2], [4, 1]]`
- **Output:** `[[1, 6], [2, 3], [3, 2], [4, 6]]`
- **Explanation:** IDs $1$ and $4$ occur in both inputs, so their paired values are added.

#### Example 2

- **Input:** `nums1 = [[2, 4], [3, 6], [5, 5]], nums2 = [[1, 3], [4, 3]]`
- **Output:** `[[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]`
- **Explanation:** The ID sets are disjoint, so all records are interleaved without changing their values.

#### Example 3

- **Input:** `nums1 = [[1, 1]], nums2 = [[1, 2]]`
- **Output:** `[[1, 3]]`
- **Explanation:** The only shared ID appears once with the sum of its two values.
