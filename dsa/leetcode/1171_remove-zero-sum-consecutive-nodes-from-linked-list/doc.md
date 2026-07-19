# Remove Zero Sum Consecutive Nodes from Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1171 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) |

## Problem Description

### Goal

You are given the `head` of a singly linked list whose nodes contain integers. Repeatedly choose a consecutive sequence of nodes whose values sum to zero and remove that entire sequence from the list. A removal may join nodes that were previously separated, so it can expose another zero-sum consecutive sequence that must also be eligible for removal.

Continue until the list contains no consecutive sequence with sum zero, then return its head. If more than one sequence can be removed at some stage, any final list obtainable by valid repeated removals is accepted.

### Function Contract

**Inputs**

- `head`: The first node of a singly linked list containing between $1$ and $1000$ nodes.
- Every node value is between $-1000$ and $1000$, inclusive.
- Let $n$ be the number of nodes in the input list.

**Return value**

- The head node of the resulting linked list after repeated zero-sum removals. Return `None` if all nodes are removed.

### Examples

**Example 1**

- Input: `head = [1,2,-3,3,1]`
- Output: `[3,1]`

Removing `[1,2,-3]` leaves `[3,1]`. The list `[1,2,1]` is another accepted result because removing `[-3,3]` is also valid.

**Example 2**

- Input: `head = [1,2,3,-3,4]`
- Output: `[1,2,4]`

**Example 3**

- Input: `head = [1,2,3,-3,-2]`
- Output: `[1]`
