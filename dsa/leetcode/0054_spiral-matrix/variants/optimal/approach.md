## General
**Four boundaries describe the entire unvisited rectangle**

Maintain inclusive `top`, `bottom`, `left`, and `right` boundaries. Traverse the top edge left-to-right and increment `top`; traverse the remaining right edge top-to-bottom and decrement `right`. If cells remain, traverse the bottom edge right-to-left and decrement `bottom`, then the remaining left edge bottom-to-top and increment `left`.

Shrinking immediately after each edge means its corner cells are excluded from the following edge, so corners are not appended twice.

**A final one-row or one-column layer needs guards**

After consuming the top and right edges, the rectangle may have become empty. Check `top <= bottom` before traversing a bottom edge and `left <= right` before traversing a left edge. These guards prevent duplicating a lone row or column.

**Every perimeter removal leaves a smaller rectangle**

At the start of each loop, every cell outside the boundary rectangle has been emitted exactly once in spiral order, and no cell inside it has been emitted. Walking its perimeter and shrinking all visited sides preserves the invariant.

**Trace a rectangular, not merely square, matrix**

For a 3-by-4 matrix, emit the first row, the remaining right column, the bottom row in reverse, and the remaining left column upward. The boundaries then surround `[6,7]`, which forms the final top edge.

**Shrinking boundaries partition the matrix into perimeters**

At the start of an iteration, the four boundaries enclose exactly the unvisited rectangle. Traversing its top, right, bottom, and left edges in that order emits its outer perimeter clockwise. Guards before the reverse edges prevent a collapsed single row or column from being emitted twice.

Moving every boundary inward removes exactly those perimeter cells and leaves the next inner rectangle. Repeating this disjoint decomposition until the boundaries cross visits every cell once, and concatenating the nested perimeters gives the required global spiral order.

## Complexity detail
Each of the `mn` cells is appended once, so time is $O(mn)$. Excluding the required output list, four boundaries and loop indices use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Visited matrix plus direction changes:** is correct but uses $O(mn)$ extra state.
- **Repeatedly remove the first row and rotate the remainder:** is concise in Python but copies and shifts matrix data repeatedly.
- **Recursive layer traversal:** mirrors the boundary method but adds call-stack state without simplifying the edge guards.
- A one-row matrix is emitted only by the top-edge pass; a one-column matrix is emitted by the top cell and remaining right-edge pass.
- The traversal works for rectangular dimensions and does not assume $m = n$.
