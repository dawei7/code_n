## Description

Given an $n \times n$ matrix `grid` containing only `0` and `1`, return the root of a Quad-Tree that represents the
entire matrix.

Every internal Quad-Tree node has exactly four children: `topLeft`, `topRight`, `bottomLeft`, and `bottomRight`.
Each node also has these attributes:

- `val` is `True` for a leaf region filled with `1` and `False` for a leaf region filled with `0`. Either Boolean
  value is accepted when `isLeaf` is `False`.
- `isLeaf` is `True` for a leaf and `False` for an internal node with four children.

Construct the representation by applying the following rules to each square region:

1. If every cell has the same value, make a leaf whose `val` is that value, set all four children to `null`, and
   stop processing that region.
2. Otherwise, make an internal node whose `val` may be either Boolean value, divide the region into four equal
   subgrids, and recurse on each child region.

The source's quadrant diagram corresponds to these exact half-open ranges for a region starting at row $r$, column
$c$, with side length $s$ and $h = s/2$:

| Child | Row range | Column range |
|---|---|---|
| `topLeft` | $[r, r+h)$ | $[c, c+h)$ |
| `topRight` | $[r, r+h)$ | $[c+h, c+s)$ |
| `bottomLeft` | $[r+h, r+s)$ | $[c, c+h)$ |
| `bottomRight` | $[r+h, r+s)$ | $[c+h, c+s)$ |

**Quad-Tree format**

The displayed output is a level-order serialization included only to explain the examples. A `null` entry ends a
path because no node exists below it. Each real node is encoded as `[isLeaf, val]`; `True` becomes `1` and `False`
becomes `0` in either position. This is analogous to binary-tree serialization, except each internal node has four
ordered children.
