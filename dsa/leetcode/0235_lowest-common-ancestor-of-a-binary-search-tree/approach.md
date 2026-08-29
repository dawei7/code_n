## General

**Use value order to locate the first split point**

In a binary search tree with unique values, every value in a node's left
subtree is smaller than the node's value, and every value in its right subtree
is larger. At a current node, the two targets have only three meaningful
configurations:

- both target values are larger, so both nodes lie in the right subtree;
- both target values are smaller, so both nodes lie in the left subtree;
- the current value lies between the target values, or equals one of them, so
  the target paths split at the current node.

The lowest common ancestor is the first node encountered from the root where
the targets no longer lie strictly in the same child subtree.

**Normalize the target order with `min` and `max`**

The caller may provide `p` and `q` in either value order. The expression
`min(p.val, q.val)` is the lower target value, and
`max(p.val, q.val)` is the higher target value.

If `root.val < min(p.val, q.val)`, the current value is smaller than both
targets. BST ordering places both target nodes in `root.right`, so the current
root cannot be their lowest common ancestor: a deeper common ancestor exists
inside that right subtree. The loop assigns `root = root.right`.

If `root.val > max(p.val, q.val)`, the current value is larger than both
targets, so both lie in `root.left`; the loop descends left for the symmetric
reason.

Otherwise the current value is in the inclusive interval between the two
target values. Either one target is on each side, or the current node is itself
one of the targets. In both cases, the current node is the LCA and is returned.

The source recomputes `min` and `max` on each iteration. Since each operation
compares only two integers, this is constant work. They could be stored once,
but that would not change the algorithm or its complexity.

**Why equality must return the current node**

The LCA definition allows a node to be a descendant of itself. If
`root.val == p.val`, then current `root` is node `p` because values are unique.
The other target lies somewhere in `p`'s subtree at the point where the search
reaches it, so `p` is a common ancestor and no descendant can be an ancestor of
`p` itself. The same reasoning applies when the current node equals `q`.

Using strict `<` and `>` in the descent conditions ensures equality falls into
the return branch rather than incorrectly moving past a target.

**Trace the two reference relationships**

In the tree rooted at 6 with targets 2 and 8, the lower target is 2 and the
higher is 8. Root value 6 lies between them, so their search paths diverge
immediately and node 6 is returned.

With targets 2 and 4, root 6 is greater than both, so the method descends left
to node 2. There, the current value equals the lower target and lies in the
inclusive target interval. Node 2 is returned, correctly using the rule that a
target can be its own ancestor.

If both targets were 7 and 9, root 6 would be below both and the method would
descend right to node 8. Value 8 lies between 7 and 9, making it their first
split and therefore their LCA.

**Why descending cannot skip the LCA**

When both target values are smaller than the current value, both target nodes
are in the left subtree. Any common ancestor lower than the current node must
also lie there, and the true lowest common ancestor cannot lie in the right
subtree. Discarding the current node and right subtree is therefore safe. The
same argument holds when both targets are larger.

The loop descends only while both targets share one child direction. The first
node where they split is an ancestor of both, since one target is in each child
subtree. No child of that node can contain both targets, so no lower node can be
a common ancestor. If the node equals a target, the self-descendant rule gives
the same conclusion. Hence the returned node is both common and lowest.

**The unbounded loop relies on valid-tree guarantees**

The source uses `while 1` and accesses `root.val` without checking for `None`.
The contract guarantees that both distinct target nodes exist in the supplied
BST. Following their shared search direction must eventually reach their split
point or one target, so the method returns before `root` can become `None`.
Missing targets or a non-BST input would violate that assumption.

Assignments to `root` move only the method's local reference. No child link or
value is modified. The quoted `'TreeNode'` annotations are forward references
to the platform-provided helper type.

## Complexity detail

Let $h$ be the tree height. Each iteration moves down exactly one level, and
the method stops no later than the deeper target path, so time is $O(h)$. This
is $O(\log n)$ for a balanced BST and $O(n)$ for a skewed BST.

The iterative method retains only the current node reference and fixed target
references, using $O(1)$ auxiliary space. It does not allocate a traversal
stack or recurse.

## Alternatives and edge cases

- **Recursive BST descent:** Apply the same three cases recursively. It is concise and still takes $O(h)$ time, but uses $O(h)$ call-stack space instead of the exact source's constant space.
- **General binary-tree LCA:** Recursively search both subtrees and combine returned targets. It ignores BST ordering and can take $O(n)$ time even when the ordered search path is short.
- **Root is the LCA:** If target values lie on opposite sides of the initial root, the first iteration returns immediately.
- **One target is an ancestor of the other:** Equality places the ancestor target in the return branch, as required by the LCA definition.
- **Both targets in the left subtree:** The loop repeatedly descends left only while both values remain below the current value.
- **Both targets in the right subtree:** The symmetric lower-than-both condition repeatedly descends right.
- **Targets supplied in reverse order:** `min` and `max` remove any dependency on parameter order.
- **Negative and large values:** Only integer ordering matters; sign and magnitude do not alter the search.
- **Unique-value guarantee:** Equality with a target value identifies that exact node. Duplicate BST values would require an identity-aware policy not present in this solution.
- **Targets absent from the tree:** The source has no failure return and could dereference `None`; the contract explicitly excludes this case.
- **Input preservation:** The algorithm changes only its local `root` variable and leaves the tree topology and all node values intact.
