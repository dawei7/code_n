## General
**Match one pair of roots at a time.** Two missing nodes match. If exactly one node is missing, or their values differ, the subtrees cannot be flip equivalent. Otherwise their roots already agree, and only their children remain to be matched.

**Try the two meanings of a flip.** The subtrees match if either the left children match and the right children match without flipping, or the first left child matches the second right child and the first right child matches the second left child after a flip. Apply this rule recursively.

The base cases exactly characterize empty and unequal roots. For equal roots, every valid transformation either flips that root or does not; the two recursive alternatives cover those exhaustive choices. By induction on subtree size, a branch returns `true` exactly when its paired subtrees are flip equivalent. Unique values cause an incorrectly paired child root to fail immediately, so nodes are not repeatedly explored.

## Complexity detail
Across successful and failed orientations, unique node values let the recursion examine $O(n)$ nodes. The call stack follows at most one root-to-leaf path at a time and uses $O(h)$ space.

## Alternatives and edge cases
- **Canonical subtree serialization:** Recursively canonicalize the two child strings into a fixed order and compare the root serializations. It is correct, but repeated immutable-string concatenation can take $O(n^2)$ time on a skewed tree.
- **Repeated value lookup:** With unique values, find each matching node in the other tree and compare its unordered pair of child values. Repeating a full tree search for every node is correct but takes $O(n^2)$ time.
- **Canonical child ordering by root value:** With unique values, treat a missing child as a sentinel and compare smaller-root children together. This also yields a linear recursive test but relies directly on the uniqueness guarantee.
- **Breadth-first paired states:** A queue can process corresponding subtree pairs iteratively, though it still must choose flipped or unflipped child alignment.
- **Both trees empty:** They are flip equivalent without any operation.
- **Only one tree empty:** No flip can create or remove a node.
- **Different root values:** Flips change child positions only, never node values.
- **One child:** A flip may move that child from left to right or conversely.
