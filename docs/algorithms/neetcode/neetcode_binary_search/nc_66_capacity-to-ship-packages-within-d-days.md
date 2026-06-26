## Problem Description & Examples
### Goal
Merge two sorted linked lists (as arrays) and return a sorted merged list.

### Function Contract
**Inputs**

- `list1`: List[int] (sorted)
- `list2`: List[int] (sorted)

**Return value**

List[int] - merged sorted list

### Examples
**Example 1**

- Input: `list1 = [1, 2, 4], list2 = [1, 3, 4]`
- Output: `[1, 1, 2, 3, 4, 4]`

**Example 2**

- Input: `list1 = [50], list2 = [98]`
- Output: `[50, 98]`

**Example 3**

- Input: `list1 = [18], list2 = [73]`
- Output: `[18, 73]`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
