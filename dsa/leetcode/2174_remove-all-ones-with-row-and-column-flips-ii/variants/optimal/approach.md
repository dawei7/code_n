## General

**Encode only cells that remain one**

Let $k=mn$. Number the cells from $0$ through $k-1$ and store the current
matrix as a $k$-bit mask. For every position, precompute a mask containing its
entire row and column. Choosing that position changes a state with one bitwise
operation: `mask & ~clear_masks[position]`.

Zeros never become ones, so the mask completely describes every future legal
choice. The history and order used to reach it are irrelevant.

**Explore legal choices once per state**

For a nonzero mask, try every set bit because only a current `1` may be
selected. Each choice costs one operation plus the optimal result for the
strictly smaller resulting mask. Take the minimum of those candidates.
Memoization ensures that different operation orders reaching the same
remaining set share one computation.

The zero mask needs no operations. By induction on the number of set bits,
every recurrence candidate uses an optimal continuation, and considering every
legal first operation guarantees that their minimum is globally optimal.

## Complexity detail

Let $k=mn$, with $k\le15$. There are at most $2^k$ masks, and a computed state
examines at most $k$ cells, giving $O(k2^k)$ time. The memo table and recursion
use $O(2^k)$ space; the recursion depth is at most $k$.

## Alternatives and edge cases

- **Breadth-first search over masks:** It finds the first route to zero and has
  the same exponential state bound, but stores a queue as well as visited
  states.
- **Unmemoized operation-order search:** It is correct but repeats the same
  remaining mask through many different choice orders.
- **Greedy largest-clear choice:** Removing the most current ones need not
  preserve the intersections needed for the best later operations.
- An all-zero grid is already the base state and returns `0`.
- A selected cell must currently be `1`; choosing a zero intersection is not a
  legal way to clear its row and column.
- Clearing a row and column counts as one operation even though their selected
  cell belongs to both.
