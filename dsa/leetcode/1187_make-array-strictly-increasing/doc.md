# Make Array Strictly Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1187 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-array-strictly-increasing/) |

## Problem Description

### Goal

You are given two integer arrays, `arr1` and `arr2`. An operation chooses indices `i` and `j` within their respective arrays and performs the assignment `arr1[i] = arr2[j]`. The chosen value is not removed from `arr2`, so any index there remains available for later operations.

Find the minimum number of operations, possibly zero, needed to make `arr1` strictly increasing: every element must be greater than the element immediately before it. Return `-1` if no sequence of allowed assignments can produce such an array.

### Function Contract

**Inputs**

- `arr1`: A list of length $n$, where $1\le n\le2000$ and $0\le\texttt{arr1[i]}\le10^9$.
- `arr2`: A list of length $m$, where $1\le m\le2000$ and $0\le\texttt{arr2[j]}\le10^9$.

**Return value**

- The minimum number of assignments required to make `arr1` strictly increasing, or `-1` when it is impossible.

### Examples

**Example 1**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [1,3,2,4]`
- Output: `1`

Replace `arr1[1]` with `2` to obtain `[1,2,3,6,7]`.

**Example 2**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [4,3,1]`
- Output: `2`

Replacing the two middle values produces `[1,3,4,6,7]`.

**Example 3**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [1,6,3,3]`
- Output: `-1`
