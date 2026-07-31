## General

**Separate the independent levels.** A legal operation never moves a value between levels, so the minimum total is the sum of the independent minimum swap counts for each level. Breadth-first traversal visits the tree level by level and records each level's values in their required left-to-right order.

**Turn one level into a permutation.** Because all tree values are unique, sorting the indices by their associated values gives an unambiguous permutation. At sorted position `i`, `order[i]` identifies the original position of the value that belongs there.

Every permutation decomposes into disjoint cycles. A cycle of length $c$ can be fixed in $c-1$ swaps: keep one position as an anchor and place each of the other $c-1$ values. Fewer swaps cannot suffice because one swap can increase the number of correctly separated cycle components by at most one. Sum `cycle_length - 1` over every nontrivial cycle and every level.

The breadth-first grouping matches the definition of a level, and the cycle decomposition gives the exact minimum for the unrestricted swaps permitted within that level. Since levels do not interact, their summed minimum is the global minimum.

## Complexity detail

Let $n$ be the number of nodes and $W$ the maximum level width. Sorting a level of width $w$ costs $O(w\log w)$, while its traversal and cycle scan cost $O(w)$. Summed over all levels, this is $O(n\log W)$ time.

The queue, one level's values, permutation, and visited array contain at most $W$ entries, giving $O(W)$ auxiliary space.

## Alternatives and edge cases

- **Selection-sort each level:** Repeatedly locating the next smallest value counts valid swaps but takes $O(W^2)$ time on a wide reversed level.
- **Value-to-index swap simulation:** Sorting a copy and maintaining each value's current index also reaches the minimum in $O(W\log W)$ time; cycle decomposition avoids mutating the level values.
- **Already sorted level:** Every permutation entry is a fixed point, so the level contributes zero.
- **Single-node level:** Its only permutation cycle has length one and needs no operation.
- **Sparse tree:** Breadth-first queue order still records only existing nodes from left to right at each level.
- **Unique values:** Uniqueness makes the strictly increasing target and its permutation unambiguous; no duplicate tie policy is needed.
