## General

**Describe a complete cutting order by its orientations.** Once some horizontal and vertical boundaries have been processed, there are `horizontal_pieces` row bands and `vertical_pieces` column bands. Processing a horizontal boundary now costs its stored value once per current column band; a vertical boundary similarly costs its value once per current row band.

**Put an expensive boundary before a cheaper perpendicular boundary.** Consider adjacent choices with horizontal cost $a$ and vertical cost $b$. If horizontal comes first, their contribution is $aV + b(H+1)$; in the opposite order it is $bH + a(V+1)$, where $H$ and $V$ are the current piece counts. The first order is no more expensive exactly when $a \geq b$. Therefore, any inversion that places a cheaper cut before a more expensive perpendicular cut can be exchanged without increasing the cost.

Sort both cost arrays in descending order and merge them from largest to smallest. Charge a horizontal cost by the current number of vertical pieces, then increment the horizontal-piece count; handle a vertical cost symmetrically. The exchange argument transforms an optimal order into this greedy order, proving that the resulting total is minimum. Equal costs may be processed in either orientation.

## Complexity detail

Sorting the $m-1$ horizontal and $n-1$ vertical costs takes $O(m\log m+n\log n)$ time. The merge is linear in the number of boundaries. The sorted copies use $O(m+n)$ auxiliary space in the app-local implementation.

## Alternatives and edge cases

- **Rectangle interval dynamic programming:** Minimizing every subrectangle is correct for these small bounds, but it uses many more states and split transitions than the greedy exchange property requires.
- **Process the cheapest cost first:** This multiplies expensive perpendicular cuts across more pieces and can be strictly suboptimal.
- When $m=1$, there are no horizontal boundaries and every vertical cost is paid once; the symmetric rule holds when $n=1$.
- Equal costs can be taken in either order because the two local-order totals are equal.
- Cost arrays need not already be sorted, and their original line positions do not affect the total once every boundary must be used.
