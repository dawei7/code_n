## Hints

1. Determine both the sum and the node count for every subtree.
2. A node's subtree sum and count can be assembled from its own value and the corresponding summaries for its left and right subtrees.
3. Use depth-first search to solve both child subtrees first, then combine their summaries to evaluate the current node.
