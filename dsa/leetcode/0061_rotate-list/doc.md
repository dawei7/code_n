# Rotate List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 61 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rotate-list/) |

## Problem Description
### Goal
You are given the head of a singly linked list and a nonnegative integer `k`. One right rotation removes the final node and places that same node before the former head, leaving the cyclic order of all nodes otherwise unchanged.

Apply this operation `k` times and return the resulting head. Rotation counts larger than the list length wrap around, so only `k` modulo the length affects a nonempty list. Do not reorder values independently of their nodes. Empty and one-node lists remain unchanged for every `k`.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases; it may be empty
- `k`: a nonnegative rotation count

**Return value**

The resulting linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1,2,3,4,5], k = 2`
- Output: `[4,5,1,2,3]`

**Example 2**

- Input: `head = [0,1,2], k = 4`
- Output: `[2,0,1]`

**Example 3**

- Input: `head = [], k = 7`
- Output: `[]`
