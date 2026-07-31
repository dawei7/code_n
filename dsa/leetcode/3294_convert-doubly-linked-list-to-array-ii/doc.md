# Convert Doubly Linked List to Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3294 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Doubly-Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/) |

## Problem Description

### Goal

You receive an arbitrary node from a nonempty doubly linked list. Every node stores an integer together with `prev` and `next` pointers, so the supplied node may be the head, the tail, or somewhere in the middle.

Return an integer array containing every list value in its original head-to-tail order. Reaching only nodes after the supplied node is insufficient: the result must begin at the actual head and include the entire list through its tail.

### Function Contract

**Inputs**

- `node`: Any node belonging to the doubly linked list.

The list contains from 1 through 500 nodes. Each value is between 1 and 1000, and all node values are unique.

In JSON cases, `node` is encoded as `{"values": [...], "node_index": k}`: `values` gives the head-to-tail list and `node_index` selects the supplied node.

**Return value**

- A list of all node values in head-to-tail order.

### Examples

**Example 1**

- Input: list `[1,2,3,4,5]`, supplied node value `5`
- Output: `[1,2,3,4,5]`

**Example 2**

- Input: list `[4,5,6,7,8]`, supplied node value `8`
- Output: `[4,5,6,7,8]`
