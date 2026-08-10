## General

**Rotate the left spine without recursion**

The competitive solution performs the transformation in place while walking
from the original root down through left children. It keeps three conceptual
pieces of state:

- `p` is the original-spine node currently being processed;
- `parent` is the already processed original parent, which becomes the new
  right child of `p`;
- `parent_right` is that parent's original right child, which becomes the new
  left child of `p`.

Initially `p` is the root and both carried values are `None`. This matches the
future position of the original root: after inversion it has no new left child
from an earlier right sibling and no new right child from an earlier parent.

Each loop iteration converts one original node into its final local
orientation, then advances to its original left child.

**Save every link before overwriting it**

The first statement inside the loop is `left = p.left`. This saves the next
node on the original left spine. It must happen before `p.left` is overwritten;
otherwise the algorithm would lose access to the unprocessed remainder.

Next, `p.left = parent_right` installs the original right sibling from the
previous level as `p`'s new left child. On the first iteration,
`parent_right` is `None`, correctly clearing the original root's left link in
its eventual leaf position.

Then `parent_right = p.right` saves the current node's original right child.
That saved leaf is not attached immediately. It belongs as the new left child
of the next original left node, so it must be carried into the next iteration.
This assignment occurs before `p.right` is changed, preventing loss of the
subtree.

Finally, `p.right = parent` reverses the left-spine relationship: the processed
original parent becomes the current node's new right child.

**Advance all roles together**

After rewiring `p`, the source sets `parent = p` because this node will be the
new right child at the next level. It then sets `p = left` to move to the saved
original left child.

At the start of every iteration, the following invariant holds:

- nodes above `p` on the original left spine have been placed into their final
  relationships;
- `parent` is the root of that processed chain and must become `p.right`;
- `parent_right` is the original right sibling that must become `p.left`;
- the untouched original subtree from `p` downward is still reachable.

The order of assignments maintains all four statements. This is why the three
variables are not arbitrary bookkeeping; each protects a relationship that
would otherwise be destroyed during in-place mutation.

**Trace the five-node example**

Start with one as `p`, and with two and three as its original children.

During the first iteration, save two in `left`, set `1.left` to `None`, save
three in `parent_right`, and set `1.right` to `None`. Then carry one as
`parent` and move `p` to two.

During the second iteration, save four. Set `2.left = 3`, save five as the new
`parent_right`, and set `2.right = 1`. Then carry two as `parent` and move to
four.

During the third iteration, the saved next-left link is `None`. Set
`4.left = 5` and `4.right = 2`. Carry four as `parent`, then move `p` to
`None`.

The loop stops and returns `parent`, which is four. The resulting tree is
`[4,5,2,null,null,3,1]`.

This trace also explains why the algorithm does not return `p`: after the final
advance, `p` is `None`. `parent` holds the last processed node, which was the
deepest original left node and is now the new root.

**Why the transformation is complete**

At one level, the saved original left child is the next node to process, the
saved original right child is carried to that child's future left position,
and the original parent becomes that child's future right position. These are
exactly the three transformation rules.

The contract guarantees that every original right child is a leaf and has a
left sibling. Consequently, carrying it as one pointer is sufficient; there
are no right-child descendants requiring separate placement.

When the loop finishes, every node on the original left spine has been
processed. Every permitted right leaf was carried exactly once and attached at
the following level. Old forward links were overwritten by their final
relationships, so no cycle remains. Thus `parent` is the correct new root.

For an empty input, the loop never executes and `parent` remains `None`. For a
single node, one iteration clears its already-empty links, assigns it to
`parent`, and returns the same node.

**Source-supplied node class**

The competitive file includes its own `TreeNode` definition before the
selected `Solution`. In the native platform contract, tree nodes are normally
provided by the harness. The algorithm needs only readable and writable
`left` and `right` attributes; it allocates no new node.

## Complexity detail

Let $n$ be the number of nodes in the tree.

The loop processes each original left-spine node once. Under the guaranteed
shape, every other node is a right leaf paired with one of those nodes and is
reattached in constant work. Total time is $O(n)$.

Only `p`, `parent`, `parent_right`, and `left` are stored, regardless of tree
size. The mutation reuses the existing nodes and avoids recursion, so auxiliary
space is $O(1)$. These bounds match the manifest.

The source comment above the selected class also states $O(n)$ time and $O(1)$
space. The later `Solution2` is recursive and has a different space profile,
but it is not the selected implementation described here.

## Alternatives and edge cases

- **Recursive unwind:** Descend to the deepest left node, then attach each old right sibling and parent while returning. It is elegant but uses $O(h)$ call-stack space.
- **Store the spine explicitly:** Pushing nodes into a list and rebuilding backward is straightforward, but adds $O(h)$ storage that the pointer method avoids.
- **Construct new nodes:** Preserves the input tree but uses $O(n)$ extra space and is not required.
- **Empty tree:** No iteration occurs, and `None` is returned.
- **One node:** It becomes `parent` in one iteration and is returned unchanged in identity.
- **Missing right sibling:** `parent_right` can be `None`, producing no new left child at the following level.
- **Save-before-overwrite rule:** Both `p.left` and `p.right` must be captured before their assignments, or unprocessed nodes would be lost.
- **Original right node with children:** This violates the stated guarantee; the one-pointer carry is designed for right leaves.
- **Return variable:** The new root is `parent`, not `p`, because `p` advances to `None` at termination.
- **In-place side effect:** The original tree object is destructively rewired; callers retaining references to its nodes will observe their new relationships.
