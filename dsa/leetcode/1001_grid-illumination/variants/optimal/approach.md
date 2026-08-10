## General

**Represent only active lamps, never the enormous grid**

The grid side length can be as large as one billion, so constructing even one row is impossible. Fortunately, illumination depends only on the at most twenty thousand listed lamps and queries.

The solution stores active lamp coordinates in a set and maintains how many active lamps lie on each relevant row, column, and diagonal. A query can then be answered with four counter lookups instead of scanning any cells.

**Deduplicate the initial lamp list**

The set comprehension

`s = {(i, j) for i, j in lamps}`

stores each physical lamp once even if its coordinate appears repeatedly in the input. This matches the statement: listing the same lamp multiple times still turns on only one lamp.

Deduplication must occur before the line counters are built. Otherwise, counters would claim multiple active lamps at one coordinate, and turning that lamp off once would leave false positive counts.

**Identify rows, columns, and both diagonal families**

Four `Counter` objects store active-lamp counts:

- `row[i]` counts lamps with row coordinate `i`;
- `col[j]` counts lamps with column coordinate `j`;
- `diag1[i - j]` counts lamps on a top-left to bottom-right diagonal;
- `diag2[i + j]` counts lamps on a top-right to bottom-left diagonal.

Why do these diagonal keys work? Moving one step down and right increases both coordinates by one, leaving `i - j` unchanged. Moving down and left increases the row and decreases the column, leaving `i + j` unchanged.

Every active lamp in the deduplicated set increments one entry in each counter.

**Answer illumination before turning lamps off**

For query cell `(i, j)`, the code tests:

`row[i] or col[j] or diag1[i - j] or diag2[i + j]`.

Any positive count means at least one active lamp shares a permitted line with the cell, so `ans[k]` becomes one. If all counts are zero, no active lamp illuminates it and the preinitialized answer remains zero.

The answer must be computed before the shutdown step. A lamp at the query cell or one of its neighbors still illuminates the cell for that query and is turned off only afterward.

Counter lookups for missing keys yield zero, which makes the Boolean expression direct.

**Turn off the query cell and its eight neighbors**

The two ranges

`range(i - 1, i + 2)` and `range(j - 1, j + 2)`

generate the complete `3 x 3` neighborhood centered at the query: the cell itself, four side neighbors, and four diagonal neighbors.

For each coordinate `(x, y)`, membership in `s` determines whether an active lamp is actually present. If it is:

1. remove the coordinate from `s`;
2. decrement its row count;
3. decrement its column count;
4. decrement both diagonal counts.

Keeping all five structures synchronized is essential. The set answers whether a physical lamp exists, while the counters answer whether an entire line has any lamps.

**Why explicit boundary checks are unnecessary in shutdown**

Near a grid edge, the `3 x 3` ranges generate some negative or too-large coordinates. Such coordinates cannot be in `s` because every input lamp coordinate is legal. Their membership tests simply fail, so no counter is accessed or changed for them.

This safely avoids four additional comparisons inside every neighborhood check.

**Why counters never become negative**

A coordinate is decremented only if it is currently in `s`, and it is removed from `s` at the same time. A later query encountering that coordinate cannot remove it again. Since initialization also counted every set coordinate exactly once, every decrement corresponds to a previous increment.

Zero-valued counter entries may remain stored, but zero is false in the illumination test and causes no correctness problem.

**Trace the first example**

With active lamps `(0, 0)` and `(4, 4)`, both lie on diagonal key `i - j = 0`.

Query `(1, 1)` has the same diagonal key, so it is illuminated and produces one. The following neighborhood shutdown includes `(0, 0)`, so that lamp is removed and every one of its line counts is decremented.

Query `(1, 0)` is not on the row, column, or either diagonal of the remaining lamp at `(4, 4)`, so it produces zero.

In the repeated-query example, the first query at `(1, 1)` removes the nearby lamp at `(0, 0)` but not the distant lamp at `(4, 4)`. The second identical query is still illuminated by that distant lamp, demonstrating that shutdown affects only the local neighborhood, not every lamp illuminating the query.

**Why the data structures answer every query exactly**

Maintain the invariant that `s` is exactly the set of currently active lamps and every counter equals the number of coordinates in `s` with its key.

Initialization establishes this from the deduplicated lamp set. The illumination test checks precisely the four line families in the movement rule. Each shutdown removal deletes one active coordinate and decrements all and only its four associated counters, preserving the invariant.

Thus a positive queried counter exists exactly when an active lamp shares the corresponding line, and every output bit is correct for the state before that query's removals.

**Sparse state is the crucial optimization**

The numeric value of `n` affects only which coordinates are legal; it does not affect storage or iteration counts. The method's work scales with the number of lamps and queries, not with `n^2`.

## Complexity detail

Let `L` be the number of listed lamps, `U` the number of unique lamp coordinates, and `Q` the number of queries.

Building the set and counters takes expected `O(L)` time. Each query performs four expected constant-time counter lookups and exactly nine expected constant-time set membership checks, so all queries take expected `O(Q)` time. Total expected time is `O(L + Q)` under standard hash-table assumptions.

The active set and four counters together store `O(U)` meaningful lamp-derived entries, which is `O(L)` space. The returned answer uses `O(Q)` output space; auxiliary state excluding the output is `O(L)`.

## Alternatives and edge cases

- **Materialize the grid:** Impossible when `n` can be one billion; sparse lamp state is mandatory.
- **Scan all active lamps per query:** It can test shared lines directly but costs `O(LQ)` in the worst case.
- **Store Boolean line presence only:** Counts are necessary because turning off one lamp must not clear a line still illuminated by another.
- **Duplicate input lamps:** The set collapses them before counters are incremented, preventing phantom multiplicity.
- **No lamps:** All counters return zero, every answer is zero, and neighborhood scans remove nothing.
- **No queries:** The preallocated answer is empty and returned after initialization.
- **Lamp on the queried cell:** It illuminates the query first, then is removed during the centered neighborhood scan.
- **Lamps sharing one line:** Removing one decrements the count but the line remains illuminated while another count is positive.
- **Edge and corner queries:** Out-of-range neighborhood coordinates fail set membership harmlessly.
- **Repeated queries:** Each uses the current state after all earlier shutdowns; previously removed lamps cannot be removed twice.
- **Two diagonal types:** Checking only `i - j` or only `i + j` would miss half of diagonal illumination.
- **Input preservation:** The original `lamps` and `queries` lists are not modified; the active set is separate.
