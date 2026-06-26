## Problem Description & Examples
### Goal
Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

### Function Contract
**Inputs**

- `n`: int - range limit
- `k`: int - combination size

**Return value**

List[List[int]] - combinations

### Examples
**Example 1**

- Input: `n = 4, k = 2`
- Output: `[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]`

**Example 2**

- Input: `n = 2, k = 1`
- Output: `[[1], [2]]`

**Example 3**

- Input: `n = 3, k = 2`
- Output: `[[1, 2], [1, 3], [2, 3]]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
