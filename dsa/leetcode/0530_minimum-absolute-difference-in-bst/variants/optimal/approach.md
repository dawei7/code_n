## General
**Use the ordering already stored in the tree**

An inorder traversal of a binary search tree visits its distinct values in strictly increasing order. This turns the tree problem into finding the smallest gap in a sorted sequence without first materializing or sorting that sequence.

**Compare each value with its predecessor**

Maintain the previously visited value during iterative inorder traversal. For every visit after the first, subtract the predecessor from the current value and minimize the answer. Then make the current value the predecessor for the next visit.

**Why adjacent values are sufficient**

For any two sorted values $a < b$ with another value `c` between them, both $c - a$ and $b - c$ are no greater than $b - a$. Therefore a globally minimum pair cannot require skipping an intervening inorder value. Since the traversal checks every adjacent pair exactly once, it finds the global minimum.

**Avoid recursion-depth dependence**

An explicit stack descends each left chain, visits the node, and then moves into its right subtree. This preserves inorder while handling a highly skewed tree without relying on the language call-stack limit.

## Complexity detail
Every one of the `n` nodes is pushed and popped once, so time is $O(n)$. The explicit traversal stack contains at most the tree height `h`, giving $O(h)$ auxiliary space: $O(\log n)$ for a balanced tree and $O(n)$ in the worst case.

## Alternatives and edge cases
- **Recursive inorder traversal:** uses the same adjacent-value reasoning and $O(h)$ call-stack space, but a skewed tree can exceed recursion limits.
- **Collect and sort all values:** works for an arbitrary binary tree but costs $O(n \log n)$ time and $O(n)$ extra space, discarding the BST ordering advantage.
- **Compare every pair:** is correct but takes $O(n^2)$ time.
- **Two nodes:** their single difference is necessarily the answer.
- **Minimum at non-parent nodes:** inorder adjacency, rather than tree-edge adjacency, is what matters.
- **Unbalanced tree:** iterative traversal prevents call-stack failure while retaining the same result.
- **First inorder value:** initializes the predecessor and does not form a difference by itself.
