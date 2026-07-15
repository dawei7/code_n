# Coloring A Border

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1034 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/coloring-a-border/) |

## Problem Description

### Goal

You are given an $m\times n$ integer matrix `grid` and integers `row`, `col`, and `color`. Each grid value is the color of that square.

Two squares are adjacent when they share a side in one of the four directions. Squares with the same color belong to one connected component when a path of such adjacent, same-colored squares joins them.

A square on a component's border either lies on the first or last row or column of the grid, or has at least one adjacent square that is not in the component. Recolor only the border of the connected component containing `grid[row][col]` with `color`, then return the final grid.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ color matrix, where $1 \le m,n \le 50$ and every value is between $1$ and $1000$.
- `row` and `col`: a valid starting coordinate in `grid`.
- `color`: the new border color, between $1$ and $1000$.
- Let $P$ be the number of cells in the starting cell's connected component.

**Return value**

- The grid after recoloring exactly the component's border cells.

### Examples

**Example 1**

- Input: `grid = [[1,1],[1,2]], row = 0, col = 0, color = 3`
- Output: `[[3,3],[3,2]]`

**Example 2**

- Input: `grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3`
- Output: `[[1,3,3],[2,3,3]]`

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2`
- Output: `[[2,2,2],[2,1,2],[2,2,2]]`
- Explanation: The center belongs to the component but is not on its border.

### Required Complexity

- **Time:** $O(P)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Traverse the original component:** Record the starting color before any mutation. Use an explicit stack and a `seen` set to visit exactly the four-directionally connected cells with that color.

**Classify a cell while its neighbors are unchanged:** A visited cell is a border if it lies on a grid edge. It is also a border if any of its four neighbor positions is outside the grid or contains a color different from the original component color. Store border coordinates separately instead of recoloring immediately.

**Recolor after discovery:** Once traversal finishes, change every stored border coordinate to `color`. Delaying mutation prevents the new color from making later component cells appear disconnected or falsely bordered.

The traversal reaches every cell in the starting component and no cell outside it. The neighbor test is exactly the source definition of a component border, so every stored cell must be recolored and every unstored component cell must remain unchanged. Cells outside the component are never added to either collection.

#### Complexity detail

Each of the $P$ component cells is pushed once and checks four neighbors, so traversal and recoloring take $O(P)$ time. The `seen` set, stack, and border list each contain at most $P$ coordinates, using $O(P)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive depth-first search:** It expresses the same traversal compactly, but a 2500-cell component can exceed Python's recursion limit.
- **Temporary in-place markers:** Negate or otherwise mark component values during traversal, then restore interiors and recolor borders. This can reduce separate visited storage but requires care when the target color equals existing values.
- **Repeated reachability tests:** Determine component membership independently for many cells. This repeats traversal work and can take quadratic time.
- **Single-cell component:** Its neighbors are outside the component, so it is always a border.
- **Whole uniform grid:** Only the outer ring changes; interior cells keep the original color.
- **Disconnected equal colors:** Same-colored cells without a connecting path are not part of the selected component.
- **Unchanged color:** If `color` equals the original color, the returned values remain identical even though the border classification is the same.

</details>
