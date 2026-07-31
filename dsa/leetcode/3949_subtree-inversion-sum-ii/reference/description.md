## Description

An undirected tree with $n$ nodes is rooted at node `0`. Its nodes are numbered from `0` through `n - 1`; `edges[i] = [u_i, v_i]` joins two nodes, and `nums[i]` is the initial integer value stored at node $i$.

You may choose a subset of nodes at which to perform subtree inversion operations. Inverting node $u$ multiplies by $-1$ every value in the rooted subtree of $u$, including `nums[u]`. Operations may overlap, so a value covered by several selected ancestors is multiplied by $-1$ once per covering operation.

The selected inversion nodes must also satisfy a global distance restriction. Every two distinct selected nodes must be separated by at least `k` edges along their unique tree path. This rule applies equally to ancestor-descendant pairs and to nodes lying in different child subtrees.

Return the greatest possible sum of all node values after applying any valid set of inversions, including the empty set.
