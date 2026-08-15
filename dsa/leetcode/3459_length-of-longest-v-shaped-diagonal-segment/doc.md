# Length of Longest V-Shaped Diagonal Segment

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3459 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/) |

## Problem Description

### Goal

The cells of `grid` contain only `0`, `1`, and `2`. Find the longest path that starts on a cell containing `1` and then follows the repeating value sequence `2, 0, 2, 0, ...`.

Every move must go to a diagonally adjacent cell. The path initially chooses one of the four diagonal directions: down-right, down-left, up-left, or up-right. It may continue in that direction without turning, or it may make exactly one clockwise $90^\circ$ turn to the next diagonal direction and continue there. A second turn and a counterclockwise turn are forbidden, and the value sequence does not restart at the turn.

A single `1` is itself a valid segment of length one. If the matrix contains no starting `1`, no valid segment exists and the result is zero.

### Function Contract

**Inputs**

- `grid`: An $n\times m$ matrix whose entries belong to $\{0,1,2\}$.

The constraints are $1 \le n,m \le 500$.

**Return value**

Return the maximum number of cells in a valid V-shaped diagonal segment, or `0` if no such segment exists.

### Examples

#### Example 1

- **Input:** `grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]`
- **Output:** `5`

One longest segment follows `(0,2)`, `(1,3)`, `(2,4)`, turns clockwise, and continues through `(3,3)` and `(4,2)`.

#### Example 2

- **Input:** `grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]`
- **Output:** `4`

The cells `(2,3)`, `(3,2)`, `(2,1)`, and `(1,0)` form a valid segment with one clockwise turn.

#### Example 3

- **Input:** `grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]`
- **Output:** `5`

The main diagonal already supplies a length-five segment, so a turn is unnecessary.

#### Example 4

- **Input:** `grid = [[1]]`
- **Output:** `1`
