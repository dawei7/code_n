## General

Two trees are the same only when two conditions hold simultaneously:

1. every corresponding position is either empty in both trees or occupied in both; and
2. every pair of occupied corresponding nodes has the same value.

The selected solution checks these conditions recursively. Each call compares one position in the first tree with the same position in the second tree, then delegates the left and right subtrees to identical calls.

**The `p == q` shortcut**

Under the standard platform `TreeNode` class, nodes do not define structural equality, so `p == q` is effectively an object-identity comparison. It is true in two useful cases:

- both references are `None`; or
- both references point to the exact same node object.

Both cases are immediately safe. Two absent subtrees are structurally identical. If both references are the same real node, they lead to the exact same descendants and values, so that entire subtree is necessarily the same as itself.

This line should not be misunderstood as comparing two independently allocated nodes by value. For ordinary `TreeNode` objects with equal values, `p == q` remains false unless they are the same object, and the method continues with explicit checks.

If a surrounding application supplied a custom `TreeNode.__eq__`, the meaning of `==` could differ. The canonical challenge node uses identity behavior.

**Rejecting a structural or value mismatch**

After the identity shortcut fails, `p is None or q is None` means exactly one position is empty. The structures differ, so the answer is false even if all previously visited values matched.

If both nodes exist but `p.val != q.val`, their contents differ at this corresponding position, so the trees are not the same.

Combining these tests in one conditional is safe because Python evaluates `or` left to right and short-circuits. If `p` is `None`, it never evaluates `p.val`; if `q` is `None`, it never needs a value comparison that would dereference it.

**Comparing both child directions**

Once the current nodes are known to exist and have equal values, the method checks:

`isSameTree(p.left, q.left)`

and then:

`isSameTree(p.right, q.right)`.

Left must be paired with left and right with right. Cross-pairing would test whether trees are mirrors, a different property. Even if a left and right child happen to have equal values, their positions are part of structure and cannot be exchanged.

The `and` operator short-circuits. If the left subtrees differ, the right subtrees are not visited because one false component already proves the whole conjunction false. If the left sides match, the right sides must still be checked.

**Trace of a structural mismatch**

Compare `[1,2]` with `[1,null,2]`. The roots are distinct objects but both exist and both contain one, so recursion enters their left children.

The first left child is node two, while the second left child is `None`. The identity shortcut is false, and the missing-node condition returns false. This rejects the trees even though each serialized tree contains values one and two. Same multiset of values is not sufficient; positions matter.

**Trace of a value mismatch**

For `[1,2,1]` and `[1,1,2]`, root values match. The left recursive call compares nodes valued two and one and returns false. Because of short-circuiting, no further comparison is needed.

**Why the recursion is correct**

For empty corresponding positions or one shared object, returning true is correct. If exactly one node exists or values differ, returning false is correct.

In the remaining case, current values and occupancy match. The full subtrees are identical exactly when their left subtrees are identical and their right subtrees are identical. The two recursive results test precisely those smaller conditions. Structural induction from empty subtrees therefore proves the result for every tree.

The method never mutates either tree. It only reads references and values.

## Complexity detail

Let $n$ be the number of corresponding nodes examined in the worst case, bounded by the total size of either equal tree. When trees are identical but separately allocated, every node position is visited, so time is $O(n)$. A mismatch may short-circuit earlier. If roots are the same object, the identity shortcut returns in $O(1)$ time.

The recursion stack follows one pair of root-to-current paths at a time. If $h$ is the maximum height reached among the compared trees, auxiliary space is $O(h)$, matching the manifest. Balanced trees use $O(\log n)$ stack depth; skewed trees use $O(n)$.

No result collection is built, and the returned Boolean occupies constant space.

## Alternatives and edge cases

- **Breadth-first paired queue:** Enqueue corresponding node pairs and check them iteratively. It avoids recursion but may store an entire level, using $O(w)$ space for maximum width $w$.
- **Depth-first explicit stack:** Preserves $O(h)$ storage without recursion-limit concerns.
- **Serialize with null markers:** Equal canonical serializations imply equal trees, but building them costs $O(n)$ extra memory and null markers are essential to preserve structure.
- **Both roots empty:** `p == q` is true, correctly returning true.
- **One root empty:** The second condition rejects the pair immediately.
- **Same object:** Identity permits a constant-time result; no descendant traversal is necessary for an acyclic tree.
- **Duplicate values:** Equal values at different nodes cause no ambiguity because comparisons are position-based.
- **Different shapes with equal traversal values:** The `None` checks reveal positional differences that a value-only traversal could miss.
- **Very deep trees:** The challenge bound of 100 is safe for Python recursion; larger skewed external trees may favor an explicit stack.
