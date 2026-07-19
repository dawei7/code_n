## General
**Every color has a mandatory bounding rectangle**

For each color, find the smallest rectangle containing all of its final cells. Because that color can be printed only once, its actual print rectangle must contain this bounding box. Printing anything larger cannot remove a dependency, so the smallest box is sufficient for deciding feasibility.

Suppose color `b` appears inside color `a`'s bounding rectangle. The one print of `a` must initially cover that cell with `a`; for the final cell to be `b`, color `b` must be printed later. Record the directed dependency `a -> b`.

**Feasibility is exactly acyclicity**

Build all such edges by scanning each color's bounding rectangle, ignoring cells already equal to that color. Then topologically sort the color graph.

If every color is removed by the sort, print colors in that topological order using their bounding rectangles. Every foreign color inside a rectangle comes later by its recorded edge and overwrites the appropriate cells. A cell's final color is therefore the last dependency-compatible rectangle covering it, which is exactly the target color.

Conversely, any valid printing sequence must place `a` before every foreign `b` found in `a`'s mandatory rectangle. Thus it must respect every graph edge. A directed cycle would require each color in the cycle to be printed before the next and ultimately before itself, which is impossible. The grid is printable exactly when the graph is acyclic.

Kahn's algorithm starts with colors of indegree zero, removes their outgoing edges, and counts processed colors. Processing all $C$ colors proves acyclicity; getting stuck early proves a cycle.

## Complexity detail
Computing bounding boxes takes $O(MN)$ time. Each of the $C$ boxes contains at most $MN$ cells, so dependency construction takes $O(CMN)$ time. Topological sorting takes $O(C^2)$ in the worst case, which is covered by the same bound under the grid constraints.

The adjacency sets may contain $O(C^2)$ edges, while bounds, indegrees, and the worklist use $O(C)$ additional space.

## Alternatives and edge cases
- **Repeated rectangle elimination:** find a color whose bounding rectangle contains only itself or already erased cells, erase it, and repeat. This peels the last print first and is correct, but synchronous rescanning can take $O(C^2MN)$ time.
- **Depth-first cycle detection:** build the same dependency graph and use DFS states instead of indegrees. It has the same principal complexity.
- **One color:** its bounding rectangle is the entire occupied area and is always printable in one turn.
- **Separated cells of one color:** they can still be valid when one rectangle covers the gap and later colors overwrite it.
- **Checkerboard alternation:** mutually enclosing colors create a dependency cycle.
- **Nested rectangles:** print outer colors first and inner colors later.
- **Disjoint rectangles:** their colors have no dependency and may be printed in either order.
- **Duplicate edges:** store adjacency in sets so one color pair changes indegree only once.
- **Color labels:** labels need not be contiguous; graph nodes come from the colors actually present.
