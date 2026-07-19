## General
**Use leaf values as region-wide facts**

A leaf represents a uniform square. OR with a true leaf makes the whole corresponding region true, so return a true leaf immediately. OR with a false leaf leaves the other region unchanged, so return the other subtree.

**Recurse only when both regions are divided**

When both nodes are internal, combine their matching top-left, top-right, bottom-left, and bottom-right children. Each recursive call represents the OR of exactly the same spatial quadrant.

**Compress uniform children**

After computing four children, check whether all are leaves with the same Boolean value. If so, replace them with one leaf; otherwise retain an internal node with those four results.

**Why the returned tree represents the cell-wise OR**

At a leaf shortcut, Boolean identity or domination gives the correct value for every cell in that square. At two internal nodes, the four recursive calls partition the square into disjoint quadrants and are correct by induction. Recombining them covers the whole square, and compressing four equal uniform children changes only representation, not any cell value.

## Complexity detail
Let `q` be the number of paired quad-tree nodes actually examined. Each examined pair performs constant work before either returning or making four disjoint recursive calls, so time is $O(q)$. Recursion follows at most the tree height `h`, using $O(h)$ call-stack space; returned nodes are output storage.

## Alternatives and edge cases
- **Expand both trees into dense grids:** is correct but can use time and space proportional to every represented cell, exponentially larger than a sparse tree's node count.
- **Always clone the untouched subtree:** preserves immutability but performs avoidable work when a false leaf lets the existing subtree be returned safely.
- **True leaf:** short-circuits the entire paired region to true.
- **False leaf:** acts as the identity and preserves the other region.
- **Both leaves:** reduce immediately to one leaf containing their Boolean OR.
- **Uniform recursive result:** four equal leaves must be compressed into one canonical leaf.
- **Internal node value:** is semantically irrelevant; only `isLeaf` and the children describe a divided region.
