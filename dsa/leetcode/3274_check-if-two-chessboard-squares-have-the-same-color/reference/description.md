## Description

You are given two strings, `coordinate1` and `coordinate2`, representing the coordinates of a square on an `8 x 8` chessboard.

Below is the chessboard for reference.

![](images/screenshot-2021-02-20-at-22159-pm.png)

Return `true` if these two squares have the same color and `false` otherwise.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** coordinate1 = "a1", coordinate2 = "c3"

**Output:** true

**Explanation:**

Both squares are black.

</div>
#### Example 2

<div class="example-block">
**Input:** coordinate1 = "a1", coordinate2 = "h3"

**Output:** false

**Explanation:**

Square `"a1"` is black and `"h3"` is white.

</div>
### Constraints

- $\text{coordinate1.length} = \text{coordinate2.length} = 2$

- $'a' \le \text{coordinate1}[0], \text{coordinate2}[0] \le 'h'$

- $'1' \le \text{coordinate1}[1], \text{coordinate2}[1] \le '8'$