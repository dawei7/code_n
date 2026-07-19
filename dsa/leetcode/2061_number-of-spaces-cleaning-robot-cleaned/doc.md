# Number of Spaces Cleaning Robot Cleaned

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2061 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/) |

## Problem Description

### Goal

A binary matrix represents a room: `0` is an empty space and `1` is an object. The upper-left space is always empty. A cleaning robot starts there facing right, and its starting space and every empty space it visits become clean.

The robot repeatedly attempts to move one cell straight ahead. If the next cell is outside the room or contains an object, it stays in place and turns $90^\circ$ clockwise; otherwise it advances without changing direction. The robot runs indefinitely. Return the number of distinct spaces it eventually cleans.

### Function Contract

**Inputs**

- `room`: an $m\times n$ binary matrix, where $1 \le m,n \le 300$ and `room[0][0] == 0`.

**Return value**

- Return the number of distinct empty cells visited by the indefinitely running robot.

### Examples

**Example 1**

- Input: `room = [[0,0,0],[1,1,0],[0,0,0]]`
- Output: `7`
- Explanation: The robot follows the open outer path and visits every empty cell.

**Example 2**

- Input: `room = [[0,1,0],[1,0,0],[0,0,0]]`
- Output: `1`
- Explanation: Objects or boundaries block all four directions from the start.

**Example 3**

- Input: `room = [[0,0,0],[0,0,0],[0,0,0]]`
- Output: `8`
- Explanation: The motion cycles around the boundary and never visits the center.

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Direction is part of the deterministic state**

Represent direction by an index into right, down, left, and up step vectors. From `(row, column, direction)`, the rules determine exactly one next state: turn clockwise in place when blocked, or move forward otherwise. A repeated complete state therefore proves that every future state will repeat as well.

**Separating visited states from cleaned cells**

Maintain one set of complete states for cycle detection and another set of positions for the answer. At each new state, add the current position to the cleaned set, then apply the movement rule. Stop when the current state has already appeared and return the number of cleaned positions.

There are only four possible directions per cell. The simulation follows the unique path through this finite state graph until it repeats; every state before that repetition is exactly the nonrepeating prefix and cycle the robot reaches. Consequently, every position the infinite run can visit has already been recorded.

#### Complexity detail

At most $4mn$ complete states exist, and each simulation step performs constant work, giving $O(mn)$ time. The state and cleaned-position sets contain at most $4mn$ and $mn$ entries, respectively, for $O(mn)$ space.

#### Alternatives and edge cases

- **Mutate the room to mark cells:** This can count cleaned positions, but position-only marks cannot detect a motion cycle because revisiting a cell from another direction may lead elsewhere.
- **List-based state history:** Linear search detects the same repeated state correctly but can require $O((mn)^2)$ time.
- Turning does not clean a new cell, though it creates a different state at the same position.
- An open room does not imply every cell is cleaned; an empty square room leaves interior cells untouched.
- A one-cell room cycles through four directions and cleans exactly one space.

</details>
