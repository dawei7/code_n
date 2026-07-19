## General
**Match preorder one node at a time.** Keep an index into `voyage` and traverse the effective tree in preorder with a stack. When a popped node does not equal the next voyage value, no flip at that node or below can change which node is visited now, so return `[-1]`.

**The next value forces every flip.** After matching a node, preorder must enter its first non-null child. If a left child exists but its value is not the next voyage value, the only possible correction is to flip the current node and visit its right subtree first. Record the current node's value. Otherwise keep the normal left-before-right order.

**Push children in effective reverse order.** Because the stack is last-in, first-out, push the later subtree first. Without a flip, push right then left; after a flip, push left then right. This simulates the changed traversal without mutating the tree.

**Why the flip count is minimum.** A mismatch between the required next value and an existing left child forces a flip: no operation below the current node can replace that first subtree root. Conversely, when the next value already matches the left child, flipping would immediately contradict the voyage. Every recorded choice is therefore necessary, and the complete successful traversal uses the unique minimum set.

## Complexity detail
Each of the $N$ nodes is pushed, popped, and compared once, so the running time is $O(N)$. The traversal stack and returned flip list use $O(N)$ space in the worst case.

## Alternatives and edge cases
- **Recursive preorder:** Carry a shared voyage index and recurse into children in the forced order. This has the same bounds but depends on the call stack.
- **Try both orders at every node:** Backtracking over flip and no-flip choices is correct but can explore exponentially many configurations even though the next voyage value already determines the choice.
- **Repeated suffix searches:** Scan the unconsumed voyage to locate child values at every node. It adds no useful information and can take $O(N^2)$ time.
- **Root mismatch:** Return `[-1]` immediately because flips never change the root.
- **One child:** A flip can change whether that subtree is visited as left or right, but cannot change its root value or preorder position.
- **Already matching:** Return an empty list when the original preorder equals `voyage`.
