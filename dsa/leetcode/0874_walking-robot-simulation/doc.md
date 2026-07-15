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

### Required Complexity
- **Time:** $O(n+b+S)$
- **Space:** $O(b)$

<details>
<summary>Approach</summary>

#### General

**Encode direction and obstacles for constant-time updates**

Store the four direction vectors in clockwise order: north, east, south, and west. A right turn increments the direction index modulo four, while a left turn decrements it modulo four. Convert every obstacle pair to a tuple in a hash set so each proposed point can be checked in expected constant time.

**Simulate every unit because every intermediate point matters**

For a positive command, compute the next point one unit in the current direction. If it belongs to the obstacle set, stop processing that command; otherwise, assign the new coordinates and update the maximum with $x^2+y^2$. Checking one unit at a time is necessary both because an obstacle can interrupt a longer command and because the requested maximum may occur before the final command.

The maintained coordinates are exactly the robot's position after each processed instruction: turns change only the direction, successful unit moves enter the requested adjacent point, and a blocked candidate ends that movement command without changing position. Since the squared distance is inspected after every reachable point, the recorded maximum is precisely the required result. Keeping `(0, 0)` in the obstacle set naturally permits the initial state but blocks any later proposed move into it.

#### Complexity detail

Building the obstacle set takes $O(b)$ time and space. The command loop handles $n$ instructions and attempts at most $S$ unit moves, each with expected $O(1)$ hash lookup, for $O(n+b+S)$ total time. Apart from the obstacle set and a constant amount of simulation state, no additional storage is needed, so auxiliary space is $O(b)$.

#### Alternatives and edge cases

- **Scan the obstacle array for every step:** This preserves the simulation but can take $O(Sb)$ time; hashing removes the repeated linear membership search.
- **Jump directly by each positive command:** A direct endpoint update can pass through an obstacle and therefore violates the one-unit-at-a-time rule.
- **Group obstacles by row or column:** Sorted coordinate maps can jump to the nearest blocker and may reduce work for very large command distances, but commands here are at most `9` and the extra machinery is unnecessary.
- **Obstacle at the origin:** Starting on `(0, 0)` is allowed, but after leaving, a proposed return to that point is blocked.
- **Blocked first unit:** The robot does not move for the remainder of that positive command and proceeds to the following instruction.
- **Turns only:** The position never changes, so the answer remains `0`.
- **Path returns toward the origin:** The answer is a maximum over the whole path and must not be replaced by the final squared distance.

</details>
