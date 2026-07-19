# Put Boxes Into the Warehouse I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1564 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/put-boxes-into-the-warehouse-i/) |

## Problem Description
### Goal

You have a collection of boxes, where `boxes[i]` is the height of one box, and a warehouse divided into rooms from left to right, where `warehouse[i]` is the height of one room. Every room can hold at most one box. You may rearrange the boxes before inserting them.

Boxes enter only through the left side of the warehouse. A box may be pushed to the right through empty rooms, but it cannot pass through a room whose height is smaller than the box. Once a box is left in a room, it occupies that room and cannot be moved again. Determine the maximum number of boxes that can be stored in the warehouse.

### Function Contract
**Inputs**

- `boxes`: A nonempty list of box heights. Let $B$ be its length, where $1 \le B \le 10^5$, and each height lies from $1$ through $10^9$.
- `warehouse`: A nonempty list of room heights ordered from the entrance to the deepest room. Let $W$ be its length, where $1 \le W \le 10^5$, and each height lies from $1$ through $10^9$.

**Return value**

Return the largest number of boxes that can be placed while respecting the left-entrance, clearance, and one-box-per-room rules.

### Examples
**Example 1**

- Input: `boxes = [4,3,4,1], warehouse = [5,3,3,4,1]`
- Output: `3`

**Example 2**

- Input: `boxes = [1,2,2,3,4], warehouse = [3,4,1,2]`
- Output: `3`

**Example 3**

- Input: `boxes = [1,2,3], warehouse = [1,2,3,4]`
- Output: `1`
