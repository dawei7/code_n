# Count of Range Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 327 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-range-sum/) |

## Problem Description
### Goal
Given an integer array and bounds `lower <= upper`, consider every nonempty contiguous subarray. A subarray qualifies when the sum of all its elements lies within the inclusive interval `[lower, upper]`.

Return the number of qualifying index intervals. Different start or end positions count separately even when their values or sums are equal, and sums exactly at either boundary are included. Negative values and zero prevent simple monotone-window reasoning. The answer is a count rather than a list of ranges, and the required solution must avoid enumerating and summing all quadratic subarrays independently.

### Function Contract
**Inputs**

- `nums`: the integer array
- `lower`: the inclusive lower sum bound
- `upper`: the inclusive upper sum bound

**Return value**

The number of index pairs defining a contiguous subarray with sum between the two bounds, inclusive.

### Examples
**Example 1**

- Input: `nums = [-2,5,-1], lower = -2, upper = 2`
- Output: `3`

**Example 2**

- Input: `nums = [0], lower = 0, upper = 0`
- Output: `1`

**Example 3**

- Input: `nums = [1], lower = 0, upper = 0`
- Output: `0`
