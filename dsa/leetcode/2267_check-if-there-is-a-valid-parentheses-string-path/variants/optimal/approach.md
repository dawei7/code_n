## General

**Track validity through the unmatched-opening balance**

For a parentheses prefix, define its balance as the number of opening parentheses minus the number of closing parentheses. A complete parentheses string is valid exactly when two conditions hold:

- the balance never becomes negative at any prefix, because a closing parenthesis cannot be matched before an opening one exists;
- the final balance is zero, because every opening parenthesis must eventually be closed.

The grid path determines a string one cell at a time. The memoized search therefore needs only its current cell and the balance accumulated along the path, rather than the entire path string.

**Reject globally impossible endpoint patterns first**

Every path from the upper-left to the bottom-right visits exactly

$$
m + n - 1
$$

cells: the starting cell plus `m - 1` downward moves and `n - 1` rightward moves. A valid parentheses string has even length, so an odd value of `m + n - 1` makes every path impossible.

A valid non-empty string must start with `'('` and end with `')'`. The outer condition checks these facts before recursion:

- if the fixed path length is odd, return false;
- if `grid[0][0]` is `')'`, return false;
- if the bottom-right cell is `'('`, return false.

These tests are not required for the recursive logic to eventually reject the grid, but they avoid exploring states whose failure is already certain.

**Define exactly what a cached state means**

The function `dfs(i, j, k)` receives `k` as the balance before consuming cell `(i, j)`. It calculates `d = 1` for an opening parenthesis and minus one for a closing parenthesis, then performs `k += d`. From that point onward in the call, `k` is the balance after including the current cell.

This distinction prevents double-counting. The initial call uses `dfs(0, 0, 0)` because no cell has yet been consumed. Every recursive call passes the current post-cell balance to a neighbor, where that neighbor consumes its own character.

The `@cache` key consists of the arguments `(i, j, k)` as they enter the call. Since the grid cell is fixed, an incoming balance deterministically maps to one outgoing balance, so this key contains all information needed to reuse the result.

**Prune a negative prefix immediately**

After consuming the current character, `k < 0` means the path prefix has used more closing than opening parentheses. No future opening parenthesis can repair an invalid earlier prefix, because validity requires every prefix to be nonnegative. The state can safely return false without exploring either neighbor.

This is the essential validity pruning. It prevents the search from carrying paths that have already violated the parentheses grammar.

**Prune balances that are far too large**

From cell `(i, j)`, the exact number of cells still to visit after the current one is

$$
R = (m - 1 - i) + (n - 1 - j)
  = m + n - i - j - 2.
$$

Even if all `R` remaining cells are closing parentheses, they can reduce the balance by at most `R`. A balance greater than `R` cannot finish at zero.

The exact source checks the looser condition `k > m - i + n - j`, whose right side is `R + 2`. This test is conservative: every state it rejects is certainly impossible, so it cannot remove a valid path. It does not reject all balances that already exceed the exact closing capacity, and some extra impossible states may therefore remain for the terminal test or later recursion to reject. The explanation must preserve this distinction because the executable bound is safe but not tight.

**Explore the only legal moves**

Applying `pairwise` to `(0, 1, 0)` produces direction pairs `(0, 1)` and `(1, 0)`. They mean right and down. For each direction, the code forms neighbor coordinates `(x, y)`, checks that they lie inside the grid, and recursively tests the neighbor with the current balance.

The loop returns true as soon as either continuation succeeds. If neither in-bounds continuation can lead to a valid completion, it returns false. No up or left move is generated, so every explored state belongs to a legal monotone path and recursion cannot cycle by position.

**Recognize success only at the destination**

When `(i, j)` is the bottom-right cell, its parenthesis has already been incorporated into `k`. The call returns `k == 0`. All earlier negative balances were pruned, so zero at the end supplies the second and final condition for a valid parentheses string.

Reaching balance zero at an intermediate cell is not automatic success. The path must still reach the destination, and later characters may open or close new pairs. Accordingly, the destination coordinates are part of the base case.

**Why memoization is valid**

Many different right/down paths can reach the same cell with the same balance. From that moment onward, their past details no longer matter: they share the same current grid character history effect, the same allowed future cells, and the same number of unmatched openings.

Without caching, the search could revisit identical subproblems through exponentially many path prefixes. `@cache` computes each distinct triple once and returns the stored Boolean on later visits. Paths reaching the same cell with different balances remain separate because they have different abilities to match future closing parentheses.

**Why the search is complete and correct**

Every recursive branch appends the current cell to a legal right/down path. Negative-prefix pruning removes only strings that can never be valid. The upper-balance test also removes only states whose excessive unmatched openings cannot all be closed, although its loose bound retains some additional failures.

At every surviving non-destination state, both possible legal directions are examined when in bounds. Therefore, any valid path has a corresponding unpruned chain of recursive calls. Its prefixes never have negative balance, and its destination balance is zero, so that chain returns true.

Conversely, a true result can originate only from the destination with zero balance and propagate through legal neighbor calls. Since negative prefixes never survive, the represented path's parentheses string is valid. The returned Boolean is therefore true exactly when at least one valid path exists.

**A useful balance perspective**

The grid may contain exponentially many geometric paths, but the balance at a position is at most proportional to the path length. Memoization replaces “which route did we take?” with “what position and unmatched-opening count did that route produce?” This state compression is the core reason the problem is tractable.

Parity also constrains reachable balances: after a fixed number of consumed cells, only balances with matching parity can occur. The code does not store a separate parity check because impossible parities are never generated by adding exactly plus or minus one per cell.

## Complexity detail

At a cell, the balance can take `O(m + n)` possible values along paths of length at most `m + n - 1`. Across `mn` cells, the cache can therefore contain `O(mn(m+n))` states. Each newly computed state performs constant work and makes at most two cached recursive calls, so worst-case time is `O(mn(m+n))`.

The memoization cache stores one Boolean result and tuple key per reachable state, giving `O(mn(m+n))` worst-case auxiliary space for the exact source. The recursion stack has depth at most `m + n - 1`, adding `O(m+n)` space, which is dominated by the cache.

The manifest's `O(n(m+n))` space corresponds to a row-compressed iterative propagation design. The executable code is a whole-grid memoized DFS and does not discard prior rows, so its exact worst-case space includes the factor `m`.

## Alternatives and edge cases

- **Iterative sets of balances per cell:** Propagate reachable balances row by row. Keeping only the current and previous row can achieve `O(n(m+n))` space while retaining the same time bound.
- **Three-dimensional Boolean table:** It mirrors the cached states deterministically but allocates space even for unreachable combinations.
- **Enumerate complete paths:** There can be exponentially many right/down paths, so testing each resulting string separately is infeasible.
- **Store complete prefix strings:** Future feasibility depends only on balance and position, making full strings unnecessary and much more expensive.
- **Tighter closing-capacity prune:** Rejecting `k > m + n - i - j - 2` would safely remove more impossible states than the exact code's `R + 2` threshold.
- **Odd path length:** A valid parentheses string cannot have odd length, so the top-level test returns false before DFS.
- **Closing parenthesis at the start:** The first balance would be negative; the endpoint precheck rejects it immediately.
- **Opening parenthesis at the destination:** Final balance cannot be zero after consuming an opening parenthesis, so it is rejected early.
- **Balance becomes negative later:** That prefix is permanently invalid even if later cells contain openings.
- **Balance reaches zero early:** Search continues because later path cells must still form valid matched content.
- **Same cell, same balance via different paths:** Caching merges these states because their future possibilities are identical.
- **Same cell, different balances:** They cannot be merged; future closings may complete one and not the other.
- **Single row or single column:** There is only one geometric path, but the same balance logic evaluates it correctly.
- **One-cell grid:** Its path length is odd, so no valid non-empty parentheses string can be formed.
- **Direction order:** Right is tried before down, but short-circuit order affects only which successful path is discovered first, not existence.
- **Loose upper prune:** It preserves correctness but may cache states that a tighter remaining-cell calculation could reject sooner.
- **Recursion depth:** The stack grows with path length, up to `m+n-1`, which is modest under the given dimensions.
- **Input preservation:** Grid characters are inspected but never modified.
