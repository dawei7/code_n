## General

**View the matrix as a directed acyclic graph.**

Treat every cell as a vertex. From cell $(i,j)$, draw a directed edge to each orthogonally adjacent cell $(x,y)$ whose value is strictly larger:

$$
\text{matrix}[x][y] > \text{matrix}[i][j].
$$

Then every allowed increasing path in the matrix is exactly a directed path in this implicit graph. “Implicit” means the source never constructs adjacency lists; it checks the four neighboring coordinates whenever it evaluates a cell.

This directed graph cannot contain a cycle. Along every edge, the value strictly increases. Returning to a previously visited cell would require ending with the same value with which the cycle began, contradicting a chain of strict increases. This acyclic property is why a recursive longest-path recurrence is safe without a per-call visited set.

**Define the recursive state.**

The cached helper has the meaning

$$
\operatorname{dfs}(i,j)
=\text{length of the longest increasing path that starts at }(i,j).
$$

The path counts cells, not moves. A path containing only its starting cell has length one.

From $(i,j)$, the first move may go to any larger orthogonal neighbor $(x,y)$. Once that move is chosen, the best possible continuation is `dfs(x, y)`. Therefore the recurrence is

$$
\operatorname{dfs}(i,j)
=1+\max_{(x,y)}\operatorname{dfs}(x,y),
$$

where the maximum ranges only over in-bounds, orthogonally adjacent cells with a strictly larger value. If there is no such neighbor, the maximum over continuations is treated as zero, so the state returns one.

The source realizes this by starting `ans = 0`, maximizing it with each eligible neighbor's result, and returning `ans + 1`. The added one accounts for the current cell.

**Generate exactly four directions.**

The expression `pairwise((-1, 0, 1, 0, -1))` produces these consecutive pairs:

$$
(-1,0),\ (0,1),\ (1,0),\ (0,-1).
$$

They mean up, right, down, and left. There are no diagonal pairs. Repeating `-1` at the end closes the direction pattern so the final pair is `(0,-1)`.

For each direction `(a, b)`, the candidate neighbor is `(i + a, j + b)`. The compound condition verifies both row and column bounds before indexing the matrix. It then requires the neighbor value to be greater. Equality is rejected because the path must be strictly increasing, not merely non-decreasing.

**Why memoization changes the running time completely.**

Many starting cells can eventually reach the same larger cell. Without caching, the recursion would recompute the complete best path from that cell every time, creating an exponential number of repeated calls on some grids.

The `@cache` decorator stores the returned value for each coordinate pair `(i, j)`. The first call computes the state. Every later call with the same coordinates returns the stored integer directly. Because the matrix never changes, the answer for a coordinate is stable and is a valid memoization key.

There are only $mn$ possible coordinate states. Each genuinely computed state checks four directions once, so the overlap among possible paths no longer causes repeated exploration.

**Why every cell must be considered as a start.**

The recurrence answers the longest path from one specified cell, but the problem allows the path to begin anywhere. The final expression evaluates `dfs(i, j)` for every row and column and returns their maximum.

Memoization makes this exhaustive start scan efficient. If an earlier start already caused a cell's state to be calculated, its outer call becomes a constant-time cache lookup. A single arbitrarily chosen start would be insufficient because it might not reach the globally best path: directed movement only goes toward larger values, so different low regions can lead to different chains.

**Walk through the first matrix.**

For

$$
\begin{bmatrix}
9&9&4\\
6&6&8\\
2&1&1
\end{bmatrix},
$$

consider the cell containing `1` at row two, column one. It can move left to `2`. From `2`, the path can move up to `6`; from that `6`, it can move up to `9`. A `9` has no larger neighbor, so its state is `1`. The `6` state is `2`, the `2` state is `3`, and the starting `1` state is `4`. Thus the path `[1,2,6,9]` has length four.

Other branches are still checked. A neighbor with a larger immediate value is not automatically the best choice; its continuation may be short. Taking the maximum of complete cached neighbor paths handles this correctly.

**Why the recurrence is correct.**

First consider a local maximum, a cell with no larger neighbor. No legal move can leave it, so its longest path is the cell itself, length one. This matches the base behavior.

For any other cell, every legal increasing path must choose one of its larger neighbors as the second cell. Once that neighbor is fixed, the best continuation length is exactly the cached recursive state for that neighbor. The algorithm tries every legal first move and selects the greatest continuation, then adds the current cell. It therefore cannot return less than the optimum or construct anything longer than a valid path.

This reasoning is well founded because dependencies always point to strictly larger values. One can imagine proving the states in descending value order: local maxima are known first, and each smaller cell depends only on already valid larger-cell states. Memoized DFS discovers that dependency order automatically.

Finally, every increasing path has some starting cell. Taking the maximum correct state over all starts therefore returns the global longest length.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. There are $mn$ cacheable states. Each state is computed once and checks exactly four candidate directions, so total time is $O(mn)$. Cache hits from other branches or the final outer scan take constant time.

The cache may store one result for every cell, using $O(mn)$ space. The recursion stack can also reach $O(mn)$ depth in a matrix whose cells form one long increasing path, so total auxiliary space remains $O(mn)$.

The manifest's time and space bounds match the source, but its summary describes topological layer peeling from local maxima. The checked-in optimal code uses memoized depth-first search instead. Both exploit the same increasing DAG, but this explanation follows the exact recursive implementation.

## Alternatives and edge cases

- **Topological layer peeling:** Compute each cell's number of outgoing edges to larger neighbors, enqueue local maxima, and remove the graph layer by layer. The number of layers equals the longest increasing path. This also runs in $O(mn)$ time and space, avoids recursion, and matches the manifest summary, but it is not the exact source.

- **Naive DFS from every cell:** The recurrence is correct without caching, but shared suffix paths are recalculated many times and can cause exponential work. Memoization is the essential optimization.

- **Sort cells by value:** Process coordinates in descending value order and fill a DP table from larger neighbors. This makes the dependency order explicit but adds an $O(mn\log(mn))$ sorting cost.

- **Equal adjacent values:** They do not form an edge because the comparison is strict `>`. Allowing equality could create cycles among equal-valued neighbors and would solve a different non-decreasing-path problem.

- **One cell:** It has no in-bounds neighbor, so `ans` stays zero, `dfs` returns one, and the outer maximum returns one.

- **All cells equal:** Every state is a local maximum under strict movement. Each returns one, so the answer is one.

- **Matrix boundaries:** Bounds are checked before `matrix[x][y]` is read, preventing wrap-around through Python's negative indices and preventing access beyond the last row or column.

- **No empty-matrix branch:** The constraints guarantee at least one row and one column. The source therefore safely reads `len(matrix[0])`; an empty input outside the contract would require an explicit guard.

- **Recursion depth:** A valid path can contain up to $mn$, or `40000`, cells. Python's default recursion limit is much smaller, so a specially shaped long path can present an implementation-level recursion risk. Topological peeling or an explicit iterative formulation removes that risk while preserving the same graph reasoning.
