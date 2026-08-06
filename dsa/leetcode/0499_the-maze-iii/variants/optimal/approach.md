## General

**Precompute every wall-bounded roll endpoint**

Scan each maximal horizontal open segment and write its left and right endpoints into the corresponding cells. Then
do the same for vertical segments to obtain top and bottom endpoints. These monotonic scans take linear grid time and
let every later roll find its wall-bounded destination in constant structural time.

**Let the hole interrupt a roll**

For a proposed direction, begin with the precomputed endpoint. If the hole lies on the same row or column between
the current cell and that endpoint, use the hole instead: the ball falls as soon as it reaches that cell. The absolute
coordinate difference is exactly the number of empty spaces traveled by the roll.

**Order states by both objectives**

Treat stopping cells, together with the hole, as graph vertices. A heap entry is `(distance, path, row, col)`, so
Python orders it first by traveled distance and then by the complete instruction string. The `best` map stores the
smallest `(distance, path)` pair known for each cell. Relax a roll only when its pair is smaller, and discard a popped
entry when it no longer equals the map's current pair.

Every moving edge has positive length. Dijkstra therefore finalizes states in nondecreasing distance, while the
secondary heap key finalizes equal-distance states in lexicographic path order. Consequently, the first current entry
for the hole has both the minimum distance and the smallest instruction string among routes with that distance.

## Complexity detail

Let $V = rows \cdot cols$, and let $P$ be the maximum number of direction characters in a path string retained by
the search. Endpoint preprocessing takes $O(V)$ time. The roll graph has at most $V$ vertices and four outgoing edges
per vertex, so its structural Dijkstra work is $O(V \log V)$ time and $O(V)$ space.

The Python implementation stores full immutable path strings in map values and heap entries. Charging string
construction and comparison by their lengths gives the explicit worst-case bounds $O(VP \log V)$ time and $O(VP)$
space. The shorter structural bounds apply when path-key operations are treated separately from graph operations.

## Alternatives and edge cases

- **Step-by-step rolling during Dijkstra:** is correct, but it may rescan the same corridor from several stopping
  states instead of using constant-time endpoint lookups.
- **Linear frontier selection:** preserves Dijkstra's result but can require quadratic work in the number of reachable
  stopping states.
- **Bellman-Ford relaxation:** handles the nonnegative roll graph correctly but performs repeated full passes that the
  heap avoids.
- **Breadth-first search:** minimizes the number of direction choices rather than traveled distance and therefore
  solves a different objective.
- **Hole before the wall:** replace the ordinary segment endpoint with the hole and stop immediately.
- **Equal distances:** compare complete instruction strings, not merely the next direction.
- **Unreachable hole:** return `"impossible"` after the heap is exhausted.
- **Coincident positions outside the source contract:** the initialization would return the empty string, although
  the source guarantees that `ball` and `hole` start at distinct cells.
