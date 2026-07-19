# Maximum Number of Points with Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1937 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-points-with-cost/) |

## Problem Description
### Goal
An $M \times N$ integer matrix `points` assigns a non-negative value to every
cell. Choose exactly one cell from each row, starting with a score of zero.
Selecting column $c$ in row $r$ adds `points[r][c]` to the score.

Selections in adjacent rows also incur a movement cost. If column $a$ is
chosen in one row and column $b$ in the next, subtract
$\lvert a-b\rvert$. Return the maximum final score obtainable after choosing
one cell from every row.

### Function Contract
**Inputs**

- `points`: an $M \times N$ matrix of integers between $0$ and $10^5$,
  inclusive. Both dimensions are at least one, and
  $1 \le MN \le 10^5$.

**Return value**

- The largest total of selected cell values minus the absolute column
  movement costs between each pair of consecutive rows.

### Examples
**Example 1**

- Input: `points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]`
- Output: `9`

Choosing columns `2`, `1`, and `0` gains `11` points and pays movement cost
`2`.

**Example 2**

- Input: `points = [[1, 5], [2, 3], [4, 2]]`
- Output: `11`

**Example 3**

- Input: `points = [[7]]`
- Output: `7`
