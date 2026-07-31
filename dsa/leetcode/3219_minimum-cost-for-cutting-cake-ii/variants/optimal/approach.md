## General

**Charge a boundary once per perpendicular piece.** After some cuts, let $H$ be the number of horizontal pieces and $V$ the number of vertical pieces. A horizontal boundary of cost $a$ contributes $aV$ when processed; a vertical boundary of cost $b$ contributes $bH$.

**Exchange any cheaper-before-expensive inversion.** If these perpendicular cuts are adjacent, horizontal then vertical costs $aV+b(H+1)$, while vertical then horizontal costs $bH+a(V+1)$. The first order is no more expensive precisely when $a\geq b$. Thus an optimal order can always place the larger remaining cost first, regardless of its orientation.

Sort both arrays descending and merge their frontiers. For a horizontal choice, add its cost times the current vertical-piece count and increment $H$; do the symmetric update for a vertical choice. Repeated exchanges transform an optimal order into this greedy order without increasing its cost, proving optimality. Python integers naturally hold the large total; fixed-width implementations require a 64-bit accumulator.

## Complexity detail

Sorting takes $O(m\log m+n\log n)$ time, and merging all $m+n-2$ boundaries takes linear time. The app-local sorted copies require $O(m+n)$ auxiliary space. These bounds remain practical at the $10^5$ dimension limits.

## Alternatives and edge cases

- **Repeatedly search for the largest remaining cost:** This preserves the greedy choice but can take $O((m+n)^2)$ time without sorting or a priority queue.
- **Subrectangle dynamic programming:** It is exact on tiny cakes but its state space is infeasible for dimensions up to $10^5$.
- With one row or one column, all costs in the other orientation are paid exactly once.
- Equal horizontal and vertical costs may be processed in either order.
- The result can exceed a signed 32-bit integer even though every individual cost is at most $10^3$.
