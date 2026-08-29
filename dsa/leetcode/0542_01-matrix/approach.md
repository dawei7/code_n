## General

Every zero is already at distance zero from a zero. Every one needs the shortest number of horizontal or vertical steps to **any** zero. This is a shortest-path problem on an unweighted grid, and starting breadth-first search from all zero cells at once finds all answers in one expansion.

Think of each matrix cell as a graph vertex. Two vertices share an edge when their cells share a side. Every edge has cost one, exactly matching the distance definition.

**Use a separate answer matrix as both distance storage and visited state.** The solution creates `ans` filled with `-1`. Here, `-1` means that no shortest distance has been assigned yet.

During the initial matrix scan, every cell whose input value is zero receives `ans[i][j] = 0` and is appended to queue `q`.

This is called multi-source BFS: instead of choosing one source zero, the queue initially contains all zero sources at the same distance layer. The source guarantees at least one zero, so the queue is nonempty.

Input cells containing one remain `-1` in `ans` until the BFS first reaches them.

**Why all zeroes must start together.** If BFS ran separately from each zero, the matrix could be rescanned many times. By inserting every zero before expansion begins, the wave from the nearest zero reaches each cell first. The queue automatically interleaves the source waves in increasing distance order.

**Generate four side-sharing directions compactly.** Tuple:

`dirs = (-1, 0, 1, 0, -1)`

combined with `pairwise(dirs)` produces:

- `(-1, 0)` for up;
- `(0, 1)` for right;
- `(1, 0)` for down;
- `(0, -1)` for left.

No diagonal pair is generated, so every traversal step matches the common-edge distance rule.

**Expand in queue order.** The BFS removes `(i, j)` from the left of the deque. For each direction `(a, b)`, neighbor coordinates are `x = i + a` and `y = j + b`.

The neighbor is processed only if it is in bounds and `ans[x][y] == -1`. The method then assigns:

`ans[x][y] = ans[i][j] + 1`

and appends that neighbor to the queue.

The assignment reflects one edge from the current cell. Marking the distance before enqueueing is important: if several current-layer cells touch the same neighbor, only the first one enqueues it. Later attempts see a nonnegative value and skip it.

**Why the first assignment is the shortest distance.** All initial queue entries have distance zero. A FIFO queue processes every distance-zero cell before distance-one cells, every distance-one cell before distance-two cells, and so on. Therefore, when an unvisited cell is first reached from a cell at distance `d`, no path of length below `d + 1` can remain undiscovered. Its assigned value is final.

For:

`[[0,0,0],[0,1,0],[1,1,1]]`,

all border zeroes enter the queue at distance zero. The center one is reached in one step. Bottom-left and bottom-right are also one step from zeroes above them. Bottom-center is first reached from a distance-one neighbor and receives two.

**Why the nearest source wins without being identified.** The answer needs only a distance, not which zero supplies it. Multi-source BFS is equivalent to adding a virtual super-source connected to every zero by a zero-cost conceptual start, then exploring outward. The first wave reaching a cell necessarily came along a shortest path from some zero.

**Why every cell is eventually reached.** The rectangular grid is connected through side-sharing moves. Since at least one zero exists, repeated neighbor expansion can reach every cell. Thus no `-1` remains in the returned matrix.

**Why zero cells stay zero.** They are initialized as visited before BFS. Neighbor scans never update cells whose answer is not `-1`, so another source or wave cannot overwrite a zero with a positive distance.

The input `mat` is read but not modified. The returned `ans` matrix contains only computed distances.

## Complexity detail

Let $R$ and $C$ be the dimensions. The initialization scans all $RC$ cells. Each cell enters and leaves the queue at most once, and each dequeue checks four neighbors. Time is therefore $O(RC)$.

The answer matrix contains $RC$ integers, and the queue can hold $O(RC)$ coordinates in the worst case. Auxiliary/output construction space is $O(RC)$, matching the manifest.

The direction tuple and scalar coordinates use constant additional storage.

## Alternatives and edge cases

- **Two-pass dynamic programming:** A top-left pass uses top and left neighbors, then a bottom-right pass uses bottom and right. It also runs in $O(RC)$ time.
- **BFS from every one:** Repeating a search for each cell can become quadratic in the number of cells.
- **BFS from one zero at a time:** It repeats overlapping exploration; multi-source initialization merges all waves.
- **Use the input as visited storage:** It can reduce one separate state structure but mutates the caller's matrix and requires safe sentinel choices.
- **All zeroes:** Every answer starts at zero; BFS performs no positive assignments.
- **One zero:** The wave expands Manhattan distances from that single source.
- **One row or one column:** The same four-direction logic reduces naturally to the valid two directions.
- **Multiple equally near zeroes:** The first source wave assigns the same minimum distance either way.
- **No diagonal movement:** The direction pairs include only common-edge neighbors.
- **Boundary cells:** Coordinate checks prevent invalid accesses.
- **At least one zero:** This guarantee ensures every cell has a finite answer.
