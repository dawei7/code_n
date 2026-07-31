# Find the Integer Added to Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3131 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-integer-added-to-array-i/) |

## Problem Description

### Goal

You are given two integer arrays `nums1` and `nums2` of the same length. An unknown integer $x$ was added to every element of `nums1`, after which the resulting elements were rearranged to form `nums2`.

Determine the value of $x$. The input guarantees that one integer shift transforms the complete multiset of values in `nums1` exactly into the multiset in `nums2`.

### Function Contract

**Inputs**

- `nums1`: A nonempty list of integers.
- `nums2`: A list with the same length as `nums1`.

Both lengths are between $1$ and $100$, inclusive. Every element of both arrays is between $0$ and $1000$, inclusive.

**Return value**

- Return the integer $x$ that was added to every value in `nums1`.

### Examples

**Example 1**

- Input: `nums1 = [2, 6, 4], nums2 = [9, 7, 5]`
- Output: `3`
- Explanation: Adding `3` gives `[5, 9, 7]`, whose elements can be rearranged into `nums2`.

**Example 2**

- Input: `nums1 = [10], nums2 = [5]`
- Output: `-5`

**Example 3**

- Input: `nums1 = [1, 1, 1, 1], nums2 = [1, 1, 1, 1]`
- Output: `0`
