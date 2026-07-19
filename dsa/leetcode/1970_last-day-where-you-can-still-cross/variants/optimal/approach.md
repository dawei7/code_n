## General
**Reverse flooding into land activation**

After the final day every cell is water. Process `cells` backward, turning one
cell back into land at each step. Maintain connected components of activated
land cells with a disjoint-set union structure. A cell is joined to each
active cardinal neighbor.

Add two virtual nodes: one represents the top boundary and the other the
bottom boundary. Join every activated top-row cell to the top node and every
activated bottom-row cell to the bottom node. A crossing exists exactly when
these two virtual nodes belong to the same component.

**Translate the first reverse connection into the last forward day**

Suppose reverse processing activates `cells[day]`. The active cells are then
precisely those that remain land after the first `day` forward floods. If the
virtual boundaries become connected at this moment, day `day` is crossable.

Later reverse steps correspond to earlier forward days and can only add land,
so connectivity cannot disappear. The first reverse connection is therefore
the latest crossable forward day. Union-find cannot invent a path: every union
represents either a real cardinal land adjacency or a cell touching the
appropriate boundary. Conversely, every land path is joined edge by edge, so
an actual crossing necessarily connects the virtual nodes.

## Complexity detail
Here $N=\texttt{row}\cdot\texttt{col}$. Each cell is activated once and causes
at most six union operations: four neighbors and up to two virtual
boundaries. Union by size with path compression gives $O(N\alpha(N))$ total
time. The parent, component-size, and active-cell arrays use $O(N)$ space.

## Alternatives and edge cases
- **Binary search plus BFS or DFS:** Crossability is monotone over days, so
  search for the last true day and traverse the grid for every probe. This is
  correct but costs $O(N\log N)$ time.
- **Test every day forward:** Flood one cell and rerun a complete traversal.
  This can take $O(N^2)$ time.
- **Diagonal movement:** Diagonally touching land cells are not connected;
  only four cardinal directions are legal.
- Coordinates in `cells` are 1-based, whereas flattened array indices are
  naturally 0-based. Convert both coordinates before computing the index.
- Any dry top-row cell may start the path and any dry bottom-row cell may end
  it; no particular column must remain open.
- The returned day counts completed floods. It is not the zero-based index of
  the last dry cell in `cells`, although those values coincide in the reverse
  activation step used by the algorithm.
