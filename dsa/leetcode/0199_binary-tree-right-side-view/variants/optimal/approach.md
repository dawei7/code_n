## General
Visibility is determined independently at each depth, which makes breadth-first search a natural fit. Initialize a queue with the root. At the start of each outer iteration, capture the queue's current length; those nodes are exactly one level in left-to-right order.

Remove exactly that many nodes, enqueueing each existing left child before its right child. The final node removed from the captured group is the rightmost node at that depth, so append its value. Children added during the loop belong to the next level and are not processed until the next outer iteration.

For `[1,2,3,null,5,null,4]`, the queue groups are `[1]`, `[2,3]`, and `[5,4]`. Their final nodes are `1`, `3`, and `4`. Notice that blindly following right-child pointers would miss a left descendant that becomes visible when no node lies farther right at its depth.

The queue never needs null placeholders. Missing children simply are not enqueued; the last existing node in each actual level remains well-defined.

At the beginning of every level iteration, the queue contains exactly that depth's existing nodes in left-to-right order. This holds for the root, and enqueueing left then right children while consuming a whole level establishes the same order for the next depth. Therefore the last consumed node is precisely the rightmost existing node and is the one visible from the right side. Every occupied depth is processed once, so the result is complete and ordered top to bottom.

## Complexity detail
Every node enters and leaves the queue once, giving $O(n)$ time. The queue holds at most the tree's maximum width, $O(w)$ and worst-case $O(n)$ space. The output itself uses $O(h)$ entries for tree height `h`.

## Alternatives and edge cases
- A right-first depth-first traversal records the first node encountered at each new depth and uses $O(h)$ call-stack space.
- Following only right-child links is incorrect when a visible node lies in a left subtree below a missing or shallower right branch.
- Enqueueing null placeholders wastes memory and is unnecessary for this view.
- An empty tree returns an empty list. A left-only chain contributes every node, and irregular gaps do not create empty result levels.
