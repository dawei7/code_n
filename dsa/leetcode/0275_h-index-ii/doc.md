# H-Index II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 275 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/h-index-ii/) |

## Problem Description
### Goal
Given nonnegative citation counts already sorted in ascending order, compute the researcher's h-index. A value `h` is valid when at least `h` papers have citation counts greater than or equal to `h`.

Return the largest valid `h`, bounded by the number of papers rather than by the largest citation count. Use the supplied sorted order to meet the required logarithmic running time, locating the boundary where the number of remaining papers can be supported by their citation values. For one paper, the result is `1` when it has at least one citation and `0` otherwise; duplicate citation counts occupy separate paper positions.

### Function Contract
**Inputs**

- `citations`: sorted nonnegative citation counts

**Return value**

The largest `h` for which at least `h` papers have at least `h` citations.

### Examples
**Example 1**

- Input: `citations = [0,1,3,5,6]`
- Output: `3`

**Example 2**

- Input: `citations = [1,2,100]`
- Output: `2`

**Example 3**

- Input: `citations = []`
- Output: `0`
