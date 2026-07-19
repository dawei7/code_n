## General
**Mark one complete island.** Find the first land cell and run depth-first or breadth-first search through its four-directional land neighbors. Mark every cell of this first island as visited and place all of them into a queue. Using the whole island as the initial frontier allows the bridge to begin from whichever shoreline cell is best.

**Expand through water in distance layers.** Run a multi-source breadth-first search from that queue. Unvisited water neighbors are marked and enqueued with distance one greater than their predecessor. The distance assigned to a water cell is exactly the minimum number of flips needed to connect it to the first island, because breadth-first search explores all positions requiring fewer flips before any position requiring more.

**Stop at the second island.** When expansion first reaches an unvisited land cell, that cell belongs to the other island. Return the distance of the cell from which it was reached: it counts precisely the intervening water cells, while neither original land endpoint needs a flip. Breadth-first ordering proves minimality—any bridge with fewer flips would have reached the second island in an earlier layer. Marking cells when they enter the queue prevents repeated work and leaves the input unchanged.

## Complexity detail
The island-marking traversal and bridge expansion each visit any grid cell at most once and inspect four neighbors, so the total time is $O(n^2)$. The visited matrix, island frontier, and breadth-first queue can each hold $O(n^2)$ cells.

## Alternatives and edge cases
- **Pairwise island-cell distances:** Label both islands and minimize Manhattan distance minus one over every cross-island cell pair. This is correct but may require $O(n^4)$ time when both islands contain quadratic area.
- **Start BFS from only one shoreline cell:** This can miss a shorter bridge beginning elsewhere; all first-island cells or all boundary cells must seed the search.
- **Diagonal islands:** Diagonal adjacency is not connectivity, but one intervening orthogonal water flip may connect the cells.
- **Nested islands:** One island may surround the other with a water ring; multi-source expansion still finds the ring's minimum thickness.
- **Visited timing:** Mark a water cell when enqueuing it, not when removing it, to avoid adding the same cell from several frontier cells.
