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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Measure the actual group before deciding**

The first one-node group never changes, so keep a pointer to its tail and begin with target length two. From `group_tail.next`, advance a probe by at most the target length to count how many nodes the next group actually contains and to remember the first node after it. This count, not the target, determines parity for a truncated final group.

**Reverse and reconnect one even group**

For an even group, perform standard in-place pointer reversal for exactly its actual length, initializing the reversal's previous pointer to the node after the group. Connect the prior group's tail to the new group head. The old group head becomes its new tail and is the boundary pointer for the following iteration. For an odd group, simply advance the boundary pointer across its nodes.

The measurement step partitions the remaining list exactly according to the required natural-number lengths. Odd groups retain every link. Reversing exactly the measured nodes in an even group flips their internal order while the two reconnections preserve both neighboring groups. Repeating this argument across all groups yields precisely the required list.

#### Complexity detail

Each node is visited at most once while measuring its group and at most once more while either reversing or advancing the boundary. The total time is $O(n)$. Only a fixed number of node pointers and counters are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Copy nodes into an array:** Group boundaries and slice reversals become simple, but the extra array requires $O(n)$ space.
- **Relocate from the head for every group:** The pointer changes can remain correct, but repeatedly traversing the processed prefix costs $O(n^{3/2})$ time across roughly $\sqrt n$ groups.
- The one-node first group is odd and never reverses.
- The last group's actual length, rather than its intended length, controls reversal.
- A truncated final group can be even even when its intended length is odd.
- Repeated values do not change the operation: node order, not value distinctness, is reversed.
- A single-node list is returned unchanged.

</details>
