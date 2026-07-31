## General

**Translate a row into its card cost**

A row containing $k$ triangles uses $2k$ leaning cards and $k-1$ horizontal
cards, for a total of

$$
2k+(k-1)=3k-1.
$$

The horizontal cards of a $k$-triangle row provide exactly $k-1$ support
positions for the row above. Because every higher triangle occupies the
leftmost available position, consecutive row widths must strictly decrease
from bottom to top. Conversely, any strictly decreasing sequence of positive
triangle counts produces a supported, left-aligned house.

**Count each set of row widths once**

The possible costs for one row are therefore $2,5,8,\ldots$ up to $n$, and a
valid house selects each cost at most once. Its vertical order is already
forced: the largest selected width is the bottom row, followed by the
remaining widths in decreasing order. Counting houses is thus the same as
counting subsets of these costs whose sum is $n$.

Initialize `ways[0] = 1`. Process each possible row cost once. For that cost,
visit card totals from $n$ downward and add `ways[total - row_cost]` into
`ways[total]`. Descending order prevents the current row width from being
selected twice. By induction after each cost, `ways[x]` counts exactly the
subsets of processed row widths totaling $x$; hence `ways[n]` is precisely the
number of distinct houses.

## Complexity detail

There are $\lfloor(n+1)/3\rfloor$ possible row widths. Each scans at most $n$
card totals, so the running time is $O(n^2)$. The counting array uses $O(n)$
space.

## Alternatives and edge cases

- **Enumerate row-width subsets:** Recursively choose or skip every possible
  width and test the resulting total. This is direct but exponential in $n$.
- **Two-dimensional subset DP:** Retain a separate row for every processed
  width. It also takes $O(n^2)$ time but consumes $O(n^2)$ space.
- Fewer than two cards cannot form even one triangle, so the answer is zero.
- A single row is valid exactly when $n=3k-1$ for some positive integer $k$.
- Different selections of row widths define different houses; their row order
  is not an additional choice.
- Iterating totals upward would incorrectly allow the same row width more than
  once.
