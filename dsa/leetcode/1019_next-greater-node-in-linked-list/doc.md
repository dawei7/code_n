# Next Greater Node In Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1019 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/next-greater-node-in-linked-list/) |

## Problem Description

### Goal

You are given the `head` of a singly linked list containing $N$ nodes. For each node, find the value of its next greater node: the first later node in list order whose value is strictly larger.

Return an integer array `answer` aligned with the list positions, where `answer[i]` is that next greater value for the node at position `i`. If no strictly larger node occurs later, set the corresponding result to `0`. Equal values do not satisfy the requirement.

### Function Contract

**Inputs**

- `head`: the first node of a nonempty singly linked list with $1\le N\le10^4$ nodes and $1\le\texttt{Node.val}\le10^9$.

**Return value**

- An $N$-element array containing each node's first strictly greater value to the right, or `0` when absent.

### Examples

**Example 1**

- Input: `head = [2, 1, 5]`
- Output: `[5, 5, 0]`
- Explanation: The final value `5` is the first greater value after both earlier nodes.

**Example 2**

- Input: `head = [2, 7, 4, 3, 5]`
- Output: `[7, 0, 5, 5, 0]`
- Explanation: No later value exceeds `7` or the final `5`.

**Example 3**

- Input: `head = [5, 4, 3]`
- Output: `[0, 0, 0]`
- Explanation: A strictly decreasing list has no next greater node.
