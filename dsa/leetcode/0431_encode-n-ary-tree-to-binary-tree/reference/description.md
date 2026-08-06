## Description

Design a reversible mapping between an N-ary tree and a binary tree. An N-ary tree is rooted and allows each node
to have at most $N$ children, whereas a binary-tree node has at most two children.

The encoding convention is unrestricted. It only needs to preserve every value and enough structure for decoding
the binary tree back into the original N-ary tree. LeetCode displays N-ary inputs in level order, placing `null`
between consecutive groups of children.

For example, the source diagram shows the N-ary tree rooted at `1`, with ordered children `3`, `2`, and `4`; node
`3` in turn has children `5` and `6`. It illustrates this possible binary encoding:

| N-ary relationship | Binary representation |
|---|---|
| First child of `1` is `3` | `1.left = 3` |
| Later children of `1` are `2` and `4` | `3.right = 2`, then `2.right = 4` |
| First child of `3` is `5` | `3.left = 5` |
| Later child of `3` is `6` | `5.right = 6` |

The corresponding N-ary level-order serialization is `[1,null,3,2,4,null,5,6]`. This layout is only an example
and is not guaranteed to be the required convention; any stateless design that round-trips the exact tree is valid.
