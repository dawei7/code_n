## Description

Design a bidirectional iterator over the inorder traversal of a binary search tree. The inorder values form the iterator's ordered sequence. At construction, place the cursor before the smallest value, rather than on a tree node.

`next()` moves the cursor one position to the right and returns that value, while `hasNext()` reports whether such a move is possible. Symmetrically, `prev()` moves one position to the left and returns the new current value, while `hasPrev()` reports whether a value exists on that side. Calls to `next()` and `prev()` are guaranteed to be valid.

The same iterator must preserve its position across an arbitrary valid mixture of forward and backward calls. In particular, moving backward and then forward must revisit already discovered values without advancing the underlying inorder traversal twice.
