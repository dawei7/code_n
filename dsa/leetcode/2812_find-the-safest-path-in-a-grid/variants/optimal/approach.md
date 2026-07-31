## General

**Compute distance from danger everywhere at once**

Place every thief cell into one queue with distance zero. A multi-source breadth-first search expands all sources simultaneously through orthogonal edges. The first time an empty cell is reached is along a shortest unweighted path from some thief, so the resulting value is exactly its minimum Manhattan distance to any thief.

**Optimize a bottleneck instead of a sum**

A path's score is the minimum distance value on it. Run a maximum-bottleneck form of Dijkstra's algorithm from `(0, 0)`. For each cell, store the greatest safeness achieved by any discovered path to it. Extending a path to a neighbor produces

$$
\min(\text{current path safeness},\text{neighbor distance}).
$$

Use a max-priority queue so the unsettled path with greatest safeness is processed first. If that state improves the neighbor's recorded value, update and push it. When the destination is removed from the heap, no later path can have a higher bottleneck: every later frontier state is no safer, and extension can only preserve or lower a bottleneck. Its value is therefore optimal.

This separates two concerns cleanly. The BFS derives the cell weight imposed by all thieves; the heap search selects a path maximizing the minimum of those weights. Thief cells remain traversable because their computed weight is simply zero.

## Complexity detail

Let $N=n^2$ be the number of grid cells. Multi-source BFS visits every cell and edge in $O(N)$ time. The maximin search may push each cell after improvements and uses heap operations costing $O(\log N)$, for $O(N\log N)$ total time. The distance matrix, best-safeness matrix, queue, and heap use $O(N)$ space.

## Alternatives and edge cases

- **Binary search plus reachability BFS:** Testing whether a path exists above each threshold is correct in $O(N\log n)$ time after the distance pass, but repeats grid traversals.
- **Union-find by descending distance:** Activating cells from safest to least safe and joining neighbors also works in $O(N\log N)$ due to sorting.
- **Compare every cell with every thief:** This computes correct distances but can take $O(N^2)$ before path search; multi-source BFS is linear.
- A thief at either endpoint forces the answer to `0`.
- A one-cell grid necessarily contains a thief under the input guarantee and returns `0`.
- Paths may cross thief cells; they are not blocked obstacles.
- Manhattan distance matches shortest orthogonal-grid distance, which is why multi-source BFS applies.
- Multiple equal-priority heap entries are harmless; stale states are skipped using the best-safeness matrix.
