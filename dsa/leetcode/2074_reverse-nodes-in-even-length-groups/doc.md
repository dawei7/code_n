# Reverse Nodes in Even Length Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2074 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/) |

## Problem Description

### Goal

Partition a singly linked list into consecutive nonempty groups. The intended group lengths are $1,2,3,4,\ldots$: the first node forms group one, the next two nodes form group two, the next three form group three, and so on.

The final group contains every remaining node and may therefore be shorter than its intended length. Reverse the node order inside each group whose actual length is even. Leave odd-length groups unchanged, preserve the group order, and return the modified list's head.

### Function Contract

**Inputs**

- `head`: the first node of a singly linked list containing $n$ nodes, where $1 \le n \le 10^5$ and every node value lies between $0$ and $10^5$.

**Return value**

- Return the head node of the same linked list after reversing every group with an even actual node count.

### Examples

**Example 1**

- Input: `head = [5,2,6,3,9,1,7,3,8,4]`
- Output: `[5,6,2,3,9,1,4,8,3,7]`
- Explanation: Groups have lengths $1,2,3,4$; the groups of lengths $2$ and $4$ reverse.

**Example 2**

- Input: `head = [1,1,0,6]`
- Output: `[1,0,1,6]`
- Explanation: The groups have actual lengths $1,2,1$, so only the middle group reverses.

**Example 3**

- Input: `head = [1,1,0,6,5]`
- Output: `[1,0,1,5,6]`
- Explanation: The final group has actual length $2$ rather than its intended length $3$, so it also reverses.
