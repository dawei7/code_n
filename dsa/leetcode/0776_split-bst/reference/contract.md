## Function Contract

**Inputs**

- `root`: the root node of a binary search tree, represented in cases by level-order values.
- `target`: the integer threshold used to partition the nodes; it need not equal any node value.

The operation reuses the original nodes. For every original parent-child edge whose endpoints remain in the same output subtree, that direct relationship must be preserved.

**Return value**

- A two-element list `[smaller, greater]`. `smaller` contains exactly the nodes with values smaller than or equal to `target`, and `greater` contains exactly the nodes with values greater than `target`. Either root may be `None`.
