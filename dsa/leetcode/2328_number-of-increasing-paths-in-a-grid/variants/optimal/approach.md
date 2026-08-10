## General

**Count paths by their first cell**

The memoized function `dfs(i, j)` counts all strictly increasing paths that start at cell `(i, j)`. Such a path has two possible forms:

- it stops immediately, using only the starting cell;
- it moves first to one of the four adjacent cells with a strictly larger value, then follows any increasing path starting there.

This gives a direct recurrence. Start `ans` at one for the single-cell path, and for every larger neighbor add that neighbor's `dfs` count.

The outer expression calls `dfs` for every cell and sums the results. Every increasing path has exactly one starting coordinate, so it belongs to exactly one of those counts.

**Generate the four directions from one compact sequence**

`pairwise((-1, 0, 1, 0, -1))` produces the consecutive pairs

`(-1,0), (0,1), (1,0), (0,-1)`.

They represent up, right, down, and left. For each direction `(a, b)`, the candidate neighbor is `(i + a, j + b)`.

The bounds checks ensure the candidate stays inside the `m x n` matrix. The final comparison

`grid[i][j] < grid[x][y]`

permits movement only to a strictly larger value. Equal neighbors are deliberately excluded because the path must be strictly, not merely non-decreasingly, increasing.

**Strict increase turns the grid into a directed acyclic graph**

Imagine a directed edge from each cell to every larger adjacent cell. Along an edge, the grid value strictly rises. Following a directed cycle would require returning to the starting cell with a value greater than itself, which is impossible. The implicit graph is therefore a directed acyclic graph.

`dfs(i, j)` counts paths beginning at one vertex of this DAG. Its recursive calls always move forward to a larger value, so recursion must eventually reach a cell with no larger neighbor. At that sink, the count is one: the path containing the sink alone.

The acyclic property is also why no separate “currently visiting” marker is needed. There can be no recursive cycle.

**Memoization prevents repeated suffix counting**

Many starting cells may reach the same larger cell. Without caching, the collection of paths beginning at that larger cell would be recomputed for every predecessor, causing an exponential recursion tree.

The `@cache` decorator stores the returned count for each coordinate pair. The first call to `dfs(i, j)` explores its larger neighbors. Every later call with the same coordinates returns the stored result immediately.

This is valid because the grid never changes and the result depends only on `i` and `j`. At most one full computation occurs per cell.

**Why adding neighbor counts is exact**

Fix starting cell `u`. The single-cell path is one valid choice. Every longer increasing path from `u` has a unique second cell `v`, which must be one of its larger four-neighbors. After that first step, the remaining sequence is exactly an increasing path counted by `dfs(v)`.

Paths grouped under different second cells cannot be the same because their second coordinates differ. Therefore the groups are disjoint and their counts should be added. Conversely, prefixing `u` to any path counted by a larger neighbor produces a valid increasing path from `u`.

This one-to-one decomposition proves the recurrence. Summing over all starts is also disjoint because two paths with different first cells have different visited-cell sequences and are considered distinct.

**Reduce counts while computing**

After each neighbor contribution, the code applies modulo `10^9 + 7`. Modular addition preserves the final requested remainder and keeps every cached count bounded. The final sum across starting cells is reduced once more.

The single-cell contribution starts at one and is never lost. Even a grid in which all values are equal has exactly one path per cell and no recursive neighbor contributions.

**The exact source uses recursive memoization**

The variant summary describes Kahn topological propagation, but the provided Optimal solution is a recursive memoized DAG count. Both exploit the same increasing-edge acyclicity and have the same asymptotic bounds, but their execution details differ.

A strictly increasing path may contain up to `mn` cells. On a grid arranged as one long increasing snake, recursive depth can therefore be linear in the cell count and can exceed Python's default recursion limit. An iterative value order or explicit topological traversal avoids that runtime limitation.

## Complexity detail

Let `N = mn` be the number of cells. Memoization fully evaluates each cell once, and each evaluation checks exactly four directions. Cache hits are constant-time expected dictionary operations. Total running time is `O(N) = O(mn)`.

The cache stores one result for each cell, so it uses `O(mn)` space. The recursion stack can also reach `O(mn)` depth in the worst case, while typical grids may have much shorter increasing paths. Together, auxiliary space remains `O(mn)`.

The outer generator and direction tuple use only constant additional storage. Cached values stay below the modulus. The input grid is read and never modified.

## Alternatives and edge cases

- **Kahn topological propagation:** Compute indegrees in the increasing-edge DAG, start from local minima, and propagate path counts toward larger cells. This is iterative `O(mn)` time and space and avoids recursion depth.
- **Sort all cells by value:** Process from largest to smallest for starting-path counts or smallest to largest for ending-path counts. This is straightforward but costs `O(mn \log(mn))` time.
- **DFS toward smaller neighbors:** Define the state as paths ending at the current cell instead. This is equally valid if the outer sum and comparison direction remain consistent.
- **Plain DFS without cache:** Overlapping suffix subproblems would be recomputed many times and can cause exponential work.
- **Allow equal-valued moves:** That violates strict increase and can also introduce directed cycles between equal neighbors, invalidating the simple recursion.
- **One cell:** `dfs` returns its single-cell path, and the total is one.
- **All values equal:** No edge passes the strict comparison, so the answer is the number of cells.
- **Several cells with the same value:** They are distinct possible single-cell paths but cannot move directly between equal values.
- **Multiple paths with identical value sequences:** They are still different when their coordinate sequences differ, and separate neighbor branches count them separately.
- **Local maximum:** It has no larger neighbor, so its only starting path is itself.
- **Local minimum:** It may begin many paths through different larger neighbors; their disjoint second steps make addition correct.
- **Very long increasing path:** The mathematical count is correct, but recursive depth can exceed the Python interpreter limit.
- **Modulo during recursion:** Reducing each addition preserves the final answer and prevents exponential-size cached integers.
- **Availability of helpers:** The exact source relies on `cache` and `pairwise` being provided by the Python environment, conventionally from `functools` and `itertools`.
- **Input preservation:** No cell is marked or reordered; all traversal state lives in the function cache.
