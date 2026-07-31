## General

**A valid move is bounded by two opposite non-enemy values**

The moving army starts at a position containing `1` and ends at a position containing `-1`. Every position strictly between them must contain `0`. Therefore a valid move corresponds exactly to two consecutive nonzero entries in the array whose values differ. If another `1` or `-1` lies between them, the army would cross something other than an enemy fort and the move would be invalid.

**Measure each maximal enemy run once**

Scan from left to right while remembering the index of the most recent nonzero value. Zeros need no immediate action: they simply lengthen the current run of enemy forts.

When the next nonzero value appears, it and the remembered boundary enclose one maximal run of zeros. If their values are `1` and `-1` in either order, the run is capturable and its size is the index gap minus one. Update the maximum. Regardless of whether the boundary types match, make the current position the new remembered boundary because any later valid run must start after it.

Every possible valid move is examined when its right boundary is reached, and no invalid segment is counted because only consecutive nonzero boundaries can have exclusively zeros inside. The largest recorded gap is therefore the maximum number of capturable enemy forts.

## Complexity detail

Let $n = \lvert\texttt{forts}\rvert$. The scan examines each position once, taking $O(n)$ time. It stores only the previous boundary index and the best gap, requiring $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Check every endpoint pair:** Testing all pairs and then validating their interior is correct but takes at least $O(n^2)$ time and can reach $O(n^3)$ with repeated interior scans.
- **Expand from every owned fort:** Walking left and right through adjacent enemy runs is workable, but the single boundary scan expresses the same logic without repeated traversal.
- **No owned fort or no empty position:** No pair of opposite boundaries exists, so the answer remains `0`.
- **Adjacent `1` and `-1`:** The move is valid but crosses zero enemy forts, contributing `0`.
- **Equal boundary values:** Two owned forts or two empty positions cannot serve as the required start and destination, even if enemies lie between them.
- **Direction:** Both `1 ... -1` and `-1 ... 1` are valid because the army may move right or left.
