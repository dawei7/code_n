# Merge Nodes in Between Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2181 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-nodes-in-between-zeros/) |

## Problem Description

### Goal

A singly linked list contains positive values arranged into groups separated
by nodes whose value is `0`. The first and last nodes are both separators, and
no two zero-valued nodes are adjacent, so every pair of consecutive separators
encloses a nonempty group.

Replace all nodes strictly between each pair of consecutive zero-valued nodes
with one node holding that group's sum. Preserve the groups' original order,
remove every separator from the result, and return the head of the modified
linked list.

### Function Contract

**Inputs**

- `head`: the head node of the linked list; authored cases display the chain as
  an array of node values.

The list contains between $3$ and $2\cdot10^5$ nodes. Every node value is in
$[0,1000]`; the endpoints are zero, interior zeros are not adjacent, and all
values between separators are positive.

**Return value**

Return the head node of the modified list of group sums in their original
left-to-right order, with no zero separators.

### Examples

#### Example 1

- **Input:** `head = [0,3,1,0,4,5,2,0]`
- **Output:** `[4,11]`

#### Example 2

- **Input:** `head = [0,1,0,3,0,2,2,0]`
- **Output:** `[1,3,4]`

#### Example 3

- **Input:** `head = [0,5,0]`
- **Output:** `[5]`
