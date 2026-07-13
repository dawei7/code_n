# Island Perimeter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 463 |
| Difficulty | Easy |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/island-perimeter/) |

## Problem Description
### Goal
Given a rectangular binary grid, `1` marks land and `0` marks water. The grid contains exactly one island connected horizontally or vertically, is completely surrounded by water, and has no lakes: no interior water region is cut off from the surrounding water.

Return the island's perimeter measured in unit cell edges. Every land edge bordering a water cell or the outside contributes one, while an edge shared by two land cells is internal and contributes nothing. Diagonal contact does not remove perimeter because cells do not share an edge. Count the complete outline without modifying the grid; the function returns a length rather than the number of land cells.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix where `1` is land and `0` is water

**Return value**

- The number of unit edges separating land from water or from the outside of the grid

### Examples
**Example 1**

- Input: `grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]`
- Output: `16`

**Example 2**

- Input: `grid = [[1]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1, 1, 1]]`
- Output: `8`

### Required Complexity

- **Time:** $O(rows \cdot cols)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Begin with four edges per land cell**

An isolated unit square contributes four perimeter edges. Scan every grid position and add four whenever it contains land.

**Cancel shared interior edges once**

Two orthogonally adjacent land cells share an edge that is internal to the island. That edge was counted once for each cell, so subtract two. It is sufficient to check only the neighbor above and the neighbor to the left: every adjacent pair has exactly one lower or right cell that performs this cancellation.

**Why the remaining count is the perimeter**

Every land edge belongs to exactly one of two categories. If another land cell touches it, the pairwise subtraction removes both initial contributions. Otherwise the edge touches water or the grid exterior and remains counted once. The final total is therefore precisely the exposed boundary length, independent of the island's shape or holes excluded by the contract.

#### Complexity detail

The scan examines each of `rows * cols` cells once and performs constant work per cell, giving $O(rows \cdot cols)$ time. Only the running perimeter and loop indices are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Check all four neighbors:** add one for every land side facing water or the boundary; this is also linear and often intuitive.
- **DFS or BFS the island:** counts exposed sides while traversing land but needs $O(rows \cdot cols)$ visited or queue space in the worst case.
- **Land-coordinate list membership:** avoids mutating the grid but linear membership checks for every side can become quadratic in the number of land cells.
- **Single land cell:** all four sides are exposed.
- **One-row or one-column island:** shared edges cancel normally at the narrow boundary.
- **Concave boundary:** each water-facing side is counted independently, so indentations need no special geometry.
- **Grid border:** absence of a neighbor is water for perimeter purposes and causes no subtraction.

</details>
