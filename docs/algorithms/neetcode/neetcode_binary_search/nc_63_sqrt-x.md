## Problem Description & Examples
### Goal
Given a linked list `nodes` with a possible cycle at `cycle_pos`, return the index where the cycle begins, or -1 if no cycle.

### Function Contract
**Inputs**

- `nodes`: List[int]
- `cycle_pos`: int - cycle start index, -1 for none

**Return value**

int - index of cycle start, or -1

### Examples
**Example 1**

- Input: `nodes = [3, 2, 0, -4], cycle_pos = 1`
- Output: `1`

**Example 2**

- Input: `nodes = [-2, 94], cycle_pos = -1`
- Output: `-1`

**Example 3**

- Input: `nodes = [-66, 45], cycle_pos = -1`
- Output: `-1`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
