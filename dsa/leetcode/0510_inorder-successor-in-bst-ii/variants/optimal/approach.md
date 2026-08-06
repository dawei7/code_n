## General

**Descend to the next node when a right subtree exists**

Inorder traversal visits a node's right subtree immediately after the node itself. The first visit within that
subtree is its leftmost node. Therefore, move once to `node.right` and follow `left` references until none remains;
that final node is the successor.

**Otherwise climb out of completed right subtrees**

When `node` has no right child, its successor must be an ancestor. Climb through `parent` references while the
current node is exactly its parent's right child. Each such parent was already visited before the traversal entered
its right subtree. The first parent reached from its left child has not yet been visited and is therefore the
successor.

If this climb passes the root, the selected node lies on the tree's right boundary and is last in inorder order, so
the answer is `None`. The algorithm compares node identity and child relationships only; it never reads `val`, which
also satisfies the source follow-up.

## Complexity detail

Let $h$ be the tree height. The algorithm follows either one downward path or one upward path, both bounded by $h$,
for $O(h)$ time. It stores only a constant number of node references and therefore uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Search from the root by value:** can track the smallest greater ancestor in $O(h)$ time, but the root is not
  supplied and reading values violates the follow-up.
- **Full inorder traversal:** is correct but takes $O(n)$ time and $O(h)$ stack space to answer one query.
- **Stored inorder links:** can make successor queries constant time but requires augmenting and maintaining the tree.
- **Right subtree present:** follow its entire left chain, even when the right child itself is not the successor.
- **Selected node is a left child:** with no right subtree, its parent is immediately the successor.
- **Maximum node:** climbing passes the root and returns `None`.
- **Single-node tree:** has neither a right subtree nor a parent and therefore has no successor.
