# Combination Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_126` |
| Frontend ID | 40 |
| Difficulty | Medium |
| Topics | Array, Backtracking |
| Official Link | [combination-sum-ii](https://leetcode.com/problems/combination-sum-ii/) |

## Problem Description & Examples
### Goal
Given a collection of candidate numbers `candidates` and a target number `target`, find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. Note: The solution set must not contain duplicate combinations.

### Function Contract
**Inputs**

- `candidates`: List[int]
- `target`: int

**Return value**

List[List[int]] - unique combinations

### Examples
**Example 1**

- Input: `candidates = [10, 1, 2, 7, 6, 1, 5], target = 8`
- Output: `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]`

**Example 2**

- Input: `candidates = [7, 7], target = 4`
- Output: `[]`

**Example 3**

- Input: `candidates = [2, 3], target = 8`
- Output: `[]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
