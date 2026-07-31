## General

**Use the tree's mirror symmetry.** Reversing one level pairs its leftmost node with its rightmost node, its second node with its second-to-last node, and so forth. In a perfect tree, these pairs can be reached without collecting an entire level: start with the root's left and right children and traverse them as mirrors.

**Descend in crossed pairs.** For a mirrored pair `(left, right)`, the next outer pair is `left.left` with `right.right`, while the next inner pair is `left.right` with `right.left`. These recursive calls cover every node pair at the next level exactly once. A boolean records whether the current level is odd; when it is, swap the two values before descending.

The first pair lies on level 1, so swapping begins immediately and alternates at each recursive depth. Mirror pairing is precisely the left-to-right reversal relation, and even levels are visited without modification. Because only values are exchanged, every node and edge remains in its original structural position.

## Complexity detail

Each non-root node belongs to exactly one mirrored pair and is visited once, giving $O(n)$ time. The recursion depth equals the tree height $h=O(\log n)$ for a perfect tree, so the auxiliary space is $O(\log n)$.

## Alternatives and edge cases

- **Breadth-first traversal:** Collecting each level and swapping values from both ends is also $O(n)$ time, but its queue can contain $O(n)$ nodes.
- **Repeated level searches:** Traversing from the root separately for each odd level is correct but revisits upper subtrees and costs $O(n\log n)$ over a perfect tree.
- **Single node:** There is no odd level, so the root is returned unchanged.
- **Repeated values:** Swapping equal values has no visible effect but remains correct.
- **Deepest odd level:** Leaf values are swapped normally; no child access occurs after the base case.
- **Structure preservation:** Only `val` fields change; child references must not be exchanged.
