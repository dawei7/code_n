# Split a Circular Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2674 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-a-circular-linked-list/) |

## Problem Description

### Goal

You are given the head of a circular singly linked list of positive length. Its tail points back to the first node rather than to `null`. Split the existing nodes into two circular linked lists while preserving their original order.

The first result must contain the first $\lceil m / 2 \rceil$ nodes of the original list, where $m$ is its length. The second result contains the remaining $\lfloor m / 2 \rfloor$ nodes. Close each half into its own cycle and return their heads in that order.

### Function Contract

**Inputs**

- `list`: The `ListNode` head of a circular linked-list containing $m$ nodes, where $2 \le m \le 10^5$ and $0 \le \texttt{Node.val} \le 10^9$. The final node points to `list`.

**Return value**

- Return two circular linked-list heads. The first cycle contains the longer half when $m$ is odd, and both cycles preserve the input order.

### Examples

**Example 1**

- Input: `list = [1,5,7]` with its tail linked to the first node
- Output: `[[1,5],[7]]`
- Explanation: The first cycle receives $\lceil 3/2 \rceil = 2$ nodes.

**Example 2**

- Input: `list = [2,6,1,5]` with its tail linked to the first node
- Output: `[[2,6],[1,5]]`
- Explanation: An even-length list splits into two equal cycles.
