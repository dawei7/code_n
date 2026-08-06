## Description

Each node of a binary tree stores an integer. Removing one existing parent-child edge separates the original tree into exactly two nonempty trees: the subtree below the removed edge and the component that still contains the original root. Every node remains in exactly one component, and node values do not change.

Given the tree's root, determine whether some choice of exactly one edge makes the sums of the node values in the two resulting trees equal. Return `true` when such an edge exists; otherwise return `false`.
