# Find the Number of Ways to Place People II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3027 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Sorting, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/) |

## Problem Description

### Goal

You are given $N$ distinct integer-coordinate points in a two-dimensional plane, and exactly one person will stand at each point. Increasing $x$ moves right, decreasing $x$ moves left, increasing $y$ moves up, and decreasing $y$ moves down.

Choose an ordered pair of positions for Alice and Bob. Alice must be the upper-left corner and Bob the lower-right corner of an axis-aligned rectangular fence, so $x_A\le x_B$ and $y_A\ge y_B$. The fence may have zero width or zero height and therefore may be a vertical or horizontal line.

Alice and Bob want no third person inside the closed fence or anywhere on its border. Count the ordered pairs for which every other supplied point lies outside that rectangle or line. Reversing the two people is not allowed unless the reversed positions independently preserve the required upper-left and lower-right roles.

### Function Contract

**Inputs**

- `points`: A list of $N$ distinct coordinate pairs `[x, y]`, where $2\le N\le1000$ and $-10^9\le x,y\le10^9$.

**Return value**

The number of ordered Alice-Bob placements whose closed upper-left-to-lower-right fence contains no third point.

### Examples

#### Example 1

- **Input:** `points = [[1, 1], [2, 2], [3, 3]]`
- **Output:** `0`

Every point to the right is also higher, so no ordered pair has the required orientation.

#### Example 2

- **Input:** `points = [[6, 2], [4, 4], [2, 6]]`
- **Output:** `2`

The adjacent pairs on the descending diagonal are empty; the outer fence contains `[4, 4]`.

#### Example 3

- **Input:** `points = [[3, 1], [1, 3], [1, 1]]`
- **Output:** `2`

The horizontal and vertical line placements are valid, while the larger rectangle is blocked by `[1, 1]` on its border.
