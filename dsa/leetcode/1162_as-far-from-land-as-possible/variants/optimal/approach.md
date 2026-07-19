## General
**Start from every land cell at once.** Put all land coordinates into one breadth-first queue and mark them visited. This is a multi-source search: level zero contains every possible nearest-land origin rather than choosing one land cell and repeating a search.

**Expand equal distances together.** Each queue layer reaches the unvisited orthogonal neighbors of the preceding layer. Moving one step up, down, left, or right increases Manhattan distance by exactly one. Therefore, the first time a water cell is reached, the current BFS depth is the length of its shortest path to any land cell—and hence its nearest-land Manhattan distance.

Continue until no cells remain. The last newly reached water layer has the largest of these nearest-land distances, so its depth is the answer. Every cell is marked before it is enqueued, preventing duplicate work from different land sources. Before expansion, reject an empty initial queue (all water) and a queue containing all $n^2$ cells (all land), both of which require `-1`.

## Complexity detail
The initialization scans all $n^2$ cells. Each cell is then enqueued at most once and checks four neighbors, so the search also costs $O(n^2)$ time. The visited matrix and queue can each hold $O(n^2)$ entries in the worst case, giving $O(n^2)$ auxiliary space.

## Alternatives and edge cases
- **Search from every water cell:** Scanning all land cells for each water cell is direct but can require $O(n^4)$ time.
- **Run one BFS per land cell:** This repeats most grid exploration and can also become quartic.
- **Two-pass dynamic programming:** Forward and backward distance passes achieve $O(n^2)$ time, but require careful initialization and boundary handling.
- **All water:** With no land source, nearest-land distance is undefined and the result is `-1`.
- **All land:** There is no water cell to choose, so the result is also `-1`.
- **Diagonal cells:** Diagonal movement is not allowed; a diagonal offset of one row and one column contributes distance $2$.
