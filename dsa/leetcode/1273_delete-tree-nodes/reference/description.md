## Description

A tree is rooted at node `0` and represented by three pieces of information:

- `nodes` gives the number of nodes.
- `value[i]` gives the value stored at node `i`.
- `parent[i]` identifies the parent of node `i`.

Remove every subtree for which the sum of all node values in that subtree is zero. Removing a subtree removes its root together with every descendant in that subtree.

Return the number of nodes that remain in the tree after all such zero-sum subtrees are removed.
