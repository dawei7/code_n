## Description

Given the root of a binary tree, turn the tree upside down and return its new root. Apply these changes one level at a time:

- The original left child becomes the new root of that level.
- The original root becomes its new right child.
- The original right child becomes its new left child.

Every right child is guaranteed to have a left sibling with the same parent, and every right child is a leaf.
