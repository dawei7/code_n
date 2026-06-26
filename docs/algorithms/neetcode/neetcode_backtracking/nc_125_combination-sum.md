## Problem Description & Examples
### Goal
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order. The same number may be chosen from `candidates` an unlimited number of times.

### Function Contract
**Inputs**

- `candidates`: List[int] - distinct integers
- `target`: int

**Return value**

List[List[int]] - unique combinations

### Examples
**Example 1**

- Input: `candidates = [2, 3, 6, 7], target = 7`
- Output: `[[2, 2, 3], [7]]`

**Example 2**

- Input: `candidates = [8], target = 5`
- Output: `[]`

**Example 3**

- Input: `candidates = [3, 4], target = 9`
- Output: `[[3, 3, 3]]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
