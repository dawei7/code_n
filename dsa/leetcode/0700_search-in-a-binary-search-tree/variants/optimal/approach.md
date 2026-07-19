## General
**Use the ordering at every node**

At a binary search tree node, every value in the left subtree is smaller and every value in the right subtree is larger. Comparing `val` with the current node therefore rules out one entire subtree.

**Descend along one path**

While a node exists, return it immediately when its value matches. Move left when `val` is smaller and right when it is larger. If the selected child is absent, the search ends without a result.

**Return the node rather than reconstructing output**

The requested result is the original matching node. Returning its reference automatically preserves the complete subtree rooted there; the judge serializes that subtree only for comparison.

**Why the discarded side cannot contain the target**

Each move follows the only subtree whose allowed value range still contains `val`. The BST invariant proves the other subtree cannot contain it. Thus a match is genuine, and reaching `null` after repeatedly preserving the only possible region proves the value is absent.

## Complexity detail
The algorithm visits one node per tree level along a single root-to-node path, taking $O(h)$ time for tree height `h`. It uses one moving node reference and no traversal stack, so the extra space is $O(1)$.

## Alternatives and edge cases
- **Recursive BST search:** recurse into only the ordered child; it also takes $O(h)$ time but uses $O(h)$ call-stack space.
- **Generic depth-first traversal:** search both subtrees without using their ordering; it is correct for any binary tree but can take $O(n)$ time here.
- A match at the root returns the entire original tree.
- A leaf match returns a one-node subtree.
- An absent value eventually selects a missing child and returns `null`.
- A skewed BST has $h = n$, so the worst-case running time is linear even though balanced-tree search is logarithmic.
