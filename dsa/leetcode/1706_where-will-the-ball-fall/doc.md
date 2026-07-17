# Where Will the Ball Fall

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1706 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/where-will-the-ball-fall/) |

## Problem Description
### Goal

A box is represented by an $m \times n$ matrix `grid`, with its top and bottom open. Each cell contains one diagonal board. A value of `1` is a board descending from the cell's top-left corner to its bottom-right corner and redirects a ball right; `-1` descends from top-right to bottom-left and redirects a ball left.

Drop one ball into the top of every column. A ball moves through the rows in order, but it becomes stuck if a board directs it into a side wall or if two neighboring boards form a `V` around it. Return the bottom exit column of every ball in starting-column order, using `-1` for each ball that cannot leave the box.

### Function Contract
**Inputs**

- `grid`: an $m \times n$ matrix containing only `1` and `-1`
- $1 \le m,n \le 100$, and every row has exactly $n$ entries

**Return value**

A length-$n$ list where entry `start` is the exit column for the ball dropped above `grid[0][start]`, or `-1` when that ball gets stuck.

### Examples
**Example 1**

- Input: `grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]`
- Output: `[1, -1, -1, -1, -1]`

Only the ball from column zero follows compatible adjacent boards through every row and exits at column one.

**Example 2**

- Input: `grid = [[-1]]`
- Output: `[-1]`

The only board points through the left wall, so the ball is immediately stuck.

**Example 3**

- Input: `grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]`
- Output: `[0, 1, 2, 3, 4, -1]`

The first five balls alternate right and left moves and return to their starting columns; the last ball hits the right wall in the first row.

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Translate one board into a column transition**

Simulate each starting column independently. When a ball reaches column `column` in a row, its board direction is `row[column]`, so the candidate destination is `next_column = column + row[column]`. A destination outside `[0, n)` means the board points into a wall and the ball's answer is `-1`.

Remaining inside the box is not enough. The neighboring cell must contain a board with the same direction. If `row[next_column] != row[column]`, the two boards slope toward each other and form a `V`, so the ball is trapped. Otherwise the matching pair creates a continuous channel into the next row at `next_column`.

**Preserve the first failed transition**

Process rows from top to bottom until a transition fails or the ball passes the final row. Each successful update gives the ball's only physically possible column in the next row. Inductively, the simulation therefore matches its unique path. A failed wall or `V` transition cannot be bypassed, while a ball that completes all $m$ transitions exits at its final column.

Repeat this deterministic simulation for all $n$ starting columns and append results in their original order.

#### Complexity detail

In the worst case, each of the $n$ balls crosses all $m$ rows, for $O(mn)$ time. The returned list stores $n$ exit values and uses $O(n)$ space; the simulation itself needs only constant auxiliary state per ball.

#### Alternatives and edge cases

- **Recursive depth-first simulation:** recursion follows the same unique paths but uses up to $O(m)$ call-stack space per active traversal.
- **Memoize cell outcomes:** suffix outcomes can be cached, but valid ball paths do not merge without first encountering a trapping `V`, so this does not improve the worst-case $O(mn)$ bound.
- **Check only the wall:** an in-range move can still be invalid when adjacent boards have opposite signs.
- **Check only the current sign:** a right board followed by a left board, or vice versa, forms a trap and must return `-1`.
- **Single column:** every direction points into a wall, so its only ball is stuck.
- **Immediate `V`:** both balls bordering the opposing pair become stuck in that row.
- **Later trap:** a ball may move successfully through several rows before returning `-1`.
- **Exit indexing:** report the zero-based column below the final row, not the number of horizontal moves.

</details>
