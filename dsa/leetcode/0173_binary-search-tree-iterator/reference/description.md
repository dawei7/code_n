## Description

Implement `BSTIterator`, an iterator over the in-order traversal of a binary search tree:

- `BSTIterator(TreeNode root)` initializes the iterator for the supplied BST. Its pointer begins before the traversal, at a conceptual value smaller than every tree element.
- `hasNext()` returns `true` when another number remains to the right of the pointer and `false` otherwise.
- `next()` advances the pointer one position and returns the number now under it.

Because the initial pointer precedes every element, the first `next()` call returns the BST's smallest value. Every call to `next()` is guaranteed to be valid: at least one traversal value remains when it is called.
