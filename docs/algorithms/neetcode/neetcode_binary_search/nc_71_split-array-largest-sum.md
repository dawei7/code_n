## Problem Description & Examples
### Goal
Given a linked list (as an array), swap every two adjacent nodes and return the result.

### Function Contract
**Inputs**

- `head`: List[int]

**Return value**

List[int] - list with adjacent pairs swapped

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4]`
- Output: `[2, 1, 4, 3]`

**Example 2**

- Input: `head = [50, 98]`
- Output: `[98, 50]`

**Example 3**

- Input: `head = [18, 73]`
- Output: `[73, 18]`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
