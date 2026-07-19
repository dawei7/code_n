## General
**Encode the usable grid as a graph:** Assign a bit index to every non-obstacle square. Two vertices are adjacent when their grid squares share an edge. A bitmask then records exactly which squares a partial walk has visited.

**Memoize position and visited set:** Define a state by the current vertex `position` and the `visited` mask. From that state, try every adjacent vertex whose bit is not set and add the counts returned after setting it. Different walk prefixes can arrive at the same vertex with the same visited set; their possible suffixes are identical, so caching prevents those suffixes from being explored repeatedly.

**Accept the end only after full coverage:** If the current vertex is the end, return one exactly when `visited` equals the mask containing all $V$ usable squares; otherwise return zero immediately. This prevents a walk from reaching the end early, leaving other squares unvisited, and later treating that prefix as valid.

Every legal walk corresponds to one sequence of recursive transitions because each move follows a graph edge and sets one previously clear bit. Conversely, every counted transition sequence is four-directional, never revisits a square, covers the full mask, and finishes at the end. The state sum therefore counts precisely the required walks.

## Complexity detail
There are at most $V2^V$ pairs of current vertex and visited mask. Each state examines at most four grid neighbors, so the bound remains $O(V2^V)$ time. The memo table can store $O(V2^V)$ results, and recursion uses at most $O(V)$ additional stack depth.

## Alternatives and edge cases
- **Plain backtracking:** Marking cells in place uses only $O(V)$ stack space, but it can recompute the same position-and-visited-set suffix many times and has an exponential $O(3^V)$ upper bound.
- **Permute usable squares:** Generating orders and checking adjacency explores up to $V!$ candidates and ignores the grid graph until too late.
- **Reach the end early:** Such a path contributes zero because every other usable square must already have been visited.
- **Obstacles:** They receive no bit and no graph edges, so they are neither visited nor included in the full-coverage mask.
- **No Hamiltonian walk:** The recurrence naturally returns zero when every branch either gets stuck or reaches the end with an incomplete mask.
