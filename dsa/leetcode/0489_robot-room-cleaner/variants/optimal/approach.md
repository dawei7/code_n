## General
**Create virtual coordinates**

Treat the start as `(0, 0)` and its initial facing as virtual north. Every successful move changes that virtual coordinate by the delta for the currently explored relative direction.

**Explore through the interface**

Depth-first search records and cleans each newly reached coordinate. For four directions, move only when the target coordinate is unvisited. A failed move reveals a wall while leaving the robot in place.

**Restore position and orientation**

After exploring a neighbor, turn twice, move back, and turn twice again. After every direction attempt, turn right once. These operations restore the parent's exact physical state before its next branch.

**Why every reachable cell is cleaned**

DFS eventually tries every edge leaving every discovered cell. Induction along a path from the start shows every reachable cell is entered. The visited set prevents cycles, and exact physical backtracking preserves access to every unexplored branch.

## Complexity detail
Let `c` be the reachable-cell count. Each cell considers four directions and every traversed edge uses constant robot operations, so time is $O(c)$. The visited set and recursion stack use $O(c)$ space.

## Alternatives and edge cases
- **Visited coordinates in a list:** is correct but linear membership checks produce $O(c^2)$ time.
- **Known-grid DFS:** violates the interactive contract because the room is hidden.
- **Breadth-first search:** requires costly physical navigation back to queued cells.
- **Single cell:** clean it even though every move fails.
- **Cycles:** require the visited set.
- **Disconnected regions:** unreachable cells are outside the required result.
- **Arbitrary orientation:** relative coordinates need no global compass.
- **Dead ends:** backtracking must restore orientation as well as position.
