## Problem Description & Examples
### Goal
Given a singly linked list as an array of values `head`, reverse it and return the reversed list.

### Function Contract
**Inputs**

- `head`: List[int] - linked list values

**Return value**

List[int] - reversed list

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5]`
- Output: `[5, 4, 3, 2, 1]`

**Example 2**

- Input: `head = [50]`
- Output: `[50]`

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
