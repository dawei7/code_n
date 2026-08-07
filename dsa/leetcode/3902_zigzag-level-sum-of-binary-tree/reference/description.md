## Description

You are given the `root` of a **binary tree**.

Traverse the tree level by level using a zigzag pattern:
* At **odd-numbered** levels (1-indexed), traverse nodes from **left to right**.
* At **even-numbered** levels, traverse nodes from **right to left**.

While traversing a level in the specified direction, process nodes in order and **stop** immediately before the first node that violates the condition:
* At **odd** levels: the node does not have a **left** child.
* At **even** levels: the node does not have a **right** child.

Only the nodes processed before this stopping condition contribute to the level sum.

Return an integer array `ans` where `ans[i]` is the **sum** of the node values that are processed at level `i + 1`.

