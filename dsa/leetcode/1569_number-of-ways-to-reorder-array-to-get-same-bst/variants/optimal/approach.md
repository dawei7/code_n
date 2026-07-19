## General
**View insertion time as a priority over sorted keys**

Within any contiguous key interval, the first key inserted becomes the root of that BST subtree. Therefore, if keys are listed in numeric order and each key is labeled with its position in `nums`, the desired BST is exactly the min-Cartesian tree of those insertion-time labels: its inorder traversal is key order, and every subtree root has the earliest insertion time in its interval.

Build this Cartesian tree in one pass over keys `1..N` with a monotonic stack. While the stack top was inserted later than the current key, pop it; the last popped subtree becomes the current key's left child. The remaining stack top, if any, receives the current key as its right child. Each key is pushed and popped at most once.

**Count valid interleavings bottom-up**

For a node with $L$ keys in its left subtree and $R$ in its right subtree, the node itself must appear before all descendants. The valid left and right insertion sequences can otherwise be interleaved in

$$
\binom{L+R}{L}
$$

ways while preserving each subtree's internal order. Thus the subtree count is that binomial coefficient multiplied by the independently valid counts for both children.

Precompute factorials and inverse factorials modulo the prime modulus so each binomial coefficient is available in constant time. Traverse the Cartesian tree iteratively and evaluate nodes in reverse traversal order, after both child results are known. The Cartesian-tree identity proves that this is the original BST, and the interleaving formula counts every order that preserves it exactly once. Subtract one at the end to exclude the given order.

## Complexity detail
Building insertion times, factorial tables, the monotonic-stack Cartesian tree, and the bottom-up counts each takes $O(N)$ time. Modular exponentiation for the one factorial inverse costs $O(\log M)$ for fixed modulus $M=1{,}000{,}000{,}007$, so it does not change the $O(N)$ bound with respect to $N$.

The child arrays, traversal order, subtree sizes, counts, factorial tables, and stack each contain $O(N)$ values, giving $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Recursive root partitioning:** split every sequence into values smaller and larger than its first value, then combine recursively. It mirrors the proof directly but takes $O(N^2)$ time on a skewed BST.
- **Reverse insertion with union-find:** activate keys from latest to earliest and merge adjacent active key intervals while combining their counts. This runs in near-linear time and exploits the same contiguous-key subtree property.
- **Explicit BST insertion:** building the BST by ordinary unbalanced searches can itself take $O(N^2)$ time for monotone input.
- **Single key or two-key chain:** no different ordering can preserve the BST, so the answer is `0`.
- **Strictly increasing or decreasing input:** the BST is a chain with only one valid insertion order, again producing `0` after subtraction.
- **Balanced subtrees:** left and right sequences admit many interleavings, so the binomial factor is essential.
- **Relative order within a subtree:** arbitrary interleaving between sides is allowed, but changing the valid internal construction order of either child subtree can change its structure.
- **Modulo subtraction:** compute `(ways - 1) % modulus` so exclusion remains nonnegative.
- **Deep trees:** iterative construction and evaluation avoid recursion-depth failures at $N=1000$.
