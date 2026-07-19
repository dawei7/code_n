## General
**Turn the adjacency rule into an upper bound**

Consider a cell and any water cell at Manhattan distance $d$. Along a shortest path of $d$ side-adjacent moves, the height can rise by at most one per move from the water's required height $0$. Consequently, that cell's height cannot exceed $d$. Taking the nearest water source gives the strongest bound: every valid assignment has

$$
\text{height}(r,c)\le \min_{\text{water }(x,y)}\bigl(\lvert r-x\rvert+\lvert c-y\rvert\bigr).
$$

**Use the distance bound as the assignment**

Assign each cell exactly its distance to the nearest water cell. Water then has distance $0$, all values are non-negative, and moving across one grid edge changes a shortest-path distance by at most one. The assignment is therefore valid and reaches every cell's individual upper bound. In particular, no other valid assignment can have a larger overall maximum.

**Start breadth-first search from all water cells**

Place every water cell in one queue at height $0$. This is a multi-source breadth-first search: rather than running a separate search from each source, all distance-zero cells form the first layer. Whenever a cell is removed, assign each still-unvisited neighbor its height plus one and append that neighbor.

**Why the first visit is final**

The queue processes cells in nondecreasing distance layers. A cell first reached from layer $d$ has a water path of length $d+1`; any undiscovered alternative path is no shorter. Marking the cell when it is enqueued both fixes its nearest-water distance and prevents duplicate work. Since at least one water cell exists and the rectangular grid is connected, every cell is eventually assigned.

## Complexity detail
There are $RC$ cells. Each cell enters and leaves the queue once, and at most four neighbors are inspected for it, so the running time is $O(RC)$. The returned height matrix and the breadth-first queue can each contain $O(RC)$ entries, giving $O(RC)$ space.

## Alternatives and edge cases
- **Search separately from every water cell:** Repeating breadth-first search can require $O(WRC)$ time for $W$ water cells, even though all sources can share one traversal.
- **Compare every cell with every water coordinate:** Direct Manhattan-distance minimization is correct but also takes $O(WRC)$ time.
- **Two dynamic-programming sweeps:** Forward and backward distance passes can solve this rectangular Manhattan-distance problem in $O(RC)$ time, but the boundary dependencies are easier to implement incorrectly than multi-source BFS.
- **Single water cell:** Heights become ordinary Manhattan distances from that source.
- **All cells are water:** Every source begins at height $0$, and the returned matrix is all zeros.
- **Multiple equidistant sources:** The identity of the source does not matter; only the shared minimum distance determines the height.
- **No diagonal movement:** Only north, east, south, and west neighbors contribute one BFS step.
- **One-row or one-column maps:** The same traversal reduces to distances along a line.
- **Maximum dimensions:** Iterative BFS avoids recursion depth and visits each cell only once.
