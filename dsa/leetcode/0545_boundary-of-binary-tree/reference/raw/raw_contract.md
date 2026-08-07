## Function Contract

**Inputs**

- `root`: the root node of the binary tree. Each node provides an integer `val` and optional `left` and `right`
  children.

Legal source inputs contain at least one node. Let $n$ be the number of nodes and $h$ be the tree height. Nodes are
classified by structure rather than by value, so equal values in different boundary nodes remain separate output
entries.

**Return value**

Return a list of node values ordered as root, non-leaf left boundary from top to bottom, all leaves from left to
right, and non-leaf right boundary from bottom to top. No physical node is included in more than one portion.
