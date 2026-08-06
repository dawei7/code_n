## Description

An N-ary tree contains unique node values, and two distinct existing nodes are designated as `p` and `q`. Detach the entire subtree rooted at `p` from its current position and make `p` the last direct child of `q`.

If `p` is already a direct child of `q`, leave the tree unchanged. Otherwise, preserve the order of every child list except for the removals and insertions required by the move.

Special care is required when `q` belongs to the subtree rooted at `p`: attaching `p` below `q` without another change would form a cycle and disconnect the original parent side. In that case, first detach `q` from its parent, place `q` where `p` used to be (or make `q` the root when `p` was the root), and then append `p` to `q`. Return the root of the resulting valid tree.
