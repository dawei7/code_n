## General
**Describe the first path by its drop column.** If the first robot moves down
at column `c`, it zeros the top row through `c` and the bottom row from `c`
onward. The only positive regions left are the top suffix strictly after `c`
and the bottom prefix strictly before `c`.

**Turn the second robot's choice into a maximum.** A second path cannot collect
both residual regions: reaching the bottom prefix prevents returning to the
top suffix. It can choose whichever region has the larger total, so its best
score after drop `c` is
`max(top_suffix_after_c, bottom_prefix_before_c)`. The first robot chooses the
drop column minimizing that value.

Initialize the remaining top sum with the whole top row and the bottom prefix
with zero. At each column, remove the current top cell before evaluating the
maximum, then add the current bottom cell afterward. These update positions
preserve the strict suffix and prefix definitions. Since every legal first
path has one drop column and the formula gives the optimal response to that
path, the minimum across columns is the game's minimax value.

## Complexity detail
Here $N$ is the number of columns. The initial top-row sum and the drop-column
scan each take $O(N)$ time. Two running sums and the current minimum use
$O(1)$ additional space.

## Alternatives and edge cases
- **Recompute both regions per drop:** Summing a fresh suffix and prefix for
  every column is correct but takes $O(N^2)$ time.
- **Two prefix arrays:** Precomputing both row sums supports constant-time
  drop evaluation but uses unnecessary $O(N)$ space.
- With one column, the first robot clears both cells and the second scores
  zero.
- The best drop may occur at either boundary, leaving one residual region
  empty.
- Total scores can exceed 32-bit range, so the result must preserve a wide
  integer value.
