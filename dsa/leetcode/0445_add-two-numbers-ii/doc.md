# Add Two Numbers II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 445 |
| Difficulty | Medium |
| Topics | Linked List, Math, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/add-two-numbers-ii/) |

## Problem Description
### Goal
Two nonempty singly linked lists encode nonnegative integers with one decimal digit per node in most-significant-first order. Add the represented values using ordinary base-ten arithmetic while preserving the forward digit convention.

Return a linked list containing the sum's digits from most significant to least significant, with no leading zero except for the number zero itself. Propagate carries across unequal list lengths and create a new leading digit when needed. Meet the follow-up challenge without reversing the input lists, and return actual linked nodes rather than only a numeric string.

### Function Contract
**Inputs**

- `l1`: the app-local list of digits for the first number in forward order
- `l2`: the app-local list of digits for the second number in forward order

**Return value**

- Return the sum's digits in forward order with no leading zero except for zero itself. The native artifact accepts and returns LeetCode `ListNode` chains.

### Examples
**Example 1**

- Input: `l1 = [7, 2, 4, 3], l2 = [5, 6, 4]`
- Output: `[7, 8, 0, 7]`

**Example 2**

- Input: `l1 = [2, 4, 3], l2 = [5, 6, 4]`
- Output: `[8, 0, 7]`

**Example 3**

- Input: `l1 = [0], l2 = [0]`
- Output: `[0]`
