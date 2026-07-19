## General
**Use the search-tree ordering to discard whole sides**

If a node value is below `low`, its left subtree is also below `low`; none of those nodes can survive. The trimmed result for that entire subtree is therefore obtained by trimming only the node's right child. Symmetrically, when a node value is above `high`, its right subtree can be discarded and only its left child can contain retained values.

**Reconnect both children of an in-range node**

A node within the interval must remain. Recursively trim its left and right subtrees, then replace its child pointers with the returned roots. Each returned subtree contains exactly the valid descendants from that original side, so these assignments bypass removed boundary nodes without disturbing the ordering among retained nodes.

**Why the returned tree has exactly the required structure**

Each recursive call handles one of three exhaustive value positions. An out-of-range node returns the only side that could still contain valid values; an in-range node retains itself and attaches the correctly trimmed results of both children. Induction over subtree height therefore shows that every returned subtree contains all and only its in-range original nodes. Because every surviving child remains on its original BST side, the relative ancestor structure and search-tree ordering are preserved.

## Complexity detail
Every visited node is processed once, and discarded subtrees need not be traversed after the BST ordering proves that all their values are invalid. The worst case still visits all `N` nodes, so time is $O(N)$. Recursive calls occupy one frame per level, using $O(H)$ auxiliary space for tree height `H`; this is $O(\log N)$ for a balanced tree and $O(N)$ for a skewed tree.

## Alternatives and edge cases
- **Iterative boundary repair:** move the root into range, then repair invalid left and right boundary chains with pointers; it also runs in $O(N)$ time and $O(1)$ auxiliary space, but its asymmetric pointer logic is easier to get wrong.
- **Filter preorder values and rebuild a BST:** can reproduce the retained structure when insertion follows the original preorder, but ordinary insertion can take $O(N^2)$ time on a skewed tree and allocates a new tree.
- **Inorder collection followed by balanced rebuilding:** returns a valid BST with the right values, but changes the required relative structure and is therefore not semantically equivalent.
- Bounds are inclusive, so nodes equal to `low` or `high` remain.
- If the original root is outside the interval, a descendant can become the new root.
- A one-node tree is returned unchanged when its value is in range.
