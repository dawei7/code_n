## General

Each die roll costs one move and creates at most six possible next states. The board therefore defines an unweighted directed graph whose vertices are square labels. Breadth-first search finds the minimum number of edges—dice rolls—from square 1 to square $n^2$.

**Convert a label to matrix coordinates.** Labels begin at the bottom-left and alternate direction row by row. For label `y`, `divmod(y - 1, n)` returns:

- `i`: how many board rows upward from the bottom the label lies;
- `j`: its zero-based offset within that row's labeling direction.

When `i` is odd, that row runs right to left in matrix coordinates, so `j = n - j - 1` reverses the column. Finally `i = n - i - 1` converts the bottom-based row number into the matrix's top-based row index.

This order is important: row parity refers to distance from the bottom, so reversal is decided before replacing `i` with its matrix row.

For example, with $n=6$, labels 1 through 6 have bottom-row offset `i=0` and columns 0 through 5. Labels 7 through 12 have offset `i=1`, so their preliminary columns are reversed: label 7 maps to matrix column 5 and label 12 maps to column 0. Converting the row afterward places them on matrix row 4. This trace helps prevent accidentally computing alternating direction from the top.

**Generate one-roll destinations.** From current label `x`, the die can choose every `y` from `x + 1` through `min(x + 6, m)`, where `m = n * n`. The inclusive Python range uses an upper endpoint one greater, giving exactly those possibilities.

After locating `board[i][j]`:

- if it is `-1`, final state `z` is `y`;
- otherwise the snake or ladder is mandatory, so `z` is the stored destination.

The code does not inspect the board cell at `z` again during the same roll. That correctly follows at most one snake or ladder, even when its destination begins another.

**Visit final states, not landing labels.** The visited set stores `z`. Two different die results can lead through different snake or ladder starts to the same final square; BFS needs to process that resulting state once. Marking only `y` could enqueue the same actual square repeatedly.

**BFS levels equal dice-roll counts.** The queue starts with square 1 and `ans = 0`. The outer loop captures the current queue length and processes exactly one distance layer. All neighbors appended during that layer require one additional roll and are processed only in the next layer. After the layer, `ans` increments.

When square `m` is removed from the queue, `ans` is its shortest distance from square 1. BFS explores all states at smaller roll counts first, so no shorter strategy can remain undiscovered.

**Why revisiting a square is unnecessary.** The rules after arriving at a square depend only on that square, not on the path used. The first BFS arrival is shortest. A later arrival uses at least as many rolls and cannot lead to a better total route, so `vis` safely suppresses it.

If the queue becomes empty before reaching `m`, every reachable state has been exhausted and the answer is `-1`.

The graph may contain cycles after snakes send the player backward, but every queued state is a square label and `vis` admits it only once. Cycles therefore cannot make the search infinite. A snake or ladder destination may also be reachable by an ordinary roll elsewhere; it is still the same state and needs only its earliest BFS arrival.

For the $2\times2$ example, a roll from square 1 may select square 2, whose board entry sends the player to 3. On a board where that destination also starts a ladder to 4, the same roll still ends at 3; only a later roll can activate a transition from another selected landing square.

## Complexity detail

There are $n^2$ square states. Each is enqueued at most once, and processing it examines at most six die outcomes.

- **Time complexity:** $O(n^2)$.
- **Space complexity:** $O(n^2)$ for the queue and visited set.

Coordinate conversion and snake/ladder lookup are constant time per candidate edge.

## Alternatives and edge cases

- **Depth-first search:** It can explore reachability but does not naturally guarantee the fewest rolls without additional distance relaxation.
- **Dijkstra's algorithm:** All moves have equal cost one, so BFS is simpler and faster.
- **Flatten the board first:** Building a label-to-destination array makes BFS coordinate lookup simpler at $O(n^2)$ preprocessing space and time.
- **Follow a chain of ladders in one roll:** Incorrect; only the initially selected destination triggers one snake or ladder.
- **Mark raw die landing as visited:** The meaningful state after a mandatory jump is `z`, which should be deduplicated.
- **Die near the end:** `min(x + 6, m)` prevents labels beyond the board.
- **Snake back to an earlier square:** Visited-state logic handles cycles without infinite traversal.
- **Ladder directly to the final square:** It is enqueued at the next level and returned with the correct one-roll increment.
- **Unreachable target:** Cycles and backward snakes may exhaust the queue, producing `-1`.
- **Alternating row direction:** Odd bottom-based rows reverse columns; even ones do not.
- **Start and final squares:** The contract guarantees neither begins a snake or ladder.
- **Smallest board:** The same coordinate formula and six-outcome cap work for $n=2$.
- **Level counter:** Check for the target when dequeuing before incrementing the next layer, so square 1 correctly has distance zero.
