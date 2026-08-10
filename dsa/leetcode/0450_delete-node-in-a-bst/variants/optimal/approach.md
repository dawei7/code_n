## General

Deleting from a binary search tree has two separate parts: locate the node efficiently by using the ordering property, then reconnect its remaining subtrees without breaking that property. The exact solution performs the search recursively and returns the root of the updated subtree from every call. Returning a subtree root is important because deletion may replace the node at that subtree's top.

**Use BST ordering to search one path**

If `root` is `None`, the current subtree does not contain the key, so the method returns `None`.

For a real node, compare `root.val` with `key`:

- If `root.val > key`, every value in the right subtree is even larger than `root.val`, so the key can occur only in the left subtree. Recursively delete there, assign the returned subtree to `root.left`, and return `root`.
- If `root.val < key`, the symmetric argument sends the search only into `root.right`. Assign the recursive result back to `root.right`, then return `root`.
- Otherwise, `root.val == key`, so this is the node that must be removed.

The assignments to `root.left` and `root.right` are not optional bookkeeping. If the recursive call deletes the child at the top of that subtree, it may return a different node as the new child. The parent must retain that returned reference.

Because all node values are unique, equality identifies at most one node. Once it is found and removed, no second search is necessary.

**Deleting a node with at most one child**

If `root.left is None`, returning `root.right` removes the current node and promotes its right subtree. This covers both a leaf, where the right child is also `None`, and a node with only a right child.

If the left child exists but `root.right is None`, returning `root.left` similarly promotes the left subtree.

These promotions preserve the BST property. The promoted child subtree was already valid, and every value in it already satisfied all ordering restrictions imposed by ancestors of the deleted node.

**Deleting a node with two children**

The difficult case is a node whose left and right subtrees both exist. Simply returning either child would lose the other subtree. The implementation keeps the entire right subtree as the replacement and attaches the entire old left subtree beneath the smallest node in that right subtree.

Start at `root.right` and repeatedly follow `.left`. The final `node` is the leftmost node of the right subtree, also called the inorder successor of the deleted root. It has no left child; otherwise the loop would have continued.

Set `node.left = root.left`. This empty position can safely receive the old left subtree because of the value relationships:

$$
\text{every old-left value} < \text{deleted root value} < \text{every old-right value}.
$$

In particular, every value in the old left subtree is smaller than the leftmost node of the old right subtree. Attaching those values as that node's left subtree therefore respects the BST rule. The right subtree's existing internal relationships are unchanged.

Finally, assign `root = root.right` and return it. The old right-subtree root becomes the top of the replacement subtree; the old left subtree remains reachable through the leftmost node. The deleted node itself is no longer reachable from the returned tree.

This is slightly different from the familiar method that copies the successor's value into the deleted node and then recursively deletes the successor. Here no node value is copied and no second deletion search occurs. Instead, the two surviving subtrees are spliced together directly.

**A two-child example**

Use `root = [5,3,6,2,4,null,7]` and delete `3`. Searching from `5` goes left because `3 < 5`. The node `3` has children `2` and `4`.

Its right subtree is rooted at `4`, and `4` has no left child, so `4` is the leftmost right-subtree node. Assigning `4.left = 2` joins the old left subtree beneath it. Returning the old right root `4` replaces node `3` in `5.left`. The resulting tree has inorder sequence `2,4,5,6,7`, which is exactly the original sorted sequence with `3` removed.

For a deeper successor, imagine the right subtree root has several left descendants. The algorithm promotes the right-subtree root, not the successor itself, but attaches the old left subtree at the successor's formerly empty left pointer. Every ancestor on that left chain remains greater than the successor, and the attached old-left values are smaller than all of them, so the whole structure remains valid.

**Why the returned tree contains exactly the right nodes**

During the search, the ordering property proves that every skipped subtree cannot contain `key`; those subtrees remain unchanged. If the key is absent, recursion eventually reaches `None`, and each caller reconnects the same subtree reference, leaving the tree unchanged.

When the key is found, one node—the matching root—is excluded from the returned structure. In the zero- or one-child cases, all descendants are preserved by returning the existing child. In the two-child case, both original child subtrees are preserved by the splice, and no new node is created. Since values within each retained subtree keep their original ordering and the new cross-subtree attachment obeys the strict inequality above, the result is a valid BST containing every original value except `key`.

## Complexity detail

Let $h$ be the height of the tree and $n$ its number of nodes. The search follows one root-to-node path, costing at most $O(h)$. In the two-child case, the loop then follows a leftward path inside the right subtree. The search prefix and successor path lie along a combined path whose length is bounded by the tree height up to a constant factor, so total time is $O(h)$.

For a balanced BST, $h=O(\log n)$, giving logarithmic time. For a completely skewed tree, $h=O(n)$, giving worst-case $O(n)$ time. The manifest's $O(n)$ time is therefore a valid worst-case bound, while $O(h)$ is the more informative structural bound requested by the follow-up.

Recursive search uses one stack frame per visited level, so auxiliary space is $O(h)$: $O(\log n)$ for a balanced tree and $O(n)$ in the worst case. The successor search itself is iterative and adds only constant space. The implementation creates no new tree nodes.

## Alternatives and edge cases

- **Copy the inorder successor's value:** Replace the target value with the minimum value from its right subtree, then recursively delete that successor. This is standard and correct, but it performs an additional deletion traversal and mutates a node value rather than directly splicing subtrees.
- **Use the inorder predecessor:** The maximum node in the left subtree can play the symmetric role. Attach or copy it consistently while preserving both subtrees.
- **Iterative search with a parent pointer:** This avoids recursion-stack space, but root deletion and reconnecting the parent's correct child require more explicit cases.
- **Key absent:** Search reaches `None`, returns it, and all ancestors reconnect their unchanged child references. The original tree is returned unchanged.
- **Empty tree:** The first condition returns `None`; there is nothing to delete.
- **Deleting a leaf:** Both children are `None`, so the first child case returns `None` and the parent's link is cleared.
- **Only a right child:** Returning `root.right` promotes the right subtree directly.
- **Only a left child:** The second child case returns `root.left` directly.
- **Deleting the overall root:** The caller receives whichever subtree root the deletion case returns, which is why the function's return value may differ from its input root.
- **Immediate right-child successor:** If `root.right` has no left child, it is already the splice point; the old left subtree becomes its left child.
- **Deep successor:** Walking left ends at a node whose left pointer is guaranteed empty, so attaching there never overwrites an existing subtree.
- **Recursion depth:** A tree with `10^4` nodes can be highly skewed. The algorithmic space is correctly $O(h)$, but a Python runtime may need an iterative version or a sufficiently high recursion limit for the deepest legal shape.
