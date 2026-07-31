## General

A query affects a node precisely when the queried label is one of that node's ancestors, including the node itself. Because flipping twice restores the original value, only the parity of the number of queries at each label matters. Toggle one parity bit for every query instead of visiting its subtree.

Labels already give a parent-before-child order: for each `node > 1`, `node // 2` is smaller. Scan labels from 1 through `n`. The final value at a node is its own query parity XOR the accumulated parity at its parent. Store that result back in the node's parity slot, then add it to the answer.

Inductively, the propagated parity at a node is the XOR of query parities along the complete root-to-node path. Those are exactly the subtree flips that affect the node. Thus every final bit is computed correctly, and summing the bits counts all nodes with value 1.

## Complexity detail

Let $q=\lvert\texttt{queries}\rvert$. Recording query parity takes $O(q)$ time, and propagating it over all labels takes $O(n)$ time, for $O(n+q)$ total time. The parity array uses $O(n)$ space.

The tree's edges need not be materialized because the parent of every label is available by integer division.

## Alternatives and edge cases

- **Flip every queried subtree:** Traversing descendants for each query is direct but can take $O(nq)$ time when the root is queried repeatedly.
- **Euler tour and range XOR:** Flattening subtrees and applying difference-array toggles also gives $O(n+q)$ time, but the implicit heap labeling makes ancestor propagation simpler.
- **Repeated query:** Two occurrences at the same node cancel; only odd frequency matters.
- **Root query:** It flips all nodes because every label descends from node 1.
- **Leaf query:** It affects only that leaf.
- **Ancestor and descendant queries:** Their effects XOR on the descendant's subtree rather than replacing one another.
- **Incomplete final level:** Labels stop at `n`; nonexistent heap children are never included.
- **Single node:** Every query targets the root, so the result is determined by query-count parity.
