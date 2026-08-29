## General

**A recursive call returns the surviving subtree root**

Deleting a node changes the pointer held by its parent. The helper `dfs(node)` therefore returns either the same node after cleaning its descendants or `None` when that node is deleted.

The parent assigns these returned values back into `root.left` and `root.right`. This physically disconnects deleted child roots and preserves surviving, possibly modified subtrees.

**Use postorder so children are already settled**

The helper first recursively processes both children, then decides what to do with the current node. This postorder is crucial when the current node will be deleted: its surviving children become new forest roots, but only after all requested deletions inside those child subtrees have already been applied.

After:

`root.left, root.right = dfs(root.left), dfs(root.right)`,

each pointer is either a valid surviving subtree or `None`. No later work below those children is necessary.

**Keep an undeleted node attached**

If `root.val not in s`, the node survives. Returning `root` tells its parent to retain the connection. Any deleted descendants have already been removed from its child pointers, so the returned subtree contains no forbidden node.

The surviving node is not immediately appended to the forest. It still has a surviving parent unless that parent is later deleted. A node becomes a forest root only when it has no surviving parent.

**Promote children of a deleted node**

If the current value belongs to the deletion set, the current node must disappear. Each non-null processed child no longer has a surviving parent, so it becomes the root of a new tree and is appended to `ans`.

The helper then returns `None`, causing the deleted node’s parent to remove its pointer to this node. The deleted node itself is never placed in the answer.

If a deleted node’s child was also deleted, that recursive call already returned `None` and may have promoted deeper surviving descendants. The current node therefore does not append a deleted child or duplicate those deeper roots.

**Handle the original root separately**

The original root has no parent that could promote it. After `dfs(root)` finishes, a truthy return means the original root survived and must be appended to `ans`. If it was deleted, the helper already appended each surviving child subtree and returned `None`.

This rule gives every forest tree exactly one root. A surviving node is appended either because its parent was deleted or because it is the surviving original root, never both.

**Why the produced forest is correct**

By induction on a subtree, `dfs` removes every requested node inside it and returns the root exactly when that root survives. When the root is deleted, every surviving child subtree is disconnected and recorded as a new component. When it survives, those child subtrees remain attached.

Applying this reasoning at the original root removes all and only requested nodes, retains every legal parent-child edge, and records every connected component once. Thus `ans` is precisely the required forest, in an allowed arbitrary order.

## Complexity detail

Let $N$ be the number of tree nodes and $D$ the length of `to_delete`. Building set `s` costs $O(D)$ expected time and space. DFS visits each node once and performs expected constant-time membership lookup, costing $O(N)$.

Total time is $O(N+D)$. The deletion set uses $O(D)$ space, recursion can reach $O(N)$ depth in a completely skewed tree, and the answer can contain $O(N)$ roots. The stated space bound is therefore $O(N+D)$.

The method mutates child pointers of the supplied tree rather than copying nodes. Output trees reuse the original node objects.

## Alternatives and edge cases

- **Preorder with parent flag:** Pass whether the current node is a potential root, append it when appropriate, and recursively process children. This works but still must return or clear deleted child pointers.
- **Breadth-first processing:** A queue can delete links iteratively, but tracking parents and newly promoted roots is more cumbersome than postorder returns.
- **Repeated list membership:** Checking `root.val in to_delete` directly would cost up to $O(D)$ per node; converting to a set provides expected constant-time tests.
- **Delete nothing:** DFS returns the intact root, which is appended as the only forest tree.
- **Delete the original root:** It is not appended; each surviving processed child becomes a new root.
- **Delete a leaf:** Its helper returns `None` and adds no children, simply removing the leaf pointer.
- **Delete adjacent parent and child:** The child’s surviving descendants are promoted during its own call; the parent sees `None` and does not duplicate them.
- **Delete every node:** Every call returns `None` and no surviving child is appended, producing an empty forest.
- **Empty root:** The helper returns `None` and the answer remains empty.
- **Distinct node values:** Set membership by value uniquely identifies the intended nodes.
- **Arbitrary result order:** Postorder promotion order is acceptable because the contract imposes no ordering.
- **Tree mutation:** Callers needing the original tree structure must copy it before invoking this method.
