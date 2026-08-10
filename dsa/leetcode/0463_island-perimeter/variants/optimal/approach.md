## General

Each land cell is a unit square. Considered by itself, it contributes four unit edges to a perimeter. When two land cells share a side, that side becomes internal to the island: neither copy of the shared side belongs to the outside boundary. Starting from four edges per land cell and subtracting two per shared land-land side therefore gives the perimeter.

The exact solution scans every grid cell. For each land cell, it adds four, then checks only the cell below and the cell to the right. Each neighboring land cell found in those two directions removes two from the running answer.

**Why one shared side removes two edges**

Suppose two horizontal or vertical land squares touch. Adding four for each square initially counts the touching segment once as an edge of the first square and once as an edge of the second. The segment lies inside the combined shape, so both contributions are wrong. Subtracting two removes exactly those two copies.

No other perimeter contribution changes when the cells touch. Their remaining six unit edges stay exposed unless other neighbors cover them.

**Why checking only down and right is enough**

Every orthogonally adjacent pair has one cell above the other or one cell left of the other. The upper cell sees the pair when checking downward; the lower cell must not count it again. Similarly, the left cell sees a horizontal pair when checking rightward.

Thus, checking down and right finds every shared side exactly once. Checking all four directions would find each shared side twice and would require subtracting one per neighbor rather than two. The exact formulation avoids redundant comparisons while keeping the simple `+4, -2` accounting.

Boundary checks prevent accessing outside the matrix:

- `i < m - 1` means a row below exists before reading `grid[i + 1][j]`.
- `j < n - 1` means a column to the right exists before reading `grid[i][j + 1]`.

An edge on the grid boundary has no neighboring cell and remains in the four-edge contribution, correctly counting the exterior water that conceptually surrounds the grid.

**A compact formula**

If $L$ is the number of land cells and $A$ is the number of orthogonally adjacent land-cell pairs, then the scan computes

$$
4L-2A.
$$

This equals the perimeter because the first term counts every edge of every land square, while the second removes both copies of every internal shared edge.

**Trace simple shapes**

For a single land cell, add four. There is no land below or right, so nothing is subtracted and the answer is four.

For two horizontally adjacent cells `[1,1]`, add four for the first cell and subtract two for its right neighbor, leaving two so far. Add four for the second cell, whose right boundary has no cell. The total is six, matching the perimeter of a `1 x 2` rectangle.

For a solid `2 x 2` land block, four cells contribute 16. There are four shared sides—two horizontal and two vertical—so subtract eight. The perimeter is eight.

**Why every and only boundary edge remains**

Take any unit edge belonging to a land cell. If another land cell lies across it, the pair is encountered exactly once and both initial copies are removed. The edge contributes zero, as an internal edge should. If water or the grid exterior lies across it, no land-land pair exists, so the edge is never subtracted and contributes one. Summing over all edges therefore counts precisely those separating land from water or the exterior.

The method does not need to traverse the island as a graph, mark visited cells, or use the guarantee that there is exactly one connected component. The counting identity would sum the perimeters of multiple islands too. The no-lakes guarantee is also unnecessary for the local edge definition: if a lake existed, its land-water boundary would correctly contribute to perimeter under the usual geometric definition.

Diagonal contact has no effect because diagonal cells share a point, not a unit edge. The code checks only row- or column-adjacent cells.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. The nested loops visit all $mn$ cells exactly once. Each cell triggers only a fixed number of comparisons and arithmetic operations, so time complexity is $O(mn)$.

Only `m`, `n`, loop indices, and `ans` are stored. The grid is read but never modified, and no recursion, queue, visited matrix, or copied grid is created. Auxiliary space is $O(1)$.

The answer is at most $4mn$, safely small for the given dimensions. Each adjacency deduction is local and constant-time.

## Alternatives and edge cases

- **Check all four neighbors:** For every land cell, add one for each side adjacent to water or the exterior. It is equally $O(mn)$ and $O(1)$ but performs more neighbor checks.
- **Depth-first or breadth-first search:** Traverse the island and count exposed sides. This works, but needs a visited mechanism or input mutation and adds traversal machinery that whole-grid counting does not require.
- **Count land and adjacency separately:** First count all land cells and then all right/down land pairs; return `4 * land - 2 * pairs`. This is algebraically identical to the running update.
- **Single land cell:** No shared edges exist, so the result is four.
- **Land on a grid boundary:** Missing neighbors leave those unit edges counted as perimeter.
- **Diagonal land cells:** They do not share sides and therefore do not reduce one another's perimeter.
- **A thin line of cells:** Every consecutive pair removes two, leaving the perimeter of the resulting rectangle-like strip.
- **Water cells:** They add nothing; perimeter is attributed entirely through exposed land edges.
- **Multiple components outside the contract:** The formula would return their combined perimeter even though the source guarantees one island.
- **Input preservation:** The scan never changes any cell value.
