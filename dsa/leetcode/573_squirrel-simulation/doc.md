# Squirrel Simulation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 573 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/squirrel-simulation/) |

## Problem Description
### Goal
On a two-dimensional grid, a squirrel must collect every nut and bring it to a fixed tree. The squirrel can move one cell horizontally or vertically per step, may carry only one nut at a time, and must place the carried nut at the tree before collecting another one.

The first trip begins at the squirrel's initial position; after returning the first nut, every later trip begins at the tree. Return the minimum total Manhattan distance needed to place all nuts at the tree. The order of collection is free, so the choice of the first nut is the only trip whose outward route does not start at the tree.

### Function Contract
**Inputs**

- `height`: the grid height
- `width`: the grid width
- `tree`: the tree coordinate
- `squirrel`: the squirrel's starting coordinate
- `nuts`: the nut coordinates

**Return value**

- The minimum Manhattan distance needed to bring every nut to the tree

### Examples
**Example 1**

- Input: `height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0],[2,5]]`
- Output: `12`

**Example 2**

- Input: `height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]`
- Output: `3`

**Example 3**

- Input: the squirrel starts at the tree
- Output: the sum of all tree-to-nut round trips

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use tree round trips as a baseline**

After delivering any nut, the squirrel is at the tree. Thus every nut except the first costs twice its Manhattan distance to the tree. Start with that round-trip cost for all nuts.

**Measure the first-trip replacement**

If a nut is collected first, its baseline outbound leg from the tree is replaced by a leg from the squirrel's initial position. Relative to the baseline, choosing that nut saves `tree_distance - squirrel_distance`.

**Choose the greatest saving**

Scan all nuts, add twice each tree distance to the baseline, and track the maximum saving. Subtract that saving from the baseline. The saving may be negative when the squirrel starts farther from every nut than the tree; the least-negative choice still gives the optimum because some nut must be first.

**Why only the first nut affects the choice**

Once the first nut is delivered, every remaining trip starts and ends at the tree, regardless of collection order. Those round-trip costs are fixed. The only variable part of any valid route is which nut replaces its tree-to-nut outbound leg with the initial squirrel-to-nut leg, so maximizing that one saving minimizes the complete route.

#### Complexity detail

Each of the `n` nuts requires two constant-time Manhattan distance calculations, giving $O(n)$ time. The baseline and best-saving scalars use $O(1)$ space.

#### Alternatives and edge cases

- **Try every first nut and recompute all trips:** is correct but repeats the fixed baseline and takes $O(n^2)$ time.
- **Choose the nut closest to the squirrel:** can be wrong because the tree distance determines how much baseline travel is replaced.
- **One nut:** the route is squirrel to nut to tree.
- **Squirrel at the tree:** every saving is zero and all trips are round trips.
- **Negative saving:** must not be clamped to zero because the squirrel cannot skip the initial trip.
- **Grid dimensions:** bound valid coordinates but do not change Manhattan distance calculations.
- **Collection order after the first:** has no effect on total distance.

</details>
