## General

**Why every possible path must be considered**

A valid collection route may begin at any positive cell, may stop at any time, moves only in four orthogonal directions, and may not revisit a cell. The locally largest neighboring amount is not necessarily the best choice: taking it can lead into a short dead end, while a smaller neighbor may open a much longer, richer route. Because the grid has at most 25 gold-containing cells, exhaustive search with backtracking is feasible and avoids an unjustified greedy decision.

The solution defines `dfs(i, j)` as the maximum gold collectable by a valid path that starts at cell `(i, j)`, assuming cells already used earlier on the current recursive path have temporarily been changed to zero.

**The base case combines every invalid continuation**

The condition

`not (0 <= i < m and 0 <= j < n and grid[i][j])`

returns zero when the coordinates are outside the grid or the cell value is zero. Short-circuit evaluation matters: Python checks the bounds before evaluating `grid[i][j]`, so an out-of-range coordinate does not index the list. A zero may be an originally empty cell or a temporarily marked visited cell. Both must stop the current continuation, and both correctly contribute no additional gold.

**Choose, explore, and undo**

For a valid gold cell, `v = grid[i][j]` saves its amount. Then `grid[i][j] = 0` marks it unavailable on the current path. This single in-place change acts as the visited set. Any recursive call that tries to return to the cell sees zero and stops, enforcing the “visit at most once” rule.

The tuple `dirs = (-1, 0, 1, 0, -1)` compactly encodes the four direction vectors. `pairwise(dirs)` produces `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`: up, right, down, and left. For each vector `(a, b)`, the recursive expression explores `dfs(i + a, j + b)`.

Only one next neighbor can be chosen by a single path, so the code takes the maximum of the four returned continuation totals. It then adds the current cell’s saved amount:

`ans = max(...) + v`.

Stopping at the current cell is included automatically. If every neighbor is invalid, all four recursive calls return zero, their maximum is zero, and the result is simply `v`.

Before returning, `grid[i][j] = v` restores the cell. This undo step is the heart of backtracking. The zero marker should affect sibling choices within the current path, but it must not leak into a different path explored after recursion returns. Restoration means each recursive branch receives exactly the visited history belonging to that branch, and the outer caller ultimately receives its original grid contents back.

**Why all starting cells are tried**

A maximum path need not begin at the first positive cell or at the largest individual cell. The outer expression calls `dfs(i, j)` for every coordinate and takes the maximum result. Calls that start on zero cells immediately return zero, while calls on gold cells enumerate paths starting there.

Trying every start also covers every orientation of a path. If an optimal path’s cells are \(p_1,p_2,\ldots,p_r\), the call starting at \(p_1\) can choose \(p_2\), then \(p_3\), and so on. No special endpoint detection is required.

For the first example, starting at the cell containing 9 allows the search to mark 9, continue to 8, and then compare the available continuations. Choosing 7 produces \(9+8+7=24\). A different branch might choose 6 or 5 after 8, but `max` retains the richest legal continuation. When each branch returns, all three visited cells are restored for later starting positions.

**Why the returned maximum is correct**

At a valid cell, every legal path must first collect that cell’s gold. Afterward it either stops or moves to exactly one valid, unvisited orthogonal neighbor. The four recursive calls cover all possible moves, and an invalid move contributes zero, which also represents stopping. Assuming the recursive calls correctly return the best continuation under their marked visited set, taking their maximum and adding `v` returns the best path from the current state.

Marking the current cell before recursion guarantees none of those continuations repeats it. Restoring afterward changes no result already computed; it merely prepares the shared grid for another branch. By induction on the number of still-available gold cells, `dfs` is correct for every state. Finally, every valid path has a starting coordinate, and the outer maximum considers all coordinates, so the returned value is the global maximum.

**The grid is used as workspace, not permanently changed**

Although the method mutates `grid` during search, every successful recursive frame restores exactly the value it saved before returning. Normal completion therefore leaves the input matrix identical to its initial contents. This technique saves the memory of a separate visited matrix or set. It relies on the stated fact that zero means unavailable and every collectable amount is positive.

## Complexity detail

Let \(m\) and \(n\) be the grid dimensions, and let \(g\) be the number of cells containing gold. The outer generator makes \(mn\) starting calls. A zero start ends in constant time.

From a gold starting cell there can initially be up to four choices. After the path moves, the immediately previous cell is marked zero, so there are at most three forward choices in a coarse worst-case search-tree bound. This gives a conventional upper bound of \(O(mn\cdot3^g)\), matching the manifest. A tighter way to separate the work is \(O(mn + g\cdot3^g)\): scan all coordinates, then perform exponential exploration from the \(g\) positive starts. Grid geometry and blocked cells usually prune the tree much more heavily, but exponential time is unavoidable for this direct enumeration.

The deepest recursive path contains at most \(g\) gold cells because no cell may repeat. The recursion stack and generator evaluation state therefore use \(O(g)\) auxiliary space. No visited collection is allocated; marking happens inside the input grid. The four direction values use \(O(1)\) space.

## Alternatives and edge cases

- **Explicit visited set:** Store coordinates used by the current path instead of changing the grid. This can make mutation concerns more visible, but membership records consume \(O(g)\) additional space and require their own add-and-remove discipline.
- **Visited bitmask:** Number the at most 25 gold cells and represent visited status in an integer. It avoids mutating the input and supports memoization by state, but requires preprocessing adjacency and more complex state handling.
- **Breadth-first enumeration:** A queue can hold partial paths and their visited sets, but many large path states coexist at once. DFS backtracking retains only one active path and is much more space-efficient.
- **Greedy neighbor choice:** Always taking the richest adjacent cell can miss a longer route with greater total gold. Backtracking is necessary because immediate reward does not determine future connectivity.
- **All-zero grid:** Every starting call returns zero, so the outer maximum returns zero. The grid dimensions are at least one, so the generator passed to `max` is never empty.
- **Single gold cell:** Its four continuations return zero, making `dfs` return exactly that cell’s value.
- **Disconnected gold regions:** A path cannot cross zero cells. Trying every coordinate independently lets the algorithm find the best path in whichever connected component is most valuable.
- **Cycles of gold cells:** Temporary zero marking prevents revisiting a cell, so recursion terminates and explores only simple paths.
- **Starting and stopping anywhere:** Zero-valued continuation results let a path stop at its current cell; the outer maximum supplies every possible beginning. No forced corner or boundary start is assumed.
- **Input restoration:** Each visited cell is restored after its descendants finish, so ordinary completion preserves `grid`. Removing that restoration would incorrectly erase cells for sibling branches and later starting calls.
- **Positive-gold guarantee:** Using zero as a visited marker is valid because zero cells are forbidden and all collectable values are positive. The same technique would need reconsideration if legitimate zero-valued traversable cells were allowed.
- **Required helper import:** The exact source uses `pairwise`, introduced in `itertools`. A standalone execution environment must import it; the algorithm assumes the package harness supplies the name.
