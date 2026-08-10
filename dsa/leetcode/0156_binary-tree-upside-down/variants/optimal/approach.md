## General

**Understand the permitted tree shape**

The transformation follows the tree's left edge. For every original parent
with a left child:

- that left child moves above the parent;
- the parent's original right child becomes the new left child of that node;
- the original parent becomes its new right child.

The guarantee about right children is what makes this operation well-defined.
Every right child has a left sibling and is a leaf. Therefore, when a parent is
rotated beneath its left child, the right sibling can be attached as a new left
child without carrying an additional subtree that would need another rule.

For the tree represented by `[1,2,3,4,5]`, the left spine is
`1 -> 2 -> 4`. Node four becomes the new root. At its level, five becomes its
left child and two its right child. At the next level, three becomes the left
child of two and one becomes its right child.

**Recurse to the future root first**

The selected solution uses postorder-style recursion along only left links. Its
base case is either an empty tree or a node with no left child. Such a node is
already the bottom of the original left spine, so it will be the root of the
transformed tree and is returned unchanged.

For any other node named `root`, the method first calls itself on `root.left`.
That recursive call completely transforms the lower portion and returns its
new root. The current call stores that result in `new_root` and must not replace
it: every level should return the same deepest-left node upward.

This ordering is important. The original `root.left` relationship is still
available when the recursive call begins. On the way back, the child subtree
has already been transformed, but the object referenced by `root.left` is
still the node that must become the current node's parent in the new
orientation.

**Reverse one local family while unwinding**

After recursion returns, let `child = root.left` conceptually. The source
performs two assignments through that node:

- `root.left.right = root` makes the original parent the child's new right
  child;
- `root.left.left = root.right` makes the original right sibling the child's
  new left child.

These lines implement exactly the problem's level rule. Notice that
`root.right` is read before its link is erased, so the original right child is
not lost.

The source then sets both `root.left` and `root.right` to `None`. Without this
cleanup, the old parent-to-child edges would remain alongside the new
child-to-parent edges. In particular, retaining `root.left` after making that
child point right to `root` would create a cycle. Clearing the links turns the
former parent into a leaf at its new position unless a higher unwind later
attaches its old sibling and parent around it.

**Trace the recursion on a small tree**

Take root one with left child two and right leaf three; node two has left child
four and right leaf five.

The calls descend through one, two, and four. Four has no left child, so it
returns itself as `new_root`.

While the call for two unwinds, it assigns `4.right = 2` and `4.left = 5`,
then clears both links from two. The local result is rooted at four.

While the call for one unwinds, its original left node is still two. It assigns
`2.right = 1` and `2.left = 3`, then clears the original links from one.
Again it returns four. The final structure is rooted at four and serializes as
`[4,5,2,null,null,3,1]`.

The example reveals a subtle point: after the lower transformation, node two
temporarily has cleared links, but the higher call then attaches node three and
node one to it. The recursive unwind constructs the final tree from bottom to
top.

**Why every node is preserved exactly once**

Assume recursively that the subtree beginning at the original left child has
been correctly inverted and that its deepest-left node is returned. The current
call attaches the original right leaf and original parent into the two empty
positions prescribed by the transformation. It then removes the two obsolete
forward edges.

No unrelated subtree is overwritten: by contract, the original right child is
a leaf, and the recursive transformation has prepared the old left child as
the attachment point for this level. Each original left-spine node becomes one
node on the new right spine, and each original right sibling becomes the
corresponding new left leaf.

The base case is already correct, and the local step preserves the claim at
every higher level. Therefore the shared `new_root` is the correct result.
Empty and one-node trees return immediately without mutation.

**Native interface dependency**

The selected source relies on platform-provided `TreeNode` and uses
`Optional[TreeNode]` annotations. In a standalone module, the appropriate
definitions or imports must be present. They are part of the problem harness,
not data structures the solution algorithm is meant to recreate.

## Complexity detail

Let $h$ be the number of nodes on the original left spine, and let $n$ be the
total number of nodes. Under the promised shape, every non-spine node is a
right leaf attached to a spine node, so $h \le n$.

The recursion visits every left-spine node once and performs constant work per
level. It also reattaches each existing right leaf once. Time is $O(n)$.

The selected source is recursive. Its maximum recursion depth is $h$, so its
auxiliary call-stack space is $O(h)$ and can be $O(n)$ for a fully left-skewed
tree. This does not match the manifest's $O(1)$ space claim. The transformation
is in-place with respect to heap nodes—no new tree nodes or collections are
allocated—but recursive stack frames still count as auxiliary space.

## Alternatives and edge cases

- **Iterative pointer rotation:** Walk down the left spine while carrying the previous parent and previous right sibling. It performs the same rewiring in $O(n)$ time with genuine $O(1)$ auxiliary space.
- **Copy into a new tree:** Easier to visualize in some settings, but unnecessary and uses $O(n)$ additional node storage.
- **Breadth-first reconstruction:** Recording levels before rebuilding also costs $O(n)$ space and ignores the simple left-spine structure.
- **Empty root:** The base case returns `None`.
- **Single node:** With no left child, it is already the new root and remains unchanged.
- **Left child without a right sibling:** The source attaches `None` as the new left child, which is valid.
- **Original right leaf:** It is saved through `root.right` before the old links are cleared.
- **Cycle prevention:** Clearing `root.left` and `root.right` is required after reversing the parent relationship.
- **Contract violation:** A right child with its own children would contain subtrees for which the stated transformation gives no preservation rule; correctness relies on the guarantee.
- **Recursion depth:** Although the documented input has at most ten nodes, the asymptotic implementation still uses $O(h)$ stack space.
