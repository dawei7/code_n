## General
**The height order fixes the sequence of destinations**

Collect every cell whose value exceeds one and sort those cells by height. Tree heights are distinct, so there is no choice about which destination comes next. Cutting a tree changes its value to open ground but does not change whether the cell is traversable, so all shortest-path searches use the same obstacle layout.

**Use breadth-first search for each required leg**

From the current position, run BFS through nonzero cells until reaching the next tree. BFS explores positions in nondecreasing step count, making the first arrival the shortest possible distance for that leg. Add the distance and continue from that tree. If a BFS exhausts the reachable region, the mandatory destination is impossible and the entire answer is `-1`.

**Why independently shortest legs minimize the total**

Every valid walk must visit the same sorted sequence of tree positions. Its portion between two consecutive required positions cannot be shorter than the grid shortest-path distance between them. BFS attains that lower bound for each leg, and concatenating these shortest legs is valid because each endpoint is the next leg's start. Their sum is therefore the minimum possible total.

## Complexity detail
Let `T` be the number of trees in an `R` by `C` grid. Sorting destinations costs $O(T \log T)$. Each of up to `T` breadth-first searches visits at most `RC` cells and edges, giving $O(T \log T + TRC)$ total time. A queue and visited set for one BFS use $O(RC)$ auxiliary space and are reused between legs.

## Alternatives and edge cases
- **A* search for each leg:** Manhattan distance is an admissible heuristic and may inspect fewer cells in practice, but the same grid-sized worst case remains.
- **Bidirectional BFS:** can reduce explored layers for distant targets, though it adds two frontier and visited structures for every leg.
- **All-pairs shortest paths:** precomputes every passable-cell distance, but Floyd-Warshall takes $O((RC)^3)$ time and $O((RC)^2)$ space.
- A tree at the starting cell costs zero steps to cut before moving onward.
- If there are no trees, the required total is zero.
- If the start is blocked and any tree exists elsewhere, the first required tree is unreachable.
