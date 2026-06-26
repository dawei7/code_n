# Permutations

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_128` |
| Frontend ID | 46 |
| Difficulty | Medium |
| Topics | Array, Backtracking |
| Official Link | [permutations](https://leetcode.com/problems/permutations/) |

## Problem Description & Examples
### Goal
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

### Function Contract
**Inputs**

- `nums`: List[int] - distinct integers

**Return value**

List[List[int]] - all permutations

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

**Example 2**

- Input: `nums = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `nums = [1, 2]`
- Output: `[[1, 2], [2, 1]]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
