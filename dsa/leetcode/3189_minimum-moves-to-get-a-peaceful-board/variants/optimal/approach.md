## General

**Separate every move into a row cost and a column cost**

Moving a rook from $(x,y)$ to $(a,b)$ takes
$\lvert x-a\rvert+\lvert y-b\rvert$ unit moves. A peaceful final board uses
every target row $0,1,\ldots,n-1$ exactly once and independently uses every
target column exactly once. Consequently, the minimum row cost and the minimum
column cost can be derived as two separate one-dimensional matching problems.

**Match equal ranks after sorting**

Let $r_0 \le r_1 \le \cdots \le r_{n-1}$ be the sorted starting rows. If two
coordinates $a \le b$ are assigned to targets $j \le i$ in crossing order,
then exchanging those targets cannot increase their total distance:

$$
\lvert a-i\rvert+\lvert b-j\rvert
\ge
\lvert a-j\rvert+\lvert b-i\rvert.
$$

Repeatedly uncrossing assignments proves that an optimum pairs `r_i` with
target row `i`. Apply the same argument to the sorted column coordinates.
Therefore the answer is

$$
\sum_{i=0}^{n-1}
\left(\lvert r_i-i\rvert+\lvert c_i-i\rvert\right),
$$

where $c_i$ is the $i$-th sorted starting column.

**Why the no-collision rule does not add distance**

First move every rook vertically to its assigned target row. Within any one
column, rooks start in strict row order, and rank matching preserves that
order, so their vertical paths never need to cross. These moves can therefore
be scheduled without a collision. The board then has exactly one rook in each
row. Move each rook horizontally to its assigned target column; because the
rooks now occupy different rows, those paths cannot collide either. Every move
belongs to a shortest vertical-then-horizontal path, so the row-plus-column
lower bound is attainable without extra distance. For $n=1$, the only rook is
already peaceful.

## Complexity detail

Sorting the $n$ row coordinates and $n$ column coordinates costs
$O(n\log n)$ time. The final paired sum is $O(n)$. The two sorted coordinate
lists use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Counting coordinates:** Because every coordinate lies in $[0,n-1]$, two
  frequency arrays can enumerate the sorted row and column multisets in
  $O(n)$ time and $O(n)$ space, at the cost of a more specialized
  implementation.
- **Repeatedly choose the smallest coordinate:** Removing the minimum row and
  column at each rank produces the same matching but takes $O(n^2)$ time with
  ordinary lists.
- **Choose a nearby empty row and column greedily:** Local choices can cross;
  without the rank-matching argument they may force a later rook to travel
  farther.
- A board is already peaceful whenever its row coordinates and column
  coordinates are both permutations of $0,1,\ldots,n-1$, regardless of which
  row is paired with which column.
- Repeated rows or columns are allowed; only repeated complete cells are
  forbidden in the input.
- The two coordinate matchings may be analyzed independently even though each
  rook keeps its own paired final row and column.
