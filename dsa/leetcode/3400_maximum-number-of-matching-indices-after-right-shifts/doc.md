# Maximum Number of Matching Indices After Right Shifts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3400 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/) |

## Problem Description

### Goal

You are given integer arrays `nums1` and `nums2` with the same length $n$. An index matches when the values at that position in the two arrays are equal.

You may right-shift `nums1` any number of times. One right shift moves every element formerly at index $i$ to index $(i+1)\bmod n$, so the final element wraps around to index zero. Among all possible circular alignments of `nums1` against the unchanged `nums2`, return the largest number of matching indices.

### Function Contract

**Inputs**

- `nums1`: A list of $n$ integers.
- `nums2`: A second list of exactly $n$ integers.

The shared length satisfies $1\le n\le3000$, and every element of both arrays lies between 1 and $10^9$, inclusive.

**Return value**

- The maximum number of equal-index pairs obtainable after any number of right shifts of `nums1`.

### Examples

**Example 1**

- Input: `nums1 = [3, 1, 2, 3, 1, 2], nums2 = [1, 2, 3, 1, 2, 3]`
- Output: `6`

Two right shifts make `nums1` equal to `nums2`, so all six indices match.

**Example 2**

- Input: `nums1 = [1, 4, 2, 5, 3, 1], nums2 = [2, 3, 1, 2, 4, 6]`
- Output: `3`

After three right shifts, indices 1, 2, and 4 match; no circular alignment matches more positions.
