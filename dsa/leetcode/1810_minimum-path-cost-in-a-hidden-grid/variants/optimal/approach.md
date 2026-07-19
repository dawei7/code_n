## General
**Discover the weighted component while preserving physical position**

Assign relative coordinate `(0, 0)` to the unknown start. From each discovered coordinate, test all four directions. When a move reaches a new cell, store the cost returned by `master.move`, note the coordinate if `master.isTarget()` is true, and explore from there. After finishing that branch, move in the opposite direction to restore the robot to its parent position. An explicit stack tracks the next direction and backtrack command, avoiding recursion failure on a long component.

**Why the recorded map is complete and correctly weighted**

A coordinate is recorded only after a legal physical move, so every mapped cell is reachable. Every direction of every mapped cell is eventually tested; if another reachable cell were missing, the first edge from the mapped component to that cell would have been followed. The forward `move` returns exactly the cost of entering the newly recorded coordinate. Costs returned by later backtracking moves are deliberately ignored: exploration is only measurement, while the requested answer describes the cheapest hypothetical start-to-target path.

**Run Dijkstra after the target and costs are known**

The mapped component is a graph with at most four edges per vertex. Traversing an edge into coordinate $v$ costs the stored entry cost of $v$, and the start distance is zero. All weights are positive, so Dijkstra's algorithm is applicable. Repeatedly remove the coordinate with the smallest tentative distance from a min-heap and relax its mapped neighbors. The first non-stale removal of the target has minimum total cost. If exploration never encounters the target, return `-1`.

The app-local adapter receives the matrix and endpoints directly, so it skips physical discovery and runs the same Dijkstra relaxation over legal matrix neighbors.

## Complexity detail
Native discovery tests four directions for each of the $V$ reachable cells and traverses every discovery edge only a constant number of times, taking $O(V)$ time. The grid graph has $O(V)$ edges. Dijkstra performs $O(V)$ heap removals and $O(V)$ successful relaxations, each costing $O(\log V)$, for $O(V\log V)$ total time. The mapped costs, exploration stack, distance map, and heap use $O(V)$ space.

## Alternatives and edge cases
- **Breadth-first search:** BFS minimizes the number of moves, not the sum of unequal entry costs, and can choose an expensive short route.
- **Bellman-Ford relaxation:** It handles positive weights correctly but repeatedly scans all grid edges and can require $O(V^2)$ time here.
- **Recursive discovery:** It mirrors backtracking naturally but may exceed Python's recursion depth on a long reachable corridor.
- **Dijkstra directly through `GridMaster`:** One stateful robot cannot remain at every heap frontier coordinate; build a reusable map before weighted search.
- **Exploration cost versus answer cost:** Physical probing may enter cells many times, but those moves do not contribute to the returned minimum path value.
- **Starting cell:** Its stored matrix cost is excluded; initialize its distance to zero.
- **Unreachable target:** The target may exist in the hidden matrix without belonging to the discovered component.
- **Cycles:** Record coordinates before exploring them so a cycle cannot trigger repeated physical traversal.
- **Several routes:** A longer route can be cheaper when it avoids high-cost cells; Dijkstra compares total cost rather than step count.
- **Backtracking:** Every forward discovery move must be paired with its opposite move before the parent frame resumes.
