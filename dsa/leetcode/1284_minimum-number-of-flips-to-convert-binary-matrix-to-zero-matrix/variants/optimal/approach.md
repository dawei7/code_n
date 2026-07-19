## General
**Encode matrices as graph states.** Number the $k$ cells and store a matrix as a $k$-bit integer, with a set bit representing a one. Precompute one bit mask per cell containing that cell and all of its valid orthogonal neighbors. Applying a move is then an exclusive-or with the corresponding mask, which toggles exactly the required cells.

**Breadth-first search gives the minimum.** Treat every encoded matrix as a graph vertex and every legal flip as an unweighted edge. Begin at the input mask. Breadth-first search visits states in nondecreasing numbers of moves, so the first time it generates mask zero, that path uses the minimum possible number of flips. A visited set prevents cycles caused by undoing or recombining flips. If the queue empties without reaching zero, every reachable state has been examined and the required answer is `-1`.

## Complexity detail
There are at most $2^k$ binary matrix states. Expanding one state tries all $k$ cell flips, and each transition is a constant-time bitwise operation, so the worst-case time is $O(k2^k)$. The queue and visited set can hold $O(2^k)$ masks. Because $m,n \le 3$, $k \le 9$; this domain is too small for honest runtime scaling, so exhaustive regression replaces a measured verdict.

## Alternatives and edge cases
- **Enumerate flip subsets:** Because applying a flip twice cancels it and flip order is irrelevant, all $2^k$ subsets can be tested; this also takes $O(k2^k)$ time but does not naturally discover answers layer by layer.
- **Matrix copies in BFS:** Storing full matrices is correct but makes transitions and state hashing more expensive than bit masks.
- **Already zero:** The start state must return zero before any move is generated.
- **Unreachable state:** Not every board shape makes every binary configuration reachable; exhausting the queue must return `-1`.
- **Corners and edges:** Their flip masks contain fewer than five cells because nonexistent neighbors are ignored.
