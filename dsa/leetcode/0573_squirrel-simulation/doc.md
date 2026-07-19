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
