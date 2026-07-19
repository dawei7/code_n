## General
**Start from every rotten orange at once:** Scan the grid once, enqueue all initially rotten cells, and count the fresh oranges. These sources form minute zero of a multi-source breadth-first search. Processing them together is essential because rotting from every source occurs simultaneously.

**Advance one breadth-first layer per minute:** For each queued cell, inspect its four neighbors. When a neighbor is fresh, change it to rotten immediately, decrement the remaining-fresh count, and enqueue it with the next minute. Immediate marking prevents two sources from enqueuing the same orange. The greatest minute assigned to any newly rotten orange is the elapsed time.

Breadth-first search reaches each orange by the shortest 4-directional path from any initial rotten source, so its layer number is exactly the earliest minute when that orange can rot. After the queue empties, a positive fresh count proves that barriers or disconnected cells made complete rotting impossible.

## Complexity detail
The initial scan and breadth-first traversal each inspect $O(A)$ cells, and every cell is enqueued at most once, so time is $O(A)$. The queue can hold $O(A)$ cells, giving $O(A)$ space.

## Alternatives and edge cases
- **Rescan the entire grid each minute:** Simulating simultaneous changes with repeated full-grid scans is correct, but a long narrow propagation path can require $O(A^2)$ time.
- **Depth-first search from each source:** DFS does not naturally preserve earliest arrival times and may revisit cells unless distances are repeatedly relaxed.
- **No fresh oranges:** Return zero even if the grid contains only empty cells and rotten oranges.
- **No initial rotten orange:** Return `-1` when any fresh orange exists because propagation cannot begin.
- **Disconnected fresh region:** Empty cells block movement, and diagonal contact does not spread rot.
