## General
**Handle the empty tree directly**

If `root` is absent, the new node is itself the root and can be returned immediately.

**Follow the only legal insertion path**

Starting at the root, compare `val` with the current node. A smaller value belongs somewhere in the left subtree and a larger value belongs somewhere in the right subtree. Continue down that chosen child while it exists.

**Attach at the first missing child**

When the required left or right child is `null`, create the node there and stop. All ancestors already constrain that position to a range containing `val`, and the final comparison puts it on the correct side of its parent.

**Why the original root remains the answer**

For a nonempty tree, insertion changes exactly one missing child reference and leaves every existing relationship intact. The new leaf satisfies all ancestor comparisons along its path, so the whole structure remains a BST and the original root still reaches every node.

## Complexity detail
Insertion visits one node per level along a single root-to-leaf path, taking $O(h)$ time for tree height `h`. The iterative version keeps only the current node and the new node, using $O(1)$ extra space.

## Alternatives and edge cases
- **Recursive insertion:** return the recursively updated left or right child; it has the same $O(h)$ time but uses $O(h)$ call-stack space.
- **Full inorder search:** locate the adjacent predecessor and successor before attaching the node; it is correct but discards the BST search advantage and takes $O(n)$ time.
- An empty input tree becomes a one-node tree.
- Inserting below the minimum follows only left children; inserting above the maximum follows only right children.
- The input guarantees `val` is absent, so duplicate-placement rules are unnecessary.
- A skewed BST can have $h = n$, making even ordered insertion linear in the worst case.
