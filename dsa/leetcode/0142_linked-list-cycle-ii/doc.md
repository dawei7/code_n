# Linked List Cycle II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 142 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/) |

## Problem Description
### Goal
Given the head of a singly linked list that may contain a cycle, locate the first node on the loop. Starting from the head and following `next` links, this is the node reached when the noncyclic prefix first enters the repeating portion; it may also be the head itself.

For the native contract, return that exact node object, or `null` when the chain terminates without cycling. Do not modify the linked list or confuse an earlier node with the first repeated value, because values need not be unique and identity determines the structure. The app-friendly contract reports the cycle-entry node's zero-based index, using `-1` when no entry exists.

### Function Contract
**Inputs**

- `head`: linked list head, encoded in app cases as `{"values": [...], "pos": index}` where `pos = - 1` means no cycle and otherwise the tail links to that index

**Return value**

The app-friendly `solve(...)` returns the zero-based index of the cycle-entry node, or `-1` if no cycle exists. The submit-ready LeetCode implementation returns the entry node itself, as required by the native platform contract.

### Examples
**Example 1**

- Input: `values = [3,2,0,-4], pos = 1`
- Output: `1`

**Example 2**

- Input: `values = [1,2], pos = 0`
- Output: `0`

**Example 3**

- Input: `values = [1], pos = -1`
- Output: `-1`
