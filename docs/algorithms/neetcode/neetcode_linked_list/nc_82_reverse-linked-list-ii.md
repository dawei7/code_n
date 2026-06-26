## Problem Description & Examples
### Goal
Design an LRU (Least Recently Used) cache with capacity `cap`. Process operations `["get", key]` and `["put", key, value]`.

- `get(key)` returns the value or -1 if not present (moves to most recently used).
- `put(key, value)` inserts/updates; evicts least recently used if over capacity.

`solve(cap, operations)` returns results of all `get` operations.

### Function Contract
**Inputs**

- `cap`: int - cache capacity
- `operations`: List[List] - get/put operations

**Return value**

List[int] - results of get operations

### Examples
**Example 1**

- Input: `cap = 2, ops = [put(1, 1), put(2, 2), get(1), put(3, 3), get(2)]`
- Output: `[1, -1]`

**Example 2**

- Input: `cap = 2, operations = [['put', 4, 66], ['put', 4, 39], ['put', 4, 28], ['put', 5, 18]]`
- Output: `[]`

**Example 3**

- Input: `cap = 1, operations = [['get', 3], ['put', 1, 64], ['put', 2, 49], ['put', 1, 4]]`
- Output: `[-1]`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
