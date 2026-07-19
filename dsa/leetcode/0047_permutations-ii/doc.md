# Permutations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 47 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/permutations-ii/) |

## Problem Description
### Goal
You are given an integer array `nums` that may contain repeated values. Rearrange all of its positions in every possible way while preserving the original multiplicity of each value.

Return all possible unique permutations in any order. Swapping two equal occurrences does not create a new permutation, so an ordering must not be repeated even when several index-level arrangements produce it. An input whose values are all equal produces exactly one permutation.

### Function Contract
**Inputs**

- `nums`: `List[int]`, possibly containing duplicates

**Return value**

A `List[List[int]]` containing every unique permutation in any order.

### Examples
**Example 1**

- Input: `nums = [1, 1, 2]`
- Output: `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`

**Example 2**

- Input: `nums = [1, 2, 3]`
- Output: all six ordinary permutations

**Example 3**

- Input: `nums = [1, 1]`
- Output: `[[1, 1]]`
