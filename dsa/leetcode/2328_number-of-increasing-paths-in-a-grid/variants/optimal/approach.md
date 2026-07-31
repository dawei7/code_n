## General

Direct every valid move from its smaller endpoint to its larger endpoint.
Strict increase makes a directed cycle impossible, so the matrix becomes a
directed acyclic graph. Let `path_count[row][column]` count increasing paths
that end at that cell; initialize it to one for the one-cell path.

**Build the topological prerequisites**

For every cell, count its adjacent smaller neighbors. This is its indegree in
the increasing-edge graph. Cells with indegree zero are local minima and can
enter a queue immediately.

**Propagate complete path counts**

When a cell leaves the queue, all paths ending there are final because every
smaller predecessor has already been processed. For each larger neighbor, add
the current cell's path count to that neighbor: appending the larger neighbor
creates one distinct path for every path ending at the current cell. Decrement
the neighbor's remaining smaller-neighbor count and enqueue it when that count
reaches zero.

Kahn's process eventually handles every cell because the graph is acyclic.
Every increasing path has a unique last edge, or no edge when it contains one
cell, so initialization and edge propagation count each path exactly once.
Summing all ending counts therefore gives the requested total.

## Complexity detail

There are $mn$ cells and at most four directed edges incident from each cell.
Building indegrees and processing every edge take $O(mn)$ time. The indegree
matrix, path-count matrix, and queue each use $O(mn)$ space.

## Alternatives and edge cases

- **Memoized depth-first search:** Counting paths that start at each cell also
  takes $O(mn)$ time and space, but a legal grid can create a recursion chain
  of length $mn$, which is unsafe for Python's usual call-stack limit.
- **Sort all cells by value:** Processing cells in numeric order avoids graph
  indegrees but requires $O(mn\log(mn))$ time.
- **Equal adjacent values:** No edge connects them because every move must be
  strictly increasing; equal-valued cells remain distinct one-cell paths.
- **Multiple predecessors:** A cell is processed only after every smaller
  neighbor has contributed, preventing partial counts from propagating.
- **Single cell:** Its indegree is zero, its initialized count is one, and it
  contributes the sole valid path.
