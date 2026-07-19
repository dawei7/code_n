# Swapping Nodes in a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1721 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) |

## Problem Description

### Goal

You are given the head of a non-empty singly linked list containing $n$ nodes and a 1-indexed position `k`. Identify the $k$th node when counting from the beginning and the $k$th node when counting backward from the end.

Swap the values stored in those two nodes and return the original list head. The links between nodes do not need to be rearranged, and `k` is guaranteed to name a valid position.

### Function Contract

**Inputs**

- `head`: the first node of a singly linked list with $1 \le n \le 10^5$ and $0 \le \texttt{Node.val} \le 100$.
- `k`: a 1-indexed position satisfying $1 \le k \le n$.

**Return value**

- Return the linked-list head after swapping the values at positions $k$ and $n-k+1$.

### Examples

**Example 1**

- Input: `head = [1,2,3,4,5], k = 2`
- Output: `[1,4,3,2,5]`
- Explanation: The second node from the start and the second node from the end contain $2$ and $4$.

**Example 2**

- Input: `head = [7,9,6,6,7,8,3,0,9,5], k = 5`
- Output: `[7,9,6,6,8,7,3,0,9,5]`
- Explanation: Positions $5$ and $6$ exchange their values.

**Example 3**

- Input: `head = [1], k = 1`
- Output: `[1]`
- Explanation: Both positions refer to the sole node, so the list is unchanged.
