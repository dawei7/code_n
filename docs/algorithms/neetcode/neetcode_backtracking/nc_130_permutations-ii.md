## Problem Description & Examples
### Goal
Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.

### Function Contract
**Inputs**

- `nums`: List[int] - duplicates allowed

**Return value**

List[List[int]] - all unique permutations

### Examples
**Example 1**

- Input: `nums = [1, 1, 2]`
- Output: `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`

**Example 2**

- Input: `nums = [2]`
- Output: `[[2]]`

**Example 3**

- Input: `nums = [1, 3]`
- Output: `[[1, 3], [3, 1]]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
