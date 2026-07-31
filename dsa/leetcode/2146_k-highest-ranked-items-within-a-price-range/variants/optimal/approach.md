## General

**Compute every reachable shortest distance**

Run breadth-first search from `start`. All moves have unit cost, so the first
visit to a traversable cell gives its shortest-path distance. Mark cells when
they enter the queue to prevent duplicate work, and never enqueue a wall.

**Record complete ranking tuples**

Whenever a visited cell contains a price in `[low, high]`, record
`(distance, price, row, column)`. A value of `1` is empty rather than an item,
and an out-of-range item remains traversable even though it is not recorded.
The starting cell is examined at distance zero.

Sort all eligible tuples lexicographically. Their field order exactly matches
the four ranking criteria, so the first `k` tuples identify the requested
coordinates. BFS proves every recorded distance is minimal; sorting therefore
produces the required global order.

## Complexity detail

Let $V=mn$ be the number of grid cells. BFS processes each reachable cell and
edge in $O(V)$ time. Sorting at most $V$ eligible items takes
$O(V\log V)$ time, so total time is $O(mn\log(mn))$. The queue, visited set,
and ranking list use $O(mn)$ space.

## Alternatives and edge cases

- **Layer-by-layer sorting:** Sort eligible items within each BFS layer and stop
  once `k` results are secured. This can avoid visiting farther layers while
  preserving the same ranking.
- **Repeated minimum selection:** Selecting the next ranking tuple with a full
  scan is correct but takes $O(V^2)$ time when all cells are eligible.
- **Priority-queue traversal:** A heap ordered by the full rank also works, but
  BFS already supplies distances in layers and has lower queue overhead.
- The starting cell may itself be an eligible item at distance zero.
- Walls block traversal; out-of-range item cells do not.
- Price `1` is empty space and must never be returned.
- If fewer than `k` eligible items are reachable, return every one found.
