# Flatten a Multilevel Doubly Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 430 |
| Difficulty | Medium |
| Topics | Linked List, Depth-First Search, Doubly-Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) |

## Problem Description
### Goal
Given a multilevel doubly linked list, each node may have `next`, `prev`, and `child` pointers, and a child pointer heads another doubly linked level. Flatten the complete structure in depth-first order, visiting a node's child list before continuing with that node's original next sibling.

Return the original top-level head after rewiring all existing nodes into one doubly linked list. Clear every `child` pointer, make all adjacent `next` and `prev` links reciprocal, preserve each level's order, and reconnect the tail of a flattened child section to the saved next node. Empty input returns `null`.

### Function Contract
**Inputs**

- `nodes`: the app representation of one level as `[value, child_nodes]` entries, recursively, with an empty child list when absent

**Return value**

- Return the first flattened node. Every `child` link must be cleared, `next` and `prev` must be reciprocal, and examples show the complete forward value order.

### Examples
**Example 1**

- Input: `nodes = [[1, []], [2, []], [3, [[7, []], [8, [[11, []], [12, []]]], [9, []], [10, []]]], [4, []], [5, []], [6, []]]`
- Output: `[1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]`

**Example 2**

- Input: `nodes = [[1, [[3, []]]], [2, []]]`
- Output: `[1, 3, 2]`

**Example 3**

- Input: `nodes = []`
- Output: `[]`
