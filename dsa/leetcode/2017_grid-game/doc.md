# Grid Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2017 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/grid-game/) |

## Problem Description

### Goal

Two robots traverse a $2\times N$ grid from the top-left cell to the
bottom-right cell. A move goes only right or down, so each path changes from
the top row to the bottom row exactly once.

The first robot moves first, collects its path's points, and replaces every
visited cell with zero. The second robot then chooses a path through the
modified grid. The first robot minimizes the second robot's score, while the
second maximizes it. Return the score produced when both choose optimally;
their paths may intersect on cells that have become zero.

### Function Contract

**Inputs**

- `grid`: exactly two rows of $N$ integers, where
  $1\le N\le5\cdot10^4$ and $1\le\texttt{grid[r][c]}\le10^5$.

**Return value**

Return the minimum score the first robot can force against an optimal second
robot.

### Examples

**Example 1**

- Input: `grid = [[2, 5, 4], [1, 5, 1]]`
- Output: `4`

**Example 2**

- Input: `grid = [[3, 3, 1], [8, 5, 2]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1, 3, 1, 15], [1, 3, 3, 1]]`
- Output: `7`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Describe the first path by its drop column.** If the first robot moves down
at column `c`, it zeros the top row through `c` and the bottom row from `c`
onward. The only positive regions left are the top suffix strictly after `c`
and the bottom prefix strictly before `c`.

**Turn the second robot's choice into a maximum.** A second path cannot collect
both residual regions: reaching the bottom prefix prevents returning to the
top suffix. It can choose whichever region has the larger total, so its best
score after drop `c` is
`max(top_suffix_after_c, bottom_prefix_before_c)`. The first robot chooses the
drop column minimizing that value.

Initialize the remaining top sum with the whole top row and the bottom prefix
with zero. At each column, remove the current top cell before evaluating the
maximum, then add the current bottom cell afterward. These update positions
preserve the strict suffix and prefix definitions. Since every legal first
path has one drop column and the formula gives the optimal response to that
path, the minimum across columns is the game's minimax value.

#### Complexity detail

Here $N$ is the number of columns. The initial top-row sum and the drop-column
scan each take $O(N)$ time. Two running sums and the current minimum use
$O(1)$ additional space.

#### Alternatives and edge cases

- **Recompute both regions per drop:** Summing a fresh suffix and prefix for
  every column is correct but takes $O(N^2)$ time.
- **Two prefix arrays:** Precomputing both row sums supports constant-time
  drop evaluation but uses unnecessary $O(N)$ space.
- With one column, the first robot clears both cells and the second scores
  zero.
- The best drop may occur at either boundary, leaving one residual region
  empty.
- Total scores can exceed 32-bit range, so the result must preserve a wide
  integer value.

</details>
