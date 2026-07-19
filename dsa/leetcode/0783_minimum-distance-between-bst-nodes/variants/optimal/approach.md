## General
**Use the BST's sorted traversal**

An inorder traversal of a binary search tree visits its distinct values in strictly increasing order. Maintain the previously visited value and update the best difference when the next node is reached.

**Why only neighbors matter**

For sorted values, the difference between two nonadjacent entries contains one or more positive adjacent gaps. It cannot be smaller than every gap inside that interval. Therefore the globally closest pair must appear consecutively in the inorder sequence, and comparing each node only with its predecessor is sufficient.

An explicit stack descends left until it reaches the next smallest unvisited node, then moves into that node's right subtree. This produces exactly the sorted order without storing all values. Every candidate adjacent gap is examined once, so the smallest recorded gap is the required answer.

## Complexity detail
Every one of the `n` nodes is pushed, popped, and processed once, taking $O(n)$ time. The traversal stack holds at most the tree height `h`, giving $O(h)$ auxiliary space.

## Alternatives and edge cases
- **Recursive inorder traversal:** Carry the previous value and current minimum through recursion; this has the same $O(n)$ time and $O(h)$ call-stack space.
- **Collect and sort values:** A traversal followed by sorting works for any binary tree but takes $O(n \log n)$ time and $O(n)$ space.
- **Compare every pair:** Directly testing all node pairs is correct but takes $O(n^2)$ time.
- **Exactly two nodes:** Their absolute difference is the answer.
- **Skewed tree:** The explicit stack may grow to $O(n)$, matching $h = n$.
- **First inorder node:** It initializes the predecessor and does not form a gap by itself.
- **Distinct values:** The minimum is positive; duplicates do not need special handling under the contract.
