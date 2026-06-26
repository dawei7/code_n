## Problem Description & Examples
### Goal
Given an array `nums` of `n` integers and an integer `target`, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that they sum to `target`.

### Function Contract
**Inputs**

- `nums`: List[int]
- `target`: int

**Return value**

List[List[int]] - unique quadruplets summing to target

### Examples
**Example 1**

- Input: `nums = [1, 0, -1, 0, -2, 2], target = 0`
- Output: `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`

**Example 2**

- Input: `nums = [-9, -2, 2, 3], target = 12`
- Output: `[]`

**Example 3**

- Input: `nums = [-8, -6, -2, 8], target = -13`
- Output: `[]`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^3)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
