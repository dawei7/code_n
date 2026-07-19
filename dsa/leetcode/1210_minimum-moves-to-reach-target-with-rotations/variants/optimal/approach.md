## General
**Encode position and orientation together.** Represent a state as `(r, c, orientation)`, where `(r, c)` is the snake's upper or left pivot cell and `orientation` is horizontal or vertical. This identifies both occupied cells; coordinates alone would confuse configurations with different legal next moves.

**Generate only geometrically legal neighbors.** From a horizontal state, moving right checks the new rightmost cell. Moving down and rotating clockwise both require the two cells below the snake to be empty. From a vertical state, moving down checks the new bottom cell. Moving right and rotating counterclockwise both require the two cells to its right to be empty. Bounds are checked before grid access.

**Use breadth-first search for the minimum.** Begin with the horizontal state at `(0, 0)` in a queue and visited set. Every edge is exactly one move, so BFS removes every state at distance $d$ before any state at distance $d+1$. The first removal of the horizontal target therefore has minimum distance. Marking states when enqueued prevents cycles caused by reversing translations or rotations.

There are at most two orientations for each pivot cell. If the queue empties without the target, every reachable configuration has been explored and no valid sequence exists.

## Complexity detail
At most $2n^2$ states exist, and each produces at most three constant-time transition checks. Hash-set membership is expected $O(1)$, so total time is $O(n^2)$. The queue and visited set each hold at most $O(n^2)$ states.

## Alternatives and edge cases
- **Depth-first search over paths:** DFS can establish reachability but does not produce the minimum without exploring and comparing many paths.
- **BFS with a list for visited states:** It remains correct, but linear membership checks can raise total time to $O(n^4)$.
- **Dijkstra's algorithm:** It gives the same distances, but all moves have unit cost, so a priority queue adds unnecessary overhead.
- **Track occupied cells without orientation:** Normalizing cell pairs works, but explicit orientation makes rotations and target comparison clearer.
- **Blocked target cell:** The target configuration is unreachable and the search returns `-1`.
- **Open grid:** Translations alone can reach the target, although rotations create extra states.
- **Rotation clearance:** Both cells in the swept $2\times2$ area must be empty, not only the new endpoint.
- **Two-by-two grid:** One downward move reaches the target without a special case.
