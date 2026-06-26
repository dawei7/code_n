# Design Front Middle Back Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1670 |
| Difficulty | Medium |
| Topics | Array, Linked List, Design, Queue, Doubly-Linked List, Data Stream |
| Official Link | [design-front-middle-back-queue](https://leetcode.com/problems/design-front-middle-back-queue/) |

## Problem Description & Examples
### Goal
Design a queue that supports inserting and removing at the front, middle, and back. When there are two middle positions, the frontmost middle is used for removal, and insertion goes before the back middle.

### Function Contract
**Inputs**

- A sequence of operations on `FrontMiddleBackQueue`.
- Push operations receive one integer value.

**Return value**

Return the result of each operation: `null` for pushes and constructor calls, the removed value for pops, or `-1` when popping from an empty queue.

### Examples
**Example 1**

- Input: `["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]`, `[[],[1],[2],[3],[4],[],[],[],[],[]]`
- Output: `[null,null,null,null,null,1,3,4,2,-1]`

**Example 2**

- Input: `["FrontMiddleBackQueue","pushBack","pushBack","pushBack","popMiddle","popMiddle","popMiddle"]`, `[[],[1],[2],[3],[],[],[]]`
- Output: `[null,null,null,null,2,1,3]`

**Example 3**

- Input: `["FrontMiddleBackQueue","pushMiddle","pushMiddle","pushFront","pushBack","popFront","popBack","popMiddle"]`, `[[],[1],[2],[3],[4],[],[],[]]`
- Output: `[null,null,null,null,null,3,4,2]`

---

## Underlying Base Algorithm(s)
Maintain two balanced deques: the left half and the right half. Keep `len(left)` equal to `len(right)` or exactly one larger. Front operations touch `left`, back operations touch `right`, middle operations use the end of `left`, and a small rebalance after every mutation restores the invariant.

---

## Complexity Analysis
- **Time Complexity**: `O(1)` per operation
- **Space Complexity**: `O(n)`
