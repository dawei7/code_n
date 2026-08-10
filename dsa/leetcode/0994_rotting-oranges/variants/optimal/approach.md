## General

**Model each minute as one breadth-first layer**

Rotting spreads one grid edge per minute: a rotten orange affects fresh oranges immediately above, below, left, or right. This is the same structure as shortest distances in an unweighted graph, where orange cells are vertices and four-directional adjacencies are edges.

Breadth-first search processes vertices by increasing distance. If all initially rotten oranges enter the queue at time zero, then the next BFS layer contains oranges that rot after one minute, the layer after that contains oranges that rot after two minutes, and so on.

This must be a multi-source BFS. Starting separately from each rotten orange and taking a minimum afterward would repeat work. Placing all sources in one queue lets their waves expand simultaneously, just as the physical process does.

**Scan the grid to establish the initial state**

The first nested loop performs two jobs:

- every cell containing `2` is appended to queue `q` as an initial rotten source;
- every cell containing `1` increments `cnt`, the number of fresh oranges still unrotted.

Empty cells need no stored state. Dimensions `m` and `n` support boundary checks later.

After this scan, `cnt` is the exact remaining work. It provides an efficient success test without rescanning the entire grid after BFS.

**Freeze the current minute's frontier**

The main loop runs while both `q` and `cnt` are nonzero. At its start, all coordinates currently in `q` became rotten no later than the same current time frontier and are ready to spread during the next minute.

The code increments `ans` once, then executes

`for _ in range(len(q))`.

As with level-order tree traversal, `len(q)` is captured before processing the layer. Newly rotten neighbors appended during the loop are not processed until the next outer iteration. That delay is essential: an orange that rots at minute one cannot rot another orange during that same minute; its effect begins in the following minute.

**Generate four-directional neighbors**

Tuple

`dirs = (-1, 0, 1, 0, -1)`

combined with `pairwise(dirs)` produces offsets up, right, down, and left. For a popped coordinate `(i, j)`, each candidate is `(x, y) = (i + a, j + b)`.

The compound condition verifies that the coordinate is inside the grid and that `grid[x][y] == 1`. Rotten cells, empty cells, and out-of-bounds positions are ignored.

When a fresh neighbor is found, the code immediately:

1. changes its grid value from one to two;
2. appends its coordinate to the queue for the next layer;
3. decreases `cnt`.

Marking it rotten at enqueue time prevents two current rotten oranges from enqueueing and counting the same neighbor twice.

**Return at the exact minute the final orange rots**

After decrementing `cnt`, the code checks whether it became zero. If so, it returns the current `ans` immediately.

Since `ans` was incremented at the beginning of this frontier expansion, it equals the minute in which these neighbors rot. There is no need to process unused coordinates already in the queue or begin another layer.

**Handle cases where BFS does not run**

The final line is:

`return -1 if cnt else 0`.

There are two important ways to reach it:

- If `cnt == 0` immediately after scanning, no fresh orange existed at minute zero. The loop is skipped and zero is correct, whether or not rotten oranges exist.
- If `cnt > 0` but the queue becomes or starts empty, no remaining rotten frontier can reach those fresh oranges. The loop ends and `-1` reports impossibility.

If BFS rots every fresh orange, the method normally returns early inside the neighbor loop. The conditional final return still correctly covers all non-early paths.

**Trace the propagation by layers**

For

`[[2, 1, 1], [1, 1, 0], [0, 1, 1]]`,

the initial queue contains the top-left orange and `cnt = 6`.

- Minute one processes only the initial source, rotting its right and lower neighbors.
- Minute two processes those two newly rotten oranges and reaches the next fresh positions.
- Minute three advances the frontier farther toward the bottom right.
- Minute four rots the final fresh orange, makes `cnt = 0`, and returns four.

Even if one source can reach a cell by a longer route and another by a shorter route, multi-source BFS first enqueues it from the shortest layer. Immediate marking prevents a later, longer route from changing its time.

**Why `ans` is the minimum possible time**

For any fresh orange that can eventually rot, its rotting time is the length of the shortest four-directional path from any initially rotten orange through orange cells. Empty cells cannot carry the process.

Multi-source BFS visits coordinates in nondecreasing shortest-path distance. By induction on layers, coordinates in the first generated layer have distance one, and any coordinate first generated from layer `t - 1` has a path of length `t`. If a shorter path existed, it would have been generated from an earlier layer.

Therefore, when the last fresh orange rots in layer `ans`, no process obeying the one-edge-per-minute rule could finish sooner. If a fresh orange is never reached, no such path exists and completion is impossible.

**Input mutation serves as visited state**

Changing fresh cells from one to two records both their new physical state and that BFS has discovered them. A separate visited matrix would duplicate this information. The tradeoff is that the caller's grid no longer retains its original fresh/rotten layout.

## Complexity detail

Let `A = mn` be the number of grid cells.

The initial scan examines all `A` cells. Every orange coordinate enters and leaves the queue at most once because it is marked rotten when first enqueued. Each dequeue checks four directions, a constant amount of work. Total time is `O(A)`.

In the worst case, the queue can hold `O(A)` rotten coordinates across its frontier, so auxiliary queue space is `O(A)`. The algorithm uses the grid itself instead of a separate `O(A)` visited matrix.

## Alternatives and edge cases

- **Run BFS from each source separately:** It repeats traversal and requires combining arrival times. One multi-source queue obtains nearest-source distances directly.
- **Depth-first search:** DFS does not naturally preserve simultaneous minute layers. It would need stored arrival times and repeated relaxations to recover shortest propagation times.
- **Minute delimiter in the queue:** A sentinel can mark layer endings. Freezing `len(q)` is simpler and avoids special coordinates.
- **Timestamp values in the grid:** Repeatedly scan for cells of the current timestamp to avoid a queue. This saves queue space but can make time quadratic in the number of cells.
- **No fresh oranges:** Return zero immediately through the skipped loop and final conditional.
- **Fresh oranges but no rotten source:** The empty queue cannot start propagation, so return `-1`.
- **Isolated fresh region:** Empty cells or boundaries may disconnect it from every source; `cnt` remains positive after the queue empties.
- **Several sources reaching one orange:** The first source marks it at enqueue time, so it is counted once at its minimum arrival minute.
- **Diagonal contact:** Diagonal positions are never generated by the four offsets and do not spread rot.
- **Single cell:** A fresh-only cell returns `-1`, while an empty or already-rotten cell returns zero.
- **Input mutation:** If the original grid must be preserved outside this call, the caller must provide a copy.
