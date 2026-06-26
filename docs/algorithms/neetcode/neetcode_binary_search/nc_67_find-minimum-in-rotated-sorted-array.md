## Problem Description & Examples
### Goal
Merge `k` sorted linked lists (as arrays) into one sorted list and return it.

### Function Contract
**Inputs**

- `lists`: List[List[int]] - k sorted lists

**Return value**

List[int] - merged sorted list

### Examples
**Example 1**

- Input: `lists = [[1, 4, 5], [1, 3, 4], [2, 6]]`
- Output: `[1, 1, 2, 3, 4, 4, 5, 6]`

**Example 2**

- Input: `lists = [[50], [98]]`
- Output: `[50, 98]`

**Example 3**

- Input: `lists = [[18], [73]]`
- Output: `[18, 73]`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
