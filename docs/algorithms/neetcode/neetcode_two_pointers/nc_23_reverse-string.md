## Problem Description & Examples
### Goal
Given a **1-indexed** sorted array `numbers`, find two numbers such that they add up to `target`. Return their indices as `[index1, index2]` (1-indexed). Each input has exactly one solution.

### Function Contract
**Inputs**

- `numbers`: List[int] (sorted)
- `target`: int

**Return value**

List[int] - 1-indexed positions of the two elements

### Examples
**Example 1**

- Input: `numbers = [2, 7, 11, 15], target = 9`
- Output: `[1, 2]`

**Example 2**

- Input: `numbers = [2, 3, 4], target = 6`
- Output: `[1, 3]`

**Example 3**

- Input: `numbers = [-1, 0], target = -1`
- Output: `[1, 2]`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
