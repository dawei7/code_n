## Problem Description & Examples
### Goal
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

### Function Contract
**Inputs**

- `nums`: List[int] - unique integers

**Return value**

List[List[int]] - all subsets

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`

**Example 2**

- Input: `nums = [25]`
- Output: `[[], [25]]`

**Example 3**

- Input: `nums = [9, 37]`
- Output: `[[], [9], [9, 37], [37]]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
