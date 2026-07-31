## General

**Take the easiest available collision first**

Sort asteroid masses in ascending order. Scan them while maintaining the
planet's current mass. If the planet can destroy the current asteroid, add
that mass and continue. If it cannot, return false immediately.

Suppose some successful ordering exists while the smallest remaining asteroid
$x$ has not been chosen. Its next chosen asteroid $y$ satisfies $x\le y$. If
the planet can destroy $y$, it can also destroy $x$. Swapping $x$ before $y$
cannot hurt: after absorbing $x$, the planet has at least as much mass for the
collision with $y$ as it had before. Repeating this exchange transforms any
successful ordering into ascending order.

Therefore, if the ascending scan fails at mass $x$, every remaining asteroid
is at least $x$ and no alternative next collision is possible. If it finishes,
the scan itself supplies a valid order. This proves the greedy test is both
necessary and sufficient.

## Complexity detail

Sorting $n$ asteroid masses takes $O(n\log n)$ time, and the scan takes
$O(n)$. The sorted copy uses $O(n)$ space; the running mass uses $O(1)$ more.

## Alternatives and edge cases

- **Min-heap:** Heapify all asteroids and repeatedly remove the smallest. This
  also takes $O(n\log n)$ time and $O(n)$ space.
- **Repeated linear minimum search:** Find and delete the lightest remaining
  asteroid without sorting. This is correct but takes $O(n^2)$ time.
- **Try every collision order:** Permutation search is factorial and ignores
  the exchange argument.
- A planet may destroy an asteroid of exactly equal mass.
- If the smallest asteroid is initially too heavy, no ordering can succeed.
- Duplicate asteroid masses are processed independently.
- The running planet mass can exceed the individual input bounds, so
  fixed-width implementations may need wider integer arithmetic.
