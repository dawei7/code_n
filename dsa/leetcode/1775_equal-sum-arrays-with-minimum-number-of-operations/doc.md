# Equal Sum Arrays With Minimum Number of Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1775 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/) |

## Problem Description

### Goal

You are given two integer arrays, `nums1` and `nums2`, which may have different lengths. Every value in both arrays is between `1` and `6`, inclusive.

One operation selects any single element from either array and replaces it with any value from `1` through `6`. Determine the minimum number of operations needed to make the sum of `nums1` equal to the sum of `nums2`. If no sequence of permitted replacements can make the sums equal, return `-1`.

### Function Contract

**Inputs**

- `nums1`: the first array of values in the inclusive range $[1,6]$, with length $n$.
- `nums2`: the second array of values in the inclusive range $[1,6]$, with length $m$.
- The constraints guarantee $1 \le n,m \le 10^5$.

**Return value**

Return the fewest single-element replacements that make the array sums equal, or `-1` when equality is impossible.

### Examples

**Example 1**

- Input: `nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]`
- Output: `3`
- Explanation: Three replacements can close the sum difference; no two replacements have enough combined effect.

**Example 2**

- Input: `nums1 = [1,1,1,1,1,1,1], nums2 = [6]`
- Output: `-1`
- Explanation: Even the smallest possible sum of the seven-element array exceeds the largest possible sum of the one-element array.

**Example 3**

- Input: `nums1 = [6,6], nums2 = [1]`
- Output: `3`
- Explanation: Three replacements are necessary and sufficient to bring the sums together.
