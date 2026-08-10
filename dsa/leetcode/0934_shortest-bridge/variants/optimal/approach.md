## General

**Separating identification from expansion**

The grid contains exactly two islands. A bridge is formed by changing water cells from `0` to `1` until the islands become connected, and the goal is to change as few cells as possible.

The optimal solution has two distinct phases:

1. Find and mark every cell of one island.
2. Expand outward from that entire island through water, one distance layer at a time, until the other island is reached.

The first phase uses depth-first search because it needs to collect one connected component. The second phase uses breadth-first search because breadth-first layers correspond exactly to the number of water cells that would be changed.

**Finding the first island**

The generator expression searches the grid in row-major order and returns the first coordinate whose value is nonzero. Since the original grid contains only `0` and `1` at this point, this is a land cell.

Calling `dfs(i, j)` from that coordinate visits every four-directionally connected land cell in the same island. The direction tuple is `(-1, 0, 1, 0, -1)`. Applying `pairwise` produces the four direction vectors `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)` without listing four separate pairs.

For each visited island cell, DFS performs two actions:

- it appends the coordinate to `q`;
- it changes the grid value from `1` to `2`.

Changing the value marks the cell as visited. The recursive search continues only into neighbors that are still `1`, so no island cell is processed twice.

DFS cannot accidentally absorb the second island. The two islands are separate four-directional components, so moving from the first island to the second requires crossing at least one water cell. DFS follows only cells whose value is `1` and never crosses `0`.

When DFS finishes, every cell of the chosen first island is marked `2` and stored in the queue. Every untouched `1` belongs to the second island.

**Why every first-island cell enters the BFS**

The shortest bridge might leave the first island from any boundary cell. Starting breadth-first search from just the originally discovered cell would also count travel inside the first island, even though moving across existing land requires no water conversion. One could explicitly find boundary cells, but that extra filtering is unnecessary.

Instead, the queue initially contains all cells of the first island as simultaneous sources at distance zero. This is multi-source breadth-first search. It behaves as though a wave starts from the entire island at once, ensuring that the first contact with the second island uses the best departure point automatically.

Interior island cells are harmless seeds. They cannot expand through other marked island cells because the BFS adds only water cells, and they do not make the answer too small. They merely perform constant neighbor checks.

**How a breadth-first layer represents bridge length**

The variable `ans` starts at `0`. At the beginning, the queue contains original first-island land, for which no water cell has been changed.

The loop records `len(q)` and processes exactly that many coordinates. Those coordinates form one breadth-first layer. When a processed coordinate sees a neighboring water cell, the code marks that water cell `2` immediately and appends it for the next layer.

Marking at enqueue time is essential. Two cells in the same layer may touch the same water cell. If marking were delayed until removal from the queue, the coordinate could be enqueued repeatedly, wasting work and complicating the layer interpretation.

After the whole current layer is processed, `ans` is incremented. Therefore:

- while processing the original island, `ans = 0`;
- while processing water cells one step away, `ans = 1`;
- while processing water cells two steps away, `ans = 2`;
- and so forth.

When a processed coordinate has a neighbor whose value is still `1`, that neighbor belongs to the second island. The method returns the current `ans`. It does not add one for the second-island cell because that cell is already land and does not need to be changed.

For example, if one water cell lies directly between the islands, processing the initial island enqueues that water while `ans` is zero. The layer completes and `ans` becomes one. Processing the water cell then sees the second island and returns one, exactly matching the single required conversion.

**Why the first contact is globally shortest**

Breadth-first search processes cells in nondecreasing number of water steps from the first island. Every water cell added in layer one can be reached by changing one water cell; every water cell in layer two requires two; and so on.

Suppose the search first reaches the second island while `ans = d`. Then it has constructed a connection using `d` water cells. If a bridge using fewer than `d` cells existed, its water cells would form a route from some first-island cell to the second island through an earlier BFS layer. Because every first-island cell was a source, the search would have encountered that route and reached the second island before layer `d`. This contradicts the fact that the first contact occurred at `d`. The returned value is therefore minimal.

**Using the grid as the visited set**

The value `2` has a unified meaning: it is part of the region already claimed by the search. During DFS, that region is the first island. During BFS, it grows to include water cells already enqueued. Reusing the grid avoids a separate visited matrix.

The second island remains `1` so the BFS can recognize its first contact. The method intentionally mutates the input grid; callers should not expect its original zeros and ones to remain afterward.

## Complexity detail

Let `n` be the side length of the square grid.

The initial scan examines at most `n^2` cells before finding land. DFS visits each cell of the first island once. BFS marks and processes each reachable water cell at most once and stops no later than reaching the second island. Neighbor work is constant because each cell has four directions. The total time complexity is `O(n^2)`.

The queue can hold `O(n^2)` coordinates in the worst case, especially because all first-island cells are initially added and a broad BFS frontier may also be large. Recursive DFS can have depth `O(n^2)` for a long, winding island. Thus auxiliary space is `O(n^2)`.

Mutating the grid avoids an additional `O(n^2)` visited matrix, but it does not eliminate the queue or recursion stack. In Python, a worst-case deeply recursive island may also exceed the interpreter's recursion limit even though the asymptotic bound is valid.

## Alternatives and edge cases

- **Run BFS from only one first-island cell:** This can overcount movement through existing land and miss the best shoreline. Multi-source BFS correctly assigns zero distance to the entire first island.
- **Start BFS from boundary cells only:** This is also correct and may reduce the initial queue, but it requires an additional boundary test. Enqueuing every island cell is simpler and retains the same `O(n^2)` bound.
- **Compute all pairs of island cells:** Measuring distances between every cell of one island and every cell of the other can become quadratic in the number of land cells, which is up to `O(n^4)` overall. BFS explores the grid once.
- **Depth-first search for both phases:** DFS is suitable for identifying a component, but ordinary DFS does not visit positions by shortest distance. Using it for expansion would require extra distance bookkeeping or exhaustive search.
- **Bidirectional breadth-first search:** Expanding from both islands can reduce practical search depth, but one side must still be identified and the meeting-distance accounting becomes more involved. The one-sided multi-source BFS already satisfies the optimal asymptotic bound.
- **Iterative island marking:** Replacing recursive DFS with an explicit stack preserves the algorithm and `O(n^2)` bounds while avoiding Python recursion-limit failures on large or snake-shaped islands.
- **One water cell between islands:** The first water layer sees the second island and returns `1`. The algorithm counts converted water cells, not graph edges between land cells.
- **Grid edges and corners:** Every neighbor is checked against `0 <= x < n` and `0 <= y < n` before access, so cells on the border need no special branch.
- **Repeated discovery of the same water:** Setting a water cell to `2` before enqueueing it ensures that later neighbors do not add it again.
- **Input mutation:** The marking strategy destroys the original binary grid. If preservation were required, the algorithm would need a separate visited set or a copied grid, increasing memory use.
- **Exactly two islands:** The recognition that every untouched `1` belongs to the target relies on this contract. With more islands, the first contact would find the nearest other island, which would be a different problem.
- **Direction semantics:** Only vertical and horizontal neighbors count. Diagonal contact does not join islands and is correctly ignored by the four generated direction pairs.
