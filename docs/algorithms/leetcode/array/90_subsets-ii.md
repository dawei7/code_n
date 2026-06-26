# Subsets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_129` |
| Frontend ID | 90 |
| Difficulty | Medium |
| Topics | Array, Backtracking, Bit Manipulation |
| Official Link | [subsets-ii](https://leetcode.com/problems/subsets-ii/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

### Function Contract
**Inputs**

- `nums`: List[int] - duplicates allowed

**Return value**

List[List[int]] - all unique subsets

### Examples
**Example 1**

- Input: `nums = [1, 2, 2]`
- Output: `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`

**Example 2**

- Input: `nums = [4]`
- Output: `[[], [4]]`

**Example 3**

- Input: `nums = [2, 5]`
- Output: `[[], [2], [2, 5], [5]]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
