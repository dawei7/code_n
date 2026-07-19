# Two Out of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2032 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/two-out-of-three/) |

## Problem Description

### Goal

Given three integer arrays `nums1`, `nums2`, and `nums3`, identify every value
that occurs in at least two different arrays. Repeated copies inside a single
array still establish presence in only that one array; they do not satisfy the
two-array requirement by themselves.

Return each qualifying value exactly once. The result may list those distinct
values in any order. Values appearing in only one array must be omitted, while
a value shared by all three arrays qualifies as usual.

### Function Contract

Define

$$
S = \lvert \texttt{nums1} \rvert
  + \lvert \texttt{nums2} \rvert
  + \lvert \texttt{nums3} \rvert.
$$

**Inputs**

- `nums1`, `nums2`, and `nums3`: nonempty integer lists, each of length at
  most $100$, whose values lie from $1$ through $100$.

**Return value**

- A distinct list containing exactly the values present in at least two input
  arrays, in any order.

### Examples

**Example 1**

- Input: `nums1 = [1, 1, 3, 2], nums2 = [2, 3], nums3 = [3]`
- Output: `[3, 2]`
- Explanation: `3` appears in all three arrays and `2` appears in the first
  two.

**Example 2**

- Input: `nums1 = [3, 1], nums2 = [2, 3], nums3 = [1, 2]`
- Output: `[2, 3, 1]`

**Example 3**

- Input: `nums1 = [1, 2, 2], nums2 = [4, 3, 3], nums3 = [5]`
- Output: `[]`
