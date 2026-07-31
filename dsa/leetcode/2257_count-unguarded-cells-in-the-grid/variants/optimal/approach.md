## General

**Encode blockers before propagating sight**

Build a grid whose states distinguish empty cells, guards, walls, and cells
already known to be watched. Guards and walls must remain distinguishable
because encountering a guard begins visibility beyond it, whereas encountering
a wall ends visibility. A watched cell remains transparent in every later
sweep.

**Turn each sight line into a directional sweep**

Scan every row from left to right while carrying a `visible` flag. A guard sets
the flag, a wall clears it, and an ordinary cell is marked watched whenever the
flag is set. Repeat from right to left to cover westward sight. Apply the same
two scans top-to-bottom and bottom-to-top in every column.

For any direction, the flag is true at a cell exactly when the nearest blocker
behind it in that scan direction is a guard. Therefore that directional pass
marks exactly the cells visible from a guard on that side. Combining all four
passes marks the union of north, east, south, and west visibility. Because
watched cells never act as blockers, an earlier mark cannot hide a later line
of sight.

After the sweeps, only cells still in the empty state are both unoccupied and
unseen. Counting those cells yields exactly the requested result.

## Complexity detail

Let $G=\lvert\texttt{guards}\rvert$ and
$W=\lvert\texttt{walls}\rvert$. Initializing and scanning the grid takes
$O(mn)$ time, and placing all blockers takes $O(G+W)$, for
$O(mn+G+W)$ total time. The state grid uses $O(mn)$ auxiliary space.

## Alternatives and edge cases

- **Check every guard for every empty cell:** This directly follows the definition but can require $O(mnG(m+n))$ work when line-of-sight checks also walk between coordinates.
- **Cast four rays from each guard:** This is often concise and can be efficient, but repeated visits require more delicate amortized reasoning than fixed grid sweeps.
- **Sets of guarded coordinates:** Sparse sets avoid a dense state matrix but still need blocker-aware ordering in every row and column.
- **Guard as blocker:** A guard stops sight from the other side yet begins its own sight beyond that coordinate.
- **Wall as blocker:** No visibility passes through a wall.
- **Multiple sight lines:** A cell remains guarded regardless of how many guards see it.
- **Occupied cells:** Guards and walls are never counted as guarded or unguarded empty cells.
- **One-row or one-column grid:** The same paired sweeps work without a special case.
- **Fully guarded grid:** The result may be zero.
