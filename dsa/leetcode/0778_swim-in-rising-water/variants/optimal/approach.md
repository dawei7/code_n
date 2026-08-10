## General

**View rising water as cells becoming active**

At time `t`, every cell whose elevation is at most `t` can be entered. The question is therefore: what is the earliest time when the active top-left cell and active bottom-right cell belong to the same four-directionally connected region?

The algorithm processes time in increasing order and maintains those connected regions with a disjoint-set union structure, also called union-find. Instead of finding a path from scratch at every possible time, it incrementally adds the one cell that becomes available and joins it to already available neighbors.

**Why there is exactly one newly active cell per time**

There are $n^2$ cells. Every elevation is unique, nonnegative, and smaller than $n^2$. Consequently the $n^2$ elevations are exactly the integers from zero through $n^2 - 1$ in some order.

The list `hi` reverses the grid lookup: `hi[h]` stores the flattened position of the cell whose elevation is `h`. While reading cell `(i, j)`, its flat index is `i * n + j`, so the assignment is `hi[grid[i][j]] = i * n + j`.

Now iteration `t` can locate the newly submerged cell in constant time with `hi[t]`. There is no need to sort cells, because the elevation values already form the complete required integer range.

**Represent connected regions with parent links**

The parent array `p` initially gives every flat cell index its own singleton set. Function `find(x)` follows parent links until it reaches the representative of `x`'s current connected component.

While returning from recursion, `find` assigns every visited node directly to that representative. This path compression makes later component queries faster while preserving which cells are connected.

To merge two regions, the code assigns the representative of the current cell to the representative of its neighbor:

`p[find(current)] = find(neighbor)`.

The particular representative chosen as the new parent does not affect connectivity. After the assignment, `find` returns the same representative for every member of both former sets.

**Activate and connect the cell at time `t`**

The flat position `hi[t]` is converted back to coordinates with `divmod(hi[t], n)`. The fixed direction sequence generates the four offsets up, right, down, and left through consecutive pairs.

For each in-bounds neighbor, the algorithm checks `grid[nx][ny] <= t`. Such a neighbor has already become active. Therefore an active edge exists between the current cell and that neighbor, and their sets are united.

A neighbor above water must not be united yet. Connectivity at time `t` may use only cells whose individual elevations are at most `t`.

**The union-find invariant**

After finishing all unions for time `t`, two active cells have the same representative if and only if a four-directional path of cells with elevation at most `t` connects them.

The invariant begins correctly at `t = 0`: only the elevation-zero cell is active, so its component is a singleton. For the inductive step, time `t` adds exactly one cell. Any new active path that did not exist at time `t - 1` must pass through that new cell and enter or leave through an active neighbor. Merging with every such neighbor creates precisely those new connections. No union with an inactive neighbor is performed, so no invalid path is invented.

**Detect the first feasible time**

After adding the time-`t` cell and all of its active edges, the code compares `find(0)` with `find(n * n - 1)`. Flat index zero is the top-left cell, and flat index $n^2 - 1$ is the bottom-right cell.

If the representatives match, the invariant proves that a legal route exists at time `t`. Because times were tested in increasing order, every smaller time was checked before the current activation and failed. Thus this first successful `t` is the minimum possible answer.

**Trace the two-by-two example**

For `grid = [[0,2],[1,3]]`, elevation zero activates the start. At time one, cell `(1,0)` activates and joins the start. At time two, cell `(0,1)` activates and also joins the start region.

The destination `(1,1)` has elevation three and is still inactive, so it cannot be reached earlier. At time three it activates, joins its active neighbors, and the endpoint representatives become equal. The method returns three.

**Why arbitrary swimming distance costs no extra time**

The statement allows swimming any distance instantaneously once the water is high enough. Therefore the number of grid steps on a path is irrelevant. Only the largest elevation along that path matters. Union-find captures exactly whether some fully active path exists; it does not incorrectly add a cost per edge.

The final `return 0` is a defensive fallback. Once all $n^2$ cells are active, the rectangular grid is connected, so normal valid input must already have returned from inside the loop. For `n = 1`, the only elevation is zero and the connectivity check returns zero during the first iteration.

## Complexity detail

Let $V = n^2$ be the number of cells. Building `hi` and `p` takes $O(V)$ time. Each cell examines at most four neighbors, so the algorithm performs $O(V)$ union/find operations.

This implementation uses path compression but does not maintain union-by-rank or union-by-size. A safe bound matching the package requirement is $O(V \log V)$ total time, which becomes $O(n^2 \log n)$ because $\log(n^2) = 2\log n$. With both path compression and ranked union, the conventional tighter amortized description would be $O(V\alpha(V))$.

Arrays `p` and `hi` each contain $V$ integers. The recursion used by `find` follows parent links, and path compression shortens those paths over time. Total auxiliary storage is $O(V) = O(n^2)$.

## Alternatives and edge cases

- **Minimum-bottleneck Dijkstra:** Use a min-heap where a cell's path cost is the maximum elevation seen so far. It also solves the problem in $O(n^2 \log n)$ time and is especially natural when elevations are not a complete integer range.

- **Binary search plus flood fill:** Test whether the endpoints connect below a chosen water level. This repeats a grid traversal for several levels and costs $O(n^2 \log(n^2))$.

- **Sort activation events:** Necessary if elevations are arbitrary distinct values; here `hi` replaces sorting because the constraints make elevations a permutation of `0..n^2-1`.

- **Ordinary shortest path by step count:** Incorrect objective; a longer route with lower maximum elevation may be available earlier than a short high-elevation route.

- **Single-cell grid:** Start and destination are already the same cell, and its forced elevation zero is returned.

- **Inactive neighbor:** It must not be joined merely because it is adjacent; its elevation must first be at most the current time.

- **Multiple active neighbors:** All are merged, because the new cell may connect several formerly separate regions at once.

- **Unique elevations:** The direct `hi[h]` indexing relies on uniqueness and the complete bounded range stated by the contract.
