## General

**Stop dividing once the value is small enough.** If the current value is at
most `y`, division can only move it farther from the target. The best remaining
route is therefore the direct sequence of increments, costing `y - value`.

**Only the nearest multiples matter.** For a current value above `y`, consider
using division by either 5 or 11 next. Before that division, any sequence of
unit changes that enables it must reach a multiple of the divisor. The closest
such multiple below costs the remainder in decrements; the closest one above
costs the complementary number of increments. A farther multiple adds unit
moves without producing a better post-division value than a route considered
at another recursive state.

For each divisor, try both nearest multiples, pay the unit changes plus one
division, and recurse on the quotient. Also retain the option of decrementing
directly to `y`. Every recursive quotient is smaller than the current value,
so the recurrence terminates. Memoization makes equal quotient states share
their result, and taking the minimum covers the first division of every
potentially optimal route.

## Complexity detail

After divisions by 5 and 11, a state is determined by how many times each
divisor has been used, plus a bounded rounding effect. There are
$O(\log^2 X)$ such memoized states, and each performs constant work. Time and
auxiliary space are therefore $O(\log^2 X)$, including the memo table and
recursion stack. When `x <= y`, the direct-increment base case returns in
constant time.

## Alternatives and edge cases

- **Bounded breadth-first search:** Exploring integer values finds the shortest path, but its $O(X)$ state range is unnecessarily large.
- **Only round downward:** This misses routes such as 54 to 2, where incrementing to the next multiple of 11 is optimal.
- **Direct unit changes:** The initial `x - y` candidate remains necessary because division may not help.
- **Target above the start:** When `x <= y`, exactly `y - x` increments are optimal.
- **Already equal:** Equal inputs require zero operations.
