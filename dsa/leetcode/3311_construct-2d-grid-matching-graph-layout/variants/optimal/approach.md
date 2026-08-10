## General

**Grid geometry is encoded by node degrees.** In a rectangular grid graph, a corner has degree two when both dimensions exceed one, a non-corner boundary cell has degree three, and an interior cell has degree four. In a one-cell-wide grid, the graph is a path whose endpoints have degree one. These recognizable degrees let the source discover one boundary row without knowing coordinates.

The adjacency list `g` stores the undirected graph. Array `deg` has five slots and records one example node for each observed degree. It does not count nodes; assignment `deg[len(ys)] = x` overwrites earlier examples. One representative is enough for the case analysis.

**Case one: the grid is a path.** If a degree-one node exists, one grid dimension is one. The source makes that endpoint the initial `row` of length one. Later row extension follows the path one node at a time, producing an $n\times1$ layout. Rotating it to $1\times n$ would also be valid.

**Case two: one grid dimension is two.** If there is no degree-four node, the grid has no true interior. Excluding the path case already handled, the guaranteed rectangular grid has a dimension of two. The source starts at a degree-two corner `x` and finds a degree-two neighbor `y`. Those adjacent corners form the short two-cell side, so `row = [x,y]`. In a $2\times2$ grid every node is a degree-two corner, and any adjacent pair is a valid side.

**Case three: both dimensions are at least three.** Degree-four interior nodes exist. The source chooses a degree-two corner and follows one of its two neighbors along the boundary. A boundary continuation is recognizable by degree below four. While the current node has degree greater than two, it is a degree-three non-corner boundary node. Among its neighbors, the code chooses one that is not the predecessor and also has degree below four. This walks along one outer side until reaching another degree-two corner, which is appended to complete `row`.

The first corner neighbor is `g[x][0]`, so the chosen side is arbitrary. It may be the longer or shorter dimension. Contrary to the manifest summary, the source does not search for a shortest corner-to-corner side. Either complete side is sufficient to orient a valid grid.

**Extend the boundary inward one row at a time.** The number of rows in the other dimension is `n // len(row)`. For each remaining layer, the source first marks every node in the current row visited. Then, for each current row node $x$, it scans neighbors and chooses the first unvisited one.

Why is that neighbor the cell directly across in the next row? Horizontal neighbors in the same row have just been marked. Nodes in all earlier rows were marked during previous iterations. In a valid grid, the only remaining unvisited neighbor of a non-final-row cell is its vertical neighbor in the next row. Appending these chosen nodes in current-row order preserves column alignment.

The next row becomes current and the process repeats. Grid guarantees ensure every current cell has an unvisited outward neighbor until the final required layer; no separate backtracking is necessary.

**Why adjacency is preserved in both directions.** Within the initial row, consecutive nodes came from actual boundary edges. Every later row inherits horizontal ordering because vertically corresponding nodes in a rectangular grid have horizontal edges in the same column sequence. Between adjacent rows, each new cell was selected through an edge from the cell above it.

Conversely, the original graph is guaranteed to be exactly a grid graph. Degree structure and visited filtering prevent selecting diagonal or non-grid relations. The constructed rectangle contains $n$ cells, and its horizontal and vertical adjacencies account for the graph's only edges. Thus the “if and only if” condition holds.

## Complexity detail

Let $n$ be the number of nodes and $m$ the number of edges. Building adjacency takes $O(n+m)$ time and space. Boundary discovery follows at most one side, $O(n)$. During row extension, every node becomes part of one row, and each scan inspects at most its grid degree of four; equivalently total adjacency work is $O(n+m)$. Overall time is $O(n+m)$.

Adjacency uses $O(n+m)$ space, `vis` uses $O(n)$, and the returned grid stores all $n$ node IDs. Working and output space together are $O(n+m)$, matching the manifest.

## Alternatives and edge cases

- **Coordinate propagation:** Assign a corner coordinate and infer neighbor directions through common-neighbor relationships. It is more general-looking but needs conflict handling and more bookkeeping.
- **Try all corner-side orientations:** One could build candidate layouts from both neighbors of a corner and validate edges. The guaranteed grid structure makes the source's arbitrary valid side sufficient.
- **One-row path:** Degree-one detection chooses an endpoint and the extension produces a single-column rotation of the same path.
- **Two-by-two grid:** No degree-four node exists; a corner and any degree-two neighbor form an initial side of length two.
- **Two-by-many grid:** Adjacent degree-two corners identify the short side. Degree-three nodes then fill successive rows.
- **Both dimensions at least three:** Degree-four presence selects boundary walking from one degree-two corner to another.
- **Square grid:** Either corner direction has the same length, and rotations or reflections are all accepted.
- **Rectangular non-square grid:** The source may choose either side, not necessarily the shortest. The number of generated rows adjusts through `n // len(row)`.
- **Adjacency-list order:** It affects rotation/reflection and which side is chosen, but any resulting valid layout is allowed.
- **Why mark the whole row first:** If nodes were marked one at a time while choosing neighbors, a horizontal neighbor later in the current row might still look unvisited and be mistaken for the next layer.
- **Degree representative overwrite:** `deg[d]` keeps only the last node of degree $d$; existence and one starting example are all the case split needs.
- **Malformed non-grid input:** Missing outward neighbors or unexpected degrees could leave variables unset or rows incomplete. The guarantee excludes such cases.
- **Manifest discrepancy:** No shortest-path or shortest-side computation occurs; the code follows an arbitrary boundary side determined by adjacency order.
