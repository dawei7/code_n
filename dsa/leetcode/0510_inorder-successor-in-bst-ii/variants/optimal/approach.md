## General
**Descend when a right subtree exists**

In inorder traversal, a node is followed by the first node visited in its right subtree. Move once to `node.right`, then repeatedly follow `left` links. The final node is the minimum value in that subtree and therefore the successor.

**Otherwise climb until leaving a left branch**

Without a right subtree, the traversal has finished the node and everything below it. Climb through parent links while the current node is its parent's right child; each such parent has already been visited before its right subtree. The first parent reached from a left child has not yet been visited, so it is the successor.

**Why a missing parent means no successor**

If climbing passes every ancestor and reaches `null`, the original node lies on the right boundary up to the root. All nodes in the tree occur no later than it in inorder order, making it the maximum and leaving no successor.

## Complexity detail
The algorithm follows at most one downward path or one upward path, each bounded by tree height `h`, for $O(h)$ time. It uses only node references and therefore $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Traverse from the root using BST values:** can track the lowest greater ancestor in $O(h)$ time, but the root is not provided and would first require climbing to it.
- **Full inorder traversal:** is correct but takes $O(n)$ time and $O(h)$ stack space to locate one successor.
- **Threaded or explicitly linked inorder structure:** makes successor queries constant time but requires modifying or augmenting the tree.
- **Right child present:** even a deep left chain inside that subtree must be followed to its minimum.
- **Node is a left child:** its parent is the successor when there is no right subtree.
- **Maximum node:** climbs beyond the root and returns `null`.
- **Single-node tree:** has no successor.
