## General

Inorder traversal visits a binary tree in the sequence

`left subtree -> node -> right subtree`.

The successor is the node visited immediately after the given node. Parent pointers allow that next node to be found locally even though the root is unavailable. There are exactly two structural cases, determined by whether the node has a right child.

**Case one: a right subtree exists.** In inorder order, the current node is followed by its right subtree. The first node visited inside that subtree is its leftmost node.

The code first moves once to `node.right`. It then repeatedly follows `node.left` until no left child remains. The final node is returned.

Why is it the successor? Every node in the right subtree comes after the original node in inorder order. The leftmost node is the first node visited within that subtree and, by the BST property, has its smallest key. No node can appear between the original node and this leftmost descendant in the inorder sequence.

For example, if a node's right child has a chain of left descendants, returning the immediate right child would skip those descendants. The loop is necessary even though the first move is always right.

**Case two: no right subtree exists.** After visiting a node with no right subtree, inorder traversal must move upward. If the node is the right child of its parent, then that parent has already been visited before traversal entered the right subtree. It cannot be the successor.

The same is true while climbing through a chain of right-child relationships. The loop

`while node.parent and node.parent.right is node`

moves upward past every ancestor whose right subtree is the branch just completed.

The climb stops in one of two ways:

- the current node is a left child of its parent; that parent has not yet been visited and is the successor;
- there is no parent; traversal has finished the entire tree, so no successor exists.

Returning `node.parent` handles both outcomes, producing the ancestor or `None`.

**Why identity comparison is used.** `node.parent.right is node` asks whether these are the same node objects, not whether their values are equal. The follow-up asks for a solution without reading values, and the tree has direct child and parent references. Structural identity supplies all necessary information.

Even though values are unique under the contract, comparing values would be unnecessary and would not generalize as cleanly to trees with duplicate keys. The algorithm never accesses `node.val`.

Consider node one in tree `[2, 1, 3]`. It has no right child and is the left child of parent two, so the while condition is false immediately and parent two is returned.

Consider node six when it is the maximum node in its tree. It has no right child. Every ancestor encountered while climbing is reached from that ancestor's right branch, so the loop eventually reaches the root and then `node.parent` is `None`. Returning `None` correctly reports no successor.

For a mixed climb, suppose the node is a right child, its parent is also a right child, but that grandparent is a left child of a higher ancestor. The loop skips the first two already-visited ancestors and stops at the grandparent/higher-ancestor link. The higher ancestor is the first one not yet visited and is returned.

**Complete correctness argument.** If a right subtree exists, inorder rules force the successor to be the first node of that subtree, which is its leftmost node. If no right subtree exists, all descendants of the node are already exhausted. Traversal climbs until it leaves a completed right subtree and reaches the first ancestor for which the current branch lies on the left. That ancestor is next. If no such ancestor exists, the node was last in the whole traversal. The two cases are exhaustive and each returns exactly the required node object.

The method modifies the local `node` variable while searching but does not change any tree link. The caller's tree and original node object remain intact.

## Complexity detail

Let $h$ be the tree height. In the right-subtree case, the method descends at most $h$ left edges. In the ancestor case, it climbs at most $h$ parent edges. Time is therefore $O(h)$.

Only the local node reference is reused. No recursion, stack, list, or set is allocated, so auxiliary space is $O(1)$. In a balanced tree, $h = O(\log n)$; in a skewed tree, $h = O(n)$.

## Alternatives and edge cases

- **Start from the root:** Standard BST search can track the smallest greater ancestor, but this problem does not provide the root. Parent pointers make root lookup unnecessary.
- **Full inorder traversal:** Climb to the root, traverse every node, and locate the target's next position. It costs $O(n)$ time and extra traversal state instead of exploiting local structure.
- **Value-based ancestor search:** Compare keys while climbing or searching. It is unnecessary here and fails the follow-up's goal of avoiding value access.
- **Immediate right child has a left subtree:** The successor is the deepest left descendant, not necessarily the right child itself.
- **Node is a left child:** With no right subtree, its parent is returned immediately.
- **Long right-child chain:** Every ancestor on that chain has already been visited, so all must be skipped.
- **Maximum node:** It has no right subtree and no ancestor reached from a left branch; the method returns `None`.
- **Root node:** If it has a right subtree, use its leftmost node. If not, it has no parent and no successor.
- **Return node, not value:** The contract requires the actual `Node` object. Both branches return references rather than `node.val`.
- **Tree preservation:** Only a local pointer changes; parent and child fields are never modified.
