# Merge In Between Linked Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1669 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-in-between-linked-lists/) |

## Problem Description
### Goal
Two nonempty singly linked lists, `list1` and `list2`, are provided together with zero-based positions `a` and `b` in `list1`. Remove every node of `list1` whose index lies from `a` through `b`, inclusive. The constraints guarantee a node remains before index `a` and another remains after index `b`.

Insert the complete `list2` chain into the resulting gap. The prefix of `list1` must point to the head of `list2`, and the tail of `list2` must point to the node that originally followed index `b`. Return the head of the merged chain, reusing and reconnecting the supplied nodes rather than interpreting their values as positions.

### Function Contract
**Inputs**

- `list1`: the head node of a nonempty singly linked list with length $n$.
- `a`: the zero-based index of the first node removed from `list1`.
- `b`: the zero-based index of the last node removed from `list1`, with $1 \le a \le b < n - 1$.
- `list2`: the head node of a nonempty singly linked list with length $m$.

**Return value**

Return the head node of the merged singly linked list after replacing `list1`'s inclusive index range $[a,b]$ with the entire `list2` chain.

### Examples
**Example 1**

- Input: `list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]`
- Output: `[10,1,13,1000000,1000001,1000002,5]`

**Example 2**

- Input: `list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]`
- Output: `[0,1,1000000,1000001,1000002,1000003,1000004,6]`
