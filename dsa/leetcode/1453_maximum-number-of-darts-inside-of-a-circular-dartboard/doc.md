# Maximum Number of Darts Inside of a Circular Dartboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1453 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/) |

## Problem Description
### Goal

Each entry in `darts` is the distinct Cartesian coordinate of a dart embedded
in a large wall. A circular dartboard has fixed radius `r`, but its center may
be placed at any real-valued point on the plane.

Choose the center that covers as many darts as possible and return that maximum
count. A dart on the circumference is covered as well as a dart strictly
inside the board.

### Function Contract
**Inputs**

- `darts`: a list of $n$ distinct coordinate pairs `[x, y]`, with
  $1 \le n \le 100$.
- Every coordinate is an integer satisfying
  $-10^4 \le x,y \le 10^4$.
- `r`: the positive integer board radius, with $1 \le r \le 5000$.

**Return value**

Return the greatest number of input points whose Euclidean distance from one
chosen center is at most $r$.

### Examples
**Example 1**

- Input: `darts = [[-2, 0], [2, 0], [0, 2], [0, -2]], r = 2`
- Output: `4`
- Explanation: A board centered at the origin places all four darts on its
  circumference.

**Example 2**

- Input: `darts = [[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], r = 5`
- Output: `5`
- Explanation: A center at `(0, 4)` covers every dart except `(7, 8)`.

**Example 3**

- Input: `darts = [[1, 2], [3, 5], [1, -1]], r = 2`
- Output: `2`
