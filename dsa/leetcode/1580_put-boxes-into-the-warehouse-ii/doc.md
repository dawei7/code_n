# Put Boxes Into the Warehouse II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1580 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/) |

## Problem Description
### Goal

You are given unit-width boxes with heights listed in `boxes` and a warehouse whose rooms are arranged from left to right with ceiling heights listed in `warehouse`. At most one box may occupy a room, and boxes cannot be stacked.

You may reorder the boxes and push each box into the warehouse from either the left entrance or the right entrance. A box cannot pass through a room whose height is smaller than the box; that room stops the box and any boxes queued behind it from that direction.

Choose the insertion order and entrance for every placed box. Return the maximum number of boxes that can be stored in the warehouse under these movement and height restrictions.

### Function Contract
**Inputs**

- `boxes`: A nonempty array of box heights.
- `warehouse`: A nonempty array of room heights from left to right.
- Both arrays have length at most $10^5$, and every height is between $1$ and $10^9$, inclusive.

**Return value**

Return the maximum number of boxes that can be placed, with at most one box per warehouse room.

### Examples
**Example 1**

- Input: `boxes = [1, 2, 2, 3, 4], warehouse = [3, 4, 1, 2]`
- Output: `4`

**Example 2**

- Input: `boxes = [3, 5, 5, 2], warehouse = [2, 1, 3, 4, 5]`
- Output: `3`

**Example 3**

- Input: `boxes = [1, 2, 3], warehouse = [1, 2, 3, 4]`
- Output: `3`
