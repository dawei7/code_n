# Maximum Height by Stacking Cuboids

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1691 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/) |

## Problem Description
### Goal

You are given $n$ cuboids. Each entry `cuboids[i] = [width_i, length_i, height_i]` describes the three dimensions of one distinct cuboid. You may choose any subset, rotate each chosen cuboid by rearranging its dimensions, and place the chosen cuboids in a vertical stack.

An upper cuboid may rest on a lower cuboid only when its width, length, and height are each no greater than the corresponding dimension of the lower cuboid in their selected orientations. The stack's height is the sum of the selected vertical dimensions. Return the maximum height obtainable from a valid stack; each input cuboid can be used at most once.

### Function Contract
**Inputs**

- `cuboids`: a list of $n$ three-integer dimension lists, where $1 \le n \le 100$ and every dimension is between $1$ and $100$

**Return value**

The greatest total vertical height of any compatible stack made from a subset of the cuboids.

### Examples
**Example 1**

- Input: `cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]`
- Output: `190`

After suitable rotations, all three cuboids fit in one stack with vertical dimensions 95, 50, and 45.

**Example 2**

- Input: `cuboids = [[38, 25, 45], [76, 35, 3]]`
- Output: `76`

Neither cuboid can be placed on the other, so the taller orientation of the second cuboid is optimal by itself.

**Example 3**

- Input: `cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]`
- Output: `102`

All six entries describe the same dimensions under rotation and may be stacked with height 17 each.
