## Description

An undirected tree contains `n` nodes numbered from `0` through `n - 1` and is rooted at node `0`. The array `edges` gives its `n - 1` connections, and `values[i]` is the positive integer value assigned to node `i`.

For any node, its subtree contains that node and every descendant determined by the root. Choose two subtrees that share no node. Their score is the bitwise XOR of their two value sums.

Return the maximum achievable score. If the rooted tree has no pair of non-overlapping subtrees, return `0`.
