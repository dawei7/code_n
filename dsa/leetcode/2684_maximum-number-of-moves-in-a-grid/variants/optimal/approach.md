## General

All moves advance exactly one column, so reachability can be propagated as a sequence of column frontiers. Every row is initially reachable in column zero because the path may start anywhere there.

For each later column, examine every destination row and its at most three predecessor rows in the preceding column. Add the destination row to the next frontier when at least one predecessor is reachable and has a strictly smaller value. If the new frontier is empty, no path can enter that column, so the maximum number of moves is the previous column index. If every column remains reachable, the answer is `n - 1`.

Inductively, the frontier before processing a column contains exactly the rows reachable in the preceding column. The transition adds a row exactly when one legal move reaches it, preserving that characterization. Therefore the last nonempty frontier identifies the farthest reachable column, and its zero-based column index equals the number of moves.

## Complexity detail

Let $m$ and $n$ be the row and column counts. Each cell checks at most three predecessors, so the running time is $O(mn)$. The current and next row frontiers contain at most $m$ entries, using $O(m)$ space.

## Alternatives and edge cases

- **Right-to-left dynamic programming:** Store the best remaining path length for each row while processing columns backward; this also takes $O(mn)$ time and $O(m)$ space.
- **Separate search from every starting row:** Repeating the same reachability work for all $m$ starts is correct but can take $O(m^2n)$ time.
- **Memoized depth-first search:** Caching each cell gives $O(mn)$ time but uses $O(mn)$ cache space and recursion depth up to $n$.
- **Strict comparison:** Equal adjacent values do not permit a move.
- **Immediate blockage:** If no cell in column one is reachable, return zero.
- **Row boundaries:** Top and bottom rows have only two possible destinations; out-of-range predecessors must be ignored.
