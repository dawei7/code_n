# Combination Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 39 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/combination-sum/) |

## Problem Description
### Goal
You are given distinct positive candidate values and a positive target. Build combinations whose values add exactly to the target. The same candidate may be chosen an unlimited number of times, so one value can contribute multiple copies to one combination.

Return every unique value combination and no others. Two combinations are unique when the frequency of at least one chosen number differs; reordering the same selections does not create another answer. The collection and each combination may be returned in any order. When no selection reaches the target, return an empty list.

### Function Contract
**Inputs**

- `candidates`: `List[int]` of distinct positive integers
- `target`: positive `int`

**Return value**

A `List[List[int]]` containing all unique target-sum combinations in any order.

### Examples
**Example 1**

- Input: `candidates = [2, 3, 6, 7], target = 7`
- Output: `[[2, 2, 3], [7]]`

**Example 2**

- Input: `candidates = [2, 3, 5], target = 8`
- Output: `[[2, 2, 2, 2], [2, 3, 3], [3, 5]]`

**Example 3**

- Input: `candidates = [2], target = 1`
- Output: `[]`
