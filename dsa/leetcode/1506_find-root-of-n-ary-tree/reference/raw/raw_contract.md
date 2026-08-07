## Function Contract

**Inputs**

- `tree`: A list of all $N$ N-ary `Node` objects in arbitrary order. Each node exposes a unique integer `val` and a `children` list containing references to its children.

Let $N$ be the total number of nodes in the tree.

**Return value**

Return the root `Node` object. The root is the unique node in `tree` that does not appear in any other node's `children` list.
