# Convert Doubly Linked List to Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3263 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Linked List, Doubly-Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/) |

## Problem Description

### Goal

You receive the head node of a non-empty doubly linked list. Every node stores an integer value and has both `next` and `prev` links to its neighbors.

Create an integer array containing the list's values in their forward order, beginning at `head` and following `next` until the tail. Repeated values remain repeated, and the linked list itself must not be reordered to form the result.

### Function Contract

**Inputs**

- `head`: The first node of a doubly linked list containing $n$ nodes, where $1 \le n \le 50$. Every node value is between 1 and 50 inclusive.

**Return value**

- An integer list of length $n$ whose entry at each position equals the corresponding linked-list node's value in forward order.

### Examples

**Example 1**

- Input: `head = [1,2,3,4,3,2,1]`
- Output: `[1,2,3,4,3,2,1]`

**Example 2**

- Input: `head = [2,2,2,2,2]`
- Output: `[2,2,2,2,2]`

**Example 3**

- Input: `head = [3,2,3,2,3,2]`
- Output: `[3,2,3,2,3,2]`
