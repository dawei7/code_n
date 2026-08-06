## Description

`order` is a permutation of the integers from $1$ through $n$ and describes how those keys are inserted into an initially empty binary search tree. The first key becomes the root. Each later key follows left links while it is smaller than the current node and right links while it is larger, becoming a leaf at the first empty child position.

Return the resulting tree's depth: the number of nodes on its longest root-to-leaf path. The root alone has depth one. The task asks only for this depth; the tree does not need to be returned.
