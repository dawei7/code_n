## General
**The original left spine becomes the new right spine in reverse**

Initialize `current = root`, `parent = None`, and `parent_right = None`. At each current node, save `next_left = current.left` and `next_right = current.right` before overwriting either pointer. `next_left` continues the spine and the final nonnull current becomes the new root.

**Two carried references encode the new children of the next spine node**

Set `current.left = parent_right` and `current.right = parent`. Then advance `parent = current`, `parent_right = next_right`, and `current = next_left`. On the next iteration, the previous parent's right sibling becomes the new left child, while the flipped parent chain becomes the new right child.

Saving both original children first prevents the remaining spine or sibling subtree from becoming unreachable.

**Processed and unprocessed portions stay reachable through separate variables**

Before processing `current`, `parent` is the already flipped upper chain that must attach on the right, and `parent_right` is the sibling subtree that must attach on the left. No pointer needed by the unprocessed left spine has been lost.

**Trace two spine rotations**

For `[1,2,3,4,5]`, processing `1` carries right sibling `3`; processing `2` makes `3` its eventual left attachment and carries `5`; processing `4` attaches `5` left and flipped chain `2 -> 1` right, producing root `4`.

**The flipped prefix is final before the walk advances**

Before an iteration, `parent` is the already flipped prefix and `parent_right` is the sibling that must become the current node's new left child. Saving the current left child and right sibling first prevents either unprocessed link from being lost. Assigning `root.left = parent_right` and `root.right = parent` then gives the current node its final two outgoing links.

Advancing down the saved left child extends the finalized prefix by one node. At the end, the deepest original left child heads the complete flipped structure and is therefore the new root.

## Complexity detail
The walk visits each left-spine node once; under the input structure, every other node is its attached right leaf, so all tree nodes are handled in $O(n)$ time. Only a fixed set of pointers is stored.

## Alternatives and edge cases
- **Recursive flip:** closely follows the tree definition but uses $O(h)$ call-stack space.
- **Construct a new tree:** is easier to visualize but loses node identity and uses $O(n)$ memory.
- **General tree rotation logic:** is unnecessary because the problem guarantees the right-child structure.
- Empty and one-node trees return unchanged. A pure left chain becomes a pure right chain, while paired right leaves become left children after the flip.
- The transformation relies on the stated right-child restriction; arbitrary right subtrees would not fit this local sibling-to-left mapping.
