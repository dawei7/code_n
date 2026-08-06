## General

**Search stopping positions rather than crossed cells**

The ball can choose a direction only where a wall ends its previous roll. Model each reachable stopping cell as a
graph vertex. Its four outgoing edges lead to the last empty cells before the nearest walls in the four directions.
This model deliberately excludes an intermediate destination that the ball cannot stop on.

**Precompute horizontal roll endpoints**

For each row, scan maximal contiguous segments of zeroes. If a segment spans columns `segment_start` through
`segment_end`, every member has the same left and right stopping columns. Fill `left_stop` and `right_stop` for all
members of that segment. The scan advances monotonically and assigns each empty cell once.

**Precompute vertical roll endpoints**

Perform the analogous scan down each column. Fill `top_stop` and `bottom_stop` with the first and last rows of every
vertical empty segment. The four tables now answer a complete roll from any empty cell in constant time.

**Run breadth-first search on the implicit graph**

Convert `start` and `destination` to tuples. Initialize `queue` and `visited` with the start cell. For each dequeued
`(row, col)`, return `True` if it is the target; otherwise read its four endpoints from the stop tables and enqueue
each unseen tuple. If the queue empties, no sequence of legal stopping positions reaches the destination.

Every enqueued neighbor is the endpoint of one valid complete roll. Conversely, the segment tables contain the
endpoint of every direction the ball can choose at every reachable stop. Breadth-first search therefore visits
exactly the graph-reachable stopping cells, proving that it returns `True` precisely when the ball can stop at the
destination.

## Complexity detail

Let `rows` and `cols` be the maze dimensions. The horizontal and vertical sweeps each touch every cell a constant
number of times, for $O(\text{rows} \cdot \text{cols})$ preprocessing time. Search visits at most every empty cell and
reads four constant-time transitions, preserving the same total time bound.

The four endpoint tables, queue, and visited set use $O(\text{rows} \cdot \text{cols})$ space.

## Alternatives and edge cases

- **Roll during each search expansion:** avoids four tables but may rescan the same corridors from many stops, with
  a conservative $O(\text{rows} \cdot \text{cols} \cdot (\text{rows} + \text{cols}))$ time bound.
- **Depth-first search:** reaches the same stop-position graph and has the same asymptotic bounds when using the
  precomputed transitions.
- **Visited coordinates in a list:** preserves correctness but can make membership checks quadratic in the number of
  reachable stopping cells.
- **Pass through the destination:** does not succeed unless a wall makes the destination a roll endpoint.
- **One-cell segment:** its two endpoints are the cell itself; visited-state tracking suppresses self-loop repeats.
- **Isolated start:** the four transitions are self-loops, so only the start is reachable.
- **Corridor cycles:** the hash set ensures that each stopping cell enters the queue once.
- **Distinct start and destination:** the source guarantees they differ, although the graph search would also handle
  equality immediately.
