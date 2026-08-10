## General

Ranking begins with shortest-path distance from `start`. Walls make Manhattan distance insufficient, but every legal movement has equal cost one. Breadth-first search is therefore the correct way to discover each reachable cell at its minimum distance.

The exact solution separates the work into two phases: BFS records every reachable eligible item with its complete ranking tuple, then an ordinary sort orders those tuples.

**Initialize the BFS frontier**

The starting coordinates are unpacked as `row, col` and placed into `q = deque([(row, col)])`. If the start cell’s value lies between `low` and `high` inclusive, the code records tuple

`(0, grid[row][col], row, col)`.

The first component is distance zero, followed by price, row, and column—the ranking criteria in their exact priority order.

The source then assigns `grid[row][col] = 0`. A zero represents a wall to the traversal, so this mutation also serves as the visited marker. Marking on insertion, rather than when removed from the queue, prevents another neighbor from enqueuing the same cell twice.

**Traverse one distance layer at a time**

The variable `step` begins at zero. At the start of each outer `while q` iteration, it is incremented. The inner loop runs exactly `len(q)` times using the queue length captured before processing that layer. Those queue entries all have the same current distance; their newly discovered neighbors are one step farther and therefore receive the new `step` value.

This is the standard BFS layer invariant:

- the starting cell is handled separately at distance zero;
- before an outer iteration processes a layer, `step` becomes the distance of every newly discovered neighbor;
- because the queue is first-in, first-out, no longer path can discover a cell before its shortest path does.

**Generate the four neighbors**

The direction tuple is `(-1, 0, 1, 0, -1)`. Applying `pairwise(dirs)` produces

`(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`,

which are up, right, down, and left. For each candidate `nx, ny`, the condition checks both grid bounds and `grid[nx][ny] > 0`. Positive cells are passable, whether they contain empty-space value one or an item price above one. Zero cells are either original walls or cells already visited.

If the cell’s current value is inside the inclusive price range, its tuple `(step, price, nx, ny)` is appended to `pq`. The value must be read before the next assignment because `grid[nx][ny] = 0` erases it. The cell is then marked visited and enqueued so exploration may continue through it.

Although the variable is named `pq`, it is a normal Python list, not a priority queue.

**Sort by the complete ranking tuple**

After BFS has visited the entire reachable region, `pq.sort()` uses Python tuple ordering. Tuples are compared lexicographically:

1. smaller distance first;
2. on equal distance, smaller price first;
3. then smaller row;
4. finally smaller column.

That exactly matches the problem’s ranking definition. The result expression `[list(x[2:]) for x in pq[:k]]` takes at most the first `k` sorted candidates, discards distance and price, and converts each coordinate pair from a tuple slice to the required list form.

If fewer than `k` eligible reachable items exist, `pq[:k]` simply returns all of them.

**Why the two phases are correct**

BFS records each reachable cell once at its shortest distance. Every eligible item is recorded because traversal may pass through item cells, and every recorded item satisfies the price range. Sorting these complete, accurate ranking keys produces exactly the global requested order. Taking the first `k` therefore returns the highest-ranked items and no unreachable or out-of-range cell.

## Complexity detail

Let $N=mn$ be the number of grid cells and let $q$ be the number of reachable items within the price range. BFS visits each reachable non-wall cell once and inspects four directions, costing $O(N)$ in the worst case. Sorting the candidate list costs $O(q\log q)$, which is at most $O(N\log N)$. Total time is $O(N+q\log q)$, conventionally bounded by $O(mn\log(mn))$.

The queue may hold $O(N)$ cells, and `pq` may store $O(q)$ tuples. Python’s sort also uses auxiliary memory. Peak auxiliary space is $O(N)$.

The output contains at most `k` coordinate pairs. The exact implementation mutates `grid` in place to mark visits, so it avoids a separate visited matrix but destroys the original positive values in the reachable region.

## Alternatives and edge cases

- **Layer-by-layer candidate sorting:** Collect eligible items in one BFS distance layer, sort that layer by price, row, and column, and stop after collecting `k`. This can avoid exploring and sorting farther layers once enough results are known, but it is not the exact source.
- **Priority queue over ranking keys:** A heap can combine exploration and ranking, but ordinary BFS plus one sort is simpler because distance is already generated in layers.
- **Separate visited matrix:** This preserves `grid` at the cost of $O(mn)$ additional booleans. The exact code reuses zero as a visited marker.
- **Manhattan distance:** Walls may force detours or make a cell unreachable, so coordinate distance alone is incorrect.
- **Starting cell is an item:** It is recorded at distance zero before its value is overwritten, provided its price is within range.
- **Starting cell has value one:** Since `low >= 2`, it is traversable empty space but never an eligible item.
- **Unreachable in-range item:** BFS never visits it, so it correctly does not appear in `pq`.
- **Reachable out-of-range item:** It is not recorded but remains traversable, so BFS can continue through it.
- **Wall:** Value zero is neither recorded nor enqueued.
- **Equal distance and price:** Row, then column, resolve the tie through tuple ordering.
- **Fewer than k items:** Python slicing returns the entire shorter list without padding.
- **More than k items:** Sorting all candidates is more work than strictly necessary, but `pq[:k]` returns exactly the requested prefix.
- **Mark when enqueued:** This ensures one queue entry and one candidate tuple per cell, even when several shortest paths reach it.
- **Grid mutation:** All reachable positive cells become zero, including item prices. Callers needing the original map must provide a copy.
- **Direction construction:** `pairwise` over the five-number tuple yields exactly four orthogonal moves and no diagonal move.
