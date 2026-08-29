## General

**Why trying a flood fill separately for every zero is too slow**

Changing one water cell to land can connect as many as four neighboring islands. A direct idea is to flip each zero temporarily and run a complete flood fill to measure the resulting island. An `n \times n` grid contains `O(n^2)` candidate zeroes, and one flood fill can inspect `O(n^2)` cells, leading to `O(n^4)` work.

The optimal solution separates the work into two passes:

1. discover every existing island once, give it an identifier, and record its size;
2. for each zero, add the sizes of the distinct islands touching it, plus one for the flipped cell.

Once island sizes are known, evaluating one zero needs only its four neighbors.

**Keep labels separate from the input grid**

The matrix `p` has the same dimensions as `grid` and begins filled with zeroes. For a land cell:

- `p[i][j] == 0` means the cell has not been assigned to an island yet;
- a positive value means the cell belongs to the island with that identifier.

The solution does not overwrite `grid`. It uses `p` as a parallel label matrix, which keeps the original distinction between water and land available during the second pass.

The `Counter` named `cnt` maps each positive island identifier to its number of cells. Identifier zero is reserved for “no island.” Because a `Counter` returns zero for a missing key, `cnt[0]` is harmless when a water neighbor's label is later encountered.

**The four directions encoded compactly**

`dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce:

- `(-1, 0)` for up;
- `(0, 1)` for right;
- `(1, 0)` for down;
- `(0, -1)` for left.

These are exactly the four directions allowed by the island definition. Diagonal cells are deliberately excluded.

**Label one complete island with DFS**

The outer scan visits every grid position. When it finds land `x == 1` whose label is still zero, it has found a new island. It increments `root` to obtain a fresh positive identifier and calls `dfs(i, j)`.

Inside DFS:

1. assign `p[i][j] = root`;
2. increase `cnt[root]` by one;
3. inspect each of the four neighbors;
4. recurse only when the neighbor is inside the grid, is land in `grid`, and is still unlabeled in `p`.

Marking the cell before recursing is essential. If two adjacent cells could call each other while both remained unlabeled, recursion would cycle. The early label makes each land cell enter DFS exactly once.

All cells reached by this DFS are four-directionally connected to the starting cell, so they belong to the same island. Conversely, DFS follows every valid land edge, so it reaches the entire island. When it returns, `cnt[root]` is exactly that island's area.

**Preserve the answer when no flip helps or no zero exists**

After labeling, the solution initializes

`ans = max(cnt.values() or [0])`.

If at least one island exists, this is the largest original island. That matters because the operation is allowed at most once; the result may retain an existing island even if a particular flip elsewhere creates something smaller.

If the grid contains no land, `cnt.values()` is empty. The fallback list `[0]` makes the initial answer zero without calling `max` on an empty sequence.

If the grid is already all land, the second pass finds no zero, and `ans` remains `n^2`, the correct answer.

**Evaluate one possible flip**

For each water cell `grid[i][j] == 0`, a fresh set `s` collects the labels of its in-bounds neighbors. The possible new island contains:

- the flipped cell itself, contributing one;
- every cell in each distinct adjacent island.

Its size is therefore

`1 + sum(cnt[root] for root in s)`.

The set is crucial. The same island can touch the candidate zero from two or more directions. For example, land may wrap around the zero from above and left while still belonging to one connected component elsewhere. Adding its size twice would count the same cells twice. A set retains its label only once.

Water neighbors contribute label zero. Adding zero to `s` is safe because `cnt[0]` is zero. The implementation consequently needs no separate “neighbor must be land” branch in the second pass.

The candidate updates `ans` through `max`. After every zero has been considered, `ans` is the best original or one-flip island size.

**Trace the diagonal example**

For

`[[1,0],[0,1]]`,

the labeling pass creates two islands of size one. Flipping the top-right zero touches both island identifiers. Its candidate size is

$$
1+1+1=3.
$$

The same holds for the bottom-left zero, so the answer is 3. The diagonal land cells were not initially connected, but the newly flipped cell creates two four-directional edges that merge them.

**Why the two-pass result is correct**

Any valid final result either uses no change or flips exactly one zero. The no-change possibility is covered by the initial largest island.

Fix a flipped zero. Any land cell newly connected through it must belong to one of its four neighboring original islands; no other island can gain a path to the flipped cell without first passing through such a neighbor. All distinct neighboring islands do become connected through the new land cell. Thus, one plus the sum of their distinct precomputed sizes is exactly the resulting component size.

The second pass evaluates this exact quantity for every possible zero, so its maximum includes the optimal operation. Every evaluated candidate describes a real permitted flip, so it cannot exceed what is achievable. The returned maximum is therefore exact.

## Complexity detail

The grid contains `n^2` cells. The labeling scan visits every position, and DFS labels every land cell once. Each labeled cell checks four neighbors, so the first phase takes `O(n^2)` time.

The second scan again visits every cell. Each zero checks four neighbors, builds a set of at most four labels, and sums at most four counter entries. This is constant work per cell and another `O(n^2)` time. Total time is `O(n^2)`.

The label matrix `p` uses `O(n^2)` space. The counter can contain up to `O(n^2)` islands in a checkerboard grid. Recursive DFS can have an `O(n^2)` call stack for a path-shaped or fully connected island. The temporary neighbor set has at most four elements. Total auxiliary space is `O(n^2)`.

In Python, a very deep recursive island can approach the interpreter's recursion limit. An iterative stack implements the same labeling logic and preserves the complexity while avoiding that runtime limit; the exact protected source uses recursion.

## Alternatives and edge cases

- **Flood fill after every possible flip:** It repeats almost the same island discovery for each zero and can require `O(n^4)` time.

- **Disjoint set union:** Union adjacent land cells, store component sizes at roots, and combine distinct neighboring roots for each zero. It has the same near-linear-in-cells behavior but requires parent and size machinery.

- **Overwrite `grid` with island identifiers:** This can save the separate label matrix, provided identifiers do not conflict with 0 and 1. The exact solution preserves the input and stores labels in `p`.

- **All zeroes:** No initial island exists. Any one flip creates an island of size one, and the second pass raises `ans` from 0 to 1.

- **All ones:** There is no zero to flip, so the initial size `n^2` is returned.

- **One-cell grid containing zero:** Its empty neighbor set contributes zero, and adding the flipped cell returns 1.

- **One-cell grid containing one:** The labeling pass records size 1, and no second-pass candidate is needed.

- **One island touches a zero multiple times:** Its identifier appears once in the set, preventing double counting.

- **Four distinct neighboring islands:** Flipping the center joins all four, and the set contains four positive identifiers.

- **Water neighbor:** Its label is zero and contributes `cnt[0] = 0`.

- **Diagonal land:** It is not a direct neighbor and is not merged unless a four-directional path exists.

- **At most one flip:** Initializing from existing island sizes correctly permits choosing no flip when the grid is already all land.

- **Input immutability:** Labels live in `p`, so `grid` is read but never modified.
