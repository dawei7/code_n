## General
**Visit keys from greatest to smallest:** Ordinary inorder traversal of a BST is ascending. Reversing its order to right subtree, node, left subtree visits every original key in descending order.

**Maintain the sum already passed:** Keep `running_sum` of the original values visited so far. When a node is popped from the traversal stack, add its current original value to `running_sum`, then assign `node.val = running_sum`. At that moment, the sum contains exactly that key and every greater key.

**Use an explicit traversal stack:** Descend through right children, process the deepest pending node, then move into its left subtree. This preserves reverse inorder while avoiding dependence on the language recursion limit.

Because BST ordering makes every previously visited key greater than the current key, each assignment has exactly the required sum. Every node is reached once, and mutation occurs only after its original value has been added, so later sums still include all correct original keys.

## Complexity detail
Each of the $N$ nodes is pushed, popped, and updated once, giving $O(N)$ time. The explicit stack holds at most one root-to-leaf path and uses $O(H)$ auxiliary space.

## Alternatives and edge cases
- **Recursive reverse inorder:** Carry a nonlocal running sum through right-node-left recursion for the same asymptotic bounds, but a skewed tree may approach recursion limits.
- **Collect and suffix-sum:** Store all nodes in ascending order, compute suffix sums, and write values back. This is $O(N)$ time but uses $O(N)$ extra space.
- **Rescan all keys per node:** For each node, sum every original key at least as large. It is correct but takes $O(N^2)$ time.
- **Single node:** Its value is unchanged because no greater key exists.
- **Zero key:** It becomes the sum of the entire tree.
- **Skewed BST:** The reverse-inorder logic remains correct, while $H$ may equal $N$.
- **Mutation order:** Add the original node value before overwriting it.
