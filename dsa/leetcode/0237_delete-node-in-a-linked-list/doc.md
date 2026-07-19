# Delete Node in a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 237 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-node-in-a-linked-list/) |

## Problem Description
### Goal
You are given direct access to a node that must be deleted from a singly linked list, but not to the list's head or the node preceding it. Every node value is unique, and the supplied node is guaranteed not to be the tail, so it has a successor.

Modify the list in place so the original target value disappears and every other value remains in the same order. Because the incoming link cannot be changed, make the accessible node represent its successor and bypass that successor object. Return nothing, preserve the rest of the suffix, and ensure the list loses exactly one node rather than merely marking a value as deleted.

### Function Contract
**Inputs**

- `node`: the specified non-tail node in a singly linked list, represented locally by the suffix beginning at that node

**Return value**

`None`; the linked list suffix beginning at `node` is mutated so that the original node value is removed.

### Examples
**Example 1**

- Input: `node = [5,1,9]`
- Output: `[1,9]`

**Example 2**

- Input: `node = [1,9]`
- Output: `[9]`

**Example 3**

- Input: `node = [3,4,5,6]`
- Output: `[4,5,6]`
