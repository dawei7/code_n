## Problem Description & Examples
### Goal
Given a linked list where each node has a `val`, a `next` pointer, and a `random` pointer to a random node (or None), deep copy it.

Represent the list as `nodes = [[val, random_idx], ...]` where `random_idx` is the 0-indexed position of the random pointer (or -1). Return the same structure.

### Function Contract
**Inputs**

- `nodes`: List[List] - [[val, random_idx], ...]

**Return value**

List[List] - deep copy with same structure

### Examples
**Example 1**

- Input: `nodes = [[7, -1], [13, 0]]`
- Output: `[[7, -1], [13, 0]]`

**Example 2**

- Input: `nodes = [[50, 0]]`
- Output: `[[50, 0]]`

**Example 3**

- Input: `nodes = [[18, -1], [73, 0]]`
- Output: `[[18, -1], [73, 0]]`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
