# Insert into a Sorted Circular Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 708 |
| Difficulty | Medium |
| Topics | Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) |

## Problem Description
### Goal
Given a node from a circular singly linked list whose values are sorted in non-decreasing cyclic order, insert one new node containing `insertVal`. The supplied `head` may point to any position in the cycle, not necessarily its minimum value.

Preserve the circular links and sorted cyclic order, then return the original `head`. If the input is empty, create and return a new node that points to itself. When equal values or several insertion locations make more than one result valid, any placement that preserves the required order is acceptable.

### Function Contract
**Inputs**

- `head`: the head node of a sorted circular linked list; cases encode the cycle as `{"values": [...], "pos": 0}`
- `insertVal`: the value for the new node

**Return value**

- The head node of the circular linked list after inserting exactly one node; an empty input returns the new self-linked node

### Examples
**Example 1**

- Input: `head = [3,4,1], insertVal = 2`
- Output: `[3,4,1,2]`

**Example 2**

- Input: `head = [], insertVal = 1`
- Output: `[1]`

**Example 3**

- Input: `head = [1], insertVal = 0`
- Output: `[1,0]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Recognize the two legal kinds of gap**

For neighboring nodes `current` and `following`, a normal gap accepts the value when `current.val <= insertVal <= following.val`. At the unique wrap from the maximum region to the minimum region, identified by `current.val > following.val`, the value belongs there when it is at least the current maximum or at most the following minimum.

**Walk at most one complete cycle**

Start at `head`, test each adjacent pair, and advance. Stop when a legal gap is found or when advancing returns to `head`.

**Handle indistinguishable placements**

If a full cycle has no selected gap, all values are equal or every gap is equivalent for this insertion. Inserting after the current head is valid.

**Splice one node without breaking the cycle**

Create the node, point it to `current.next`, and then point `current.next` to it. For an empty input, make the new node point to itself. Nonempty insertion returns the original head.

**Why the resulting cycle remains sorted**

In a normal gap, both adjacent inequalities remain valid after splitting the gap. At the wrap, the new value extends either the maximum or minimum end without creating a second descending transition. The fallback cycle is uniform, so any placement is valid. All untouched links retain their previous order.

#### Complexity detail

At most `n` adjacent pairs are inspected before insertion, taking $O(n)$ time. Only the current, following, and new node references are stored, so the extra space is $O(1)$.

#### Alternatives and edge cases

- **Collect and sort values:** append the new value, sort, and rebuild a cycle; it takes $O(n \log n)$ time and $O(n)$ auxiliary space while unnecessarily replacing links.
- **Restart for every candidate gap:** repeatedly walk from the head to reach each next pair; it preserves the structure but takes $O(n^2)$ time.
- An empty list becomes a one-node self-cycle.
- A one-node or all-equal cycle permits insertion at any link.
- A new minimum or maximum is inserted across the maximum-to-minimum wrap.
- Duplicate values may be inserted into any equal-valued gap.
- The supplied head need not point to the minimum value.

</details>
