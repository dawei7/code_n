## General

**Use temporary return links instead of a stack**

Ordinary preorder needs to remember where to continue after finishing a left subtree. Recursion or an explicit stack stores that information externally. Morris traversal stores it temporarily inside otherwise null right pointers of the tree.

`curr` is the node whose preorder work is next. The algorithm distinguishes whether `curr` has a left child.

If there is no left child, preorder can immediately append `curr.val` and continue to `curr.right`. There is no left subtree to postpone the right side behind.

If a left child exists, the algorithm finds `node`, the rightmost node in that left subtree. This node is the inorder predecessor of `curr` and is the last node encountered before traversal should return to `curr`’s right side.

**First encounter with a predecessor**

The inner loop follows right links until either:

- `node.right` is `None`, meaning no thread exists yet; or
- `node.right == curr`, meaning this predecessor was threaded to the current node earlier.

On the first encounter, `node.right` is null. The algorithm appends `curr.val` now, because preorder processes the root before its left subtree. It then assigns `node.right = curr`, creating a temporary return link, and moves `curr` to `curr.left`.

The left subtree can now be traversed without a stack. When traversal eventually reaches its rightmost node and follows the temporary link, it returns to the original current node.

**Second encounter removes the thread**

When the predecessor search finds `node.right == curr`, the left subtree has been fully processed. The root value must not be appended again; it was already emitted before descending.

The source restores `node.right = None`, recovering the original tree, and moves to `curr.right`.

Every temporary modification therefore has a matching removal before traversal leaves that region.

**Why the order is root-left-right**

For a node without a left child, its value is emitted and traversal proceeds right.

For a node with a left child, its value is emitted when the thread is created, then `curr` enters the left subtree. The only route back is the predecessor thread, which is reached after all nodes in that left subtree have followed the same traversal rules. On the second encounter, the thread is removed and traversal enters the right subtree.

Thus every subtree contributes its root, then its left subtree, then its right subtree.

**Why values are neither omitted nor duplicated**

Every real node eventually becomes `curr`. A node is appended either:

- in the no-left-child branch; or
- on the first predecessor encounter when it has a left child.

The second predecessor encounter deliberately performs no append. These cases are mutually exclusive for each visit role, so each node’s value appears exactly once.

For an empty tree, `curr` is null and the result remains empty. For a single node, the no-left branch appends it and moves to null.

**Why the tree is restored**

Only a predecessor whose original right pointer is `None` receives a thread. The later search recognizes that exact link back to `curr` and resets it to `None`. No original non-null right child is overwritten.

After successful traversal, every pointer has its original value. During execution the tree is temporarily threaded, so concurrent readers or exceptions between creation and removal could observe a modified structure; the usual problem setting assumes uninterrupted exclusive traversal.

## Complexity detail

Let $n$ be the number of nodes.

The predecessor search creates the appearance of nested work, but each relevant right edge is followed only a bounded number of times: while discovering a predecessor and later while returning to remove its thread. Across the entire traversal, that totals $O(n)$ pointer operations.

The algorithm stores `curr`, `node`, and scalar loop state. Excluding the returned list, auxiliary space is $O(1)$. This is tighter than the manifest’s $O(h)$ bound; $O(1)$ is of course also an upper bound within $O(h)$ for nonempty trees, but it is the informative exact auxiliary complexity of this source.

The result list contains $n$ values, so total additional storage including required output is $O(n)$. The source comment’s $O(1)$ space uses the standard output-excluded convention.

## Alternatives and edge cases

- **Recursive preorder:** Append root, recurse left, recurse right. It is simplest but uses $O(h)$ call-stack space.
- **Explicit stack:** Push right before left. It avoids temporary tree mutation while using up to $O(h)$ or $O(n)$ stack space.
- **Visited-flag stack:** Encodes entry and processing phases explicitly, making traversal order configurable at the cost of extra records.
- **Empty tree:** The outer loop skips and returns `[]`.
- **No left child:** No thread is needed; the algorithm emits and follows the real right link.
- **Left-only chain:** Each ancestor receives a predecessor thread, and every thread is later removed.
- **Right-only chain:** Every node takes the simple branch, so traversal behaves like a linear scan.
- **Second encounter:** Appending there would duplicate every node that has a left subtree.
- **Pointer restoration:** Omitting `node.right = None` would leave cycles in the tree after traversal.
- **Identity comparison:** The source uses `node.right != curr`; standard `TreeNode` equality is identity-based. An overloaded structural equality method could make identity-oriented comparison safer.
- **Manifest looseness:** The selected primary `Solution` is Morris traversal with $O(1)$ auxiliary space; the later `Solution2` is the $O(h)$ stack alternative.
- **Temporary mutation risk:** An exception before thread removal could leave the input altered, even though normal completion restores it.
