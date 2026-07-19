## General
**Map the hidden component without losing the robot**

Assign relative coordinate `(0, 0)` to the unknown start. Explore every direction from each discovered cell. After moving into a new cell, record its relative coordinate and whether it is the target. When that branch is finished, issue the opposite move so the physical robot returns to the parent cell. An explicit stack stores the next direction and required backtrack move for every active exploration frame, avoiding recursion-depth dependence.

**Why exploration records exactly the reachable cells**

A coordinate is added only after `canMove` confirms an edge and `move` traverses it, so every recorded cell is genuinely reachable. Conversely, exploration tests all four directions from every recorded cell. Any reachable but unrecorded cell would have a first edge from the recorded component, and that edge would have been tested and followed, which is a contradiction. Backtracking restores the robot to the coordinate represented by the parent frame, keeping later queries aligned with the map.

**Separate discovery from shortest-path search**

Depth-first exploration efficiently discovers the component but does not guarantee shortest distances. Once exploration finishes, run breadth-first search over the recorded coordinates from `(0, 0)`. BFS visits cells in nondecreasing distance, so the first visit to the target has the minimum number of moves. If exploration never observes `isTarget()`, return `-1`. The app-local adapter already has the matrix and performs this BFS directly.

## Complexity detail
The native exploration enters each of the $V$ reachable cells once and tests four directions per cell. Its backtracking traverses each discovery edge a constant number of times. BFS also processes each reachable cell and at most four incident edges once, so total time is $O(V)$. The discovered-coordinate set, exploration stack, BFS queue, and visited set use $O(V)$ space.

## Alternatives and edge cases
- **Recursive exploration:** A recursive DFS mirrors the physical backtracking naturally, but a long open corridor can exceed Python's recursion limit.
- **BFS directly through `GridMaster`:** A single stateful robot cannot occupy every queued frontier cell at once; it must first build a reusable map or repeatedly navigate between states.
- The target can be adjacent to the start, but the contract guarantees they are distinct.
- The target may exist in the hidden matrix while lying outside the start's reachable component.
- Cycles require a visited-coordinate set; otherwise physical exploration can repeat forever.
- Every exploratory move must have a matching opposite move when its branch ends.
