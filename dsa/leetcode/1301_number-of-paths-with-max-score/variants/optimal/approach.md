## General
**Store two values for each cell**

For each coordinate, maintain the maximum digit sum obtainable from `S` to that cell and the number of paths producing that sum. An unreachable cell has score `-1` and zero ways. Initialize `S` with score 0 and one way.

Process rows and columns from bottom-right toward top-left. The only possible predecessors of cell $(r,c)$ in this order are the cells below it, to its right, and diagonally below-right. Inspect the reachable predecessor scores and keep their maximum. When one predecessor improves the maximum, replace both the best score and its path count. When another predecessor ties that score, add its count modulo $10^9+7$.

If at least one predecessor is reachable, add the current digit to the best score; `E` contributes zero. Obstacles remain unreachable. Because every legal path into the cell must end at exactly one of those three predecessors, selecting their greatest score produces the optimal score for the cell, and summing only tied predecessor counts counts precisely the paths achieving it.

The movement graph is acyclic: every move decreases at least one coordinate. Therefore the reverse coordinate order resolves every dependency once. Reachability must be tested with the score sentinel rather than the reduced path count: a reachable cell can legitimately have zero ways modulo $10^9+7$. If `E` retains score $-1$, no route exists; otherwise its stored pair is the requested result.

## Complexity detail
The board contains $n^2$ cells, and each cell examines at most three predecessors. The total time is $O(n^2)$. The score and path-count tables each contain $n^2$ entries, using $O(n^2)$ auxiliary space.

## Alternatives and edge cases
- **Step-indexed dynamic programming:** Tracking every exact path length is correct, but scans the board for up to $2n-2$ steps and takes $O(n^3)$ time.
- **Priority-queue topological traversal:** Processing reachable cells by decreasing coordinate rank is correct, but heap operations raise the cost to $O(n^2 \log n)$.
- **Immutable anti-diagonal snapshots:** Flattening fresh score and count tables through repeated list concatenation before every coordinate rank remains correct, but can take $O(n^4)$ time.
- **Depth-first path enumeration:** Exploring complete paths without memoized score/count aggregation can require exponentially many calls.
- **Tied predecessor scores:** Add all corresponding path counts; do not keep just one predecessor.
- **Lower-scoring paths:** They must not contribute to the count even when they reach the same cell.
- **Direct diagonal route:** It is legal when the destination is not an obstacle, even if the orthogonally adjacent cells are blocked.
- **No route to `E`:** Return `[0,0]`, not a negative score.
- **Large path counts:** Apply the modulus whenever tied counts are combined.
- **Zero count after reduction:** A reachable maximum-score path family may contain an exact multiple of $10^9+7$ paths, so a returned count of 0 does not imply that the board is unreachable.
