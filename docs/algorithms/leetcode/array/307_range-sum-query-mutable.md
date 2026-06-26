# Range Sum Query - Mutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `segtree_02` |
| Frontend ID | 307 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Design, Binary Indexed Tree, Segment Tree |
| Official Link | [range-sum-query-mutable](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problem Description & Examples
### Goal
Build a segment tree, then return the range-sum for
each (l, r) query. Standard divide-and-conquer query:
if the node's range is fully inside [l, r], return the
node's value; if outside, return 0; otherwise recurse.
O(log n) per query.
Source: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/

### Function Contract
**Inputs**

- `arr`: list of n integers.
- `n`: length of arr.
- `queries`: list of (l, r) tuples.
- `q`: number of queries.

**Return value**

a list of q range sums.

### Examples
_This local spec has fewer than three authored examples. Add original examples before marking this reference complete._

---

## Underlying Base Algorithm(s)
segment_tree

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `TODO`
