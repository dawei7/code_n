## General
**Interpret the stack as the active ancestor path:** Create the root from the first preorder value and keep a stack containing the path of nodes whose right subtree may still receive values. Each later value creates exactly one new node.

**Attach smaller values immediately on the left:** If `value < stack[-1].val`, preorder and the BST ordering imply that the new node begins the current node's left subtree. Assign it to `stack[-1].left` and push it, extending the active path downward.

**Pop completed subtrees before attaching right:** Otherwise, pop while the stack's top value is smaller than `value`. The last popped node is the deepest ancestor whose left subtree and any smaller nested subtrees are complete, so the new node is its right child. Push the new node as the new end of the active path.

Each attachment respects the strict BST inequalities. Preorder supplies a child only after its ancestors and supplies the entire left subtree before the right subtree; the pop step removes exactly the ancestors whose remaining right boundary the new value has crossed. Therefore every input value is attached at its unique valid position and the constructed tree reproduces the traversal.

## Complexity detail
Each of the $N$ nodes is pushed once and popped at most once, so total time is $O(N)$. The stack contains at most the $H$ nodes on an active root-to-node path and uses $O(H)$ auxiliary space. The returned tree itself is output space.

## Alternatives and edge cases
- **Recursive upper bound:** Consuming preorder with a moving index and subtree bound also achieves $O(N)$ time and $O(H)$ call-stack space.
- **Find each subtree split:** Scanning every recursive slice for the first value greater than its root is intuitive, but a skewed tree causes $O(N^2)$ work and repeated slicing.
- **Insert nodes one at a time:** Ordinary BST insertion reconstructs the same tree, yet also takes $O(N^2)$ time for sorted preorder input.
- **Strict inequalities:** Values are unique, so no duplicate-placement rule is needed.
- **Skewed traversal:** Increasing or decreasing input produces height $H=N$; an iterative stack avoids recursion-limit concerns.
