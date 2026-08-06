## Description

You are given the root of a special binary tree containing $n$ uniquely numbered nodes. Let its original leaves, in their numbered order, be $b_1,b_2,\ldots,b_k$. The tree stores an additional cyclic link among these leaves: the right pointer of $b_i$ refers to $b_{i+1}$, wrapping from $b_k$ to $b_1$, while its left pointer refers to $b_{i-1}$, wrapping from $b_1$ to $b_k$.

Those neighbor pointers do not create deeper tree levels; they replace the otherwise empty child pointers of the leaves. Return the height of the underlying binary tree, defined as the number of edges on the longest path from the root to any node. The leaf cycle must therefore be recognized and excluded from the descendant traversal.
