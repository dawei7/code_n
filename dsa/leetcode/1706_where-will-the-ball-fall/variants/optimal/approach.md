## General
**Translate one board into a column transition**

Simulate each starting column independently. When a ball reaches column `column` in a row, its board direction is `row[column]`, so the candidate destination is `next_column = column + row[column]`. A destination outside `[0, n)` means the board points into a wall and the ball's answer is `-1`.

Remaining inside the box is not enough. The neighboring cell must contain a board with the same direction. If `row[next_column] != row[column]`, the two boards slope toward each other and form a `V`, so the ball is trapped. Otherwise the matching pair creates a continuous channel into the next row at `next_column`.

**Preserve the first failed transition**

Process rows from top to bottom until a transition fails or the ball passes the final row. Each successful update gives the ball's only physically possible column in the next row. Inductively, the simulation therefore matches its unique path. A failed wall or `V` transition cannot be bypassed, while a ball that completes all $m$ transitions exits at its final column.

Repeat this deterministic simulation for all $n$ starting columns and append results in their original order.

## Complexity detail
In the worst case, each of the $n$ balls crosses all $m$ rows, for $O(mn)$ time. The returned list stores $n$ exit values and uses $O(n)$ space; the simulation itself needs only constant auxiliary state per ball.

## Alternatives and edge cases
- **Recursive depth-first simulation:** recursion follows the same unique paths but uses up to $O(m)$ call-stack space per active traversal.
- **Memoize cell outcomes:** suffix outcomes can be cached, but valid ball paths do not merge without first encountering a trapping `V`, so this does not improve the worst-case $O(mn)$ bound.
- **Check only the wall:** an in-range move can still be invalid when adjacent boards have opposite signs.
- **Check only the current sign:** a right board followed by a left board, or vice versa, forms a trap and must return `-1`.
- **Single column:** every direction points into a wall, so its only ball is stuck.
- **Immediate `V`:** both balls bordering the opposing pair become stuck in that row.
- **Later trap:** a ball may move successfully through several rows before returning `-1`.
- **Exit indexing:** report the zero-based column below the final row, not the number of horizontal moves.
