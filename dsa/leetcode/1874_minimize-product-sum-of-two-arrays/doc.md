# Minimize Product Sum of Two Arrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimize-product-sum-of-two-arrays/) |
| Frontend ID | 1874 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The product sum of two arrays of equal length is the sum of the products at corresponding indices. For example, arrays `[1,2,3,4]` and `[5,2,3,1]` have product sum `1*5 + 2*2 + 3*3 + 4*1`.

Given positive integer arrays `nums1` and `nums2`, you may rearrange the elements of `nums1` in any order while `nums2` supplies the positions to which those values are assigned. Return the smallest product sum obtainable over all such rearrangements. Duplicate values are distinct occurrences and must all be used exactly once.

### Function Contract

**Inputs**

- `nums1`, `nums2`: positive integer arrays of the same length $N$, where $1 \le N \le 10^5$ and every value is at most $100$.

**Return value**

- Return the minimum possible value of $\sum_{i=0}^{N-1}\texttt{nums1[i]}\texttt{nums2[i]}$ after arbitrarily permuting `nums1`.

### Examples

**Example 1**

- Input: `nums1 = [5,3,4,2], nums2 = [4,2,2,5]`
- Output: `40`

Pairing the values as `[3,5,4,2]` against `nums2` yields `12 + 10 + 8 + 10`.

**Example 2**

- Input: `nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]`
- Output: `65`

The largest first-array values are assigned to the smallest second-array values.

**Example 3**

- Input: `nums1 = [7], nums2 = [9]`
- Output: `63`

With one element, there is only one possible pairing.
