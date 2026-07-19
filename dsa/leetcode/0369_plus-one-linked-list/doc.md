# Plus One Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 369 |
| Difficulty | Medium |
| Topics | Linked List, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/plus-one-linked-list/) |

## Problem Description
### Goal
Given a nonempty singly linked list whose nodes contain decimal digits in most-significant-first order, interpret the chain as one nonnegative integer. Add exactly one to that value using ordinary base-ten carrying.

Return the head of a linked-list representation of the incremented number. Preserve digit order, update all trailing `9` digits affected by the carry, and create a new leading `1` node when the original value consists entirely of nines. Otherwise reuse the existing structure where possible. The output must contain one digit per node and no reversed least-significant-first encoding.

### Function Contract
**Inputs**

- `head`: the first node of a linked list containing one digit per node, represented by a value list in app cases

**Return value**

- The head of the linked list representing the incremented number, with carries propagated and a new leading digit when required.

### Examples
**Example 1**

- Input: `head = [1,2,3]`
- Output: `[1,2,4]`

**Example 2**

- Input: `head = [1,2,9,9]`
- Output: `[1,3,0,0]`

**Example 3**

- Input: `head = [9,9,9]`
- Output: `[1,0,0,0]`
