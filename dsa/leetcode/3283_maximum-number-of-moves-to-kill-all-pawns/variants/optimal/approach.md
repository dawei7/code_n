## General

**Separate movement geometry from capture choices**

Other pawns do not block movement and are not captured when passed, so the shortest distance between two relevant cells never changes during the game. Treat the initial knight cell and all pawn cells as points. Run breadth-first search on the bounded $50\times50$ board from each point and record its distance to every other point.

Using board BFS is material near edges and corners. An unrestricted infinite-board formula can use paths that temporarily leave the legal board; for example, `(1, 1)` to `(0, 0)` takes four moves on this board.

**Memoize the alternating game state**

A game state consists of the knight's current point and a bitmask of remaining pawns. The number already removed determines whose turn it is, so no separate turn flag is needed. Initially zero pawns have been removed and Alice maximizes.

For every set bit, add the precomputed distance to that pawn to the optimal value of the state with that bit removed and the knight relocated there. Alice takes the maximum of these totals; Bob takes the minimum. The empty mask returns zero.

The recurrence considers every legal selected pawn. Its edge cost is exactly the mandated shortest capture distance, and its child state exactly describes the resulting board. Induction on the number of remaining pawns therefore gives the optimal continuation for both players. Memoization merges histories that reach the same current pawn with the same remaining set.

## Complexity detail

There are at most $p+1$ breadth-first searches over $B=2500$ cells, costing $O(pB)$ time and $O(B)$ traversal space. The minimax has $O(p2^p)$ reachable `(current, remaining)` states and examines up to $p$ choices per state, costing $O(p^2 2^p)$ time and $O(p2^p)$ memo space. The small distance matrix is covered by these bounds.

## Alternatives and edge cases

- **Uncached minimax:** Enumerating every capture order is correct but repeats subset states and grows as $O(p!)$.
- **Always choose the farthest or nearest pawn:** A locally extreme distance can place the knight favorably for the opponent, so neither greedy rule models optimal play.
- **Use infinite-board knight distance:** Boundary-forbidden intermediate cells can make that distance too small near corners.
- A pawn crossed en route remains available because only the selected pawn is captured.
- With one pawn, the answer is its bounded-board shortest distance from the knight.
- Alice maximizes on turns after an even number of captures; Bob minimizes after an odd number.
- Pawn coordinates are unique, but distinct pairs can have equal knight distances.
- Edge-separated cells still require every intermediate move to remain on the fixed board.
- The knight's current cell after a turn is exactly the captured pawn's former cell.
