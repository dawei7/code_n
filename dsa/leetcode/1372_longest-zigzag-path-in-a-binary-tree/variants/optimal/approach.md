## General
**Carry both ways a path can end.** For every visited node, maintain two lengths: the longest alternating path ending at that node whose last edge moved left, and the corresponding length whose last edge moved right.

**Extend only from the opposite direction.** When moving to a left child, its new left-ending length is the parent's right-ending length plus one; its right-ending length resets to zero. Moving to a right child symmetrically extends the parent's left-ending length and resets the other state.

Traverse with an explicit depth-first stack and update a global maximum from both states at every node. Each carried value describes a valid alternating path by construction. Any ZigZag path ending at a child must arrive from its parent in that child's direction and can extend only a path whose prior direction was opposite, so the transition also considers every possible valid path. The maximum is therefore exact.

## Complexity detail
Each of the $N$ nodes is pushed, popped, and processed once, yielding $O(N)$ time. A depth-first stack retains at most pending siblings along a root-to-leaf route, using $O(H)$ space.

## Alternatives and edge cases
- **Restart at every node:** Follow both possible initial directions independently from each node. It is correct but can take $O(N^2)$ time on an alternating chain.
- **Recursive postorder DP:** Return left-starting and right-starting lengths from each subtree. This is also linear but may exceed the language recursion limit on a deep legal tree.
- **Straight chain:** Consecutive edges in one direction cannot both belong to a ZigZag, so the maximum is one when at least one edge exists.
- **Single node:** No edge can be traversed, producing length zero.
- **Path starts below root:** Reset states at each child allow every node to serve as a new start.
- **Edge count:** Do not return the number of nodes; a $k$-node path has length $k-1$.
- **Branching tree:** Left and right states are carried separately, so one branch cannot be spliced into another through siblings.
