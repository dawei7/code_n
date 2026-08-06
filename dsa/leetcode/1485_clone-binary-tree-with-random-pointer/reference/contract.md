## Function Contract

**Input**

- `root`: the root of a binary tree whose `Node` objects contain `val`, `left`,
  `right`, and `random` fields, or `null` for an empty tree.

The app-local contract defines explicit equivalents of both source-native node
classes. Let $N$ be the number of non-null nodes.

**Return value**

Return the root of a newly allocated `NodeCopy` graph. Every copied node must
have the same value and the same labeled `left`, `right`, and `random`
relationships as its corresponding original node, with every non-null copied
pointer targeting another copied node rather than an original object. Return
`null` when `root` is `null`.
