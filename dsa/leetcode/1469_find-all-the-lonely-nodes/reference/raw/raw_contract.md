## Function Contract

**Input**

- `root`: the root of a nonempty binary tree.

The app-local contract uses the package's explicit `TreeNode` equivalent, whose
`val`, `left`, and `right` fields represent the source-native node model. Let
$N$ be the number of nodes in the tree.

**Return value**

Return the value of each non-root node whose parent has exactly one child.
Result order is unrestricted.
