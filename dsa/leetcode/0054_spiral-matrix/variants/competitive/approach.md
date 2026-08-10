## General

**Represent the remaining work as a rectangle**

Four inclusive bounds describe the unprocessed region: `left`, `right`, `top`, and `bottom`. Initially they enclose the entire matrix. One loop iteration appends the outer perimeter of that rectangle in clockwise order, then moves every bound inward by one.

The loop continues only while `left <= right` and `top <= bottom`, meaning at least one column and one row remain. This handles rectangular matrices and naturally stops after a center row, center column, or center cell is consumed.

**Traverse the top edge completely**

The first `for` loop visits columns `left` through `right` in row `top`. It includes both corners. This matches the spiral's current direction from left to right.

Because the corners are already included here, subsequent edge traversals must avoid appending them again. Most of the unusual range endpoints in the source exist specifically for that reason.

**Traverse only the interior of the right edge**

The second loop visits rows `top + 1` through `bottom - 1` at column `right`. It excludes the top-right corner already emitted by the top edge and also excludes the bottom-right corner, leaving that corner for the bottom edge.

If there is no interior row, Python's range is empty. No separate height check is necessary for this edge.

**Traverse the bottom edge in reverse when it is distinct**

The third loop iterates columns from `right` back to `left`. It includes both bottom corners. The append occurs only if `top < bottom`.

That condition prevents duplication when the remaining rectangle is a single row. In that case, top and bottom refer to the same row, which the first edge already emitted completely. For a region with at least two rows, the bottom row is distinct and must be traversed right to left.

The condition appears inside the loop rather than around it, so a single-row layer still performs range iterations without appending. This adds minor constant overhead but does not change correctness or asymptotic time.

**Traverse the interior of the left edge upward**

The fourth loop visits rows `bottom - 1` down through `top + 1` at column `left`. It excludes both left corners because the bottom and top edge traversals already handled them.

The append is guarded by `left < right`. When only one column remains, the right and left edges are the same column. The earlier top, right-interior, and bottom handling have already covered its cells, so an upward left traversal would duplicate them.

Again, keeping the guard inside the loop may iterate an otherwise unnecessary range, but it appends nothing in the degenerate case.

**Shrink to the next layer**

After the perimeter is complete, `left` and `top` increase while `right` and `bottom` decrease. Every cell on the old boundary is now outside the new rectangle. The new bounds enclose exactly the unvisited interior.

For a three-by-four matrix, the first layer produces the four top cells, the two non-corner right-edge cells as applicable, the bottom row in reverse, and the interior left edge. Shrinking leaves the middle interior segment, which the next iteration emits from left to right.

**Why every cell appears once**

At loop entry, assume the result contains exactly all cells outside the bound rectangle in spiral order and no cell inside it. The four traversals cover the rectangle's perimeter clockwise. Corner exclusions and single-row/single-column guards make these edge sets disjoint.

Shrinking removes precisely that perimeter, restoring the invariant for the inner rectangle. Eventually the bounds cross, so no unvisited rectangle remains. Every cell belongs to exactly one peeled perimeter and has been appended once in the correct order.

**Empty-input robustness**

The official reference describes a non-empty matrix, but the source checks `matrix == []` and returns an empty result. This avoids indexing `matrix[0]` for an empty outer list. It does not separately handle a nonempty outer list with an empty first row, which is also outside the rectangular non-empty contract.

## Complexity detail

Every matrix coordinate is appended exactly once. Some degenerate-layer loops may iterate without appending because their guard is inside the loop, but across all layers this remains proportional to the matrix perimeter work and bounded by $O(mn)$. Total time is $O(mn)$.

The algorithm stores four bounds, loop indices, and the result reference. `range` and `reversed(range(...))` are lazy range iterators rather than proportional lists in Python 3. Excluding the required output list, auxiliary space is $O(1)$, matching the manifest. The result itself necessarily uses $\Theta(mn)$ storage.

## Alternatives and edge cases

- **Visited-grid simulation:** Walk in a direction and turn when the next cell is outside or visited. It is intuitive but allocates $O(mn)$ marker space.
- **Direction simulation with destructive sentinel:** Mark input cells as visited in place. It saves a grid but mutates data and needs a guaranteed-safe sentinel.
- **Move guards outside loops:** Surround the entire bottom and left traversals with their conditions. This avoids empty append checks while preserving identical behavior.
- **Single row:** The top traversal emits it all, and `top < bottom` prevents bottom duplication.
- **Single column:** Top, right-interior, and bottom cover its cells; `left < right` prevents an upward duplicate pass.
- **One cell:** The top edge emits it, other traversals append nothing, and the bounds cross.
- **Empty matrix outside the primary contract:** The explicit early return yields `[]` safely.
- **Repeated cell values:** Boundaries track positions, so equal values are retained as separate output entries.
- **Tall or wide rectangle:** The same four inclusive bounds work independently of aspect ratio.
- **Input preservation:** No matrix cell is changed; only the output list is populated.
