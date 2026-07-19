# Reorder List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 143 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reorder-list/) |

## Problem Description
### Goal
Given a singly linked list ordered as $L_{0} \to L_{1} \to \ldots \to L_n$, rearrange its nodes into $L_{0} \to L_n \to L_{1} \to L_n - 1 \to L_{2} \to L_n - 2 \to \ldots$. The sequence alternates between the next unused node from the front and the next unused node from the back until every node appears once.

Perform the reordering in place by changing links between the existing nodes. Do not create a replacement list or satisfy the order by copying values into different nodes. The head remains the original first node, the new final node must point to `null`, and lists with zero, one, or two nodes require no substantive rearrangement.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as a list of values in app cases

**Return value**

`None`; mutate the linked list in place. The app displays the reordered list.

### Examples
**Example 1**

- Input: `head = [1,2,3,4]`
- Output: `[1,4,2,3]`

**Example 2**

- Input: `head = [1,2,3,4,5]`
- Output: `[1,5,2,4,3]`

**Example 3**

- Input: `head = [1]`
- Output: `[1]`
