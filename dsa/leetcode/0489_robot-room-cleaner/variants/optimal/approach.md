## General

**Build a coordinate system from the starting state**

Treat the unknown starting cell as virtual coordinate `(0, 0)` and the robot's initial upward direction as `0`.
The four entries in `directions` map relative directions to coordinate changes. Absolute room coordinates are
unnecessary: successful moves and the robot's turns keep the virtual coordinates synchronized with its physical
state.

Record `(0, 0)` in `visited`, clean it, and push the first explicit DFS frame. Each frame stores four integers:
`[row, col, direction, offset]`. `direction` is the orientation on entry to that cell, and `offset` identifies the
next of its four relative directions to try.

**Advance one DFS frame at a time**

For the top frame, `(direction + offset) % 4` is the physical direction currently faced. If the neighboring virtual
coordinate is unvisited and `robot.move()` succeeds, mark and clean the new cell, then push a child frame with that
movement direction and offset zero. The parent frame remains unchanged until the child finishes.

If the coordinate was already visited or the move is blocked, turn right and increment the frame's offset. Thus the
top frame and the physical robot advance together through all four directions.

**Restore the parent without recursion**

An offset of four means the current cell has no unexplored direction. Pop its frame. When a parent remains, call
`go_back()`: turn twice, move one cell back, and turn twice again. The robot is now at the parent's cell facing the
direction of the completed child edge. One more right turn and one parent-offset increment put it in the exact state
for the next branch.

This is the same physical backtracking discipline as recursive DFS, but the explicit stack is not bounded by
Python's recursion limit.

**Why every reachable cell is cleaned**

Whenever the algorithm pushes a frame, a successful robot move proves that its coordinate is reachable, and it is
cleaned immediately. The visited set permits at most one frame creation per coordinate, so cycles cannot cause
unbounded revisits. Conversely, every discovered cell tries all four incident directions. Along any path of open
cells from the start, induction over the path edges shows that each next unvisited cell is eventually entered and
cleaned. Exact restoration after every completed child preserves the physical state required to try all remaining
branches.

## Complexity detail

Let $c$ be the number of reachable cells. Each coordinate enters `visited` and the stack once, and its frame examines
four directions. Every successful tree edge is traversed once forward and once during `go_back`, so the total time
complexity is $O(c)$.

The visited set and explicit DFS stack each hold at most $c$ entries, giving $O(c)$ auxiliary space.

## Alternatives and edge cases

- **Recursive coordinate DFS:** the protected and immutable Accepted sources express the same traversal compactly,
  but the app-local Python execution can raise `RecursionError` on a source-legal deep room. An explicit stack keeps
  the algorithm valid through the complete room bound.
- **Visited coordinates in a list:** remains logically correct, but linear membership checks raise worst-case time
  to $O(c^2)$.
- **Known-grid traversal:** reading `room`, `row`, or `col` directly violates the blind interface contract.
- **Breadth-first search:** logical queuing does not preserve the robot's physical position, so reaching each queued
  cell would require additional navigation state and work.
- **Single open cell:** clean it before movement; all four blocked attempts then finish the sole frame.
- **Cycles:** the hash set prevents entering an already discovered coordinate even if another physical route reaches
  it.
- **Dead ends:** four direction attempts followed by `go_back()` restore both the parent cell and its orientation.
- **Initial direction:** the source guarantees that the robot faces upward, which anchors virtual direction zero.
