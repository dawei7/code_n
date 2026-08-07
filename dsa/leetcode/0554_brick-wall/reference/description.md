## Description

There is a rectangular brick wall in front of you with `n` rows of bricks. The $$i^{\text{th}}$$ row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array `wall` that contains the information about the wall, return *the minimum number of crossed bricks after drawing such a vertical line*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

![](images/a.png)

- **Input:** $wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]$
- **Output:** `2`
#### Example 2

- **Input:** $wall = [[1],[1],[1]]$
- **Output:** `3`
### Constraints

- $n = \text{wall.length}$

- $1 \le n \le 10^{4}$

- $1 \le \text{wall}[i].length \le 10^{4}$

- $1 \le sum(\text{wall}[i].length) \le 2 * 10^{4}$

- $sum(\text{wall}[i])$ is the same for each row `i`.

- $1 \le \text{wall}[i][j] \le 2^{31} - 1$