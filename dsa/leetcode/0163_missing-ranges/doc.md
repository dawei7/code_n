# Missing Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 163 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/missing-ranges/) |

## Problem Description
### Goal
You are given inclusive bounds `lower` and `upper` and a sorted array of distinct integers lying within those bounds. Identify every integer in the closed interval `[lower, upper]` that does not appear in the array.

Return the missing values compressed into the smallest ascending list of disjoint inclusive ranges `[start, end]`. Consecutive missing integers belong in one range, while a single isolated value is represented with equal endpoints. Include gaps before the first array value and after the last one, and return an empty list when the input already covers the entire bounded interval.

### Function Contract
**Inputs**

- `nums`: sorted distinct integers, each within `[lower, upper]`
- `lower`: inclusive lower bound
- `upper`: inclusive upper bound

**Return value**

A list of inclusive ranges `[start, end]` covering exactly the missing values in ascending order.

### Examples
**Example 1**

- Input: `nums = [0,1,3,50,75], lower = 0, upper = 99`
- Output: `[[2,2],[4,49],[51,74],[76,99]]`

**Example 2**

- Input: `nums = [-1], lower = -1, upper = -1`
- Output: `[]`

**Example 3**

- Input: `nums = [], lower = 1, upper = 1`
- Output: `[[1,1]]`
