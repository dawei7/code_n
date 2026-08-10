## General

**Inverting a tree is the same operation at every node**

The mirror image of a binary tree keeps each node but exchanges everything on
its left with everything on its right. At one nonempty node, that means:

1. recursively invert the original left subtree;
2. recursively invert the original right subtree;
3. attach the inverted original right subtree as the new left child;
4. attach the inverted original left subtree as the new right child.

The empty tree is already its own inverse, so `root is None` returns `None`.
That base case also handles every missing child naturally. A leaf makes two
recursive calls on `None`, receives two `None` results, swaps them, and remains
a leaf.

**Save both recursive results before changing child references**

The exact source evaluates
`l, r = self.invertTree(root.left), self.invertTree(root.right)`. Python
evaluates the right-hand side before assigning `l` and `r`, so both calls begin
from the node's original child references. `l` becomes the root of the already
inverted original left subtree, and `r` becomes the root of the already
inverted original right subtree.

Only after both subtrees are complete does the code execute
`root.left, root.right = r, l`. The simultaneous assignment places the inverted
right subtree on the left and the inverted left subtree on the right. Saving
the references first avoids losing access to one original subtree during the
swap.

Finally, the method returns `root`. It does not construct a replacement node;
the original root object remains the root, with its child links updated.

**Trace the complete seven-node example**

For root value 4, recursion first enters the subtree rooted at 2. Its leaves 1
and 3 each remain unchanged, then node 2 swaps them, becoming a subtree with 3
on the left and 1 on the right. Recursion likewise inverts the subtree rooted
at 7, placing 9 on its left and 6 on its right.

Back at node 4, `l` refers to the inverted tree rooted at 2 and `r` refers to
the inverted tree rooted at 7. Assigning `root.left = r` and `root.right = l`
produces the level-order structure `[4,7,2,9,6,3,1]`.

The traversal is postorder with respect to mutation: children are fully
inverted before the current node swaps them. Python evaluates the left
recursive call before the right one in the tuple expression, but choosing
right first would produce the same final mirror because the two subtrees are
independent until their roots are reassigned.

**Why every node ends in its mirrored position**

For an empty subtree, returning `None` is exactly its mirror. Assume the two
recursive calls correctly mirror the current node's smaller left and right
subtrees. The mirror definition requires the mirrored original right subtree
on the current root's left and the mirrored original left subtree on its right.
The simultaneous assignment does precisely that while preserving the current
node and its value. Therefore the current subtree is correctly mirrored.

Applying this reasoning upward from empty children and leaves proves that the
original root ultimately represents the mirror of the entire tree. Each node
is reached from exactly one parent reference, so no node is skipped or swapped
at multiple recursion levels.

**The operation mutates the given tree**

The same `TreeNode` objects are reused. Only `left` and `right` references are
changed; `val` is never read for a decision and never modified. Any caller
holding another reference to a node will observe its child links after
inversion. Returning the original root reference is therefore sufficient.

Running the method twice restores the original structure. The first call swaps
every pair of child positions, and the second call recursively swaps those
pairs back. This is a useful mental check on the operation, although the
solution calls it only once.

**The source differs from the manifest's traversal description**

The manifest says this branch uses an explicit stack. The exact solution uses
recursive calls and the language call stack. Both visit every node once and
swap child references in place, but their auxiliary-space behavior is
described by tree height for recursion rather than by an explicit container's
maximum contents. This document follows the executable recursive source.

The commented `TreeNode` definition is platform-provided harness structure;
the user is responsible only for `invertTree`. The source also expects
`Optional` and `TreeNode` to be available for its annotations.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Every non-null node is
visited exactly once and performs constant local work, so time is $O(n)$. This
is asymptotically necessary because every node's child references may need to
be exchanged.

The recursion stack contains at most one root-to-leaf path, using $O(h)$
auxiliary space. For a balanced tree this is $O(\log n)$; for a skewed tree it
is $O(n)$, which matches the manifest's worst-case linear space. No new tree
nodes or copied subtrees are allocated.

## Alternatives and edge cases

- **Iterative depth-first traversal:** Keep an explicit stack of nodes, pop one, swap its children, and push the non-null children. It avoids recursion depth limits, takes $O(n)$ time, and is the traversal named by the manifest.
- **Breadth-first traversal:** Use a queue and swap nodes level by level. It is equally correct and linear but can hold an entire wide level, using $O(n)$ space in the worst case.
- **Direct recursive tuple assignment:** Write `root.left, root.right = invert(root.right), invert(root.left)`. Python's right-hand-side evaluation can make this safe, but named `l` and `r` make the original-subtree relationship clearer.
- **Empty tree:** The base case returns `None` immediately, with no field access.
- **One node:** Both recursive children are `None`; swapping them leaves the node unchanged and returns that same object.
- **Only one child:** The existing subtree is recursively inverted and moves to the opposite side; the missing child moves to its former position.
- **Skewed tree:** Inversion changes a left-only chain into a right-only chain or vice versa. Recursive depth can approach $n$ and may exceed Python's default recursion limit on inputs larger than this problem's bound.
- **Duplicate node values:** Values do not identify nodes or affect structure, so duplicates are irrelevant.
- **Shared or cyclic references:** The contract supplies a proper tree. The recursion assumes no cycles and no child subtree shared by two parents.
- **Input preservation:** This method intentionally does not preserve child links. Callers requiring the original tree must deep-copy it before invoking the solution.
