# Combination Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 40 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/combination-sum-ii/) |

## Problem Description
### Goal
You are given positive candidate values, possibly including duplicates, and a positive target. Choose a subset of array positions whose values add exactly to the target. Each position may be used at most once, even when several positions store the same number.

Return every unique combination of values. Different index selections that produce the same multiset count as one answer, and value order does not distinguish combinations. The result collection may use any order. If no subset reaches the target, return an empty list.

### Function Contract
**Inputs**

- `candidates`: `List[int]` of positive integers, possibly with duplicates
- `target`: positive `int`

**Return value**

A `List[List[int]]` containing all unique target-sum combinations in any order.

### Examples
**Example 1**

- Input: `candidates = [10, 1, 2, 7, 6, 1, 5], target = 8`
- Output: `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]`

**Example 2**

- Input: `candidates = [2, 5, 2, 1, 2], target = 5`
- Output: `[[1, 2, 2], [5]]`

**Example 3**

- Input: `candidates = [7, 7], target = 4`
- Output: `[]`
