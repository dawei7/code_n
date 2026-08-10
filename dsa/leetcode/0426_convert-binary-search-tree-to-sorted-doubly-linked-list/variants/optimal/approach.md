## General

**Inorder traversal already gives the required sorted order**

In a binary search tree with unique values, every node in a node's left subtree is smaller, and every node in its right subtree is larger. An inorder traversal visits

`left subtree -> current node -> right subtree`,

so nodes are encountered in strictly increasing value order. That is exactly the order required for the doubly linked list.

The transformation can therefore link each visited node to the node visited immediately before it. No array of sorted nodes is needed; the existing `left` and `right` pointers are repurposed in place as predecessor and successor links.

**Track the first and previous visited nodes**

`head` will point to the smallest node, which is the first node visited by inorder traversal. `prev` points to the most recently visited node, which is the greatest node processed so far.

Both live in the enclosing method and are declared `nonlocal` inside `dfs`, allowing recursive calls to update the shared traversal state.

After recursively processing `root.left`, the current `root` is the next node in sorted order. If `prev` exists, the two assignments

`prev.right = root` and `root.left = prev`

create both directions of the list link: the previous smaller node's successor is `root`, and `root`'s predecessor is that previous node.

If `prev` does not exist, no node has been visited yet. The current node is the global minimum, so it becomes `head`. It has no linear predecessor at this stage; the circular predecessor will be installed after traversal.

The statement `prev = root` then makes the current node the predecessor for the next inorder node. Traversal continues into the right subtree.

**Why pointer mutation does not destroy the traversal**

The algorithm overwrites tree pointers, so the order of operations matters.

The original left subtree is completely traversed before `root.left` is reassigned to the sorted predecessor. Nothing later needs the original left-child pointer.

When linking `prev.right = root`, `prev` belongs to an already completed part of the traversal. Its original right subtree, if it had one, has already been traversed before it became `prev`, so overwriting that pointer is safe.

The current `root.right` is not overwritten before `dfs(root.right)` obtains the original right child. Later, when the first node of that right subtree is processed, linking from `prev` will turn `root.right` into its correct sorted successor. Thus every original subtree remains reachable until precisely after it has been visited.

**Close the list into a circle**

After DFS finishes, `head` is the smallest node and `prev` is the largest. All consecutive sorted nodes already have reciprocal links. Only the two ends remain open.

`prev.right = head` makes the largest node's successor wrap to the smallest. `head.left = prev` makes the smallest node's predecessor wrap to the largest. Together they create the required circular doubly linked list.

The method returns `head`, exactly the requested pointer to the smallest value.

**A traversal example**

For a BST containing values `1,2,3,4,5`, inorder traversal visits them in that order. Visiting `1` initializes `head` and `prev`. Visiting `2` links `1 <-> 2`; visiting `3` links `2 <-> 3`, and similarly through `5`. At completion, `prev` is `5`. Closing the ring adds `5.right = 1` and `1.left = 5`.

Following `right` from `head` now produces `1,2,3,4,5,1,...`, while following `left` produces `1,5,4,3,2,1,...`.


After processing any inorder prefix, the processed nodes form a correctly sorted linear doubly linked list from `head` through `prev`. The next visited node is larger than every processed node and is the smallest unprocessed node. Linking it after `prev` preserves sorted order and reciprocal adjacency, then updating `prev` preserves the invariant.

When all nodes are processed, the invariant covers the entire BST. The final two assignments add only the required wraparound links, without changing internal sorted adjacency. Therefore the result is an in-place sorted circular doubly linked list containing every original node exactly once.

**Empty and one-node trees**

If `root is None`, the method returns `None` before initializing or linking endpoints. This matches the contract and avoids dereferencing absent nodes.

For one node, DFS makes both `head` and `prev` point to it. Closing the circle assigns its `right` and `left` back to itself, which is the correct one-node circular doubly linked list.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. DFS visits each node once and performs constant linking work, so time complexity is $O(n)$.

The conversion allocates no list nodes, arrays, or maps. Recursive calls use $O(h)$ stack space: $O(\log n)$ for a balanced tree and $O(n)$ for a maximally skewed tree. Apart from recursion, only `head`, `prev`, and current-node references use $O(1)$ space.

The output reuses all original nodes, satisfying the in-place requirement. Recursion-stack space does not violate in-place pointer transformation, but it is still included in auxiliary-space analysis.

## Alternatives and edge cases

- **Collect nodes in an inorder array:** Linking adjacent array entries is simple but uses $O(n)$ additional storage regardless of tree height. The chosen method links online.
- **Iterative inorder traversal:** An explicit stack also takes $O(h)$ space and avoids recursion-depth limits. The pointer-linking logic is otherwise the same.
- **Morris traversal:** Temporary threaded links can achieve $O(1)$ auxiliary space, but combining threading with permanent pointer conversion is considerably more delicate.
- **Preorder or breadth-first traversal:** These orders do not visit BST values in sorted order, so linking them directly would produce an unsorted list.
- **Forget the wraparound links:** The result would be a linear doubly linked list, not the required circular one.
- **Return the original root:** The BST root is not generally the minimum. The first inorder node stored in `head` must be returned.
- **Empty tree:** Return `None` without attempting endpoint links.
- **Single node:** Both pointers correctly become self-links.
- **Skewed tree:** Ordering remains correct, but recursive depth reaches $O(n)$.
- **Negative values:** BST ordering, not the sign of values, determines inorder order.
- **Unique-value guarantee:** Strict ordering makes predecessor and successor unambiguous; the linking procedure would still be structurally valid with a consistent duplicate policy, but none is needed here.
