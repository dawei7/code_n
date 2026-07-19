## General
**Follow only the search path for the threshold**

At a node with `node.val <= target`, the node and its entire left subtree belong in the smaller component. Only its right subtree may contain values on both sides, so recursively split that subtree. Attach the returned smaller part back as `node.right`, then return `[node, greater_part]`.

When `node.val > target`, the node and its entire right subtree belong in the greater component. Recursively split only its left subtree, attach the returned greater part as `node.left`, and return `[smaller_part, node]`.

**Why the untouched side is already classified**

The BST ordering guarantees that every left-subtree value is below its node and every right-subtree value is above it. Therefore, each branch can classify one whole subtree without visiting it. The recursive result correctly partitions the only ambiguous child; reconnecting its same-side component preserves all original relative relationships except the one edge that must cross the split. Induction down the search path proves both returned components contain exactly the required nodes and remain BSTs.

## Complexity detail
The recursion visits one node per level along a single search path, taking $O(h)$ time for tree height `h`. The call stack uses $O(h)$ space; all result nodes are reused rather than copied.

## Alternatives and edge cases
- **Iterative path rewiring:** Two dummy chains can partition the same search path in $O(h)$ time and constant auxiliary pointer storage.
- **Copy the entire tree before splitting:** It preserves output values and shape but costs $O(n)$ time and space instead of reusing nodes along an $O(h)$ path.
- **Traverse and reinsert every value:** This loses the required relative structure and costs at least $O(n)$ work.
- **Target below every value:** Return an empty smaller component and the original entry as the greater component.
- **Target at or above every value:** Return the original entry as the smaller component and an empty greater component.
- **Missing target:** The ordering comparisons still identify the correct split boundary.
- **Skewed tree:** Height can equal the node count, making the worst case linear.
