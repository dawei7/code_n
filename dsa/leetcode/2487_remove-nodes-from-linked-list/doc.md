# Remove Nodes From Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2487 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Stack, Recursion, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-nodes-from-linked-list/) |

## Problem Description

### Goal

Given the `head` of a singly linked list, remove every node for which some node appearing later in the list has a strictly greater value. A node remains when its value is at least as large as every value to its right.

Return the head of the modified list. The relative order of all retained nodes must stay unchanged. Equal values do not cause removal because the comparison is strictly greater.

### Function Contract

**Inputs**

- `head`: The first node of a nonempty singly linked list.

Let $n$ be the number of nodes. The constraints satisfy $1 \le n \le 10^5$ and $1 \le \texttt{Node.val} \le 10^5$.

**Return value**

Return the head of the list after removing exactly those nodes that have a later node with a greater value.

### Examples

**Example 1**

- Input: `head = [5, 2, 13, 3, 8]`
- Output: `[13, 8]`
- Explanation: `13` eliminates the earlier `5` and `2`, while `8` eliminates `3`. Neither retained node has a greater value to its right.

**Example 2**

- Input: `head = [1, 1, 1, 1]`
- Output: `[1, 1, 1, 1]`
- Explanation: Equal values are not greater, so every node remains.
