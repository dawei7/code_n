## Problem Description & Examples
### Goal
Given a rotated sorted array `nums` that may contain **duplicates**, and a `target`, return `True` if target exists.

### Function Contract
**Inputs**

- `nums`: List[int] - rotated sorted, may have duplicates
- `target`: int

**Return value**

bool - True if target found

### Examples
**Example 1**

- Input: `nums = [2, 5, 6, 0, 0, 1, 2], target = 0`
- Output: `True`

**Example 2**

- Input: `nums = [6, 6, 0], target = 7`
- Output: `False`

**Example 3**

- Input: `nums = [2, 9, 1], target = 9`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
