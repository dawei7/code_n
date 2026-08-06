## Examples

**Example 1**

- Input: `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]`
- Output: `12`
- **Explanation:** One valid sequence of complete rolls is left, down, left, down, right, down, and right. Its roll
  lengths are `1`, `1`, `3`, `1`, `2`, `2`, and `2`, which sum to `12`.

The first source diagram is represented below. `S` marks the ball's start, `D` the destination, `0` another empty
cell, and `1` a wall.

| Row \ Column | 0 | 1 | 2 | 3 | 4 |
|---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 0 | S |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 1 | 0 |
| 3 | 1 | 1 | 0 | 1 | 1 |
| 4 | 0 | 0 | 0 | 0 | D |

**Example 2**

- Input: `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]`
- Output: `-1`
- **Explanation:** The ball can roll through the destination, but no legal roll stops there. Therefore no route
  satisfies the destination condition.

The second source diagram uses the same maze and start but places `D` at the pass-through cell `(3, 2)`.

| Row \ Column | 0 | 1 | 2 | 3 | 4 |
|---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 0 | S |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 1 | 0 |
| 3 | 1 | 1 | D | 1 | 1 |
| 4 | 0 | 0 | 0 | 0 | 0 |

**Example 3**

- Input: `maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]`
- Output: `-1`
