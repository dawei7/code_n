# Minimum Absolute Sum Difference

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-absolute-sum-difference/) |
| Frontend ID | 1818 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two positive-integer arrays `nums1` and `nums2` have the same length. Their absolute sum difference is obtained by adding $\lvert\texttt{nums1[i]}-\texttt{nums2[i]}\rvert$ over every corresponding index.

You may change at most one position of `nums1`. If you make a change, the replacement value must equal some value that occurs anywhere in the original `nums1`; choosing the value from another position does not remove or alter that source position. Minimize the absolute sum difference after this optional replacement and return the minimum modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums1`: an array of $n$ positive integers, each between 1 and $10^5$.
- `nums2`: an array of the same length, with values in the same range.
- The common length satisfies $1 \le n \le 10^5$.

**Return value**

- Return the smallest attainable sum of corresponding absolute differences after at most one permitted replacement in `nums1`, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums1 = [1,7,5], nums2 = [2,3,5]`
- Output: `3`

Replacing `7` with either `1` or `5` reduces its difference from 4 to 2.

**Example 2**

- Input: `nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]`
- Output: `0`

The arrays already match, so the optional replacement is unnecessary.

**Example 3**

- Input: `nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]`
- Output: `20`

Replacing the first value `1` with the available value `10` gives the optimal reduction.
