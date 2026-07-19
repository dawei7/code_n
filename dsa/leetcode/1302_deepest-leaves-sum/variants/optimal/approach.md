## General
**Let the final breadth-first level overwrite earlier sums**

Perform breadth-first traversal with a queue initialized by the root. Each queue batch contains exactly one tree depth. At the beginning of a batch, reset `level_sum` to zero; then remove every node currently in the queue, add its value, and enqueue its non-null children.

After a batch finishes, `level_sum` is the sum of every node on that depth. If children were enqueued, the next iteration deliberately replaces this sum with the next level's sum. When the queue finally becomes empty, the most recently processed batch was the deepest level.

Every node on the deepest level is necessarily a leaf: if one had a child, a still-deeper level would exist. Therefore the retained sum is exactly the sum of the deepest leaves, without separately testing leaf status.

## Complexity detail
Each of the $n$ nodes enters and leaves the queue once, so the traversal takes $O(n)$ time. The queue holds at most one level, whose width is at most $n$, giving $O(n)$ auxiliary space in the worst case.

## Alternatives and edge cases
- **Depth-first score pair:** A postorder traversal can return both maximum subtree depth and the sum at that depth in $O(n)$ time, but recursion may use $O(n)$ stack space on a skewed tree.
- **Repeated subtree-height calculation:** Choosing a deeper branch by recomputing child heights at every node is correct, but takes $O(n^2)$ time on a chain.
- **Single node:** The root is the sole deepest leaf and its value is returned.
- **Several deepest leaves:** Sum every node on the final level, including leaves from different subtrees.
- **Shallower high-value leaf:** Its value must be ignored once a deeper level exists.
- **Skewed tree:** The only deepest leaf is the final node in the chain.
