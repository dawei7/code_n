# Nearest Exit from Entrance in Maze

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1926 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [nearest-exit-from-entrance-in-maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/).

### Goal
Starting from an entrance cell in a maze, find the fewest steps to reach an exit. An exit is an open boundary cell other than the entrance.

### Function Contract
**Inputs**

- `maze`: a grid of walls `+` and open cells `.`.
- `entrance`: the starting `[row, col]`.

**Return value**

Return the minimum number of steps to an exit, or `-1` if no exit is reachable.

### Examples
**Example 1**

- Input: `maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]`
- Output: `1`

**Example 2**

- Input: `maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]`
- Output: `2`

**Example 3**

- Input: `maze = [[".","+"]], entrance = [0,0]`
- Output: `-1`

---

## Solution
### Approach
Run BFS from the entrance over open cells. Mark cells visited when enqueued. The first dequeued cell that lies on the boundary and is not the entrance is the nearest exit because BFS explores in increasing distance.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
