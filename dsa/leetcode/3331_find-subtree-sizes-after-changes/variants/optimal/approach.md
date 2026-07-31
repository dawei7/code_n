## General

Every new parent is defined by ancestry in the original tree, so the original child lists must remain the traversal structure. During a depth-first traversal, keep one stack for each of the 26 lowercase characters. A character's stack contains exactly the nodes with that character on the current original root-to-node path, in increasing depth order.

Use explicit entry and exit events to avoid Python's recursion-depth limit on a chain of $10^5$ nodes. On entry to a node, push it onto its character stack. Its children then see it as a possible same-character ancestor. On exit, first pop the node itself. The top that remains on the same character stack is precisely the closest original ancestor with an equal character. If the stack is empty, the node keeps its original parent. This uses the original path throughout, so one node's reparenting never contaminates another node's search.

Initialize every subtree size to one. Exit events occur after all original descendants have been processed. Any node whose final parent is the current node is also an original descendant, and its completed total has already been added to the current node. Thus, when a node exits, its current total is its complete final subtree size; add that total directly to its final parent. Repeating this postorder flow computes all final subtree sizes without constructing a second tree.

## Complexity detail

Let $n=\lvert\texttt{parent}\rvert$. Building the child lists takes $O(n)$ time. Each node creates one entry event and one exit event, and every stack operation and size update is constant time, so the complete algorithm takes $O(n)$ time. The child lists, traversal events, character-path stacks, and answer array together use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Build the transformed tree explicitly:** Recording every final parent and running a second postorder traversal is also $O(n)$ time and space, but the direct size flow avoids another adjacency list and traversal.
- **Climb ancestors independently:** Walking upward from every node until a matching character appears is easy to formulate, but repeated searches can revisit long paths and become quadratic.
- **Recursive depth-first search:** It expresses the same state cleanly, but a legal chain can contain $10^5$ nodes and exceed Python's recursion limit; explicit events are depth-safe.
- **Simultaneous changes:** Searches must use the original parent relationships. Following already-modified parents can skip or invent candidate ancestors.
- **No matching ancestor:** After removing the node from its character stack, an empty stack means its original parent remains unchanged.
- **Single node:** The root has no parent update and its subtree size is one.
