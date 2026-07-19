# Partition List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 86 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-list/) |

## Problem Description
### Goal
You are given a singly linked list and a partition value `x`. Rearrange its nodes so every node with value less than `x` appears before every node whose value is at least `x`.

The partition must be stable: nodes within the lower group retain their original relative order, and nodes within the upper group do the same. Return the new head after relinking the existing nodes. Values equal to `x` belong to the second group, and either group may be empty.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases; it may be empty
- `x`: the partition value

**Return value**

The partitioned linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1,4,3,2,5,2], x = 3`
- Output: `[1,2,2,4,3,5]`

**Example 2**

- Input: `head = [2,1], x = 2`
- Output: `[1,2]`

**Example 3**

- Input: `head = [], x = 0`
- Output: `[]`
