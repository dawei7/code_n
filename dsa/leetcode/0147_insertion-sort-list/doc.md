# Insertion Sort List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 147 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/insertion-sort-list/) |

## Problem Description
### Goal
Given the head of a singly linked list, sort its nodes in nondecreasing order using insertion-sort behavior. Progress through the original chain and place each encountered node into the appropriate position among the nodes that have already been arranged.

Return the head of the sorted list, reusing the original nodes and reconnecting their `next` pointers rather than returning only sorted values. Equal values may remain adjacent in either identity order, and negative values participate normally. The final chain must contain every input node exactly once and end at `null`; an empty or one-node list is already sorted.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as a list of integer values in app cases

**Return value**

The head node of the same linked-list nodes rearranged into nondecreasing order.

### Examples
**Example 1**

- Input: `head = [4,2,1,3]`
- Output: `[1,2,3,4]`

**Example 2**

- Input: `head = [-1,5,3,4,0]`
- Output: `[-1,0,3,4,5]`

**Example 3**

- Input: `head = []`
- Output: `[]`
