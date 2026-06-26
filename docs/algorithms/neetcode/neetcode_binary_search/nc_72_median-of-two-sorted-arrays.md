## Problem Description & Examples
### Goal
Given a linked list (as an array) and an integer `k`, rotate the list to the right by `k` places.

### Function Contract
**Inputs**

- `head`: List[int]
- `k`: int

**Return value**

List[int] - rotated list

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5], k = 2`
- Output: `[4, 5, 1, 2, 3]`

**Example 2**

- Input: `head = [50, 98], k = 1`
- Output: `[98, 50]`

**Example 3**

- Input: `head = [18, 73], k = 0`
- Output: `[18, 73]`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
