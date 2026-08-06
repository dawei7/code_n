## Description

The `Tree` table stores one binary-tree node per row. `N` is the node's value,
while `P` is its parent's value. The unique root has no parent and therefore
stores null in `P`. A leaf is a non-root node whose value never appears as
another row's parent; every remaining node is internal.

Classify every node as `Root`, `Leaf`, or `Inner`. Return the node value as `N`
and its label as `Type`, with rows ordered by `N` in ascending numeric order.
Node values need not be consecutive, so classification must use relationships
rather than arithmetic on the IDs.
