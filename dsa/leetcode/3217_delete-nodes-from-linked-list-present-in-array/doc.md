# Delete Nodes From Linked List Present in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3217 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/) |

## Problem Description

### Goal

You are given an integer array `nums` and the head of a singly linked list. Remove every linked-list node whose value occurs in `nums`, reconnecting the nodes that remain in their original relative order.

Return the head of the modified list. The values in `nums` are unique, and the input guarantees that at least one list node has a value absent from `nums`, so the returned list is nonempty. Nodes may repeat values even though the deletion array does not.

### Function Contract

**Inputs**

- `nums`: A list of unique integers with $1 \leq \lvert\texttt{nums}\rvert \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^5$.
- `head`: The head of a singly linked list containing between $1$ and $10^5$ nodes; every node value is between $1$ and $10^5$.

**Return value**

Return the head of the linked list after removing every node whose value belongs to `nums`.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3], head = [1, 2, 3, 4, 5]`
- **Output:** `[4, 5]`
- **Explanation:** The first three nodes have listed values and are removed.

#### Example 2

- **Input:** `nums = [1], head = [1, 2, 1, 2, 1, 2]`
- **Output:** `[2, 2, 2]`
- **Explanation:** Every node with value `1` is removed, including the original head.

#### Example 3

- **Input:** `nums = [5], head = [1, 2, 3, 4]`
- **Output:** `[1, 2, 3, 4]`
- **Explanation:** No node value occurs in `nums`, so the list is unchanged.
