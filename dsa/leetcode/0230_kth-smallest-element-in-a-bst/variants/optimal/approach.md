## General
**Inorder position is the desired rank**

An inorder traversal visits every binary search tree value in strictly increasing order. The desired value is therefore the `k`-th node visited by inorder traversal.

**Materialize only the unfinished left paths**

Push the path of left children from the root. Pop the next smallest node, decrement `k`, and return its value when `k` reaches zero. Before the next pop, push the left path beginning at the popped node's right child.

Immediately before each pop, the top of the stack is the smallest unvisited node, while every smaller node has already been visited. The stack also preserves the ancestors needed to continue inorder traversal without revisiting nodes.

**The `k`-th pop is the `k`-th smallest value**

For `[3,1,4,null,2]`, the initial stack contains `3,1`. Popping `1` produces rank one. If a later rank were requested, its right child `2` would be pushed before returning to `3`.

The stack procedure is exactly inorder traversal, and BST inorder order is ascending. Decrementing once per popped node counts ranks in that order, so the node returned when the counter reaches zero has rank `k`.

## Complexity detail
Reaching the first value costs at most $O(h)$, and at most `k` nodes are popped before the answer, for $O(h + k)$ time. The stack holds at most one root-to-leaf path, or $O(h)$ nodes.

## Alternatives and edge cases
- **Full inorder list:** is simple but always takes $O(n)$ time and space even for small `k`.
- **Augmented subtree sizes:** support repeated rank queries in $O(h)$ each, but require maintained metadata.
- Skewed trees have $h = n$; $k = 1$ and $k = n$ select the extreme values.
