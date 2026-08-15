# Find the Difference of Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2215 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-difference-of-two-arrays/) |

## Problem Description

### Goal

Given two 0-indexed integer arrays, form an answer containing two lists. The first list must contain every distinct integer that appears in `nums1` but does not appear anywhere in `nums2`.

The second list must likewise contain every distinct integer present in `nums2` and absent from `nums1`. Repeated occurrences contribute only one copy to the corresponding result list, and the values within either list may be returned in any order.

### Function Contract

**Inputs**

- `nums1`: A nonempty integer list.
- `nums2`: A nonempty integer list.

Let $n=\lvert\texttt{nums1}\rvert$ and $m=\lvert\texttt{nums2}\rvert$.

**Return value**

Return `[only_in_nums1, only_in_nums2]`, where each inner list contains distinct values and its ordering is unrestricted.

### Examples

#### Example 1

- **Input:** `nums1 = [1, 2, 3], nums2 = [2, 4, 6]`
- **Output:** `[[1, 3], [4, 6]]`

#### Example 2

- **Input:** `nums1 = [1, 2, 3, 3], nums2 = [1, 1, 2, 2]`
- **Output:** `[[3], []]`

#### Example 3

- **Input:** `nums1 = [5, 5], nums2 = [5]`
- **Output:** `[[], []]`
