## General

**View each cell as the end of a shortest path**

Movement is only rightward or downward. Therefore, every predecessor of cell $(i,j)$ is either:

- an earlier column in the same row, or
- an earlier row in the same column.

If cells are processed from top to bottom and left to right, every possible predecessor has already been processed. This turns the problem into forward dynamic programming:

$$
\texttt{dist[i][j]}
=
1+\min(\text{distance of a predecessor that can reach }(i,j)).
$$

The start cell counts as visited, so `dist[0][0] = 1`. Unreachable cells remain `-1`.

The difficulty is finding the cheapest still-capable predecessor quickly. Scanning every earlier cell would be quadratic. The solution maintains one min-heap for every row and one for every column.

**What a row heap represents**

`row[i]` stores entries `(distance, column)` for reachable cells already processed in row $i$. A stored predecessor at column $c$ can reach current column $j$ precisely when

$$
c+\texttt{grid[i][c]}\ge j.
$$

The heap is ordered first by distance, so after expired top entries are removed, its top is the reachable predecessor that produces the fewest visited cells.

Before using `row[i]` at $(i,j)$, the code repeatedly checks its top entry. If

`grid[i][column] + column < j`,

that predecessor's farthest reachable column is already left of $j$. Since future columns are even farther right, the entry can never be useful again and is permanently popped.

If the remaining heap is nonempty, its top gives candidate distance `row[i][0][0] + 1`.

**Why removing only expired heap tops is sufficient**

An expired entry may temporarily remain below the top because the heap is ordered by path distance rather than reach endpoint. That is safe.

- If the top is valid, it has the smallest distance among all stored entries, including any hidden expired entries with larger distance. The hidden entries cannot improve the current result.
- If a hidden expired entry later rises to the top after cheaper entries leave, the while-loop removes it before use.

Thus every heap value actually consulted is both minimum-distance and currently capable of reaching the cell.

**The column heaps are symmetric**

`col[j]` stores entries `(distance, row)` for reachable cells earlier in column $j$. A predecessor at row $r$ remains active while

$$
r+\texttt{grid[r][j]}\ge i.
$$

The same expiration loop removes top entries whose downward reach ends before current row $i$. A valid top supplies another candidate distance.

The solution compares both row and column candidates because a shortest path may enter the current cell from either direction. The conditional update handles `-1` as “no candidate yet” and otherwise retains the smaller value.

**Push a cell only after both directions are considered**

Once row and column heaps have offered their best predecessors, a reachable cell is pushed into:

- its own row heap as `(dist[i][j], j)`;
- its own column heap as `(dist[i][j], i)`.

This cell can then serve as a predecessor for cells to its right and below.

Pushing occurs only once, after the final minimum for the cell is known. No later cell can improve it because all legal edges move forward: future positions cannot move left or upward into $(i,j)$.

The start cell is a special case only through initialization. When the loop reaches $(0,0)$, both heaps are empty, its preset distance one remains, and it is pushed normally.

**Why the dynamic program is correct**

Process cells in row-major order and assume all earlier processed cells have correct minimum visit counts.

Every legal path into $(i,j)$ ends at a reachable earlier cell in row $i$ or column $j$. The corresponding heap contains that predecessor unless it expired, and expiration is equivalent to being unable to reach $(i,j)$. Among active row predecessors, the row heap exposes the smallest correct distance; the column heap does the same for column predecessors.

Adding one counts the current cell. Taking the smaller of these two candidates therefore considers the final step of every possible path and chooses the shortest.

Conversely, each heap candidate corresponds to a genuine allowed jump because its reach inequality was verified. So every finite distance assigned by the code describes an actual path.

By induction, `dist[i][j]` is correct for every cell. The bottom-right entry is consequently the requested answer, and it stays `-1` exactly when no path reaches it.

**Trace the information flow**

Suppose a reachable cell at $(i,c)$ has distance three and `grid[i][c] = 4`. Its row-heap entry can help columns $c+1$ through $c+4$. At each such column, it competes by distance with other row predecessors and all active column predecessors.

At column $c+5$, its reach endpoint $c+4$ is too small, so it is removed if it reaches the heap top. It is never needed again in that row.

This “insert once, remove once” lifecycle is what makes the heap strategy efficient even though a large jump may cover many future cells.

**Why the answer counts cells rather than moves**

A path using $q$ moves visits $q+1$ cells because it includes the starting cell. Initializing the source to one and adding one for every transition directly stores the required cell count.

If the grid has one cell, the start is already the destination. The loop preserves `dist[0][0] = 1` and returns one, which is the minimum number of visited cells.

## Complexity detail

Let $N=mn$ be the number of cells. Every reachable cell is pushed once into a row heap and once into a column heap. Each entry is popped at most once from each heap. A heap operation costs at most $O(\log N)$, so total time is

$$
O(N\log N)=O(mn\log(mn)).
$$

The distance matrix uses $O(N)$ space. Across all row heaps, at most $N$ entries exist, and the same is true across all column heaps. Total auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Balanced successor sets with BFS:** Enumerate each still-unvisited reachable cell once, but row and column bookkeeping is more involved.
- **Segment trees:** Range minima can support the same recurrence, usually with $O(N\log N)$ time and heavier implementation.
- **Scan every jump destination:** A cell may reach $O(N)$ later cells, leading to quadratic work.
- **Single-cell grid:** The start is the destination, so the answer is one.
- **Zero-valued nonterminal cell:** It cannot generate future moves but may still be reached and counted.
- **Unreachable predecessor:** It is never pushed into either heap.
- **Expired hidden heap entry:** It is harmless until it becomes the top, when the pruning loop removes it.
- **Two possible directions:** Both heaps must be queried before the cell is pushed.
- **Destination unreachable:** Its initialized `-1` is returned unchanged.
- **Input preservation:** The grid is only read; distances and heaps are stored separately.
