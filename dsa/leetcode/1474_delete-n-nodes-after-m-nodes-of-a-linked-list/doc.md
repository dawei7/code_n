# Delete N Nodes After M Nodes of a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1474 |
| Difficulty | Easy |
| Topics | Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) |

## Problem Description
### Goal

Given the head of a nonempty singly linked list and positive integers `m` and `n`, modify the list by repeating one positional rule from the head toward the tail: retain the next `m` nodes, then delete the following `n` nodes. After the deletion block, apply the same keep/delete pattern to the first node that remains.

If the list ends during a keep block, retain every available node. If it ends during a deletion block, remove every available node in that block. Preserve the original relative order and node identities of all retained nodes, and return the original head as the head of the modified list.

### Function Contract
**Inputs**

Let $L$ be the number of nodes in the input list.

- `head`: the first node of a singly linked list, with $1 \le L \le 10^4$.
- Each node value lies in the inclusive range $[1,10^6]$; values need not be unique.
- `m`: the positive number of consecutive nodes retained in each cycle, with $1 \le m \le 1000$.
- `n`: the positive number of consecutive nodes deleted after each keep block, with $1 \le n \le 1000$.

**Return value**

Return the head of the same linked list after rewiring it so that indices whose zero-based position modulo $m+n$ is less than $m$ remain, while all other nodes are unreachable from the returned head.

The app-local JSON adapter represents `head` and the returned linked list as arrays of node values; the native LeetCode interface receives and returns `ListNode` objects.

### Examples
**Example 1**

- Input: `head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3`
- Output: `[1,2,6,7,11,12]`
- Explanation: Retain `[1,2]`, delete `[3,4,5]`, and repeat. The final node `13` lies in a deletion block and is removed.

**Example 2**

- Input: `head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3`
- Output: `[1,5,9]`
- Explanation: Every retained node is followed by up to three deleted nodes.

**Example 3**

- Input: `head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1`
- Output: `[1,2,3,5,6,7,9,10,11]`
- Explanation: Each cycle retains three nodes and bypasses the next one.
