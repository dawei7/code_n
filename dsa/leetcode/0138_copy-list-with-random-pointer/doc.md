# Copy List with Random Pointer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 138 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/) |

## Problem Description
### Goal
Given a linked list, each node contains a value, a `next` pointer, and a `random` pointer that may refer to any node in the same list or to `null`. Random links may point forward, backward, to the node itself, or cause repeated references that do not follow list order.

Create a deep copy with one new node for each original node. Both pointer relationships must connect the corresponding clones exactly as in the source, and no pointer in the copied list may refer to an original node. Return the copied head, or `null` for an empty list. The app encoding uses `[value, random_index]` pairs while preserving these same identity relationships.

### Function Contract
**Inputs**

- `nodes`: the app encoding in next-pointer order as `[value, random_index]` pairs, where `random_index` is zero-based or `null`

**Return value**

A structurally independent copy of the encoded list. The native LeetCode artifact clones `Node` objects and both pointer types.

### Examples
**Example 1**

- Input: `nodes = [[7,null],[13,0],[11,4],[10,2],[1,0]]`
- Output: the same encoded values and random targets in newly allocated nodes

**Example 2**

- Input: `nodes = [[1,1],[2,1]]`
- Output: `[[1,1],[2,1]]`

**Example 3**

- Input: `nodes = []`
- Output: `[]`
