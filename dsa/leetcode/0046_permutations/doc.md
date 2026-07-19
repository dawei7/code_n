# Permutations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 46 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/permutations/) |

## Problem Description
### Goal
You are given an array `nums` whose integers are all unique. A permutation is an ordering that contains every input value exactly once and introduces no additional values.

Return the complete collection of permutations. For `n` values there are $n!$ results, and each distinct ordering must appear once. The permutations and the collection itself may be listed in any order. A one-element input has one permutation containing that element.

### Function Contract
**Inputs**

- `nums`: `List[int]` of distinct values

**Return value**

A `List[List[int]]` containing all $n!$ permutations.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

**Example 2**

- Input: `nums = [0, 1]`
- Output: `[[0, 1], [1, 0]]`

**Example 3**

- Input: `nums = [1]`
- Output: `[[1]]`
