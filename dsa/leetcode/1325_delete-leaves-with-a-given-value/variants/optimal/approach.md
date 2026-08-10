## General

Deleting one target-valued leaf can turn its parent into a new target-valued leaf. That means a top-down check is too early: a node that is not a leaf when first visited may need deletion after its children are removed.

The exact Optimal solution uses recursive postorder traversal. It processes both child subtrees, reconnects their returned roots, and only then decides whether the current node should survive.

**What the recursive return value means**

`removeLeafNodes(root, target)` returns the root of the fully cleaned version of the subtree that originally began at `root`.

The return can be:

- the same node, with possibly updated child pointers, when the node survives; or
- `None` when the entire subtree root is deleted.

This return convention lets a parent update its pointer without separately knowing how many deletions happened below.

**Empty subtree**

If `root is None`, there is nothing to remove, so the function returns `None`. This handles missing children and also allows a generalized empty input tree.

**Cleaning children before the parent**

The source assigns:

`root.left = removeLeafNodes(root.left, target)`

and then performs the symmetric assignment for `root.right`.

Each recursive call completes all cascading deletions in that child subtree. Assigning its return value is essential. If a child root was deleted, the corresponding pointer becomes `None`; if it survived with internal changes, the pointer remains connected to that cleaned subtree.

Only after both assignments does the current node have its final children. At that moment, the test `root.left is None and root.right is None` answers whether it has become a leaf after every lower deletion.

**Deleting the current node**

If the current node is now a leaf and `root.val == target`, the function returns `None`. The parent receives that value and disconnects this node through its own child assignment.

No explicit memory deletion is needed in Python. Removing the tree reference is the logical deletion required by the problem.

If the current node is not a qualifying leaf, it returns `root`. A target-valued internal node survives for now because the task deletes only leaves. However, if all of its descendants are later removed, postorder ensures that transformation has already happened before its test, so it will be deleted in this same call.

**Why one traversal handles repeated rounds**

It may sound as though the problem requires repeatedly scanning the whole tree: delete current leaves, scan again for new leaves, and repeat. Postorder recursion compresses all those rounds into one bottom-up pass.

Consider a chain of three nodes all equal to `target`. The deepest node returns `None`. Its parent then has no children, so it also returns `None`. The top target node receives `None` from its child, becomes a leaf, and returns `None` as well. Cascading deletion flows upward through return values without restarting traversal.

**Why preorder would fail without revisiting**

If the parent were tested before its children, it would still appear to have children and would survive. After deleting those children, a simple preorder algorithm would have already moved past the parent and miss its new leaf status.

Postorder's “left, right, node” sequence exactly matches the dependency: a node's final status depends on the final status of both children.

**Why the result is correct**

For a null subtree, the returned cleaned tree is correct. Assume recursive calls correctly remove every qualifying leaf from both child subtrees, including cascades.

After reconnecting those results, the current node's child pointers describe its final descendants. If it is now a target leaf, it must be removed and returning `None` does so. Otherwise, it must remain, and returning the node with cleaned children is correct.

By induction over subtree height, the returned root contains no target-valued leaf. Every removed node was a target leaf at the moment its descendants had been processed, so no forbidden deletion occurs.

The original root can also disappear. Because the public call returns the recursive result directly, an all-deleted tree correctly becomes `None`.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height.

Each node is entered once, has two child references processed, and performs a constant-time leaf and value test. Total time is $O(n)$.

The recursion stack has at most $O(h)$ frames. A balanced tree uses $O(\log n)$ stack space, while a skewed tree can have $h=n$, giving the manifest's worst-case $O(n)$ auxiliary space.

No separate node collection is allocated. The tree is modified in place through child-pointer assignments.

With up to 3000 nodes, a highly skewed tree can exceed Python's default recursion limit. The asymptotic method remains linear, but an iterative postorder traversal is safer for that extreme shape.

## Alternatives and edge cases

- **Repeated full-tree scans:** Delete current target leaves until no change. It is conceptually simple but can revisit a long chain many times and approach $O(n^2)$.
- **Iterative postorder stack:** It avoids recursion depth limits but requires careful tracking of parents and visited right subtrees.
- **Preorder without revisiting:** It is incorrect because a parent can become a leaf only after descendants are processed.
- **Root itself becomes a target leaf:** The top-level call returns `None`, correctly producing an empty tree.
- **Target-valued internal node:** It survives unless child deletions make it a leaf.
- **Non-target leaf:** It always remains.
- **Chain of target values:** Deletion cascades through returned `None` values in one traversal.
- **Only one target child removed:** The parent remains internal if its other child survives.
- **Empty subtree:** The base case returns `None` without dereferencing it.
- **Input mutation:** Existing node objects are reused, but their left and right pointers may change.
- **Recursion depth:** A 3000-node chain may require an iterative version in ordinary Python settings.
