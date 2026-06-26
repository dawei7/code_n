## Problem Description & Examples
### Goal
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`. No duplicate triplets.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

List[List[int]] - unique triplets summing to zero

### Examples
**Example 1**

- Input: `nums = [-1, 0, 1, 2, -1, -4]`
- Output: `[[-1, -1, 2], [-1, 0, 1]]`

**Example 2**

- Input: `nums = [-9, 2, 3]`
- Output: `[]`

**Example 3**

- Input: `nums = [-8, -6, 8]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
