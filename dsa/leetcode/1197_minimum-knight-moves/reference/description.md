## Description

In an **infinite** chess board with coordinates from `-infinity` to `+infinity`, you have a **knight** at square `[0, 0]`.

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

![](images/knight.png)

Return *the minimum number of steps needed to move the knight to the square* `[x, y]`. It is guaranteed the answer exists.
### Function Contract

**Inputs**

- `x`: The destination's horizontal integer coordinate.
- `y`: The destination's vertical integer coordinate.

The knight always starts at `[0,0]`. Each move changes the coordinate pair by one of the eight displacements listed in the Description; the board has no boundary.

**Return value**

Return the smallest number of legal knight moves in any route from `[0,0]` to `[x,y]`.

### Examples

#### Example 1

- **Input:** $x = 2, y = 1$
- **Output:** `1`
- **Explanation:** [0, 0] → [2, 1]
#### Example 2

- **Input:** $x = 5, y = 5$
- **Output:** `4`
- **Explanation:** [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
### Constraints

- $-300 \le x, y \le 300$

- $0 \le |x| + |y| \le 300$