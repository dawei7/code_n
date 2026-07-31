## Function Contract

**Inputs**

- `root`: The root node of a nonempty Binary Search Tree.
- `level`: The zero-based distance from the root whose node values are queried.

Let $N$ be the number of nodes in the tree, $K$ the number of nodes at the requested level, and $W$ the tree's maximum width.

The tree obeys the BST ordering property. Values at the requested level are interpreted in non-decreasing order when selecting their median. For $K>0$, the upper median has zero-based sorted index $\lfloor K/2\rfloor$.

**Return value**

Return the requested level's median value, using the upper median when $K$ is even. Return `-1` when $K=0$.
