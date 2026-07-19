## General
**Translate the Boustrophedon matrix into labels**

Read matrix rows from bottom to top, traversing the bottom row left to right and reversing the column order after every row. Append the encountered cell values to a one-indexed array `cells`. Then `cells[label]` directly tells whether a labeled square has a snake or ladder, avoiding repeated row-and-column conversion during the search.

**Treat each dice roll as an unweighted graph edge**

Every labeled square is a graph vertex. From `curr`, each of the at most six legal roll results creates one edge. Let `next` be the selected label. Its actual destination is `cells[next]` when that value is not `-1`, and `next` otherwise. Do not inspect the destination cell for another transition, because the rules permit only one snake or ladder per roll.

Run breadth-first search from square $1$. The queue processes all positions reached in fewer rolls before positions reached in more rolls, so the first time square $n^2$ is reached gives the least possible number of dice rolls. Mark each actual destination visited when it is enqueued. Reaching the same square later cannot improve its distance, and suppressing those revisits also prevents cycles caused by snakes. If the queue empties without reaching the target, no legal path exists.

Each generated edge matches exactly one legal roll and its mandatory transition. Conversely, every legal roll appears among the six candidates examined from its current square. Breadth-first search therefore explores precisely the game's reachable states in nondecreasing roll count, establishing both the returned minimum and the $-1$ result.

## Complexity detail
There are $n^2$ squares. Flattening visits each cell once, and breadth-first search visits each reachable square once while examining at most six rolls, for $O(n^2)$ time. The flattened board, visited set, and queue each hold at most $n^2$ entries, so auxiliary space is $O(n^2)$.

## Alternatives and edge cases
- **Depth-first search over roll sequences:** It can eventually find routes but does not naturally discover the fewest rolls and may explore exponentially many cyclic paths.
- **Repeated full-board relaxation:** Updating tentative distances until no value changes is correct but can take $O(n^4)$ time over $n^2$ squares.
- **Formula-only movement count:** Dividing the remaining labels by six works only when no snake or ladder changes the graph.
- **Alternating row direction:** Forgetting to reverse every other row attaches transitions to the wrong labels.
- **One transition per roll:** A ladder destination that starts another ladder must not be followed until a later roll lands there directly.
- **Snakes back to visited squares:** The visited set prevents those cycles from making the search infinite.
- **Transition to the target:** Reaching $n^2$ through a snake or ladder finishes the game on that same roll.
- **Unreachable target:** If all possible advances are redirected into an already visited region, return $-1$ after the queue is exhausted.
