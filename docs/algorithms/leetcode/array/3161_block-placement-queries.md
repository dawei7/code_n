# Block Placement Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3161 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Binary Indexed Tree, Segment Tree, Ordered Set |
| Official Link | [block-placement-queries](https://leetcode.com/problems/block-placement-queries/) |

## Problem Description & Examples
### Goal
We are managing a linear space of size `x` (from 0 to `x`). We receive a sequence of queries: either placing an obstacle at a specific coordinate `x` or checking if a block of size `sz` can fit into any empty segment between existing obstacles (including the boundaries 0 and `x`).

### Function Contract
**Inputs**

- `queries`: A list of lists, where each inner list is either `[1, x]` (place an obstacle at `x`) or `[2, x, sz]` (check if a gap of size `sz` exists within the range `[0, x]`).

**Return value**

- A list of booleans indicating the result of each type-2 query.

### Examples
**Example 1**

- Input: `queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]`
- Output: `[false, true, true]`

**Example 2**

- Input: `queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]`
- Output: `[true, true, false]`

**Example 3**

- Input: `queries = [[2, 1, 1], [1, 2], [1, 3], [2, 3, 1]]`
- Output: `[true, true]`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Segment Tree** that maintains the maximum gap size within specific intervals. Since the coordinates can be large, we use a coordinate-compressed or fixed-size segment tree (up to 50,000). Each node in the tree stores the length of the longest empty segment in its range, the length of the empty segment starting at the left boundary, and the length of the empty segment ending at the right boundary.

---

## Complexity Analysis
- **Time Complexity**: `O(Q log N)`, where `Q` is the number of queries and `N` is the maximum coordinate value (50,000). Each update and query operation on the segment tree takes logarithmic time.
- **Space Complexity**: `O(N)`, required to store the segment tree nodes.
