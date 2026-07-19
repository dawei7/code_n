## General
**Symmetry is a relation between two opposite subtrees**

Start with the root's left and right children as one mirrored pair. Two absent nodes mirror each other. Exactly one absent node is a shape mismatch, and two present nodes must have equal values before their descendants can mirror.

The root itself does not need a partner comparison; every possible asymmetry lies between its two child subtrees.

**Outside children pair together, as do inside children**

After a pair matches locally, compare `left.left` with `right.right`, the two outside children. Then compare `left.right` with `right.left`, the two inside children. Pairing left with left would test ordinary equality rather than reflection.

**Every call preserves mirrored positions**

Each recursive call receives nodes occupying mirrored positions around the tree's center and returns true exactly when their complete subtrees mirror one another.

**Trace equal values with asymmetric null placement**

For `[1, 2, 2, null, 3, null, 3]`, both nodes at the second level match, but the left subtree's inside child is present while the right subtree's corresponding inside child is absent. The mirror comparison therefore returns `False`.

**Outside and inside pairs encode mirror structure**

Two mirrored positions match when both are absent, or when both nodes exist with equal values and their outside children mirror each other while their inside children mirror each other. Pairing left-left with right-right and left-right with right-left enforces exactly those relationships.

Applying this test from the root's two children covers every path and its reflected counterpart. Success proves equal values and presence at all mirrored positions; any asymmetry creates a failing pair.

## Complexity detail
Every node participates in at most one mirrored comparison, giving $O(n)$ time. Recursive calls occupy at most one root-to-leaf path on each side, so auxiliary space is $O(h)$.

## Alternatives and edge cases
- **Queue of mirrored pairs:** avoids recursion and remains $O(n)$ time, but may store $O(w)$ nodes at a wide level.
- **Compare ordinary traversals:** fails unless one traversal reverses child directions and preserves null positions.
- **Compare only level values:** can miss asymmetric child placement when values repeat.
- Empty and one-node trees are symmetric. Repeated values do not remove the need to compare exact mirrored structure.
- Recursion uses $O(h)$ stack space; an iterative mirrored-pair queue may use width-proportional space instead.
