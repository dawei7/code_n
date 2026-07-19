# Design Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 707 |
| Difficulty | Medium |
| Topics | Linked List, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/design-linked-list/) |

## Problem Description
### Goal
Design a zero-indexed linked list, using either singly linked or doubly linked nodes. Support `get(index)`, `addAtHead(val)`, `addAtTail(val)`, `addAtIndex(index, val)`, and `deleteAtIndex(index)` while preserving the list across calls.

`get` returns `-1` for an invalid index. Indexed insertion places the new node before the current node at that index, appends when the index equals the length, and does nothing when the index is greater than the length; a negative index inserts at the head. Indexed deletion removes a node only when its index is valid.

### Function Contract
**Inputs**

- `operations`: ordered method calls named `get`, `addAtHead`, `addAtTail`, `addAtIndex`, or `deleteAtIndex`, followed by their integer arguments

**Return value**

- A list containing each `get` result in operation order; invalid indices return `-1`

### Examples
**Example 1**

- Input: `operations = [["addAtHead",1],["addAtTail",3],["addAtIndex",1,2],["get",1],["deleteAtIndex",1],["get",1]]`
- Output: `[2,3]`

**Example 2**

- Input: `operations = [["get",0],["addAtHead",4],["get",0]]`
- Output: `[-1,4]`

**Example 3**

- Input: `operations = [["addAtTail",1],["addAtIndex",5,9],["get",1]]`
- Output: `[-1]`
