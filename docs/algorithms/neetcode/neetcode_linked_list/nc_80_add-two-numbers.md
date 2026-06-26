## Problem Description & Examples
### Goal
Given a linked list (as array) and integer `k`, reverse every `k` consecutive nodes. If there are fewer than k nodes remaining, leave them as-is.

### Function Contract
**Inputs**

- `head`: List[int]
- `k`: int - group size

**Return value**

List[int] - list with k-groups reversed

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5], k = 2`
- Output: `[2, 1, 4, 3, 5]`

**Example 2**

- Input: `head = [50, 98], k = 2`
- Output: `[98, 50]`

**Example 3**

- Input: `head = [18, 73], k = 1`
- Output: `[18, 73]`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
