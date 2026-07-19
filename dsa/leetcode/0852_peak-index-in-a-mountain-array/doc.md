# Peak Index in a Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 852 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/) |

## Problem Description
### Goal
You are given an integer mountain array `arr`. Its values are strictly increasing up to one interior peak element and strictly decreasing after that peak, so the peak index is unique. The guarantee excludes flat adjacent values and peaks at either array boundary.

Return the index of the peak element. The solution must exploit the mountain shape and run in logarithmic time rather than scanning the entire array.

### Function Contract
**Inputs**

- `arr`: a guaranteed mountain array of length $n$, where $3 \leq n \leq 10^5$ and $0 \leq \texttt{arr[i]} \leq 10^6$.

**Return value**

Return the unique index at which the strictly increasing prefix changes to the strictly decreasing suffix.

### Examples
**Example 1**

- Input: `arr = [0,1,0]`
- Output: `1`

**Example 2**

- Input: `arr = [0,2,1,0]`
- Output: `1`

**Example 3**

- Input: `arr = [0,10,5,2]`
- Output: `1`
