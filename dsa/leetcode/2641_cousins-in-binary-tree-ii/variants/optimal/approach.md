## General

A node's cousin sum can be written as the sum of all original values on its level minus the original values of every child of its own parent. Breadth-first traversal exposes exactly the nodes needed for both quantities without storing parent maps or depth-indexed tables.

Set the root to zero and keep the current level's parents in a list. First scan those parents to collect all existing children and add their still-unmodified values into `next_sum`. Then scan the same parents again. For each parent, add the original values of its left and right children to obtain one `sibling_sum`, and assign `next_sum - sibling_sum` to each of those children.

The first scan must finish before any child value changes, ensuring that both the level total and every sibling-group total use original values. Each child at the next depth is covered by exactly one parent group. Subtracting that group removes the child itself and all its siblings while retaining precisely the nodes at the same depth with different parents, so every assigned value is the required cousin sum. The collected children then become the next level.

## Complexity detail

Let $n$ be the number of nodes and $w$ the maximum number of nodes on one level. Each node is collected once and participates in at most one sibling-group calculation, so the total time is $O(n)$. The current and next level lists contain at most $O(w)$ nodes, which is $O(n)$ in the worst case and matches the manifest space bound. The transformation otherwise uses only constant scalar state.

## Alternatives and edge cases

- **Two depth-first passes:** One pass can record every depth sum and a second can update nodes using their sibling sums, also taking $O(n)$ time and $O(n)$ storage; recursion can overflow on a legal tree of depth $10^5$.
- **Parent and depth maps:** Grouping nodes by depth and parent makes the definition explicit but retains more metadata than the level-order calculation needs.
- **Per-node cousin scans:** Searching the entire level separately for each node is correct but degrades to $O(n^2)$ time on a wide tree.
- The root has no same-depth peers and must become zero.
- All nodes at depth one share the root as their parent, so every one of them becomes zero.
- A missing child contributes nothing to its parent's sibling-group sum and is not inserted into the next frontier.
