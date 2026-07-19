# First Missing Positive

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 41 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/first-missing-positive/) |

## Problem Description
### Goal
You are given an unsorted integer array that may contain negative values, zero, positive values, and duplicates. Find the smallest strictly positive integer that does not occur anywhere in the array.

Return that missing value. For an array of length `n`, the answer always lies between `1` and $n + 1$: values outside that range cannot postpone the first gap. The required linear running time and constant auxiliary space mean the array itself must supply any bookkeeping rather than a separate set or sorted copy.

### Function Contract
**Inputs**

- `nums`: `List[int]`

**Return value**

The smallest missing positive `int`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 0]`
- Output: `3`

**Example 2**

- Input: `nums = [3, 4, -1, 1]`
- Output: `2`

**Example 3**

- Input: `nums = [7, 8, 9, 11, 12]`
- Output: `1`
