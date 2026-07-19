## General
**Reverse the direction of the searches**

Starting a search from every one repeats large portions of the grid. Instead, treat all zero cells as simultaneous sources. Their own answer is zero, and every other cell awaits the first zero-origin wave that reaches it.

**Initialize one shared breadth-first queue**

Create a distance matrix containing zero for source cells and `-1` for unvisited ones. Enqueue every zero before traversal begins. This represents BFS level zero from all possible destinations at once.

**Expand each cell only once**

Pop a cell and inspect its four valid neighbors. When a neighbor still has distance `-1`, assign the current distance plus one and enqueue it. An already assigned neighbor is never enqueued again.

**Why the first assigned distance is minimal**

Multi-source BFS processes cells in nondecreasing distance from the entire source set. Any path reaching an unvisited neighbor through the current cell has length `current + 1`; a shorter path would have placed that neighbor in an earlier BFS layer already. Thus the first assignment equals its shortest distance to any zero, and every reachable cell is eventually assigned.

## Complexity detail
Each of the `rows * cols` cells enters the queue at most once and examines four neighbors, giving $O(rows \cdot cols)$ time. The distance matrix and queue use $O(rows \cdot cols)$ space.

## Alternatives and edge cases
- **Two-pass dynamic programming:** propagates distances from top/left and then bottom/right with the same $O(rows \cdot cols)$ time and output storage.
- **BFS from every one:** is correct but repeatedly explores the matrix and can take quadratic time in the number of cells.
- **Check every zero for every cell:** is simple Manhattan-distance enumeration but costs $O(rows \cdot cols \cdot zero_count)$.
- **Zero cell:** always has distance zero and begins in the queue.
- **One row or column:** distances reduce to nearest-zero gaps along a line.
- **Several zeros:** simultaneous sources automatically select the closest one.
- **Rectangular matrix:** row and column bounds must use their separate dimensions.
