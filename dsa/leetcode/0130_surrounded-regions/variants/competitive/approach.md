## General

**Identify the cells that cannot be captured**

An `O` region is captured only when none of its cells touches the board’s edge. Equivalently, every `O` connected through up, down, left, or right moves to a border `O` must survive. The competitive solution exploits this equivalent condition and searches inward from all border `O` cells.

Safe cells are temporarily changed to `V`. That letter means “visited and connected to the border.” Since the input can contain only `X` and `O`, no original cell can be confused with this marker.

This viewpoint avoids a more complicated search from each interior cell. A search beginning inside a component would need to collect the component and remember whether it ever reaches the border. A search beginning on the border already knows that every discovered cell belongs to a non-surrounded component.

**Seed the queue without losing boundary cases**

The code creates a `deque` and scans the first and last column of every row. When either endpoint is `O`, it immediately changes that cell to `V` and appends its coordinates.

It then scans the first and last row for columns from `1` through `n - 2`. Excluding columns `0` and `n - 1` prevents the ordinary corners from being considered twice in this second loop. This is an optimization, not a correctness requirement, because a cell marked `V` would fail the later `O` check anyway.

Marking a cell at the moment it is enqueued is important. If the algorithm waited until removal, two neighboring safe cells could both enqueue the same unmarked neighbor. Early marking guarantees that each cell enters the queue at most once.

The boundary loops also behave correctly on narrow boards:

- if there is one column, the first and last column are the same, but the second test sees `V` after the first one marks an `O`;
- if there is one row, the top and bottom positions in the second loop are the same, with the same protection;
- if there are fewer than three columns, `range(1, n - 1)` is empty, which is correct because the column scan already covers every border cell.

**Propagate border reachability with breadth-first search**

While the queue is nonempty, the solution removes its oldest coordinate with `popleft`. It forms the four orthogonal neighbor coordinates and accepts a neighbor only if it is inside the matrix and currently contains `O`.

Every accepted neighbor is changed to `V` and appended. Thus the queue contains safe cells whose neighbors still need examination, while every `V` is known to have a path of original `O` cells back to a border seed.

The use of FIFO order makes this breadth-first search, but shortest distances are not needed here. FIFO simply offers an iterative way to exhaust the reachable set. A LIFO stack would discover cells in a different order and ultimately mark the same component, because reachability does not depend on traversal order.

Two facts establish the classification after the queue empties:

First, every `V` must be safe. Border seeds are safe by definition, and the search changes a neighbor to `V` only when it is an `O` adjacent to an already safe cell. Extending the known path by one edge therefore preserves connection to the border.

Second, every safe original `O` must be `V`. Take its path to a border. The border endpoint was seeded, and when the search processes each path cell it discovers the next one. Inductively, the search traverses the entire path and reaches the chosen cell.

These two directions show that `V` is neither too broad nor too narrow: it marks exactly the non-capturable `O` cells.

**Convert the classification into the requested board**

The last nested loops visit every coordinate. A `V` is restored to `O`. Every other value is assigned `X`.

Assigning `X` to every non-`V` cell is safe for both possible cases. An original `X` remains `X`; an original `O` that never became `V` is not connected to the border and must be captured. There are no other original symbols under the contract.

The function returns no value. Its result is the accumulated mutation of `board`, which matches the in-place interface.

## Complexity detail

Let $m$ and $n$ denote the row and column counts.

The border scans take $O(m+n)$ time. Because a cell is marked before enqueueing, each safe `O` is enqueued and removed at most once, and each removal checks exactly four neighbors. The concluding conversion visits all $mn$ cells. Total time is consequently $O(mn)$.

The selected manifest gives $O(mn)$ auxiliary space. In the worst-case bound, the queue can hold a number of coordinates proportional to the board area, so $O(mn)$ is safe. The source comment states $O(m+n)$, apparently treating the active breadth-first frontier as perimeter-sized; the manifest’s area bound is the conservative guarantee for arbitrary allowed `X`/`O` layouts. Apart from the queue, the algorithm uses constant scalar state and stores its visited classification inside the board.

The output mutation itself is not counted as auxiliary storage. Each queued item is a pair of integer coordinates.

## Alternatives and edge cases

- **Recursive border DFS:** It uses the same safe-cell classification and can be concise, but a connected region containing many cells may overflow Python’s recursion limit.
- **Iterative DFS:** A LIFO stack avoids recursion while preserving the same $O(mn)$ worst-case storage and reachability result.
- **Search every component:** Explore each `O` component, retain all its coordinates, and capture it if no member touches a border. This is correct but needs more bookkeeping and delays the decision until the component is complete.
- **Disjoint-set union:** Union adjacent `O` cells and connect border cells to a virtual safe node. It supports the same classification but requires an additional parent structure and more implementation detail.
- **Empty board:** The selected source explicitly returns when `board` is empty, even though the stated constraints require at least one row and column.
- **One cell:** `X` remains `X`; `O` is marked from the border and restored, so it cannot be captured.
- **One row or column:** Every `O` is on the edge. The early `V` assignment prevents duplicate queue entries when first and last boundaries coincide.
- **Enclosed holes and irregular regions:** Shape does not matter. Only four-direction reachability to a border determines whether a cell becomes `V`.
- **Diagonal chains:** Diagonal adjacency cannot transmit safety because the neighbor list contains only the four orthogonal coordinates.
- **Existing marker collision:** There can be no original `V` under the input contract. If that alphabet guarantee changed, overwriting all `V` cells at the end would no longer be safe.
- **Mark-on-enqueue invariant:** Moving `board[x][y] = 'V'` until after removal would allow duplicate queue entries and weaken the clean one-enqueue-per-cell bound.
