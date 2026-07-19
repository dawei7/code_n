## General
**Treat stopping cells as graph vertices**

A new direction may be chosen only when a roll ends. An edge therefore connects a cell to the last open cell before the next wall in each direction. Merely passing through the destination does not count.

**Precompute horizontal stops**

Scan each row into maximal open segments. Every member of a segment has the same left and right stopping columns, so filling those endpoints touches each cell once.

**Precompute vertical stops**

Scan columns into maximal open segments and similarly record top and bottom endpoints. The four tables then answer every roll in constant time.

**Search the implicit graph**

Breadth-first search starts at `start`, reads four precomputed stops for every visited cell, and enqueues unseen endpoints. The destination is reachable exactly when it is dequeued because every graph edge is one legal complete roll and every legal roll ends at a recorded segment endpoint.

## Complexity detail
The row and column sweeps take $O(rows \cdot cols)$ time. Search visits each open cell at most once and inspects four transitions, preserving that bound. The stop tables, queue, and visited set use $O(rows \cdot cols)$ space.

## Alternatives and edge cases
- **Roll during every search step:** is simpler but repeatedly scans corridors, with a conservative $O(rows \cdot cols \cdot (rows + cols))$ bound.
- **Depth-first search:** has the same bounds with precomputed transitions.
- **Visited cells in a list:** is correct but can make traversal quadratic in reachable stops.
- **Start equals destination:** succeeds without rolling.
- **Pass through destination:** is not enough.
- **Destination beside a wall:** may be a valid stop.
- **Isolated start:** reaches only itself.
- **Corridor cycles:** require visited-state tracking.
