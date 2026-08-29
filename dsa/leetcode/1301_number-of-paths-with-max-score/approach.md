## General

Each valid path must optimize two related quantities: first maximize the collected digit sum, and then count how many paths attain that maximum. Counting all paths without their scores is insufficient, and storing only a maximum score loses the number of optimal ways. The Optimal solution therefore keeps two dynamic-programming tables:

- `f[i][j]` is the maximum score obtainable on a valid route from cell `(i, j)` to `S`, or $-1$ when no such route exists;
- `g[i][j]` is the number of routes from `(i, j)` to `S` that attain `f[i][j]`.

The original movement goes from `S` upward, leftward, or diagonally up-left toward `E`. Looking from a cell toward `S` reverses those directions: its possible next cells are down, right, and diagonally down-right. This reversed viewpoint matches a bottom-right-to-top-left table scan.

**Representing unreachable cells**

Every `f` entry starts at $-1$. Valid scores are nonnegative because board digits range from one through nine and the endpoints contribute zero. Thus, $-1$ is an unambiguous marker meaning “unreachable.”

Every `g` entry starts at zero because an unreachable or not-yet-derived state has no valid optimal path.

The bottom-right start `S` is the base case:

`f[-1][-1], g[-1][-1] = 0, 1`.

There is one empty path from `S` to itself, and it collects score zero. Python's negative indices refer to the last row and last column, so `[-1][-1]` is exactly that bottom-right cell.

**Why the scan order makes dependencies ready**

Both loops count from `n - 1` down to zero. When processing `(i, j)`, its possible successor states `(i + 1, j)`, `(i, j + 1)`, and `(i + 1, j + 1)` are either outside the board or have already been processed because they have a larger row or column index.

This gives an acyclic dependency order. No recursion or repeated relaxation is needed; each cell can be finalized once from already-final successors.

The nested helper `update(i, j, x, y)` considers one successor `(x, y)` at a time. It returns immediately if the successor is outside the lower or right boundary, if its score is $-1$, or if the current board cell is `X` or `S`.

Checking `board[i][j] in "XS"` prevents obstacle cells from acquiring a state. It also preserves the manually initialized `S` base case: when the loops eventually reach `S`, all three update calls do nothing instead of replacing its zero score or adding artificial cycles.

**Selecting the best successor and counting ties**

Before considering successors, `f[i][j]` is $-1$. If a reachable successor has a strictly greater score than the current stored candidate, the code performs

`f[i][j] = f[x][y]` and `g[i][j] = g[x][y]`.

This replaces both pieces because all previously considered successor routes yield a smaller score and must not contribute to the number of maximum-score paths.

If `f[x][y] == f[i][j]`, the new successor offers the same best score. Its paths are distinct from paths beginning with the earlier successor because their first move differs, so `g[x][y]` is added to `g[i][j]`.

A lower-scoring successor does nothing. This implements lexicographic optimization: maximize score, but sum counts across every transition that achieves that same score.

The current cell's digit is not added until all three successors have been compared. That ordering is valid because every route leaving the current cell collects the same current digit. Adding a common value to all candidate scores cannot change which successor is greatest. Separating selection from digit addition makes the tie logic simpler.

**Adding the current cell's score**

After all updates, the code checks that `f[i][j] != -1` and that `board[i][j].isdigit()`. Only then does it add `int(board[i][j])`.

An obstacle remains unreachable and cannot receive a digit. `E` and `S` are not digit characters, so they contribute zero exactly as required. A reachable numeric cell adds its value once to the best suffix score, regardless of how many optimal paths leave it. The path count is not multiplied by the digit because score and number of ways are separate quantities.

For board `["E23","2X2","12S"]`, the table begins at `S` and propagates through reachable digits. Routes that touch `X` never acquire scores. At `E`, the stored value is the greatest sum among all legal routes, and `g[0][0]` counts only those routes whose propagated score equals that greatest value.

**Why the two tables are correct**

The base state correctly describes `S`. Assume every already-processed successor of `(i, j)` stores its true maximum score and exact number of maximum-score paths. Every legal route from the current cell must choose exactly one of the three successors. `update` ignores precisely the invalid or unreachable choices, retains the largest reachable successor score, and adds counts across all successors tied at that largest score. Adding the current digit then produces the true score from the current cell.

By reverse scan order, this reasoning applies to every reachable cell until `E`. If `f[0][0]` remains $-1$, no successor chain connects `E` to `S`, so `[0, 0]` is correct. Otherwise, the score is returned together with the count modulo $10^9+7$.

The exact code applies the modulus only in the final return. This does not change the mathematical remainder: addition can be reduced at the end or after every step. Python integers grow to hold the full count, so no overflow occurs.

## Complexity detail

Let $n$ be the side length of the square board. There are $n^2$ cells. Each cell considers exactly three successor positions and performs constant table and character operations under the usual arithmetic model. Time complexity is therefore $O(n^2)$.

Both `f` and `g` contain $n^2$ entries, so auxiliary space is $O(n^2)$. The input board is not counted as extra space.

There is a Python-specific nuance: because `g` is not reduced modulo $10^9+7$ during the dynamic program, path counts can become very large integers. Arithmetic on arbitrarily large integers is not literally constant-time in their bit length. The standard problem analysis treats these additions as constant or assumes modular reduction at each transition. A more robust implementation would reduce `g[i][j]` after additions, preserving the same returned remainder while keeping integers bounded. The manifest's $O(n^2)$ time uses the conventional unit-cost model.

## Alternatives and edge cases

- **Forward dynamic programming from `S`:** Propagating up, left, and up-left is equally valid if the scan order is adjusted so every predecessor is ready. The two-value state and tie handling remain necessary.
- **One-dimensional row compression:** Only the current and next row are needed, so careful bookkeeping can reduce extra space to $O(n)$. The full tables are easier to reason about and match the exact source.
- **Enumerate every path:** The number of paths grows exponentially, making direct recursion without memoization infeasible.
- **Store only the best score:** This cannot answer how many paths attain that score. Counts must travel with scores and reset whenever a strictly better score replaces the old one.
- **Count every reachable path:** Lower-scoring paths must not be included. The equality branch adds counts only for successors tied at the maximum.
- **Obstacle at a dependency position:** Its `f` value stays $-1`, so neighboring cells ignore it automatically.
- **No path from `E` to `S`:** `f[0][0]` remains $-1` and the special return produces `[0, 0]` rather than exposing the sentinel.
- **Endpoint scores:** Neither `E` nor `S` is a digit, so both correctly contribute zero.
- **Several optimal first moves:** Equal successor scores cause their counts to be added, representing distinct routes.
- **Diagonal movement:** `update(i, j, i + 1, j + 1)` is essential; omitting it changes the allowed graph and can lower both score and count.
- **Modulo timing:** Reducing counts after every addition is preferable in fixed-width languages and avoids huge Python integers. It gives the same final remainder because modular addition is associative.
- **Square-board guarantee:** The code uses one `n` for row and column bounds. A rectangular generalization would require separate dimensions.
- **Character digits only:** `isdigit()` recognizes the numeric board cells, and `int` converts their values. The local board alphabet keeps this unambiguous.
