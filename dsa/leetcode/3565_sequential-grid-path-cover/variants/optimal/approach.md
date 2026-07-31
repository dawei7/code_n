## General

Try every grid cell as the path's starting point. For one start, recursively extend the current path to each orthogonally adjacent cell that has not yet been visited. The visited matrix prevents repeats, so a branch always represents a simple path.

Carry the value of the next required checkpoint, initially 1. Entering a zero-valued cell leaves it unchanged. Entering a numbered cell is legal only when that number equals the next required value; after accepting it, advance the requirement by one. This local test is sufficient because numbered values are unique: every surviving prefix has encountered exactly an initial segment $1,2,\ldots,t-1$ and no later checkpoint.

When the path contains all $V$ cells, copy and return it. It necessarily includes every checkpoint and therefore meets the full contract. If a recursive choice fails, remove its coordinate and clear its visited mark before trying the next neighbor. Thus every self-avoiding path from every possible start is considered unless an out-of-order checkpoint proves its entire branch invalid. If all branches fail, no valid cover exists.

## Complexity detail

Let $V=mn$. There are $V$ possible starts. The first move has at most four choices, and every later step has at most three because the preceding cell is already visited. A conservative worst-case bound is therefore $O(V\cdot3^V)$ time. The visited matrix, current path, returned path, and recursion stack each use $O(V)$ space.

The benchmark size is $V$. Its grids admit an immediate depth-$V$ cover for the accepted in-place search. The calibrated slower implementation unnecessarily repeats a copied-state search from every start even after finding a valid answer, exposing an additional polynomial factor while preserving identical worst-case search semantics.

## Alternatives and edge cases

- **Subset dynamic programming:** A state `(visited_mask, last_cell, next_checkpoint)` avoids revisiting identical subproblems but can require $O(V2^V)$ states, which is substantial even at the 25-cell limit.
- **Permute all cells:** Testing arbitrary coordinate permutations wastes almost all work on non-adjacent sequences and has factorial growth.
- **Fixed snake traversal:** Every rectangle has simple snake covers, but a fixed orientation may encounter the numbered cells out of order even when another Hamiltonian path works.
- **Zero-valued start:** A path may begin on zero and reach checkpoint 1 later.
- **Numbered start:** A numbered starting cell is legal only when it contains 1.
- **Single cell:** The only cell contains checkpoint 1, so its coordinate alone is a valid cover.
- **Complete cover:** Returning early after checkpoint `k` is incorrect; all remaining zero cells must still be visited exactly once.
- **Backtracking restoration:** Both the coordinate list and visited mark must be undone after a failed branch so later starts see a clean grid.
