## General

A path is counted as soon as one move takes the ball outside the grid. The phrase “at most `maxMove` moves” is important: a path that exits on move one is already successful and must not be extended to exactly `maxMove` moves. The recursive state should therefore answer a question about the moves that are still available:

> `dfs(i, j, k)` is the number of direction sequences that move a ball currently at row `i` and column `j` out of the grid using at most `k` further moves.

This definition contains all information that can affect the future. How the ball reached `(i, j)` does not matter. Two partial paths that arrive at the same cell with the same number of moves left have identical possible continuations, which is exactly why memoization is effective.

**The two base cases and why their order matters**

The first check asks whether `(i, j)` is outside:

```python
if not 0 <= i < m or not 0 <= j < n:
    return int(k >= 0)
```

An outside position means the immediately preceding move crossed a boundary, so that branch contributes one successful path. In normal calls from an in-grid state, recursion happens only when `k > 0` and passes `k - 1`, so a newly outside state has `k >= 0`. The integer conversion turns `True` into one. The more defensive `k >= 0` check prevents an already over-budget outside state from being counted if such a call were ever made.

This boundary test must occur before the no-moves test. Imagine the ball has one move left and steps outside. The child call has `k = 0`, but it is a valid path because the crossing used the final allowed move. If `k <= 0` were tested first, that successful branch would incorrectly return zero.

If the position is still inside and `k <= 0`, no movement remains and the ball has failed to leave, so the second base case returns zero.

**Generating the four neighboring cells**

The tuple

```python
dirs = (-1, 0, 1, 0, -1)
```

is a compact encoding of four row/column changes. `pairwise(dirs)` produces `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`: up, right, down, and left. The repeated `-1` at the end closes the sequence so the fourth pair is available.

For every direction `(a, b)`, the next cell is `(i + a, j + b)` and one move is consumed, so the recursive call is `dfs(i + a, j + b, k - 1)`. Different direction sequences count as different paths even when they later reach the same state. Adding the returned counts is therefore correct: the four possibilities are disjoint according to their first move and together cover every legal first move.

**Why caching changes the problem from exponential to polynomial**

Without `@cache`, the recursion tree has up to four children at each level. Many branches repeat the same state. For example, moving right and then left can return to the starting cell with two fewer moves; many other sequences may reach that identical cell and remaining-move count.

`@cache` records the return value for each argument triple `(i, j, k)`. The first call computes the state; every later call with the same triple immediately reuses the stored count. This is valid because the grid dimensions, modulus, and direction list are fixed in the surrounding function and because `dfs` has no changing external state. Its answer depends only on `i`, `j`, and `k`.

**Modulo arithmetic**

The number of paths can grow extremely quickly, so the problem asks for the result modulo

$$
M = 10^9 + 7.
$$

After adding each child result, the code applies `% mod`. Modular addition preserves the final remainder:

$$
(x+y) \bmod M
=
\bigl((x \bmod M)+(y \bmod M)\bigr)\bmod M.
$$

Reducing during accumulation keeps intermediate values small without changing the required answer.

**Why the recurrence is correct**

Consider an in-grid state with $k>0$. Every successful path must begin with exactly one of the four legal directions. After that first move, the remaining suffix is a successful path counted by the corresponding state with $k-1$ moves left. Conversely, prefixing any path counted by such a child with that child’s direction creates a valid path from the current state. The four sets do not overlap because their first directions differ, so their counts add.

The outside base case assigns one to precisely a path that has just crossed the boundary within its allowance. The in-grid, zero-move base case assigns zero because no crossing can occur. Induction on $k$ now proves that every cached state returns exactly the number stated in its definition. Calling it at `(startRow, startColumn, maxMove)` gives the requested answer.

For `maxMove = 0`, the valid starting position is inside by contract. The boundary test is false, the no-moves test returns zero, and the answer is correctly zero.

## Complexity detail

Let $K=\texttt{maxMove}$. There are at most $m n (K+1)$ in-grid states `(i, j, k)`. Each uncached in-grid state examines four directions and otherwise performs constant work, so the time complexity is $O(mnK)$. A smaller number of outside states is also cached along the four borders; this does not exceed the same asymptotic bound for nonempty dimensions.

The exact implementation uses `@cache` on all three state coordinates, including `k`. Its memo table can therefore hold $O(mnK)$ values, and recursion adds an $O(K)$ call stack. The exact implementation’s auxiliary space is consequently $O(mnK)$, not $O(mn)$.

The variant manifest’s $O(mn)$ space bound corresponds to the bottom-up dynamic-programming optimization that retains only the previous and next move layers. That optimization computes the same recurrence but is not what this exact recursive source does. It is important not to claim rolling-array space for a cache whose key explicitly includes the remaining-move dimension. With the constraints $m,n,K \le 50$, the three-dimensional memo remains bounded and practical.

## Alternatives and edge cases

- **Bottom-up dynamic programming with two grids:** Store how many ways occupy each cell after the current number of moves, add boundary exits, and build the next layer. This has the same $O(mnK)$ time but only $O(mn)$ auxiliary space and matches the manifest’s space target.
- **Full three-dimensional table:** An iterative table indexed by move, row, and column avoids recursion but still uses $O(mnK)$ space. It can be easier to debug because every layer is explicit.
- **Uncached depth-first search:** Exploring every direction sequence is conceptually direct but takes up to $O(4^K)$ time because it recomputes equivalent states.
- **Matrix exponentiation:** Grid transitions can be represented as a matrix, but the state space and implementation overhead make that approach inappropriate for $K \le 50$.
- **Zero allowed moves:** The starting cell is guaranteed inside, so no path can leave and the result is zero.
- **One-row or one-column grids:** A cell may touch multiple boundaries. Each outward direction is a distinct path and must be counted separately; the four-direction recurrence naturally does this.
- **Corner cells:** Two of the four first moves leave immediately. They are separate direction sequences, so each contributes one.
- **Exit on the final move:** The outside check precedes `k <= 0`, ensuring a crossing that leaves zero moves remaining is counted.
- **Do not continue after exit:** An outside state returns immediately. This enforces “at most” rather than padding a successful path with meaningless later moves.
- **Direction encoding:** `pairwise` must be available from `itertools`, and `cache` from `functools`, in the execution environment. The five-number direction tuple is ordered specifically to yield all four moves.
- **Modulo placement:** Applying the modulus after every addition is safe and prevents large intermediate counts. Base-case values zero and one already have the correct remainder.
- **Recursion depth:** The deepest chain uses at most $K+1$ calls. Here $K \le 50$, so ordinary Python recursion depth is not a practical risk.
