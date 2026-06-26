## Problem Description & Examples
### Goal
Given the head of a linked list, determine if the linked list has a cycle. The linked list is represented as a list `nodes` where `nodes[i]` is the value at position `i`, and `cycle_pos` is the index where the tail connects back (-1 if no cycle).

`solve(nodes, cycle_pos)` returns `True` if there's a cycle.

### Function Contract
**Inputs**

- `nodes`: List[int]
- `cycle_pos`: int - tail connects to this index (-1 for no cycle)

**Return value**

bool - True if cycle exists

### Examples
**Example 1**

- Input: `nodes = [3, 2, 0, -4], cycle_pos = 1`
- Output: `True`

**Example 2**

- Input: `nodes = [-2], cycle_pos = -1`
- Output: `False`

**Example 3**

- Input: `nodes = [-66, 45], cycle_pos = -1`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
