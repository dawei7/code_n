# Linked List Components

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 817 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/linked-list-components/) |

## Problem Description

### Goal

You are given a singly linked list with distinct node values and a collection `nums` selecting some of those values. Consider only the selected nodes while preserving the `next` relationships from the original list. Two selected nodes are connected when they are adjacent in the list, and this connection extends transitively through a consecutive run of selected nodes.

Count the connected components in that induced structure. Equivalently, count the maximal list segments whose nodes are all selected. Numeric closeness and the order of values inside `nums` do not define connectivity; only adjacency along the linked list does.

### Function Contract

**Inputs**

- `head`: the head of a singly linked list whose node values are distinct.
- `nums`: the distinct node values selected for the induced components.

**Return value**

- The number of maximal consecutive runs of selected nodes in the linked list.

### Examples

**Example 1**

- Input: `head = [0,1,2,3], nums = [0,1,3]`
- Output: `2`
- Explanation: Nodes `0` and `1` form one run, while node `3` forms another.

**Example 2**

- Input: `head = [0,1,2,3,4], nums = [0,3,1,4]`
- Output: `2`
- Explanation: The selected runs are `0 -> 1` and `3 -> 4`; the order of `nums` is irrelevant.

**Example 3**

- Input: `head = [0], nums = [0]`
- Output: `1`
- Explanation: The selected singleton node is one component.
