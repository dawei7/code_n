# Print Immutable Linked List in Reverse

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1265 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/print-immutable-linked-list-in-reverse/) |

## Problem Description

### Goal

You receive the head of an immutable singly linked list. Its nodes cannot be inspected or changed through ordinary fields. The provided `ImmutableListNode` interface permits exactly two operations: `getNext()` returns the following node, or `null` after the tail, and `printValue()` prints the value stored in the current node.

Print every node value in reverse list order, beginning with the tail and ending with the head. The list itself must remain unchanged, and the procedure produces its answer only through calls to `printValue()`; the serialized input exists solely to construct the hidden immutable nodes for the judge.

### Function Contract

**Inputs**

- `head`: the first `ImmutableListNode` in a nonempty immutable singly linked list containing $n$ nodes, where $1 \le n \le 1000$.

A node's value is an integer in the range $[-1000,1000]$ and is accessible only by calling that node's `printValue()` method.

**Return value**

`None`. Call `printValue()` on the nodes in tail-to-head order so that the emitted sequence is the reverse of the linked-list order.

### Examples

**Example 1**

- Input: `head = [1,2,3,4]`
- Output: `[4,3,2,1]`

**Example 2**

- Input: `head = [0,-4,-1,3,-5]`
- Output: `[-5,3,-1,-4,0]`

**Example 3**

- Input: `head = [-2,0,6,4,4,-6]`
- Output: `[-6,4,4,6,0,-2]`
