# Walking Robot Simulation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 874 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/walking-robot-simulation/) |

## Problem Description
### Goal
A robot starts at `(0, 0)` on an infinite XY-plane, facing north. Execute `commands` in order: `-2` turns the robot left by $90$ degrees, `-1` turns it right by $90$ degrees, and a value $k$ from $1$ through $9$ asks it to move forward $k$ units, one unit at a time. North, east, south, and west correspond to the positive Y, positive X, negative Y, and negative X directions.

Each pair `[xi, yi]` in `obstacles` marks a blocked grid point. Before each unit move, if the next point is blocked, the robot stays on the adjacent point and immediately continues with the next command. Return the maximum squared Euclidean distance $x^2+y^2$ reached at any point along the path.

An obstacle may occupy `(0, 0)`. The robot may begin there and ignores that obstacle until it first leaves, but a later move back into the origin is blocked.

### Function Contract
**Inputs**

- `commands`: an array of $n$ instructions, where $1 \leq n \leq 10^4$ and each entry is `-2`, `-1`, or an integer from $1$ through $9$.
- `obstacles`: an array of $b$ coordinate pairs, where $0 \leq b \leq 10^4$ and each coordinate is between $-3\cdot10^4$ and $3\cdot10^4$.
- Let the total number of requested unit steps be

$$
S=\sum_{\substack{k\in\texttt{commands}\\k>0}} k.
$$

- The answer is guaranteed to be less than $2^{31}$.

**Return value**

Return the largest value of $x^2+y^2$ attained by the robot at its starting point or after any successful unit move.

### Examples
**Example 1**

- Input: `commands = [4,-1,3], obstacles = []`
- Output: `25`

The robot reaches `(0, 4)`, turns east, and finishes at `(3, 4)`.

**Example 2**

- Input: `commands = [4,-1,4,-2,4], obstacles = [[2,4]]`
- Output: `65`

The obstacle stops the eastward move at `(1, 4)`; the final northward move reaches `(1, 8)`.

**Example 3**

- Input: `commands = [6,-1,-1,6], obstacles = [[0,0]]`
- Output: `36`

The robot first reaches `(0, 6)`, then heads south but is blocked at `(0, 1)` before it can re-enter the origin.
