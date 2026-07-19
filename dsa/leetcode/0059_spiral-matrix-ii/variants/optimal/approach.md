## General
**The output matrix doubles as the destination state**

Create the `n` by `n` result matrix, then maintain inclusive `top`, `bottom`, `left`, and `right` boundaries around its unfilled rectangle. A counter supplies consecutive values beginning at `1`. No separate visited structure is needed because the shrinking rectangle identifies every unfilled cell.

**Fill and remove one clockwise perimeter**

Write across the top edge, down the right edge, across the bottom in reverse, and up the left edge. Shrink each boundary immediately after its edge and guard the final bottom or left traversal when only one row or column remains.

**Consecutive values follow the same path as spiral traversal**

At each loop start, cells outside the boundaries contain exactly `1` through `value - 1` in spiral order, while all cells inside remain unfilled. Filling the next perimeter continues that order and removes precisely those cells from the rectangle.

**Trace the center of an odd-sized matrix**

For $n = 3$, the outer perimeter receives `1,2,3,4,5,6,7,8`. Shrinking all four boundaries leaves only the center cell, which receives 9.

**Filled perimeters partition the output matrix**

At each iteration, the boundaries enclose exactly the unfilled rectangle. Traversing its four guarded edges visits the outer perimeter clockwise without duplicating a collapsed row or column, assigning the next consecutive values in spiral order.

Shrinking every boundary removes precisely that filled perimeter and exposes the next inner rectangle. These perimeters are disjoint and cover the square, so boundary exhaustion occurs only after all $n^{2}$ cells have received one value in the required order.

## Complexity detail
Every output cell is assigned once, so time is $O(n^2)$. Excluding the required result matrix, four boundaries and one counter use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Direction simulation with a visited matrix:** is intuitive but spends another $O(n^2)$ bits or booleans.
- **Check the output for zero before every turn:** reuses the matrix as visited state and remains linear in output size, though its direction logic is less structured.
- **Generate coordinates layer by layer recursively:** mirrors the same work but adds call-stack state.
- $n = 1$ fills the top edge with `1`; the remaining edge guards prevent any duplicate write.
- For odd `n`, the final rectangle is one center cell. For even `n`, the boundaries cross after the innermost perimeter without a center.
