## General

**Remoteness is constant within a connected component.** Model every nonblocked cell as a graph node and join side-adjacent nonblocked cells. Two cells are mutually reachable exactly when they belong to the same connected component. If the sum of all positive values is $T$ and one component has value sum $S$, then every cell in that component has remoteness $T-S$: precisely the values outside the component are unreachable.

**Aggregate a whole component at once.** First compute $T$. Scan the matrix, and whenever an unvisited nonblocked cell appears, run an iterative depth-first traversal. During that traversal, accumulate the component sum $S$ and its number of cells $c$. Since all $c$ cells share remoteness $T-S$, the component contributes

$$
c(T-S)
$$

to the requested total. Add this value after the traversal and continue scanning for the next component.

The visited matrix makes the components disjoint: a nonblocked cell is added to exactly one traversal. Each traversal reaches every and only side-connected cell, so its recorded $S$ and $c$ describe one complete graph component. The formula then includes every value outside that component and none inside it for each of its cells. Summing the component contributions therefore counts exactly every cell's defined remoteness, while blocked cells contribute nothing.

## Complexity detail

There are $n^2$ matrix positions. The initial sum and outer scan inspect each position once, and every nonblocked cell is removed from a traversal stack once with four constant-time neighbor checks. Total time is $O(n^2)$. The visited matrix and worst-case traversal stack each require $O(n^2)$ auxiliary space.

## Alternatives and edge cases

- **Union-find:** Unite side-adjacent nonblocked cells, then aggregate size and sum by representative. This also runs in near-$O(n^2)$ time but needs more bookkeeping than a direct traversal.
- **Recompute reachability from every cell:** A separate DFS or BFS for each nonblocked cell is correct, but it can revisit the whole matrix $n^2$ times and take $O(n^4)$ time.
- **Mutate the input as the visited marker:** Replacing processed values with `-1` removes the Boolean matrix, but the original positive values must be accumulated before mutation and callers may expect the input to remain unchanged.
- **All cells blocked:** The global sum is zero, no traversal starts, and the result is `0`.
- **One connected component:** Its component sum equals the global sum, so every cell has remoteness zero.
- **Diagonal contact:** Diagonal cells are not connected unless a path of side-adjacent nonblocked cells joins them.
- **Large values:** The total can exceed 32-bit integer range because both component sizes and global sums contribute multiplicatively.
