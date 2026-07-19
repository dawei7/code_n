# H-Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 274 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/h-index/) |

## Problem Description
### Goal
Given one nonnegative citation count for each of a researcher's papers, compute the researcher's h-index. An integer `h` is valid when at least `h` papers have received at least `h` citations each.

Return the largest valid `h`. Papers beyond those `h` may have any smaller or larger counts, and citation values above the number of papers do not make the index exceed the paper count. For one paper, the h-index is `1` when it has at least one citation and `0` otherwise. The result is a rank-like integer rather than a citation total or the number of distinct citation values.

### Function Contract
**Inputs**

- `citations`: nonnegative citation counts, one per paper

**Return value**

The researcher's h-index.

### Examples
**Example 1**

- Input: `citations = [3,0,6,1,5]`
- Output: `3`

**Example 2**

- Input: `citations = [1,3,1]`
- Output: `1`

**Example 3**

- Input: `citations = [10,8,5,4,3]`
- Output: `4`
