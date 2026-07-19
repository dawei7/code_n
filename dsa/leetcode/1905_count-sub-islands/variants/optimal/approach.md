## General
**Traverse each `grid2` component once.** Scan every cell. When an unvisited land cell is found, start an iterative depth-first search. Mark a cell visited as soon as it is placed on the stack, here by changing its `grid2` value to zero, so no land cell can enter two traversals.

**Accumulate containment without stopping early.** Begin the component with `contained = True`. For every popped cell, set this flag to false if the corresponding `grid1` position is water. Continue visiting the entire component even after a mismatch; otherwise its remaining cells could later be mistaken for separate islands. After the stack empties, add one to the answer only if the flag stayed true.

Every `grid2` island is discovered exactly once, and the flag is true exactly when all cells in that maximal component overlap land in `grid1`. Thus precisely the sub-islands are counted.

## Complexity detail
Let $m$ and $n$ be the grid dimensions. The outer scan and all traversals together process each cell a constant number of times, for $O(mn)$ time. In the worst case the explicit DFS stack holds $O(mn)$ land cells, giving $O(mn)$ auxiliary space. Reusing `grid2` as the visited marker avoids a separate visited matrix.

## Alternatives and edge cases
- **Recursive DFS:** It expresses the same logic but a large island can exceed the language's recursion limit.
- **Breadth-first search:** A queue gives the same $O(mn)$ bounds and containment test.
- **Union-find:** Components can be built with disjoint sets, but this requires additional structure without improving the asymptotic bound.
- **Stop on the first mismatch:** The answer flag may be settled, but the entire invalid component must still be consumed.
- **Diagonal land:** Diagonally touching cells belong to different islands.
- **All water:** With no `grid2` islands, return zero.
- **Extra `grid1` land:** Only cells used by a `grid2` island matter; surrounding or unrelated `grid1` land is irrelevant.
