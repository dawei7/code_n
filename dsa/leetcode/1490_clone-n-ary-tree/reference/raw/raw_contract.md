## Function Contract

**Inputs**

- `root`: The N-ary `Node` root, or `None` for an empty tree. Each node exposes `val` and an ordered `children` list.

Let $N$ be the total number of nodes in the tree and $H$ the tree height.

**Return value**

Return the root of a newly allocated N-ary tree with the same values, shape, and child ordering as the input tree. For the app-local representation, return an equal but independently allocated `Node` structure. Return `None` for an empty tree.
