## General

**Each answer is a thresholded connected region**

For a query $x$, scoring cells are exactly the cells in the top-left cell's connected component after excluding every value greater than or equal to $x$. Any path through eligible cells can be walked to score its distinct cells, while no path can cross an ineligible cell. Higher thresholds can only enlarge this component.

**Process thresholds as one growing exploration**

Sort queries together with their original indices. Maintain a minimum heap containing the boundary cells adjacent to the region already counted. The heap key is the cell value. For the current threshold, repeatedly remove the smallest boundary cell while its value is strictly below the threshold, count it, and add each unseen neighbor to the heap. Mark a neighbor seen when it is inserted so every cell enters the heap at most once.

When the heap's minimum is not eligible, no other boundary cell is eligible either. Every path to an unseen cell must first cross this boundary, so the current count is the maximum possible answer. Store it at the query's original index. Because later sorted thresholds are no smaller, the same heap and count remain valid and exploration never restarts.

## Complexity detail

Let $S=mn$ be the number of grid cells and $k$ the number of queries. Sorting queries costs $O(k\log k)$. Each cell is inserted into and removed from the heap at most once, for $O(S\log S)$ traversal time. The total is $O(mn\log(mn)+k\log k)$.

The heap and seen set contain at most $S$ cells, while sorted queries and the answer contain $k$ entries, so auxiliary space is $O(mn+k)$.

## Alternatives and edge cases

- **BFS for every query:** A fresh traversal correctly finds each thresholded component but can revisit all $mn$ cells for every query, costing $O(kmn)$ time.
- **Offline union-find:** Activate cells by increasing value and union active neighbors; this has comparable offline efficiency but needs a separate sorted cell list and component bookkeeping.
- **Strict threshold:** A cell whose value equals the query is ineligible; heap expansion must use `<`, not `<=`.
- **Blocked start:** If `grid[0][0]` is not below the threshold, the answer is `0` even when smaller values exist elsewhere.
- **Unsorted and duplicate queries:** Original indices restore input order, and equal thresholds reuse the same reached count without extra exploration.
- **Low cells behind a barrier:** A numerically small cell cannot score until an eligible path connects it to the start.
