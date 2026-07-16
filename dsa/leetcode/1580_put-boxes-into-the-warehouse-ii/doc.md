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

### Required Complexity

- **Time:** $O(B\log B + W\log W)$
- **Space:** $O(W)$

<details>
<summary>Approach</summary>

#### General

**Convert each room into a reachable capacity**

A box entering from the left can reach room `i` only if it fits every room from index zero through `i`. Its left-entry capacity is therefore the minimum height in that prefix. Similarly, its right-entry capacity is the minimum height from `i` through the final room.

Because either entrance may be used, room `i` can accept any box no taller than the larger of those two directional minima. Compute all prefix minima, scan backward for suffix minima, and replace each room by this effective capacity.

**Greedily match small boxes to small capacities**

Sort the box heights and effective room capacities. Scan capacities from smallest to largest while pointing at the smallest unplaced box. If that box fits, place it and advance the box pointer; otherwise, skip the room because no remaining box can fit it.

Using the smallest fitting box preserves every taller box for a room with at least as much capacity. If an optimal placement assigns a larger box to the current room while the smaller box is used later, swapping those boxes remains feasible. Repeating this exchange yields the greedy matching without reducing its size.

The directional minima encode a valid entrance for each matched room. Their structure comes from the same warehouse bottlenecks, so the matched capacities can be realized by filling rooms from the appropriate ends toward those bottlenecks.

#### Complexity detail

Let $B$ be the number of boxes and $W$ the number of warehouse rooms. Computing directional minima and matching take $O(B+W)$ time, while sorting dominates at $O(B\log B+W\log W)$.

The effective-capacity array uses $O(W)$ space. Sorting the box list in place does not require another asymptotically larger authored structure.

#### Alternatives and edge cases

- **Largest-box two-ended greedy:** sort boxes from largest to smallest and try each against the current left or right boundary room. This also achieves the optimal count with $O(B\log B)$ sorting time.
- **Bipartite matching:** model boxes and effective rooms as compatible vertices. It is correct but ignores the ordered threshold structure and is substantially more expensive.
- **Scan every remaining box per room:** repeatedly choose the smallest fitting unused box. This is correct but takes $O(BW)$ time.
- **One room:** place one box exactly when at least one box fits that room.
- **Central bottleneck:** boxes too tall to cross it may still occupy rooms reachable from the opposite entrance.
- **Tall rooms behind short entrances:** directional minima, not raw room heights, determine reachability.
- **More boxes than rooms:** at most $W$ boxes can be placed.
- **More rooms than boxes:** the answer is at most $B$.
- **Duplicate heights:** equal boxes and capacities are independent physical items and rooms.
- **No fitting box:** return zero.

</details>
