## Description

You are given a doubly linked list whose nodes have `next`, `prev`, and an additional `child` pointer. A `child`
may begin another doubly linked list made of the same kind of nodes, and those nodes may themselves have children,
forming a multilevel structure.

Starting from `head` on the first level, flatten every node into one single-level doubly linked list. If `curr` has
a child list, that entire child section must appear immediately after `curr` and before the node originally reached
through `curr.next`.

Return the original head of the flattened list, and set every node's `child` pointer to `null`.
