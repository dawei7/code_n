## General
**Construct the four children before deciding whether to merge**

For a one-cell region, return a leaf holding that cell. For a larger region, split its side length in half and recursively construct the top-left, top-right, bottom-left, and bottom-right quadrants.

**Collapse four equal leaves into one region**

If all four returned children are leaves and carry the same Boolean value, their parent region is uniform, so discard those four roots and return one leaf. Otherwise return an internal node containing the children in quadrant order. The value stored on an internal node is irrelevant to the represented grid.

**Why bottom-up merging produces the canonical partition**

The base case exactly represents one cell. Inductively, each child exactly represents its quadrant. Four equal leaf quadrants cover a uniform parent and may be merged; in every other case the parent contains either differing values or finer structure and must remain divided. Thus every returned node represents precisely its region, with no uniform internal region left uncompressed.

## Complexity detail
The complete recursive partition has fewer than a constant multiple of the $n^{2}$ cells, and each recursive state performs constant work after its children return, so time is $O(n^2)$. The active recursion depth is $O(\log n)$; returned nodes are the required output and are excluded from auxiliary space.

## Alternatives and edge cases
- **Prefix-sum uniformity checks:** test a region in $O(1)$ and split only mixed regions; this also runs in $O(n^2)$ worst-case time but uses $O(n^2)$ auxiliary space.
- **Rescan each region:** checking all cells before every split can take $O(n^2 \log n)$ on highly mixed grids.
- **Compare every cell pair in a region:** correctly detects uniformity but can take $O(n^4)$ work at the root alone.
- **One-cell grid:** return one leaf without creating children.
- **Uniform grid:** the entire result must collapse to a single leaf.
- **Internal-node value:** only `isLeaf` and the four children determine an internal node's meaning.
