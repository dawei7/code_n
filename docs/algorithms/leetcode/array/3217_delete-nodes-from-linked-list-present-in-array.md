# Delete Nodes From Linked List Present in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3217 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Linked List |
| Official Link | [delete-nodes-from-linked-list-present-in-array](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/) |

## Problem Description & Examples
### Goal
Given an array of integers and the head of a singly linked list, remove all nodes from the linked list whose values exist within the provided array. The function should return the head of the modified linked list, ensuring that the structural integrity of the remaining nodes is preserved.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the values to be removed from the linked list.
- `head`: The head node of a singly linked list.

**Return value**

- The head of the modified linked list after all nodes with values present in `nums` have been removed.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], head = [1, 2, 3, 4, 5]`
- Output: `[4, 5]`

**Example 2**

- Input: `nums = [1], head = [1, 2, 1, 2, 1, 2]`
- Output: `[2, 2, 2]`

**Example 3**

- Input: `nums = [5], head = [1, 2, 3, 4]`
- Output: `[1, 2, 3, 4]`

---

## Underlying Base Algorithm(s)
The problem is solved using a Hash Set for O(1) average-time complexity lookups of the values to be deleted, combined with a single-pass traversal of the linked list using a dummy head node to simplify edge cases involving the removal of the original head.

---

## Complexity Analysis
- **Time Complexity**: O(N + M), where N is the number of nodes in the linked list and M is the number of elements in the input array. We iterate through the array once to build the set and the list once to filter nodes.
- **Space Complexity**: O(M), required to store the unique elements of the input array in a hash set for efficient lookup.
