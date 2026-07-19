## General
**Compare both targets with the current split point**

At any node, all left-subtree values are smaller and all right-subtree values are larger. If both targets are smaller, continue left; if both are larger, continue right.

**The first split is the lowest shared ancestor**

The first node where the targets lie on different sides—or where one target equals the current value—is their lowest common ancestor.

Before every iteration, the current subtree contains both targets. Moving to one child is safe only when BST comparisons prove both targets lie in that child.

For targets `2` and `4` under root `6`, both are smaller, so move to `2`. Because `2` equals one target, it is an ancestor of both and is returned. Every skipped ancestor had both targets in one proper child; the first non-skipped node is therefore the lowest node containing both.

## Complexity detail
The search follows one root-to-node path, taking $O(h)$ time and $O(1)$ iterative space.

## Alternatives and edge cases
- **General binary-tree LCA:** works but may inspect every node and ignores ordering.
- **Stored root paths:** uses $O(h)$ extra space.
- One target may be an ancestor of the other; target order does not matter.
