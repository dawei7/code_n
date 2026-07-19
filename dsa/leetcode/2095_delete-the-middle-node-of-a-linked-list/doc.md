# Delete the Middle Node of a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2095 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) |

## Problem Description

### Goal

You are given the head of a nonempty singly linked list containing $n$ nodes. Under zero-based indexing, its middle node is the node at index $\lfloor n/2 \rfloor$. In an even-length list this selects the second of the two central nodes.

Remove that one node by reconnecting its predecessor to its successor, and return the head of the resulting list. When the input contains only one node, removing its middle leaves an empty list.

### Function Contract

**Input**

- `head`: the first node of a singly linked list with $1$ through $10^5$ nodes.
- Every node value is between $1$ and $10^5$.

**Return value**

Return the head after deleting the node at zero-based index $\lfloor n/2 \rfloor$, or `None` when no node remains.

### Examples

**Example 1**

- Input: `head = [1, 3, 4, 7, 1, 2, 6]`
- Output: `[1, 3, 4, 1, 2, 6]`
- Explanation: With $n=7$, index $\lfloor 7/2 \rfloor=3$ is deleted.

**Example 2**

- Input: `head = [1, 2, 3, 4]`
- Output: `[1, 2, 4]`
- Explanation: The selected middle index is `2`, the second central node.

**Example 3**

- Input: `head = [2, 1]`
- Output: `[2]`
