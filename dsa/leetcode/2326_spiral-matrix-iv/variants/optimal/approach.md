## General

Allocate the result matrix with `-1` in every cell. Maintain inclusive `top`,
`bottom`, `left`, and `right` boundaries around the portion that has not yet
been visited. For each layer, consume linked-list nodes while traversing the
top edge from left to right, the right edge downward, the bottom edge from
right to left, and the left edge upward.

**Shrink each edge after it is traversed**

Moving a boundary inward removes exactly the edge that was just filled. Guards
before the bottom and left traversals prevent a remaining single row or single
column from being visited twice. If the linked list ends during any edge,
return immediately; all untouched cells already contain the required `-1`.

At the start of each layer, every cell outside the four boundaries is either
filled in the exact prefix order of the linked list or remains `-1` because the
function would already have returned. The four guarded traversals visit the
current perimeter once in clockwise order. Successive perimeters are disjoint
and cover the matrix, so each consumed node reaches exactly the required cell.

## Complexity detail

The output contains $mn$ cells, and each cell is initialized once and visited
at most once, giving $O(mn)$ time. Excluding the required result matrix, four
boundaries and loop variables use $O(1)$ auxiliary space. The returned matrix
itself occupies $O(mn)$ space.

## Alternatives and edge cases

- **Direction simulation with the output as visited state:** Since node values
  are nonnegative, `-1` can mark unvisited cells; this is also $O(mn)$ but
  requires careful turning logic.
- **Precompute spiral coordinates:** This is correct but uses another $O(mn)$
  list; repeatedly searching or removing its front can further degrade to
  $O((mn)^2)$ time.
- **List ends early:** Immediate return is safe because the matrix was
  initialized entirely to `-1`.
- **Single row or column:** The bottom and left guards prevent a collapsed
  layer from being written twice.
- **Full matrix:** When the list has exactly $mn$ nodes, the boundaries cross
  immediately after the final cell and no `-1` remains.
