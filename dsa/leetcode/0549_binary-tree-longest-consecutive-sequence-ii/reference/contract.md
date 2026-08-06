## Function Contract

**Inputs**

- `root`: the root node of the binary tree. Each node provides an integer `val` and optional `left` and `right`
  children.

Legal source inputs contain at least one node. Let $n$ be the number of nodes and $h$ be the tree height. A path is a
simple connected sequence of nodes and may start and end anywhere in the tree.

**Return value**

Return the maximum number of nodes on a path whose values change by exactly one at each edge in one consistent
numeric direction. The result is a length, not the path itself.
