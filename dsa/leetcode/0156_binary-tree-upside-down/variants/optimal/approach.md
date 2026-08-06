## General

**Reverse the original left spine in place**

The deepest node on the original left spine becomes the new root. While walking down that spine, carry `parent`,
the portion already flipped, and `parent_right`, the previous node's original right child.

Before changing a node, save its original left child in `following`. Then assign `current.left = parent_right` and
`current.right = parent`. The first assignment moves the original sibling into its required new left position; the
second makes the former parent the new right child. Save the current node as the next `parent`, carry its untouched
original right child in `parent_right`, and continue through `following`.

At the start of each iteration, `parent` is a completely rewired prefix and `parent_right` is exactly the sibling
that must become the current node's new left child. Saving the original left link before overwriting pointers keeps
the unprocessed spine reachable. Consequently each completed node has its final two outgoing links, and the last
processed spine node is the root of the entire transformed tree.

## Complexity detail

The loop visits every node on the left spine once. Under the contract, every node outside that spine is a right leaf
handled through its parent's pointer update, so the total time is $O(n)$. The fixed set of carried references uses
$O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recursive flip:** mirrors the structural definition but consumes $O(h)$ call-stack space for tree height $h$.
- **Construct a new tree:** uses $O(n)$ extra space and fails to preserve the original node identities.
- **General tree rotation:** is unnecessary because every right child is guaranteed to be a leaf with a left
  sibling.
- An empty or one-node tree is returned unchanged.
- A pure left chain becomes a pure right chain.
- Each original right leaf becomes the left child of its former left sibling after the flip.
- The local rewiring relies on the source's right-child restriction and is not valid for arbitrary right subtrees.
