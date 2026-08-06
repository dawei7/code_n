## Description

Each node in the given binary tree has the usual child links plus a `random`
pointer. That extra pointer may target any node in the same tree or may be
`null`.

Return a deep copy of the entire tree.

The serialized input and output use the normal binary-tree layout, but each
non-null node is represented as `[val, random_index]`:

- `val` is the integer stored in `Node.val`;
- `random_index` is the input position targeted by `random`, or `null` when the
  pointer has no target.

The judge supplies the original tree using class `Node`; return the cloned tree
using class `NodeCopy`, which has the same fields and constructor shape.
