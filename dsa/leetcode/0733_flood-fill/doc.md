# Flood Fill

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 733 |
| Difficulty | Easy |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/flood-fill/) |

## Problem Description
### Goal
An image is represented by an $m \times n$ integer grid, where each value is a pixel color. Given a starting pixel `(sr, sc)` and a replacement `color`, begin a flood fill from that position.

Change the starting pixel and every pixel connected to it horizontally or vertically through pixels having the starting pixel's original color. Do not cross pixels of another original color, and diagonal contact is not connected. Return the image after the complete region is recolored; if the new color already equals the original, the image remains unchanged.

### Function Contract
**Inputs**

- `image`: a nonempty rectangular integer matrix
- `sr`, `sc`: the row and column of the starting cell
- `color`: the replacement color

**Return value**

- The image after recoloring every cell reachable from `(sr, sc)` through up, down, left, or right moves that stay on the starting color

### Examples
**Example 1**

- Input: `image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2`
- Output: `[[2,2,2],[2,2,0],[2,0,1]]`

**Example 2**

- Input: `image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0`
- Output: `[[0,0,0],[0,0,0]]`

**Example 3**

- Input: `image = [[1,0,1],[0,1,0],[1,0,1]], sr = 1, sc = 1, color = 2`
- Output: `[[1,0,1],[0,2,0],[1,0,1]]`
