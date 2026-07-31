# Find the Count of Monotonic Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3251 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/) |

## Problem Description

### Goal

For a positive integer array `nums` of length $n$, consider two arrays `arr1` and `arr2` of the same length whose entries are non-negative integers. They form a monotonic pair only when `arr1` is non-decreasing, `arr2` is non-increasing, and their entries at every index add to the supplied value: `arr1[i] + arr2[i] == nums[i]`.

Count every distinct pair satisfying all of these conditions. Because the number of decompositions may be large, return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 2000$ and $1 \le \texttt{nums[i]} \le 1000$.

Let $m=\max(\texttt{nums})$.

**Return value**

- The number of monotonic pairs `(arr1, arr2)`, modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [2,3,2]`
- Output: `4`

The four first arrays are `[0,1,1]`, `[0,1,2]`, `[0,2,2]`, and `[1,2,2]`; subtracting each entrywise from `nums` gives its unique second array.

**Example 2**

- Input: `nums = [5,5,5,5]`
- Output: `126`

**Example 3**

- Input: `nums = [1]`
- Output: `2`

The valid pairs are `([0],[1])` and `([1],[0])`.
