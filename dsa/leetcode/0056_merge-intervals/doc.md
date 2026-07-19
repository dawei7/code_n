# Merge Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 56 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-intervals/) |

## Problem Description
### Goal
You are given a nonempty collection of closed intervals `[start, end]`. Two intervals are overlapping when they share at least one point, including touching at an endpoint, and a chain of overlaps connects all intervals in that chain.

Merge every connected overlap group into its smallest covering interval. Return the resulting non-overlapping intervals in ascending start order while covering exactly the same points as the input collection. Input intervals need not initially be sorted.

### Function Contract
**Inputs**

- `intervals`: a nonempty `List[List[int]]`, where each item is `[start, end]` and `start <= end`

**Return value**

A list of the merged nonoverlapping intervals in ascending start order.

### Examples
**Example 1**

- Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`
- Output: `[[1,6],[8,10],[15,18]]`

**Example 2**

- Input: `intervals = [[1,4],[4,5]]`
- Output: `[[1,5]]`

**Example 3**

- Input: `intervals = [[5,7]]`
- Output: `[[5,7]]`
