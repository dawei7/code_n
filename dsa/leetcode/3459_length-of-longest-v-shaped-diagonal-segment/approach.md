## General

**Start only from cells containing \(1\).** Every valid segment begins with $1$, then must follow $2,0,2,0,\ldots$. The outer loops inspect every `grid[i][j] == 1` and try all four diagonal starting directions.

The direction tuple encodes offsets:

$$
(1,1),(1,-1),(-1,-1),(-1,1).
$$

In grid coordinates where row increases downward, advancing direction index by one modulo four is the required clockwise diagonal turn.

**Define what the memoized function returns.** `dfs(i, j, k, cnt)` assumes cell $(i,j)$ is already part of the segment. It returns the maximum number of additional cells that can follow, moving initially in direction `k`. `cnt` is one when the single turn remains available and zero after it has been used.

The next coordinates are computed immediately. The expected next value depends on the current cell:

- after $1$, expect $2$;
- after $2$, expect $0$;
- after $0$, expect $2$.

The expression `2 if grid[i][j] == 1 else (2 - grid[i][j])` implements these cases.

If the next cell is outside the matrix or does not match, no additional cell is possible and the function returns zero.

**Continue straight or spend the turn.** Once a valid next cell $(x,y)$ is found, one option continues in the same direction:

`dfs(x, y, k, cnt)`.

If a turn remains, the other option makes the next edge after $(x,y)$ use direction `(k + 1) % 4` and passes zero turns:

`dfs(x, y, (k + 1) % 4, 0)`.

The maximum of these options is increased by one to count $(x,y)$ itself.

This placement of the direction change correctly treats $(x,y)$ as the turning vertex: the edge into it follows the old direction, while the following edge uses the new direction.

For example, imagine a path that starts at a $1$, moves down-right to a $2$, and then turns down-left toward a $0$. The call at the starting $1$ first validates and enters the down-right $2$. The turned recursive call is then made from that $2$ with the down-left direction. Consequently, the next checked cell is the down-left neighbor of the $2$. Changing direction before entering the $2$ would instead look for a different neighbor and move the corner one cell too early. This counting and direction convention is a small implementation detail, but it is essential to matching the geometric definition.

The outer caller adds one more for the starting $1$. A one-cell grid therefore yields length one even though every DFS continuation returns zero.

**Memoization controls repeated work.** Many starting cells and paths request the same combination of cell, direction, and remaining-turn flag. `@cache` computes each state once. The next expected value need not be a state dimension because it is uniquely determined by the current grid value.

The state also does not need to remember the starting cell or the length already traveled. Once the recursion is at $(i,j)$, future possibilities depend only on that location, its outgoing direction, and whether a turn remains. Any two prefixes reaching the same state have exactly the same best continuation. The function returns an additional length rather than a total length precisely so that this reusable suffix answer is independent of how long either prefix was.

For a straight sequence, the DFS repeatedly takes the unchanged-direction branch. At any eligible cell it may compare that with turning clockwise. Counterclockwise turns and multiple turns are never generated.

**Why every valid V is considered.** A segment is determined by its starting $1$, initial direction, and either no turn or one turning vertex. The outer loops enumerate the first two choices. Along that route, the DFS reaches each possible valid turning vertex while preserving the required value sequence and considers spending the turn there. Thus every legal segment is a recursion alternative.

Every recursion alternative moves diagonally to a matching next value and changes direction at most once clockwise, so no invalid segment is counted. Maximizing across states and starts returns the global longest length.

The alternation check prevents a visually V-shaped route with the wrong values from being counted. The geometry alone is insufficient: after the initial $1$, the value sequence must be $2,0,2,0,\ldots$ across both legs without restarting at the corner. Because the expected value is derived from the current cell after every move, turning changes only direction; it never resets or skips the alternating sequence.

The four fixed directions after a turn cannot cycle back to the same state: before and after the optional turn, movement proceeds monotonically along one diagonal direction until a boundary or mismatch.

## Complexity detail

There are $mn$ cells, four directions, and two turn flags, for $O(mn)$ cached states. Each performs constant work and at most two cached calls. Total time is $O(mn)$.

The cache uses $O(mn)$ space. Recursion depth is bounded by the number of cells along two diagonal legs, $O(m+n)$, and is dominated by the cache. Total auxiliary space is $O(mn)$, matching the manifest.

The outer loops make $4mn$ initial calls in the worst case, but cached calls that repeat a state return in constant time. There are at most $8mn$ distinct tuples because direction has four choices and the turn flag has two. These constant factors disappear from big-O notation, while still explaining why the state space does not multiply by the possible path lengths.

## Alternatives and edge cases

- **Start from every cell regardless of value:** Only $1$ can begin a valid segment, so other starts are useless.
- **Track expected value separately:** It is redundant because current values determine the next alternating target.
- **Allow direction \((k-1)\):** That is the opposite rotation and violates the clockwise-only rule.
- **Turn twice:** Passing `cnt = 0` after a turn prevents it.
- **No turn:** The straight branch preserves `cnt` and can reach the end without using it.
- **Single-cell segment:** A lone $1$ is valid and counted by the outer `+1`.
- **Mismatch after \(1\):** DFS returns zero, leaving length one.
- **Several starting ones:** Cache sharing still keeps total state count linear in grid size.
- **Rectangular grid:** Separate `m` and `n` bounds handle unequal dimensions.
- **Recursion depth:** Very long diagonals may approach runtime recursion limits; an iterative DP could avoid that operational concern while using the same states.
