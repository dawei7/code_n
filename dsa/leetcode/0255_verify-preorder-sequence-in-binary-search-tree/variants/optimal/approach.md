## General
**The stack represents unfinished ancestor paths**

Keep a monotonic stack of ancestors whose right subtrees have not been closed. When a value exceeds the stack top, pop ancestors until locating the subtree that now owns the value; the last popped value becomes a strict lower bound.

The stack is decreasing and represents the active root-to-current path. Every future value must exceed `lower_bound`, because preorder has already entered the right subtree of that ancestor.

**Entering a right subtree creates a permanent lower bound**

Whenever a value exceeds an ancestor on the stack, preorder has finished that ancestor's left side and entered its right subtree. The last popped ancestor becomes a lower bound for every later value until an even higher transition replaces it. A value below that bound would violate BST ordering and must be rejected. Otherwise, popping exactly the smaller ancestors identifies the valid active path, and pushing the value preserves the representation.

## Complexity detail
Each value is pushed once and popped at most once, giving $O(n)$ time. The stack holds at most `n` values.

## Alternatives and edge cases
- **Recursively partition each range:** mirrors the tree definition but repeatedly scans skewed ranges and can take $O(n^2)$.
- Empty, singleton, increasing, and decreasing sequences are valid; distinctness removes equality handling.
