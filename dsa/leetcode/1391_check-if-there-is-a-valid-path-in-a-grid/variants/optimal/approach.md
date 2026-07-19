## General
**Treat compatible borders as graph edges.** Associate each street type with its two opening directions. Begin a breadth-first search at `(0, 0)`. From a cell, inspect only the two neighbors indicated by its street piece.

An opening alone does not establish an edge. For a proposed direction `(dr, dc)`, first require the neighbor to lie inside the grid, then require its opening set to contain the reverse direction `(-dr, -dc)`. This reciprocal check precisely matches the rule that the two street pieces connect across their shared border.

Mark a cell when it enters the queue. Every enqueued cell is reachable by a sequence of compatible borders: this is true for the start, and the reciprocal check extends such a path by one valid move. Conversely, any valid path can be followed edge by edge by the search because each of its moves passes that same check. Thus reaching the lower-right cell is equivalent to the requested path existing. The visited set prevents cycles from causing repeated work.

## Complexity detail
There are $mn$ cells. Each is enqueued at most once and exposes exactly two directions, so traversal time is $O(mn)$. The queue and visited state can each hold $O(mn)$ coordinates.

## Alternatives and edge cases
- **Depth-first search:** A stack or recursion with the same reciprocal checks also runs in $O(mn)$; recursion can exceed the language call-stack limit on a long path.
- **Union-find:** Join every reciprocally compatible neighboring pair and compare the two endpoint roots. This also costs near-linear time but builds connectivity beyond what the single query needs.
- **One-sided opening:** A current tile pointing at a neighbor is insufficient when the neighbor does not point back.
- **Boundary-facing opening:** An opening that leaves the grid produces no move.
- **Cycles:** Visited state is necessary even though each tile has only two openings.
- **Single cell:** The start already equals the destination, so the answer is `true` regardless of its street type.
- **Destination orientation:** Reaching the destination is enough; its unused opening need not lead anywhere.
