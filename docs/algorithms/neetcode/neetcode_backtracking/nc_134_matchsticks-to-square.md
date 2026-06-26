## Problem Description & Examples
### Goal
You are given an integer array `matchsticks` where `matchsticks[i]` is the length of the `i`-th matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly once. Return `True` if you can make this square and `False` otherwise.

### Function Contract
**Inputs**

- `matchsticks`: List[int]

**Return value**

bool - True if a square can be formed

### Examples
**Example 1**

- Input: `matchsticks = [1, 1, 2, 2, 2]`
- Output: `True`

**Example 2**

- Input: `matchsticks = [4, 1, 3, 5]`
- Output: `False`

**Example 3**

- Input: `matchsticks = [2, 2, 2, 1, 1]`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
