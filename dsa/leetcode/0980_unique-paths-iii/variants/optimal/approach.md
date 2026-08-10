## General

**Turn the grid into a search over complete walks**

A walk is valid only when it satisfies all three requirements at once: it begins at the unique square containing `1`, ends at the unique square containing `2`, and visits every square other than an obstacle exactly once. Merely reaching the ending square is therefore not enough. The algorithm must remember which squares the current walk has used and how many steps it took before reaching the end.

Depth-first search with backtracking fits this requirement because every choice of the next square creates a separate possible continuation. The search follows one continuation as far as it can, counts it if it becomes a complete valid walk, and then reverses its last choice so that another continuation can reuse the square. This systematically explores possible walks without allowing one attempted walk to contaminate another.

**Read the fixed information before searching**

The dimensions are stored as `m` and `n`. A generator expression scans the grid to find the coordinates of the starting square:

`start = next((i, j) ... if grid[i][j] == 1)`.

The statement guarantees exactly one start, so `next` will find one coordinate and no fallback is necessary. The code also computes

`cnt = sum(row.count(0) for row in grid)`,

which is the number of ordinary empty squares. Notice that `cnt` deliberately excludes the start and end. That detail explains the less obvious condition used when the search reaches the ending square.

The visited set initially contains only `start`. Therefore, the search can never step back onto the starting square, and every coordinate subsequently added to the set represents a square already used by the current walk.

**Understand exactly what the step counter means**

The recursive call `dfs(i, j, k)` means that the walk is currently at `(i, j)` and has made exactly `k` moves from the starting square. The first call is `dfs(*start, 0)`, so the start itself corresponds to zero moves.

Suppose there are `cnt` empty squares. A complete walk visits, in order, the start, all `cnt` empty squares, and the end. That is `cnt + 2` visited squares. A walk through that many squares contains one fewer moves, so it reaches the end after exactly `cnt + 1` moves. Consequently,

`return int(k == cnt + 1)`

returns `1` precisely when every empty square has been included, and `0` when the end was reached too early. Converting the Boolean comparison to an integer makes the base case directly contribute either one valid walk or no valid walk to the total.

The function returns immediately whenever it sees the end. It must not treat the ending square as an ordinary intermediate square and walk away from it: the required walk ends there. If it arrived too early, that branch is invalid and cannot be repaired by leaving the end and returning later.

**Generate the four neighboring coordinates**

The compact tuple

`dirs = (-1, 0, 1, 0, -1)`

works with `pairwise(dirs)` to produce `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`. These are exactly the up, right, down, and left offsets. For each offset, the code forms the neighbor `(x, y)`.

A neighbor is eligible only if all of the following are true:

- `0 <= x < m` and `0 <= y < n` keep it inside the grid.
- `(x, y) not in vis` prevents revisiting any square in the current walk.
- `grid[x][y] != -1` rejects obstacles.

These tests enforce the walk rules before recursion, avoiding calls that could never be valid.

**Backtrack so that each branch has its own history**

Before following an eligible neighbor, the code executes `vis.add((x, y))`. The recursive call then sees that coordinate as unavailable and can never use it a second time. When that call has counted every valid continuation below it, `vis.remove((x, y))` restores the set to exactly the state it had before the choice.

This removal does not mean that the square becomes unvisited within the same walk. The recursive exploration of that walk is already finished. It makes the square available only to a different branch whose earlier choices may reach it through another route. Omitting the removal would incorrectly make the first explored branch reserve squares for all later branches.

The local variable `ans` accumulates the number of valid endings reachable from the current state. Every eligible next square represents a disjoint next choice, so adding the returned counts is correct: no complete coordinate sequence can begin with two different next squares.

**A small trace**

For the single-row grid `[[1, 0, 0, 2]]`, `cnt = 2`. The initial state has `k = 0`. Moving onto the first zero gives `k = 1`, the second zero gives `k = 2`, and the end gives `k = 3`. Since `cnt + 1 = 3`, the ending call returns one.

If a layout allowed the search to reach the end after only two moves, that ending call would return zero. Even though a route to the destination existed, it would have failed the requirement to visit all non-obstacle squares.

**Why the accumulated answer is exact**

At any call, `vis` contains exactly the coordinates on the current start-to-current-cell walk. This is true initially, and adding the chosen neighbor preserves it for the child call; removing that neighbor restores it for the next choice.

Every recursive branch therefore describes a legal four-directional walk with no obstacle and no repeated square. Conversely, consider any valid complete walk. At every cell, its next coordinate passes all three eligibility checks, so the search contains a branch making that same choice. Repeating this argument follows the entire walk to the end. There the move count is `cnt + 1`, so it contributes one. Invalid walks either become impossible before the end or reach the end with the wrong count and contribute zero. Thus the returned sum counts every valid walk once and only once.

## Complexity detail

Let `V` be the number of non-obstacle squares, including the start and end. Scanning the grid for the start and counting zero squares takes `O(mn)` time.

During the search, the first square can have at most four choices. After a move, the square just left is already visited, so a recursive state has at most three usable directions before boundary, obstacle, and earlier-visit checks reduce that number further. The recursion depth is at most `V`. A standard worst-case upper bound for this path-enumerating implementation is therefore `O(4 \cdot 3^{V-1}) = O(3^V)` time. The algorithm often explores far fewer branches because borders, obstacles, the visited set, and early arrival at the end prune the tree.

The visited set holds at most `V` coordinates, and the recursive call stack has depth at most `V`. Apart from those structures, each call stores only a constant number of values. Auxiliary space is `O(V)`. The input grid itself is never modified.

## Alternatives and edge cases

- **Bitmask dynamic programming:** Encode the visited squares in a bitmask and memoize a state such as `(position, mask)`. This can avoid recomputing equivalent states and gives a subset-state formulation, but it uses substantially more memory and is more complicated than the exact backtracking implementation shown here.
- **In-place visited marking:** Temporarily replace a grid value with an obstacle-like marker and restore it after recursion. This removes the explicit set but mutates the input during the search and requires especially careful restoration.
- **Copying the visited set:** Passing a new set to every child is conceptually simple, but copying up to `V` coordinates at every branch adds unnecessary allocation and time. Add–recurse–remove provides the same isolation efficiently.
- **Reaching the end early:** Such a branch must contribute zero even if the destination is reachable, because some required square remains unvisited. The `k == cnt + 1` check enforces this.
- **Counting only zero squares:** The move target is `cnt + 1` rather than `cnt` because the final move enters the ending square, while the starting square requires no move.
- **Obstacles:** They are never added to `vis` because the eligibility condition rejects `-1` before recursion.
- **Start and end positions:** Nothing assumes corners or a particular orientation; the preliminary scan finds the start wherever it occurs, and the base case recognizes the end by its grid value.
- **Narrow grids and dead ends:** A single row, single column, or corridor works naturally. A branch with no eligible neighbor returns its current `ans` of zero unless it already ended successfully.
- **Input preservation:** Since only `vis` changes, the caller receives the grid with exactly its original values after the method returns.
