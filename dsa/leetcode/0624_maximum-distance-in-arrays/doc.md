# Maximum Distance in Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 624 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-distance-in-arrays/) |

## Problem Description
### Goal
You are given at least two integer arrays, each sorted in ascending order. Choose one integer from one array and a second integer from a different array; the two selected values may not come from the same input array.

Define the distance between integers `a` and `b` as their absolute difference $| a - b |$. Return the maximum distance obtainable from any valid choice of two arrays and values. The arrays may contain negative values, duplicate values, or only one element.

### Function Contract
**Inputs**

- `arrays`: at least two nonempty integer arrays, each sorted in ascending order

**Return value**

- The maximum absolute difference between values selected from different input arrays

### Examples
**Example 1**

- Input: `arrays = [[1,2,3],[4,5],[1,2,3]]`
- Output: `4`

**Example 2**

- Input: `arrays = [[1],[1]]`
- Output: `0`
