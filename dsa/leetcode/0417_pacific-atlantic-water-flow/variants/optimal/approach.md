## General

**Reverse the direction of the search**

Water flows from a cell to an orthogonally adjacent cell of equal or lower height. Starting a separate search from every cell would repeatedly explore many of the same paths. Instead, the solution starts from each ocean's boundary and traverses the flow relation backward.

If water can flow forward from a cell `A` to a neighbor `B`, then `height[A] >= height[B]`. A reverse search standing at `B` may therefore move to `A` when `height[A] >= height[B]`. Every cell reached by that reverse search has a valid forward downhill-or-level path to the ocean.

The algorithm performs this reverse breadth-first search twice: once from all Pacific boundary cells and once from all Atlantic boundary cells. A cell belongs in the answer exactly when both searches reach it.

**Seed each ocean with every directly touching cell**

The Pacific touches the left and top edges. For every row `i`, `(i, 0)` is placed in `q1` and marked in `vis1`; for every column `j`, `(0, j)` is also seeded.

The Atlantic touches the right and bottom edges. The corresponding seeds are `(i, n - 1)` and `(m - 1, j)` in `q2` and `vis2`.

Marking a cell when it is enqueued is important. Later traversal edges will not enqueue that cell again, preventing cycles on equal-height plateaus. The two corners shared by an ocean's two boundary loops can be inserted twice before BFS begins, but this is only a constant amount of harmless duplicate processing. Their visited flags are already true, so they do not cause their neighbors to be repeatedly enqueued.

For a one-cell grid, the sole coordinate belongs to all four conceptual edges. Both visited matrices mark it, and it correctly appears once in the final row-major scan.

**Traverse four orthogonal directions**

The tuple `dirs = (-1, 0, 1, 0, -1)` is a compact direction encoding. `pairwise(dirs)` yields

`(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`,

representing up, right, down, and left. Diagonal movement is never generated.

For a dequeued cell `(x, y)`, the candidate neighbor is `(nx, ny) = (x + dx, y + dy)`. It is enqueued only when all of the following are true:

- its row lies in `[0, m)`;
- its column lies in `[0, n)`;
- this ocean's visited matrix has not marked it; and
- `heights[nx][ny] >= heights[x][y]`.

The last comparison is the reversed flow rule. It may feel counterintuitive because the search climbs uphill, but the path is being discovered from ocean to source. Reversing the discovered path makes every step go from high or equal elevation to low or equal elevation, which is exactly how water travels.

Once accepted, the neighbor is marked before being appended to the queue. Each cell is therefore enqueued at most once per ocean during normal traversal.

**What each visited matrix means**

After `bfs(q1, vis1)`, `vis1[i][j]` is true exactly when `(i,j)` can send water to the Pacific. It is not merely an implementation-level “already processed” flag; it is also the computed reachability result. `vis2` has the same meaning for the Atlantic.

To see why, every seed directly touches its ocean, so the statement is true for seeds. Whenever reverse BFS moves from a reached lower cell to an equal-or-higher neighbor, water can flow from that neighbor back to the reached cell and then along the already known path to the ocean. This proves every marked cell really reaches the ocean.

Conversely, suppose a cell has some valid forward path to the ocean. Reverse that path. It starts at an ocean boundary and each reversed step moves to an equal-or-higher cell, so BFS is permitted to follow every edge. The cell must eventually be marked. Thus the visited set contains all and only cells that reach that ocean.

**Intersect the two reachability results**

The return comprehension scans every coordinate and includes `(i, j)` when both `vis1[i][j]` and `vis2[i][j]` are true. The two correctness statements above make this logical AND exactly equivalent to having a valid path to both oceans.

The contract allows any output order. The implementation happens to return deterministic row-major order because `i` and `j` are scanned increasingly. It returns tuples rather than explicitly constructed inner lists; in the Python execution environment these coordinate pairs represent the requested two-dimensional coordinates.

**Why two reverse searches avoid repeated work**

A forward search from one cell can branch into many paths and overlap heavily with searches from neighboring cells. Reverse traversal consolidates every source for one ocean into a single multi-source BFS. Once a cell is marked for that ocean, its entire reachability fact is reused globally. No distances are needed; the queue merely ensures every newly discovered reachable cell is eventually expanded.

## Complexity detail

Let $r=m$ be the number of rows and $c=n$ the number of columns. For each ocean, every cell is marked and enqueued at most once through traversal, and each dequeue checks four neighbors. Boundary corner duplication adds only constant extra work. Two BFS runs therefore take $O(rc)$ time. The final intersection scan also takes $O(rc)$ time, leaving total time $O(rc)$.

Each visited matrix contains $rc$ Booleans, and in the worst case each queue can hold $O(rc)$ coordinates. The returned answer can itself contain all $rc$ cells. Auxiliary space is $O(rc)$, and output space is also $O(rc)$ in the worst case.

## Alternatives and edge cases

- **Run DFS or BFS from every cell:** This directly tests whether each source reaches both oceans but can revisit the grid for every source, reaching $O((rc)^2)$ time in a worst case.
- **Reverse depth-first search:** The same multi-source and reversed-height reasoning works with DFS and still takes $O(rc)$ time. Recursive DFS risks a call stack as deep as the number of cells; the deque avoids that risk.
- **One traversal carrying ocean bit flags:** Reachability information can be combined in other graph formulations, but two independent searches make the proof and state separation simple.
- **Use the forward inequality during reverse search:** Checking `neighbor <= current` from the ocean is wrong; it finds cells the ocean could flow downhill into, not cells whose rain can flow to the ocean. Reverse traversal must accept equal-or-higher neighbors.
- **Equal-height plateaus:** The `>=` comparison permits movement across equal cells in either direction, as required. Visited marking prevents endless cycles.
- **Single row:** Every cell touches both the top Pacific edge and bottom Atlantic edge, so every coordinate is returned.
- **Single column:** Every cell similarly touches both left and right ocean edges and is returned.
- **One cell:** It touches both oceans and appears in the intersection.
- **Strictly rising terrain:** Reverse traversal climbs from each ocean until blocked according to the opposing boundary; the intersection still follows from the same reachability proof.
- **Boundary duplication:** Corner cells may be seeded twice in one queue, but they are never duplicated in the result because the final scan tests Boolean matrices once per coordinate.
- **No diagonal flow:** `pairwise(dirs)` creates exactly four orthogonal moves and cannot cross a corner diagonally.
