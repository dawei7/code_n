# Minimum Operations to Maximize Last Elements in Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2934 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/) |

## Problem Description

### Goal

Two 0-indexed integer arrays `nums1` and `nums2` have the same length `n`. In
one operation, choose an index `i` and swap `nums1[i]` with `nums2[i]`. Any
indices, including the last one, may be selected, and no operation is required
when the desired state already holds.

Find the fewest operations after which `nums1[n - 1]` is a maximum element of
`nums1` and `nums2[n - 1]` is a maximum element of `nums2`. Equal maximum
values are allowed. Return that minimum, or `-1` when no set of index-wise
swaps can satisfy both conditions.

### Function Contract

**Inputs**

- `nums1`: The first positive integer array.
- `nums2`: The second positive integer array, with the same length as `nums1`.

Let $n=\lvert\texttt{nums1}\rvert=\lvert\texttt{nums2}\rvert$. The constraints
are $1\le n\le1000$ and $1\le\texttt{nums1[i]},\texttt{nums2[i]}\le10^9$.

**Return value**

- The minimum number of vertical swaps needed to make both last elements array maxima, or `-1` if impossible.

### Examples

**Example 1**

- Input: `nums1 = [1, 2, 7], nums2 = [4, 5, 3]`
- Output: `1`
- Explanation: Swap the last pair, producing final maxima 3 and 7.

**Example 2**

- Input: `nums1 = [2, 3, 4, 5, 9], nums2 = [8, 8, 4, 4, 4]`
- Output: `2`
- Explanation: Swap indices 4 and 3; the resulting last values 4 and 9 are maxima of their arrays.

**Example 3**

- Input: `nums1 = [1, 5, 4], nums2 = [2, 5, 3]`
- Output: `-1`
- Explanation: Neither orientation of the last pair can dominate every earlier vertical pair.
