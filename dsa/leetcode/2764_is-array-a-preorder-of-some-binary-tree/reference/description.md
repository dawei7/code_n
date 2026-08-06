## Description

You are given a 0-indexed two-dimensional integer array `nodes`. Each entry `nodes[i] = [id, parentId]` describes the node appearing at index $i$: `id` is that node's identifier, and `parentId` identifies its parent. The unique root has no parent and therefore uses `parentId = -1`. The supplied pairs are guaranteed to describe a binary tree.

Determine whether the entries occur in a preorder traversal of some orientation of that tree. A preorder traversal visits the current node first, then traverses one child subtree completely, and finally traverses the other child subtree. Return whether the given ordering can follow those rules.
