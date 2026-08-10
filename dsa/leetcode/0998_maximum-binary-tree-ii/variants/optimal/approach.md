## General

**Use the fact that the new value was appended at the end**

The task is not arbitrary binary-search-tree insertion. The existing tree is the maximum tree of some hidden array `a`, and `val` is appended to the right end of that array. This positional guarantee determines exactly which part of the tree can change.

In a maximum tree, the largest value of an array segment becomes that segment's root. Values before the maximum form the left subtree, and values after it form the right subtree.

Because the appended value is after every original element, it can affect only roots of suffix segments—precisely the right spine of the existing tree. Left subtrees represent elements that appeared before their parent and remain unchanged.

**Case one: the new value is larger than the current root**

If `root is None` or `root.val < val`, the appended value is the largest value in this current segment.

For a nonempty segment, all values represented by `root` appeared before the appended `val`. Therefore, constructing the maximum tree of this segment plus `val` makes:

- `val` the new root;
- the entire old tree the new root's left subtree;
- the right subtree empty, because no element occurs after the appended value.

The expression

`TreeNode(val, root)`

creates exactly that structure: constructor arguments are the new value and left child, with the right child using its default `None`.

The same line also handles a null segment. The new node receives `None` as its left child and becomes a leaf.

**Case two: the current root remains larger**

If `root.val > val`, uniqueness guarantees strict inequality and the current root remains the maximum of this segment after appending `val`. Its left subtree is built from elements before the current maximum, so it is completely unaffected.

The appended value lies in the suffix after the current maximum. That suffix is represented by `root.right`. The correct updated right subtree is therefore:

`self.insertIntoMaxTree(root.right, val)`.

The returned subtree is assigned back to `root.right`, and the unchanged current root is returned.

This recursive step repeats the same reasoning on a smaller suffix until it finds the first right-spine node smaller than `val` or reaches an empty right child.

**What the recursion does structurally**

The algorithm walks down the right spine past every node whose value is larger than `val`. At the first node with a smaller value, it inserts `val` directly above that entire subtree, making the smaller node the new node's left child.

All larger ancestors stay in place. All subtrees not on the searched right-spine path remain untouched. This is the minimum structural change needed to match construction from the appended array.

**Trace when `val` becomes the global root**

Suppose the hidden array is `[1, 4, 2, 3]`, whose maximum-tree root is four, and append five.

At the original root, `4 < 5`. Five is larger than every original value and occurs last, so the method immediately returns a node five with the complete old tree as its left child. This is `Construct([1, 4, 2, 3, 5])`.

No deeper traversal is needed because the comparison at the global root already establishes that the appended value is the new global maximum.

**Trace insertion below a larger root**

Suppose the right spine begins with values five then four, and append three.

- Five remains the root because `5 > 3`, so recurse right.
- Four remains the suffix root because `4 > 3`, so recurse right.
- The right child is null, so create node three there.

The result preserves five and four and places the appended smaller value at the far-right end, matching its array position.

Now suppose the right spine begins five then three, and append four:

- Five remains above because `5 > 4`.
- At node three, `3 < 4`, so create node four with the old node-three subtree as its left child.
- Assign this new node as five's right child.

This matches the suffix array rule: four is the maximum of the old suffix followed by four, and all old suffix elements precede it.

**Why only the right subtree is recursive**

For any current root, its left subtree comes from array positions before that root's maximum element. Appending at the end cannot insert an element into that prefix, so reconstruction leaves it identical.

The right subtree comes from the suffix after the maximum, and the appended value belongs at the end of that suffix. Therefore, the same insertion problem recurs only there.

An algorithm that compares or rebuilds both children would ignore the strongest information in the problem and perform unnecessary work.

**Why the returned tree equals `Construct(b)`**

Use induction on the current suffix tree. For an empty tree or a root smaller than `val`, the new value is the suffix maximum and the returned new root with old tree on the left is exactly the construction rule.

Otherwise, the old root remains the suffix maximum. Its left input segment is unchanged, and by the induction hypothesis the recursive call returns the correct construction for its old right segment with `val` appended. Reattaching that result as `root.right` therefore gives the exact maximum tree for the full current segment.

Applying the argument at the original root proves the method returns `Construct(b)`.

**Mutation and returned-root behavior**

When larger ancestors remain, their `right` pointers are updated in place. If `val` exceeds the original root, the method returns a different root object and the caller must use that return value. The old tree is not discarded; it becomes the new root's left subtree.

## Complexity detail

Let `H` be the height of the tree. The method follows only the right spine and visits at most `H` nodes, so time complexity is `O(H)`. In a balanced tree this may be logarithmic in the number of nodes, while in a skewed tree `H` can equal `N`.

The exact Python implementation is recursive and therefore uses `O(H)` call-stack space in the worst case. It allocates exactly one new tree node. An iterative right-spine implementation can achieve `O(1)` auxiliary space, but recursion itself is not constant-space in Python.

## Alternatives and edge cases

- **Recover the full array and rebuild:** Inorder traversal recovers `a`, after which one can append `val` and reconstruct the maximum tree. This costs `O(N)` time and extra storage instead of exploiting the right spine.
- **Iterative right-spine insertion:** Track a parent while moving right, then splice the new node above the first smaller subtree. It preserves `O(H)` time and uses `O(1)` auxiliary space.
- **Monotonic stack reconstruction:** Useful when building a maximum tree from a complete array, but excessive when inserting one known final element.
- **New value larger than the root:** It becomes the new global root and takes the entire old tree as its left child.
- **New value smaller than every right-spine node:** It becomes the final right child at a null position.
- **New value between two right-spine values:** It is spliced between them, with the smaller suffix becoming its left subtree.
- **Null root:** Although the stated tree is nonempty, the base case correctly creates a one-node tree.
- **Unique values:** Strict comparison is sufficient; equality handling is unnecessary because the appended array is guaranteed unique.
- **Left subtrees:** They are never traversed or modified because appending does not change earlier prefixes.
- **Returned root:** Callers must assign the returned node, since insertion can replace the original root.
