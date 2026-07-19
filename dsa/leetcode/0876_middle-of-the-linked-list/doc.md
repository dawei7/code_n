# Middle of the Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 876 |
| Difficulty | Easy |
| Topics | Linked List, Two Pointers |
| Official Link | [LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/) |

## Problem Description
### Goal
Given `head`, the first node of a nonempty singly linked list, return the list's middle node. The returned object is a node from the original list, so it remains connected to every node that follows it.

An odd-length list has one middle node. An even-length list has two central nodes; in that case, return the second middle. Consequently, a serialized returned node appears as the suffix beginning at that selected position.

### Function Contract
**Inputs**

- `head`: the head of a singly linked list containing $n$ nodes, where $1 \leq n \leq 100$ and every node value is between $1$ and $100$.

**Return value**

Return the linked-list node at zero-based position $\lfloor n/2\rfloor$. For even $n$, this is the second of the two middle nodes.

### Examples
**Example 1**

- Input: `head = [1,2,3,4,5]`
- Output: `[3,4,5]`

The node with value `3` is the unique middle and heads the returned suffix.

**Example 2**

- Input: `head = [1,2,3,4,5,6]`
- Output: `[4,5,6]`

The nodes with values `3` and `4` are central, so the second one is returned.

**Example 3**

- Input: `head = [7]`
- Output: `[7]`

The only node is also the middle.
