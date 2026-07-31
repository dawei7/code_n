## General

Because every move goes right or down, all possible predecessors of `(i, j)` have already been processed during a row-major scan. A predecessor in the same row is useful while its farthest reachable column is at least $j$; a predecessor in the same column is useful while its farthest reachable row is at least $i$.

Maintain one min-heap for every row and every column. A row entry stores `(distance, farthest_column)`, and a column entry stores `(distance, farthest_row)`. Before evaluating a cell, remove heap roots whose reach ends before the current coordinate. The remaining root, if any, has the smallest visited-cell count among predecessors that can reach this cell.

The origin receives distance $1$. Every other reachable cell receives one plus the smaller valid root distance from its row and column heaps. Insert that new state into both corresponding heaps with reach extended by the cell's jump value.

An expired entry that is not currently at the root cannot affect the minimum while a cheaper valid root exists. If it later reaches the root, the expiration loop removes it before use. Thus each heap root query supplies exactly the cheapest valid predecessor. Row-major order covers all legal incoming moves, so the computed distances are the shortest path lengths measured in visited cells.

## Complexity detail

There are $mn$ cells. Each reachable cell is inserted once into a row heap and once into a column heap, and every entry is removed at most once. Heap operations cost $O(\log(mn))$ in the worst case, giving $O(mn\log(mn))$ time. The row and column heaps together store $O(mn)$ entries.

## Alternatives and edge cases

- **Successor sets with breadth-first search:** Ordered unvisited positions can ensure every cell is discovered once, also avoiding repeated range enumeration.
- **Monotonic-stack dynamic programming:** Carefully maintained row and column candidate stacks can achieve linear time but require more intricate dominance handling.
- **Enumerate every jump destination:** Ordinary BFS is correct, yet repeatedly scans already-visited cells and can require $O(mn(m+n))$ work.
- **Single cell:** The origin is the destination, so exactly one cell is visited.
- **Zero-valued cell:** It creates no outgoing moves but may still be a valid destination.
- **Visited cells versus moves:** A path with $k$ moves visits $k+1$ cells.
- **Unreachable target:** If neither heap supplies the bottom-right cell, return $-1$.
- **Boundary clipping:** Stored reach may extend outside the grid; comparison with actual coordinates is sufficient, so explicit clipping is optional.
