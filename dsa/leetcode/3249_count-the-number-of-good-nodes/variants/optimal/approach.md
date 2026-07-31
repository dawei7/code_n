## General

Let $n$ be the number of nodes. A node's status cannot be decided until the sizes of all subtrees rooted at its children are known, which makes a bottom-up traversal natural.

**Turn the undirected edges into a rooted tree**

Build an adjacency list, then traverse outward from node `0`. Record each discovered node's parent and append the node to an order list. In a tree, ignoring the parent edge is sufficient to prevent revisiting nodes. Reversing the resulting parent-before-child order gives a valid postorder: every child appears before its parent.

**Accumulate sizes and recognize good nodes**

Initialize every subtree size to one for the node itself. While processing a node in reverse order, inspect only adjacent nodes whose recorded parent is the current node. Their subtree sizes are already final. Add each size to the current node's total and compare it with the first child size seen.

The node is good exactly when no later child size differs from that first size. With zero children there is nothing to compare, and with one child no mismatch is possible, so both cases are counted automatically.

When a node is processed, all child totals are correct by postorder. Their sum plus one is therefore precisely the current subtree size, and the equality test examines every child subtree and only those subtrees. Thus the stored size and good-node decision are correct for that node. Applying this argument from the leaves up to the root establishes the final count.

## Complexity detail

Constructing the adjacency list processes each of the $n-1$ edges twice. The rooting traversal and reverse traversal each visit every node and edge a constant number of times, so the time complexity is $O(n)$. The adjacency list, parent array, traversal order, and subtree-size array require $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recursive depth-first search:** Returning a subtree size from each call expresses the postorder directly, but a chain of up to $10^5$ nodes can exceed Python's recursion depth.
- **Recount every child subtree:** Running a fresh traversal for each node is straightforward but can take $O(n^2)$ time on a long chain.
- **Sort child sizes:** Equality needs only comparison with the first size; sorting adds unnecessary work and storage.
- Every leaf is good because it has no child subtrees.
- A node with exactly one child is good regardless of that child's subtree size.
- The parent edge must not be mistaken for another child when examining an undirected adjacency list.
- Equal node degrees do not imply equal child-subtree sizes.
- Node labels and edge order provide no traversal-order guarantee.
- The root has no parent; its children are all of its adjacent nodes.
