## General

**Use breadth-first search because every move costs one**

Each legal move goes to one orthogonally adjacent cell and contributes one step. This is an unweighted graph shortest-path problem: cells are vertices and legal adjacencies are edges of equal cost.

Breadth-first search explores all cells at distance one before distance two, all distance two before distance three, and so on. Therefore the first food cell it discovers is guaranteed to have minimum path length among every reachable food cell.

**Find the unique starting position**

The source uses

`next((i, j) for i in range(m) for j in range(n) if grid[i][j] == '*')`.

The generator scans rows and columns until it finds `'*'`. The contract guarantees exactly one, so `next` always succeeds and returns its coordinates.

This initial scan costs at most one full grid traversal.

**Represent the BFS frontier with a queue**

`q = deque([(i, j)])` begins with the start cell. The queue contains positions discovered but not yet expanded.

`dirs = (-1, 0, 1, 0, -1)` works with `pairwise` to produce the four direction pairs:

`(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`.

These are up, right, down, and left. No diagonal movement is generated.

**Process one distance layer at a time**

`ans` begins at zero. At the start of each outer while iteration, it is incremented by one. The inner loop runs exactly `len(q)` times as measured before processing that layer.

Initially the queue holds the start at distance zero, and `ans` becomes one before checking its neighbors. Thus food adjacent to the start correctly returns one.

Cells enqueued from the current layer are not processed until the next outer iteration because the inner loop's range captured the original queue length. This preserves BFS layering.

**Inspect legal neighboring cells**

For each direction, the source computes `x = i + a` and `y = j + b` and first checks grid bounds.

If `grid[x][y] == '#'`, food has been reached in exactly `ans` moves, so the method returns immediately. Since BFS layers are nondecreasing distances, no later food can be closer.

If the neighbor is `'O'`, it is traversable and not yet visited. The source changes it to `'X'` and enqueues it.

Existing `'X'` obstacles, the `'*'` start marker, and any other non-`'O'` nonfood cell are not enqueued.

**Mark a cell when it is discovered**

Changing an open cell to `'X'` before enqueueing serves as the visited set. Marking on discovery rather than on removal prevents two frontier cells from enqueueing the same neighbor.

This mutation uses the same marker as an obstacle because both original obstacles and visited cells should be excluded from future traversal.

The start itself is never changed, but it cannot be re-enqueued: the enqueue branch accepts only cells equal to `'O'`, while the start remains `'*'`.

**Why the first food distance is optimal**

Maintain the invariant that every cell processed during one outer iteration has distance `ans - 1` from the start. It holds initially with the start and `ans=1`.

Every inspected neighbor is one edge farther, so a food found there has distance `ans`. Every enqueued open cell also has that distance and is processed in the next layer after `ans` increments.

By induction, layers are processed in increasing distance order. All paths shorter than the returned `ans` have already been exhausted, proving the found food is closest.

**Return negative one when exploration is exhausted**

If the queue becomes empty, every reachable open cell has been visited and none had a food neighbor. Obstacles separate all remaining food from the start, or no food exists in the reachable region.

The source returns `-1`, exactly the required unreachable result.

**Trace a short route**

Suppose the shortest food path contains three edges. The start is processed with `ans=1`, its open neighbors with `ans=2`, and distance-two cells with `ans=3`. When one of those sees food as a neighbor, it returns three.

Other food cells may exist, but BFS's first discovery already minimizes over all of them.

## Complexity detail

Let $m$ and $n$ be the grid dimensions. Finding the start costs $O(mn)$ in the worst case. Each open cell is enqueued at most once, and expansion checks four neighbors, so BFS also costs $O(mn)$. Total time is $O(mn)$.

The queue can contain $O(mn)$ positions in the worst case. No separate visited matrix is allocated because the grid is mutated. Auxiliary space is therefore $O(mn)$ in the worst case due to the queue, matching the manifest.

The input grid's reachable `'O'` cells are permanently changed to `'X'`.

## Alternatives and edge cases

- **Depth-first search:** It can test reachability but does not discover shortest paths in distance order without extra distance tracking and repeated relaxation.
- **A* search:** A Manhattan-distance heuristic can prioritize promising cells, but multiple foods and heuristic computation add complexity; BFS already gives linear worst-case time.
- **Separate visited set:** It preserves the input at the cost of another $O(mn)$ structure.
- **Food adjacent to start:** The first layer returns one.
- **Multiple foods:** The first one found by BFS has globally minimum distance.
- **No reachable food:** The queue empties and returns `-1`.
- **Narrow one-cell corridor:** BFS follows it without special handling.
- **Original obstacle:** It is never enqueued.
- **Visited open cell:** Rewriting it to `'X'` prevents duplicate queue entries.
- **Start revisitation:** The `'*'` marker is not accepted by the open-cell branch.
- **Grid mutation:** Callers must not expect original open-cell markers after execution.
- **Layer size capture:** Using the queue length before the loop is essential to keep newly added cells in the next distance layer.
- **Direction encoding:** `pairwise(dirs)` produces exactly four orthogonal moves.
