# Game of Life

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 289 |
| Difficulty | Medium |
| Topics | Array, Matrix, Simulation |
| Official Link | [game-of-life](https://leetcode.com/problems/game-of-life/) |

## Problem Description & Examples
### Goal
Given an $m \times n$ grid representing a cellular automaton, update the board to its next state simultaneously based on four specific rules:
1. Any live cell with fewer than two live neighbors dies.
2. Any live cell with two or three live neighbors lives on.
3. Any live cell with more than three live neighbors dies.
4. Any dead cell with exactly three live neighbors becomes a live cell.

The transformation must occur in-place, meaning the state of each cell is determined by its neighbors in the current state, regardless of updates made to other cells during the process.

### Function Contract
**Inputs**

- `board`: A list of lists of integers (`List[List[int]]`), where 0 represents a dead cell and 1 represents a live cell.

**Return value**

- `None`: The function modifies the input `board` in-place.

### Examples
**Example 1**

- Input: `board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]`
- Output: `[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]`

**Example 2**

- Input: `board = [[1,1],[1,0]]`
- Output: `[[1,1],[1,1]]`

---

## Underlying Base Algorithm(s)
The problem is a classic 2D grid simulation. To achieve $O(1)$ auxiliary space, we use a state-encoding technique. Instead of creating a copy of the board, we use bit manipulation or integer mapping to store the "next state" within the existing cell values:
- 0: Dead to Dead
- 1: Live to Live
- 2: Live to Dead (originally 1, now 0)
- 3: Dead to Live (originally 0, now 1)

After calculating the next state for all cells, a second pass converts these temporary states (2 and 3) into the final binary states (0 and 1).

---

## Complexity Analysis
- **Time Complexity**: $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns, as we visit each cell twice.
- **Space Complexity**: $O(1)$, as we perform the transformation in-place without allocating additional data structures proportional to the input size.
