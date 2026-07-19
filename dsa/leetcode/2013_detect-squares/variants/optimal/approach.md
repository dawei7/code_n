## General
**Store multiplicities globally and by horizontal row.** A counter keyed by
`(x, y)` records how many occurrences exist at every coordinate. A second map
from each `y` to its counter of `x` values lets a query inspect only possible
horizontal partners. Each addition increments both counters.

**Use each horizontal partner to determine both possible squares.** For query
`(x, y)` and stored partner `(other_x, y)`, let
`side = other_x - x`. Ignore `side == 0`, which would produce zero area. The
other two corners are either `(x, y + side)` and
`(other_x, y + side)`, or the corresponding coordinates at `y - side`.
For each orientation, multiply the occurrence counts at all three stored
corners and add the product.

Every positive-area axis-aligned square containing the query has exactly one
other corner on the query's horizontal row. That corner fixes its signed side
length and the two remaining coordinates, so the scan reaches the square
exactly once. Conversely, every nonzero product represents independent choices
of the three required stored occurrences, including duplicates. The sum
therefore equals the number of valid ways.

## Complexity detail
An addition takes average $O(1)$ time. A count visits the $H$ distinct
horizontal coordinates on the query row and performs constant-time counter
lookups for each, taking $O(H)$ time. Storing counters for $P$ occurrences uses
$O(P)$ space in the worst case.

## Alternatives and edge cases
- **Scan every stored coordinate:** Testing each point as a possible diagonal
  or horizontal corner takes $O(P)$ per count even when the query row is
  sparse.
- **Enumerate triples:** Choosing every three stored points is conceptually
  direct but requires cubic work before geometry checks.
- Repeated additions at one coordinate are distinct choices and multiply the
  result rather than being deduplicated.
- A stored point sharing both query coordinates cannot define a positive side
  length and must be ignored as a horizontal partner.
- Squares may extend above or below the query row, including coordinates at
  the legal boundaries $0$ and $1000$.
