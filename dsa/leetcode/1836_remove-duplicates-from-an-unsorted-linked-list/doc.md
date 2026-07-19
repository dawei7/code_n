# Remove Duplicates From an Unsorted Linked List

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/) |
| Frontend ID | 1836 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given the head of an unsorted singly linked list, identify every value that occurs more than once anywhere in the original list. Delete every node carrying any such value, including its first occurrence.

Return the head of the remaining list. Nodes whose values occurred exactly once must retain their original relative order. The list contains at least one node initially, but every node may be removed.

### Function Contract

**Inputs**

- `head`: the first node of a singly linked list containing $n$ nodes, where $1 \le n \le 10^5$.
- Each node value satisfies $1 \le \texttt{Node.val} \le 10^5$.
- The nodes are not sorted, so equal values need not be adjacent.

**Return value**

- Return the first node after removing all nodes whose value occurred two or more times in the original list.
- Return an empty list when no value was unique.

### Examples

**Example 1**

- Input: `head = [1,2,3,2]`
- Output: `[1,3]`

Both nodes valued 2 are removed.

**Example 2**

- Input: `head = [2,1,1,2]`
- Output: `[]`

Neither value occurs exactly once.

**Example 3**

- Input: `head = [3,2,2,1,3,2,4]`
- Output: `[1,4]`

Values 3 and 2 occur multiple times, while 1 and 4 are unique.
