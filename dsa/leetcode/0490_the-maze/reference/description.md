## Description

There is a ball in a `maze` with empty spaces (represented as `0`) and walls (represented as `1`). The ball can go through the empty spaces by rolling **up, down, left or right**, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the `m x n` `maze`, the ball's `start` position and the `destination`, where $start = [\text{start}_{row}, \text{start}_{col}]$ and $destination = [\text{destination}_{row}, \text{destination}_{col}]$, return `true` if the ball can stop at the destination, otherwise return `false`.

You may assume that **the borders of the maze are all walls** (see examples).
### Function Contract

**Inputs**

- `maze`: a rectangular matrix where `0` is an empty space and `1` is a wall
- `start`: the ball's initial empty cell as `[row, column]`
- `destination`: the distinct empty cell where the ball must stop

**Return value**

- Return `True` if some sequence of complete rolls stops at `destination`; otherwise return `False`.

Each chosen direction is committed until a wall stops the ball. Intermediate cells crossed during that roll are not
decision points.

### Examples
#### Example 1

![](images/maze1-1-grid.jpg)

- **Input:** $maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]$
- **Output:** `true`
- **Explanation:** One possible way is : left -> down -> left -> down -> right -> down -> right.
#### Example 2

![](images/maze1-2-grid.jpg)

- **Input:** $maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]$
- **Output:** `false`
- **Explanation:** There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
#### Example 3

- **Input:** $maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]$
- **Output:** `false`
### Constraints

- $m = \text{maze.length}$

- $n = \text{maze}[i].length$

- $1 \le m, n \le 100$

- $\text{maze}[i][j]$ is `0` or `1`.

- $\text{start.length} = 2$

- $\text{destination.length} = 2$

- $0 \le \text{start}_{row}, \text{destination}_{row} < m$

- $0 \le \text{start}_{col}, \text{destination}_{col} < n$

- Both the ball and the destination exist in an empty space, and they will not be in the same position initially.

- The maze contains **at least 2 empty spaces**.