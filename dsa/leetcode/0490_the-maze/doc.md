# The Maze

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 490 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/the-maze/) |

## Problem Description
### Goal
Given a maze of open cells and walls, a ball starts at one open position. From a stopped position it may be sent up, down, left, or right, but after choosing a direction it keeps rolling through open cells until a wall blocks the next step; only then may a new direction be chosen.

Return whether some sequence of rolls makes the ball stop exactly at the destination. Merely passing over the destination while the ball can continue does not succeed. The ball cannot cross walls or leave the maze, and a route is evaluated by its stopping positions rather than by ordinary one-cell movement at every open coordinate.

### Function Contract
**Inputs**

- `maze`: a rectangular matrix where `0` is open and `1` is a wall
- `start`: the initial open cell as `[row, column]`
- `destination`: the open cell where the ball must stop

**Return value**

- `True` if some sequence of rolls stops at the destination; otherwise `False`

### Examples
**Example 1**

- Input: `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]`
- Output: `True`

**Example 2**

- Input: `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]`
- Output: `False`

**Example 3**

- Input: `maze = [[0,0,0],[0,0,0],[0,0,0]], start = [0,0], destination = [1,1]`
- Output: `False`

### Required Complexity

- **Time:** $O(rows \cdot cols)$
- **Space:** $O(rows \cdot cols)$

<details>
<summary>Approach</summary>

#### General

**Treat stopping cells as graph vertices**

A new direction may be chosen only when a roll ends. An edge therefore connects a cell to the last open cell before the next wall in each direction. Merely passing through the destination does not count.

**Precompute horizontal stops**

Scan each row into maximal open segments. Every member of a segment has the same left and right stopping columns, so filling those endpoints touches each cell once.

**Precompute vertical stops**

Scan columns into maximal open segments and similarly record top and bottom endpoints. The four tables then answer every roll in constant time.

**Search the implicit graph**

Breadth-first search starts at `start`, reads four precomputed stops for every visited cell, and enqueues unseen endpoints. The destination is reachable exactly when it is dequeued because every graph edge is one legal complete roll and every legal roll ends at a recorded segment endpoint.

#### Complexity detail

The row and column sweeps take $O(rows \cdot cols)$ time. Search visits each open cell at most once and inspects four transitions, preserving that bound. The stop tables, queue, and visited set use $O(rows \cdot cols)$ space.

#### Alternatives and edge cases

- **Roll during every search step:** is simpler but repeatedly scans corridors, with a conservative $O(rows \cdot cols \cdot (rows + cols))$ bound.
- **Depth-first search:** has the same bounds with precomputed transitions.
- **Visited cells in a list:** is correct but can make traversal quadratic in reachable stops.
- **Start equals destination:** succeeds without rolling.
- **Pass through destination:** is not enough.
- **Destination beside a wall:** may be a valid stop.
- **Isolated start:** reaches only itself.
- **Corridor cycles:** require visited-state tracking.

</details>
