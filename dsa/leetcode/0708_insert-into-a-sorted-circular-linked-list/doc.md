# Insert into a Sorted Circular Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 708 |
| Difficulty | Medium |
| Topics | Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) |

## Problem Description
### Goal
Given a node from a circular singly linked list whose values are sorted in non-decreasing cyclic order, insert one new node containing `insertVal`. The supplied `head` may point to any position in the cycle, not necessarily its minimum value.

Preserve the circular links and sorted cyclic order, then return the original `head`. If the input is empty, create and return a new node that points to itself. When equal values or several insertion locations make more than one result valid, any placement that preserves the required order is acceptable.

### Function Contract
**Inputs**

- `head`: the head node of a sorted circular linked list; cases encode the cycle as `{"values": [...], "pos": 0}`
- `insertVal`: the value for the new node

**Return value**

- The head node of the circular linked list after inserting exactly one node; an empty input returns the new self-linked node

### Examples
**Example 1**

- Input: `head = [3,4,1], insertVal = 2`
- Output: `[3,4,1,2]`

**Example 2**

- Input: `head = [], insertVal = 1`
- Output: `[1]`

**Example 3**

- Input: `head = [1], insertVal = 0`
- Output: `[1,0]`
