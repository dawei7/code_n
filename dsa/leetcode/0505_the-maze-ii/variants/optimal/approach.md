## General

**Turn complete rolls into weighted edges**

The ball may choose a direction only while stopped. Treat each reachable stopping cell as a graph vertex and each
complete roll as an edge to another stopping cell. The edge weight is the number of cells crossed, so the sum of a
route's edge weights is exactly the distance defined by the problem. Passing through the destination does not create
a vertex visit; the ball must end a roll there.

**Precompute all four wall-bounded endpoints**

Sweep every row from left to right. An open cell shares its predecessor's left endpoint when that predecessor is
open; otherwise the cell begins a new segment. A reverse sweep gives right endpoints, and the corresponding column
sweeps give up and down endpoints. The four tables make every later roll transition and its coordinate distance
available in constant time.

**Run Dijkstra over stopping cells**

Initialize the start cell's distance to zero and store `(distance, row, col)` in a min-heap. When a current entry is
popped, relax the four precomputed endpoints. A shorter route replaces that endpoint's distance and adds a new heap
entry; an entry whose distance no longer matches the table is stale and is discarded.

Every moving roll has positive weight. Dijkstra therefore finalizes stopping cells in nondecreasing route distance,
so the first current entry for the destination is optimal. Conversely, every legal sequence of rolls is a path in
this graph. If the heap empties without finalizing the destination, no valid stopping route reaches it.

**Why the finite sentinel is safe**

The code uses `2 * rows * cols` as its unreachable value. A shortest route can be chosen without repeating a
stopping vertex and therefore without repeating a maximal horizontal or vertical segment edge. The total lengths of
all such distinct edges equal the number of open horizontal adjacencies plus open vertical adjacencies, which is
strictly less than `2 * rows * cols`. Thus every finite shortest distance is below the sentinel.

## Complexity detail

Let $V = rows \cdot cols$. The four endpoint sweeps take $O(V)$ time. The stopping-cell graph has at most $V$
vertices and four outgoing edges per vertex, so heap-based relaxation takes $O(V \log V)$ time. The endpoint tables,
distance table, and heap use $O(V)$ space.

## Alternatives and edge cases

- **Step-by-step rolling during Dijkstra:** is correct and common, but it may rescan the same long corridor from
  several stopping states.
- **Linear-scan Dijkstra:** preserves correctness but can spend quadratic time repeatedly selecting the next
  unsettled cell.
- **Breadth-first search:** minimizes the number of rolls, not the sum of their unequal traveled lengths.
- **Queue-based repeated relaxation:** can converge to the correct distances but lacks Dijkstra's efficient
  nondecreasing-distance finalization.
- **Pass through the destination:** does not count unless a wall makes the ball stop there.
- **Unreachable destination:** return `-1` after the heap is exhausted.
- **Zero-length direction:** an endpoint equal to the current cell cannot improve its distance and adds no heap
  entry.
- **Coincident positions outside the source contract:** initialization would return `0`, although the source
  guarantees distinct starting and destination cells.
