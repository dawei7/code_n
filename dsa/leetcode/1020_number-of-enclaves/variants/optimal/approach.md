## General
**Reverse the reachability question:** A land cell can escape exactly when its connected component contains boundary land. Instead of testing every cell independently, start searches from all boundary land cells and mark everything reachable from them as non-enclave land.

**Seed each boundary cell once:** Add land cells from the first and last rows and columns to a queue, changing them to sea as soon as they are enqueued. Immediate marking prevents duplicate work at corners or through multiple paths.

**Flood through four-directional land:** Repeatedly remove a cell and inspect its four neighbors. When an in-bounds neighbor is land, mark and enqueue it. After the queue empties, every land cell capable of reaching the boundary has been removed.

**Count what remains:** Sum the remaining `1` cells. Boundary-connected components were removed completely, while components without a boundary path were never reached, so the remaining total is exactly the requested enclave-cell count.

## Complexity detail
Each of the $RC$ cells is inspected a constant number of times and enqueued at most once, giving $O(RC)$ time. In the worst case, the queue can contain $O(RC)$ cells; mutating the input supplies the visited marking without another matrix.

## Alternatives and edge cases
- **Search from every land cell:** Testing boundary reachability independently repeats component traversals and can take $O((RC)^2)$ time.
- **Union-find:** Joining adjacent land and a virtual boundary node gives $O(RC)$ near-linear time but requires additional arrays.
- **All land:** Every cell connects to the boundary, so the result is zero.
- **Single row or column:** Every cell lies on the boundary; no enclave exists.
- **Diagonal contact:** It does not create a valid path because moves are only 4-directional.
