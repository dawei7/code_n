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

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Identify the only region that may change**

Read the original color at `(sr, sc)`. A cell belongs to the fill region exactly when a path of horizontal or vertical neighbors connects it to the start and every cell on that path has the original color. Equal-colored cells separated diagonally or by another color are not part of the region.

**Traverse and recolor in one pass**

Use a queue for breadth-first search. Recolor the starting cell before enqueueing it. Whenever a queued cell is removed, inspect its four neighbors; each in-bounds neighbor still holding the original color is recolored immediately and enqueued. Recoloring at discovery time doubles as the visited marker, so a cell cannot enter the queue twice.

**Handle an unchanged color before traversal**

If the replacement equals the original color, return the image immediately. Without this guard, recoloring would not mark discovery and adjacent cells could repeatedly enqueue one another.

**Why exactly the connected component changes**

The start is correctly included. Every later recolored cell is an original-colored neighbor of an already reached component cell, so it also belongs to the component. Conversely, consider any cell in the component and a shortest valid path from the start to it. Breadth-first search processes that path in order, eventually discovering the cell. Barriers and diagonal-only matches are never crossed because only four in-bounds original-colored neighbors are admitted.

#### Complexity detail

For an `m` by `n` image, each cell is discovered at most once and each discovery checks four neighbors. Time is $O(mn)$ in the worst case, and the queue can contain $O(mn)$ cells, so auxiliary space is $O(mn)$.

#### Alternatives and edge cases

- **Iterative depth-first search:** a stack visits the same component with the same asymptotic bounds and avoids recursion depth limits.
- **Recursive depth-first search:** it is concise, but a long thin region can exceed Python's recursion limit.
- **Repeated whole-image propagation:** repeatedly scanning for cells adjacent to the new color can eventually produce the right image, but may rescan the entire matrix once per frontier layer.
- **Replacement equals original:** return immediately because no visible change or traversal is needed.
- **Single-cell component:** only the starting cell changes even if equal colors exist elsewhere.
- **Diagonal contact:** diagonal cells alone are not connected under four-directional movement.
- **Boundary start:** neighbor checks must not read beyond the first or last row or column.
- **In-place result:** changing the supplied matrix is permitted, and that same matrix is returned.

</details>
