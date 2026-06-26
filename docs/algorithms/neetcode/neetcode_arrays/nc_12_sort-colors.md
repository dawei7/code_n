## Problem Description & Examples
### Goal
Given an array `nums` with only values `0`, `1`, and `2`, sort them in-place so that all 0s come first, then 1s, then 2s. (Dutch National Flag problem)

### Function Contract
**Inputs**

- `nums`: List[int] - contains only 0, 1, 2

**Return value**

None (in-place), final state of nums is checked

### Examples
**Example 1**

- Input: `nums = [2, 0, 2, 1, 1, 0]`
- Output: `[0, 0, 1, 1, 2, 2]`

**Example 2**

- Input: `nums = [1]`
- Output: `[1]`

**Example 3**

- Input: `nums = [0, 2]`
- Output: `[0, 2]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
