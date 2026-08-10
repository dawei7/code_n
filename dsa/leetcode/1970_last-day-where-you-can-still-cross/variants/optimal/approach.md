## General

**Crossing feasibility is monotone over days**

As days increase, land cells only turn into water; none return to land. If crossing is impossible on day $d$, it remains impossible on every later day. If crossing is possible on day $d$, it was also possible on every earlier day.

This true-then-false pattern supports binary search for the last feasible day.

**Build and search the grid for one proposed day**

`check(k)` constructs a fresh $row$-by-$col$ matrix filled with zeroes for land. It marks the first `k` entries of `cells` as water using one-based-to-zero-based coordinate conversion.

It initializes list `q` with every land cell in the top row. Python list iteration observes items appended during the loop, so `for x, y in q` acts as a FIFO-style breadth-first traversal.

For each reached cell, returning true when `x == row - 1` means a connected land path has reached the bottom row.

The direction tuple `(-1, 0, 1, 0, -1)` and `pairwise` generate up, right, down, and left. An in-bounds neighbor whose matrix value is zero is appended and changed to one. The same marker represents both original water and visited land; either kind must not be traversed again.

**A small visited-marking nuance**

Initial top-row cells are placed into `q` without immediately being marked. Another explored top or second-row cell can append one of these starts once more before it becomes marked. This may create a small number of duplicate queue entries, but it does not change reachability and remains linear work: once a cell is appended through a neighbor, it is marked and cannot be appended again.

Marking starts at initialization would be cleaner, but the exact source is still functionally correct.

**Binary-search the last true day**

There are $N=row\cdot col$ flooding days. The source starts `l=1` and `r=N`. With at least two rows and columns, flooding one cell cannot eliminate every top-to-bottom route, so day one is feasible. Day $N$ is fully flooded and infeasible, providing the range endpoints.

The upper midpoint `(l + r + 1) >> 1` prevents stalling when the successful branch assigns `l = mid`. If `check(mid)` succeeds, all earlier days succeed and the lower bound moves up. If it fails, that day and all later days are removed with `r = mid - 1`.

When bounds meet, `l` is the greatest feasible day.

**Keep the meaning of a day precise**

Day $k$ means that the first $k$ listed cells have already become water. The test is therefore performed on the state *after* the $k$th flood, not just before it. This distinction prevents the common off-by-one error of checking `cells[:k - 1]` or returning one day beside the true boundary. The predicate's parameter, the slice length, and the integer returned by the binary search all use this same definition.

**Why the full method is correct**

For any $k$, the grid marks exactly the cells flooded by the end of day $k$. The traversal returns true exactly when a four-direction land component connects a top cell to a bottom cell.

Monotonicity makes binary-search elimination sound. Its maintained interval always contains the last true day, and termination leaves only that value. Therefore the returned day is correct.

## Complexity detail

Let $N=row\cdot col$.

One `check(k)` allocates and initializes $N$ grid entries, copies a `cells[:k]` slice, marks $k\le N$ floods, and explores at most $O(N)$ cells. It costs $O(N)$ time.

Binary search performs $O(\log N)$ checks, so exact time is $O(N\log N)$. This differs from the manifest's $O(N\alpha(N))$ DSU claim because the concrete source uses binary search plus traversal, not reverse-time union-find.

Each check uses $O(N)$ grid and queue space. The slice adds up to $O(N)$ references, so peak auxiliary space remains $O(N)$.

## Alternatives and edge cases

- **Reverse-time DSU:** Start fully flooded, add land in reverse order, and union neighbors plus virtual top and bottom nodes. This achieves $O(N\alpha(N))$ time and matches the manifest.
- **Binary search plus DFS:** It has the same asymptotic time but recursive DFS risks Python depth limits.
- **Day zero:** The entire grid is land and crossing is always possible. The source begins at one because day one is also guaranteed feasible under row and column bounds.
- **Exact departure flooding order:** `cells[:k]` represents the first $k$ days because array index zero is day one.
- **Top cell already water:** It is excluded from the initial queue.
- **Multiple starting columns:** All land top cells are seeded, so any possible entrance can be used.
- **Visited/water marker reuse:** Both values mean “do not enqueue,” which is sufficient for reachability.
- **Duplicate initial enqueue:** Unmarked seeds may be appended again, but later marking prevents unbounded repetition.
- **Fully flooded final day:** `check(N)` is false, ensuring an infeasible upper extreme.
- **Imported `pairwise`:** The exact source assumes it is available.
- **Input preservation:** Every check builds a new grid and does not modify `cells`.
