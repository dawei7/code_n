## General

**Translate preorder directly into recursive order**

Preorder traversal means:

1. process the current node;
2. traverse the complete left subtree in preorder;
3. traverse the complete right subtree in preorder.

The nested `dfs` function follows those three actions literally. For a real node, it appends `root.val`, calls itself on `root.left`, and then calls itself on `root.right`.

This direct correspondence is the main strength of the solution. The program’s call stack remembers which right subtree must be visited after each left subtree finishes.

**Why the null case is necessary**

A missing child is represented by `None`. Such a position has no value and no children, so `dfs(None)` immediately returns.

That base case does two jobs:

- it stops recursion at leaves;
- it lets every real node use the same two child calls without special tests for whether each child exists.

For an empty input tree, the initial `dfs(root)` is `dfs(None)`. It returns immediately, leaving `ans` empty.

**What one call contributes**

For any node `x`, after `dfs(x)` returns, it has appended exactly the preorder traversal of the subtree rooted at `x`.

The argument can be followed structurally:

- if `x` is null, its subtree contains no values and the function appends nothing;
- if `x` is real, its own value is appended first;
- by the same rule, the left recursive call appends the complete left-subtree preorder;
- only after that call returns does the right recursive call append the right-subtree preorder.

Concatenating those contributions produces root-left-right order for the subtree. Applying this fact to the original root proves that `ans` is the requested traversal.

**Why each node appears once**

In a proper binary tree, every non-root node is reached from exactly one parent link. `dfs` is invoked through both child links of every real node, but only the link that actually points to a given node reaches that object. The other structural paths do not converge on it as they might in a general graph.

The function appends a value exactly when it enters a real node. It never appends during the return from recursion, so this is preorder rather than inorder or postorder.

**Trace the first nontrivial example**

For the shape encoded by `[1, null, 2, 3]`, the root value `1` is appended. Its left call sees `None`. The right call enters node `2`, appends `2`, and then enters its left child `3`, appending `3`. The final result is `[1, 2, 3]`.

For a node with both children, the entire left recursion completes before even the right child’s value is appended. This is why depth-first recursion preserves subtree grouping.

**The output list belongs outside the helper**

`ans` is created once in `preorderTraversal` and captured by the nested function. Every recursive frame appends to the same list.

Creating a new result list in every frame would require concatenating child results and could add copying overhead. The shared accumulator allows constant local work per node.

The tree is read-only. The source never assigns to `left`, `right`, or `val`.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height measured in nodes along the longest root-to-leaf path.

Every real node is entered once, and each null child causes only a constant-time return. Appending and pointer reads are constant time, so total time is $O(n)$.

The maximum number of simultaneously active recursive frames is $h$, giving $O(h)$ auxiliary stack space. A balanced tree has $h=O(\log n)$; a completely skewed tree has $h=n$ and therefore $O(n)$ stack space.

The returned `ans` list stores $n$ values. Under the standard convention that excludes required output, auxiliary space is $O(h)$ as the manifest states. Including output, total additional storage is $O(n+h)=O(n)$.

With the stated maximum of 100 nodes, Python’s normal recursion limit is not a practical concern for valid inputs.

## Alternatives and edge cases

- **Explicit stack:** Push the right child before the left child so the LIFO stack processes left first. It avoids recursion and uses $O(h)$ to $O(n)$ stack entries depending on tree shape and implementation.
- **Morris preorder:** Temporarily thread each left subtree’s predecessor back to the current node. It achieves $O(1)$ auxiliary space but mutates and restores pointers during traversal.
- **Unified visited-flag stack:** Push `(node, visited)` states to simulate call phases. It generalizes across preorder, inorder, and postorder but stores more stack records.
- **Empty tree:** The null base returns `[]`.
- **Single node:** Its value is appended, and both child calls return immediately.
- **Only left children:** Values appear from root down the chain.
- **Only right children:** The left null call returns before each right descent, still producing chain order.
- **Duplicate values:** Traversal records nodes, not unique values, so duplicates appear as often as their nodes.
- **Tree-versus-graph assumption:** A malformed cyclic node structure would recurse forever; the contract supplies a binary tree.
- **Runtime dependencies:** The source uses `Optional` and `List` without importing them. The platform supplies `TreeNode`; standalone Python also needs `from typing import List, Optional`.
