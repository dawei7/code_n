# Number of Distinct Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 694 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Sorting, Matrix, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-distinct-islands/) |

## Problem Description
### Goal
Given a binary grid, an island is a maximal group of `1` cells connected horizontally or vertically. Determine how many distinct island shapes occur across the grid.

Two islands have the same shape when one can be translated so that all of its land cells coincide with the other island's cells. Rotation and reflection do not make shapes equivalent, and an island's absolute location does not matter. Return the number of distinct translation-normalized shapes; water cells and diagonal contact do not join islands.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix whose `1` cells are land and whose `0` cells are water

**Return value**

- The number of distinct island shapes under translation

### Examples
**Example 1**

- Input: `grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]`
- Output: `1`
- Explanation: both islands are translated copies of the same `2 x 2` block.

**Example 2**

- Input: `grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1,0,1],[0,0,0],[1,0,1]]`
- Output: `1`
- Explanation: every island consists of one cell.

### Required Complexity

- **Time:** $O(RC)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**Remove absolute position from an island**

When the row-major scan finds an unvisited land cell, use it as that island's origin. During a depth-first traversal, record each reached cell as `(row - origin_row, column - origin_column)`. Translating the whole island changes both the cell and origin coordinates equally, so these offsets do not change.

**Visit every island exactly once**

Maintain a global visited set. The traversal follows the four orthogonal neighbors, marking each land cell before pushing it. Consequently, a later grid position starts a traversal only if it belongs to a different connected component.

**Hash the complete relative shape**

Store each island's offsets as a `frozenset` inside a set of shapes. Two translated copies produce the same offset set, while islands that differ in any occupied relative position produce different sets. Because no rotation or reflection is applied to the offsets, those transformations remain distinct as required.

**Why the final set size is the answer**

Every land component contributes one canonical offset set. The representation is equal exactly for components related by translation, so inserting all representations into a set creates one entry per permitted shape-equivalence class.

#### Complexity detail

Each of the $R \cdot C$ cells is scanned once, and every land cell enters a traversal once, giving $O(RC)$ time. The visited set, traversal stack, one shape, and collection of distinct shapes can together store $O(RC)$ coordinates.

#### Alternatives and edge cases

- **Traversal-direction signature:** record entry directions and backtracking markers during a fixed-order DFS; the markers are essential so different branch structures do not collide.
- **Mutate the grid:** replace visited land with water to avoid a separate visited set; this saves one structure but destroys the caller's input.
- **Union-find:** build connected components first and then normalize their coordinates; it is valid but adds machinery without improving the asymptotic bound.
- Rotated or reflected islands are different unless the resulting occupied offsets happen to be identical without applying that transformation.
- An all-water grid has no islands and returns `0`.
- All isolated land cells share the same one-cell shape.
- Grid boundaries and water terminate a traversal and never contribute offsets.

</details>
