## General

**Represent each row by its remaining suffix**

Because every successful operation chooses the smallest available seats, the
empty seats in a row always form one contiguous suffix. Store only its length.
If a row has $x$ seats remaining, the next allocated seat is `m - x`.

**Maintain both capacity and a gather predicate**

Build a segment tree over row indices. Every node stores the sum of remaining
seats in its interval and the maximum remaining seats of any row there.

For `gather(k, maxRow)`, descend left-first through nodes intersecting the
allowed prefix whose maximum is at least $k$. This finds the smallest eligible
row. Its current used count gives the first seat; subtract $k$ from that leaf
and repair ancestor sums and maxima.

For `scatter(k, maxRow)`, first query the prefix sum. If it is smaller than
$k$, return `false` before any mutation. Otherwise, repeatedly find the first
row with at least one seat, take as many seats there as possible, and update
the tree until the group is complete.

The prefix test makes failure atomic. A successful scatter's loop can finish
many rows, but each row becomes full at most once over the lifetime of the
object. Thus all such row-filling iterations contribute only $O(n)$ updates
across the entire trace, in addition to the searches performed by the $q$
calls.

## Complexity detail

Across $q$ method calls, tree construction and all successful row-filling
updates take $O((n+q)\log n)$ total time: each `gather` performs one search and
one update, while scatter's extra full-row updates total at most $n$.
Individual prefix queries and tree searches take $O(\log n)$. The remaining
seat array and segment tree use $O(n)$ space.

## Alternatives and edge cases

- **Scan rows directly:** A row array is simple and correct, but each failed gather or capacity query may inspect every eligible row, taking $O(nq)$ total time.
- **Fenwick tree alone:** Prefix sums support scatter capacity, but locating a row with a sufficiently large contiguous suffix also needs a maximum-search structure.
- **Failed scatter:** Capacity must be checked before allocation so an unsuccessful request leaves every row unchanged.
- **`maxRow` boundary:** Both searches and capacity sums include `maxRow` itself and exclude every later row.
- **Group larger than one row:** `gather` fails even if enough seats exist across several rows, while `scatter` may succeed.
- **Partially occupied row:** A gathered block begins immediately after its already booked prefix.
- **One row:** Both methods reduce to allocations from one remaining suffix.
- **Large seat count:** Prefix totals can exceed 32-bit range because both $n$ and $m$ may be large.
