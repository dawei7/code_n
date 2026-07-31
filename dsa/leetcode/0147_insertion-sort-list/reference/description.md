## Description

Given the `head` of a singly linked list, sort the list with insertion sort and return its head.

Insertion sort grows a sorted result one element at a time:

1. Each iteration removes one element from the remaining input.
2. Find that element's proper position in the portion that is already sorted, then insert it there.
3. Continue until the input has no elements left.

The sorted portion begins with the first node. On every later iteration, the next node is detached and inserted into its ordered position within that growing portion.

```text
sorted portion | unread nodes
4              | 2 -> 1 -> 3
2 -> 4         | 1 -> 3
1 -> 2 -> 4    | 3
1 -> 2 -> 3 -> 4
```
